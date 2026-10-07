"""Connected product workspace: identity, evidence, analysis and portable user observations."""
import json
from datetime import date

import pandas as pd
import streamlit as st

from price_truth.catalogue import export_csv, search
from price_truth.evidence_store import accumulated_observations
from price_truth.external import cached_products, lookup_product, search_products
from price_truth.forecast import forecast_next_day
from price_truth.history import load_observations, series_for, timing_signal
from price_truth.observations import (
    COLUMNS,
    daily_series,
    pack_changes,
    read_csv,
    validate_observations,
)
from price_truth.offers import compare_observed_offers
from price_truth.paths import EXTERNAL
from price_truth.price_api import fetch_observations
from price_truth.ui import assessment_panel, unit_page


def use_pack_for_comparison(product: dict) -> None:
    """Transfer only structured pack quantity, never invent a missing retailer price."""
    st.session_state["quantity1"] = float(product["product_quantity"])
    st.session_state["unit1"] = product["product_quantity_unit"].lower()
    st.session_state["price1"] = None
    st.session_state["count1"] = 1
    st.session_state["workspace_source"] = "Pack value comparison"


def history_panel(frame: pd.DataFrame, code: str) -> None:
    """Keep barcode, store, currency and recorded basis fixed throughout analysis."""
    if frame.empty or "product_code" not in frame:
        st.info("No dated price observations available for this barcode.")
        return
    eligible = frame[(frame.product_code == code) & frame.location_id.notna()
                     & frame.currency.notna()].copy()
    if eligible.empty:
        st.info("No identified store and currency observations available for this barcode.")
        return
    eligible["price_per"] = eligible.price_per.fillna("UNKNOWN")
    groups = eligible[["location_id", "currency", "price_per"]].drop_duplicates()
    options = list(groups.itertuples(index=False, name=None))
    store, currency, basis = st.selectbox("Comparable store / currency / basis", options,
                                         format_func=lambda v: f"Store {v[0]} · {v[1]} · {v[2]}")
    series = series_for(eligible, code, store, currency, basis)
    st.line_chart(series.set_index("date")["price"], y_label=f"{currency} / {basis}")
    evidence = eligible[(eligible.location_id == store) & (eligible.currency == currency)
                        & (eligible.price_per == basis)]
    st.dataframe(evidence[["date", "price", "currency", "source_url"]], hide_index=True)
    st.caption("The chart excludes duplicate, unproven, future and non-shop observations. Source rows remain visible for audit.")
    quote = st.number_input("Current quote for this exact recorded basis", min_value=.01, value=None)
    if st.button("Evaluate historical position"):
        if quote is None:
            st.warning("Enter a current quote first.")
        elif basis == "UNKNOWN":
            st.warning("The source lacks a price basis, so a comparable quote cannot be established.")
        else:
            st.json(timing_signal(series, quote))
    with st.expander("Next-day forecast evidence"):
        st.caption("Only recent consecutive daily history can be backtested. A barcode does not prove unchanged pack size.")
        confirmed = st.checkbox("I checked that this history represents the same pack and purchase conditions")
        if confirmed and basis != "UNKNOWN":
            st.json(forecast_next_day(series))
    st.download_button("Export sourced observations", export_csv(evidence),
                       file_name=f"price_evidence_{code}.csv", mime="text/csv")


def food_workspace() -> None:
    """Search or choose one barcode and carry it through lookup and price history."""
    products = cached_products()
    with st.form("workspace_food_search"):
        query = st.text_input("Food name or barcode", placeholder="Search by name, or paste 8–14 digits")
        offline = st.checkbox("Use saved responses only", value=True)
        submitted = st.form_submit_button("Find food product")
    if submitted:
        try:
            if query.strip().isdigit():
                found = lookup_product(query.strip(), offline)
                st.session_state["workspace_food_candidates"] = [found["product"]]
            else:
                found = search_products(query, offline)
                st.session_state["workspace_food_candidates"] = found["products"]
            st.session_state.pop("workspace_price_result", None)
        except ValueError as exc:
            st.error(str(exc))
    products = st.session_state.get("workspace_food_candidates", products)
    if not products:
        st.info("No matching products. Try another query or barcode.")
        return
    product = st.selectbox("Selected food product", products,
                           format_func=lambda p: f"{p.get('product_name') or 'Unnamed'} · {p.get('code')}")
    code = str(product.get("code", ""))
    st.caption(f"Identity: barcode {code}. No automatic match to the historical Amazon/Flipkart catalogue.")
    if st.button("Load pack details"):
        try:
            result = lookup_product(code, offline)
            st.session_state["workspace_pack"] = {"code": code, "result": result}
        except ValueError as exc:
            st.error(str(exc))
    pack = st.session_state.get("workspace_pack", {})
    if pack.get("code") == code:
        result = pack["result"]
        st.write(result["product"])
        st.caption(f"{result['mode']} · fetched {result['fetched_at']} · Open Food Facts / ODbL")
        details = result["product"]
        quantity = pd.to_numeric(details.get("product_quantity"), errors="coerce")
        if pd.notna(quantity) and 0 < quantity < 1e12 and str(details.get("product_quantity_unit", "")).lower() in {"g", "kg", "ml", "l", "count"}:
            st.button("Use this pack in unit comparison", on_click=use_pack_for_comparison, args=(details,))
    frame, metadata = load_observations()
    latest = EXTERNAL / "current/open_prices_inr.json"
    if latest.exists():
        snapshot = json.loads(latest.read_text())
        frame, metadata = pd.DataFrame(snapshot["observations"]), snapshot
    archive = EXTERNAL / "archive"
    if archive.exists():
        try:
            accumulated, collection = accumulated_observations(archive)
            if not accumulated.empty:
                frame = accumulated
                metadata["fetched_at"] = collection["latest_retrieval"]
                st.caption(f"Cumulative collection: {collection['unique_source_observations']} source observations across {collection['snapshots']} snapshots. Retrieval does not create new observation dates.")
        except ValueError:
            st.warning("The cumulative archive could not be read; using the separately dated snapshot.")
    st.caption(f"Saved price collection fetched {metadata['fetched_at']}")
    if st.button("Refresh this barcode's dated prices", disabled=offline):
        try:
            st.session_state["workspace_price_result"] = {"code": code, "result": fetch_observations(code)}
        except ValueError as exc:
            st.error(str(exc))
    saved = st.session_state.get("workspace_price_result", {})
    if saved.get("code") == code:
        result = saved["result"]
        frame = pd.DataFrame(result["observations"])
        st.caption(f"{result['notice']} Fetched {result['fetched_at']} · ODbL-1.0")
        if not result["complete_query"]:
            st.warning("Showing at most 100 observations; this is a partial history.")
    history_panel(frame, code)


def imported_history() -> None:
    """Keep personal observations in the session; users control CSV persistence and deletion."""
    st.subheader("Your dated observations")
    st.write("Import your own receipts or sourced observations for one or more products. Records stay in this browser session and never enter model training. Download a CSV to keep them; clear the session data when finished.")
    st.caption("Quantity is the total quantity purchased at the recorded price. Use stable IDs and variant names, and HTTPS evidence links. Personal data and receipt images are not needed.")
    st.download_button("Download empty CSV template", ",".join(COLUMNS)+"\n",
                       file_name="observations_template.csv", mime="text/csv")
    with st.expander("Add an observation from your own evidence"):
        observation_form()
    upload = st.file_uploader("Observation CSV (UTF-8, at most 2 MB)", type=["csv"])
    if upload is not None and st.button("Validate and replace session observations"):
        try:
            validated = read_csv(upload.getvalue())
            st.session_state["observations"] = validated
            st.success(f"Imported {len(validated)} observations. Sources are user-supplied, not independently verified.")
        except ValueError as exc:
            st.error(str(exc))
    if "observations" not in st.session_state:
        st.info("Upload real dated observations to analyse history and pack changes.")
        return
    frame = st.session_state["observations"]
    if st.button("Clear session observations"):
        del st.session_state["observations"]
        st.rerun()
    st.download_button("Save observations CSV", export_csv(frame[COLUMNS]),
                       file_name="my_observations.csv", mime="text/csv")
    with st.expander("Compare recent quotes across stores"):
        offers_panel(frame)
    # Stepwise selectors guarantee an explicit product/store/currency identity.
    selected = frame
    for column in ["product_id", "variant", "store", "currency"]:
        value = st.selectbox(column.replace("_", " ").title(), selected[column].unique(), key=f"obs_{column}")
        selected = selected[selected[column] == value]
    st.dataframe(selected, hide_index=True)
    st.caption("Analysis below uses user-supplied evidence. A valid CSV is not independent verification.")
    sizes = selected[["quantity", "unit"]].drop_duplicates()
    size = st.selectbox("Exact pack for price history", list(sizes.itertuples(index=False, name=None)))
    series = daily_series(selected[(selected.quantity == size[0]) & (selected.unit == size[1])])
    st.line_chart(series.set_index("date")["price"], y_label=selected.currency.iloc[0])
    result = forecast_next_day(series)
    st.write("Next-day forecast assessment")
    st.json(result)
    st.download_button("Download forecast assessment", json.dumps(result, indent=2),
                       file_name="forecast_assessment.json", mime="application/json")
    confirmed = st.checkbox("These records track the same variant over time, not different packs sold together")
    if st.button("Analyse pack-size changes"):
        try:
            changes = pack_changes(selected, confirmed)
            if changes.empty:
                st.info("At least two distinct observation dates are needed.")
            else:
                st.dataframe(changes, hide_index=True)
                st.bar_chart(changes.set_index("to_date")[["quantity_reduction_pct", "unit_price_increase_pct"]],
                             y_label="Change (%)")
                st.download_button("Export pack changes", export_csv(changes),
                                   file_name="pack_changes.csv", mime="text/csv")
        except ValueError as exc:
            st.error(str(exc))


def offers_panel(frame: pd.DataFrame) -> None:
    """Expose exact-pack quote comparison without calling user observations live offers."""
    st.caption("Uses only quotes dated today or yesterday. Match the same product and pack; include the same taxes, delivery and membership conditions in each total price.")
    selected = frame
    for column in ["product_id", "variant", "currency"]:
        value = st.selectbox(column.replace("_", " ").title(), selected[column].unique(), key=f"offer_{column}")
        selected = selected[selected[column] == value]
    confirmed = st.checkbox("These are identical packs under the same purchase conditions", key="offers_confirmed")
    if st.button("Compare sourced store quotes"):
        try:
            result = compare_observed_offers(selected, confirmed)
            st.dataframe(result, hide_index=True)
            st.caption("Rank 1 is the lowest supplied quote, not a guarantee of the lowest available market price.")
            st.download_button("Export quote comparison", export_csv(result), file_name="store_quotes.csv", mime="text/csv")
        except ValueError as exc:
            st.warning(str(exc))


def observation_form() -> None:
    """Accept a dated source-backed manual quote with the same validation as CSV imports."""
    with st.form("manual_observation"):
        record = {}
        for column, label in [("product_id", "Stable product ID or barcode"), ("name", "Product name"),
                              ("variant", "Variant (flavour/model)"), ("store", "Store / retailer")]:
            record[column] = st.text_input(label, key=f"manual_{column}")
        record["currency"] = st.selectbox("Quote currency", ["INR", "EUR", "USD", "GBP"])
        record["date"] = st.date_input("Observation date", value=date.today(), max_value=date.today()).isoformat()
        record["price"] = st.number_input("Total price paid", min_value=.01, value=None)
        record["quantity"] = st.number_input("Total quantity purchased", min_value=.01, value=None)
        record["unit"] = st.selectbox("Quantity unit", ["g", "kg", "ml", "l", "count"])
        record["source_url"] = st.text_input("HTTPS source / evidence link")
        submitted = st.form_submit_button("Add to my session observations")
    if submitted:
        previous = st.session_state.get("observations", pd.DataFrame(columns=COLUMNS))
        try:
            incoming = validate_observations(pd.DataFrame([record]))
            combined = incoming if previous.empty else pd.concat([previous, incoming], ignore_index=True)
            st.session_state["observations"] = validate_observations(combined)
            st.success("Observation added to this session. Download the CSV to retain it.")
        except ValueError as exc:
            st.error(str(exc))


def workspace_page(data: pd.DataFrame, model_loader) -> None:
    """One entry point for product identity, price/pack evidence and user observations."""
    st.title("Product Workspace")
    st.write("Choose an evidence source, select a product, and analyse what its data supports.")
    source = st.radio("Evidence source", ["Historical marketplace listing", "Food barcode / dated prices",
                                         "My observations", "Pack value comparison"], horizontal=True,
                      key="workspace_source")
    if source == "Food barcode / dated prices":
        food_workspace()
    elif source == "My observations":
        imported_history()
    elif source == "Pack value comparison":
        unit_page()
    else:
        query = st.text_input("Search both historical catalogues", placeholder="Product name")
        matches = search(data, query).head(200)
        if matches.empty:
            st.info("No matching listing. Try fewer words.")
            return
        key = st.selectbox("Selected listing", matches.key,
                           format_func=lambda k: f"{matches.loc[matches.key == k, 'platform'].iloc[0]} · {matches.loc[matches.key == k, 'name'].iloc[0]}")
        row = matches[matches.key == key].iloc[0].to_dict()
        st.caption(f"Identity: {key} · INR · observed {row.get('observed_at') or 'date unknown'}")
        st.info("Historical marketplace evidence. This listing is not a live offer or a verified match to a food barcode.")
        assessment_panel(row, model_loader())
