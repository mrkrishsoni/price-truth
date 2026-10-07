"""Simple presentation functions, ready for later visual redesign."""
import json

import pandas as pd
import plotly.graph_objects as go
import streamlit as st

from price_truth.calculations import compare_packs, shrink_change
from price_truth.catalogue import export_csv, safe_url, search
from price_truth.exports import assessment_pdf
from price_truth.external import cached_products, lookup_product, search_products
from price_truth.history import load_observations, series_for, timing_signal
from price_truth.model import assess
from price_truth.paths import DATA


def checker_page(data: pd.DataFrame, bundle: dict) -> None:
    """Assess a selected product's quote with actual model output and SHAP."""
    st.title("True Discount Checker")
    st.caption("A pricing assessment against historical listings—not a fraud verdict or a live price check.")
    platform = st.selectbox("Platform", ["amazon", "flipkart"])
    query = st.text_input("Find a product", placeholder="e.g. cable, television, shirt")
    matches = search(data, query, [platform])
    if matches.empty:
        st.info("No matching products. Try fewer search words.")
        return
    matches = matches.head(200)
    key = st.selectbox("Product (first 200 matches)", matches.key,
                       format_func=lambda k: matches.loc[matches.key == k, "name"].iloc[0])
    row = matches.loc[matches.key == key].iloc[0].to_dict()
    assessment_panel(row, bundle)


def assessment_panel(row: dict, bundle: dict) -> None:
    """Assess the selected identity without asking users to search a second time."""
    key = row["key"]
    st.caption(f"Source category: {row['category_path']}")
    with st.form(f"quote_{key}"):
        listed = st.number_input("Listed reference price (INR)", min_value=.01, value=float(row["listed_price"]))
        selling = st.number_input("Selling price to assess (INR)", min_value=.01, value=float(row["selling_price"]))
        submitted = st.form_submit_button("Assess price")
    if not submitted:
        return
    try:
        result = assess(bundle, row, selling, listed)
    except ValueError as exc:
        st.error(str(exc))
        return
    columns = st.columns(3)
    columns[0].metric("Advertised discount", f"{result['claimed_discount_pct']:.1f}%")
    columns[1].metric("Estimated snapshot price", f"₹{result['estimate']:,.0f}")
    columns[2].metric("Model range", f"₹{result['lower']:,.0f}–{result['upper']:,.0f}")
    st.info(result["status"].replace("_", " ").capitalize())
    st.write(f"{result['support']} training listings share this platform and source subcategory. "
             "Products may differ in specifications; this estimate is not a current fair-value guarantee.")
    st.caption("The interval is calibrated for 90% coverage on comparable data, not 90% confidence "
               "that a discount is real. Listed price influences the estimate.")
    if result["seen_in_training"]:
        st.caption("This catalogue product was used in training. Published evaluation uses separate held-out products.")
    contributions = sorted(result["shap"], key=lambda x: abs(x["contribution"]), reverse=True)
    top, remainder = contributions[:8], sum(x["contribution"] for x in contributions[8:])
    chart = go.Figure(go.Waterfall(
        x=["Baseline"] + [x["feature"] for x in top] + ["Other features", "Prediction"],
        y=[result["base_log"]] + [x["contribution"] for x in top] + [remainder, 0],
        measure=["absolute"] + ["relative"] * (len(top) + 1) + ["total"]))
    chart.update_layout(title="Why the model estimated this price", yaxis_title="log(1 + selling price)")
    st.plotly_chart(chart, width="stretch")
    st.caption("Computed Tree SHAP contributions explain estimated price, not the probability of fraud.")
    document = {**result, "listing_key": row["key"], "platform": row["platform"],
                "quoted_price": selling, "listed_price": listed, "currency": "INR",
                "scope": "historical_price_assessment_not_fraud_verification"}
    st.download_button("Download assessment", json.dumps(document, indent=2),
                       file_name="price_assessment.json", mime="application/json", on_click="ignore")
    st.download_button("Download assessment PDF", assessment_pdf(row, result, selling, listed),
                       file_name="price_assessment.pdf", mime="application/pdf", on_click="ignore")
    url = safe_url(row["product_url"])
    if url:
        st.link_button("Open original product listing", url)


def lookup_page() -> None:
    """Look up barcodes live or search names among real saved examples."""
    st.title("Live Pack Lookup")
    with st.expander("Search live by product name"):
        with st.form("name_search"):
            live_name = st.text_input("Product name", placeholder="e.g. Maggi")
            cached_search = st.checkbox("Use saved search results", value=False)
            search_submitted = st.form_submit_button("Search food database")
        if search_submitted:
            try:
                found = search_products(live_name, cached_search)
                st.session_state["food_search_results"] = found
            except ValueError as exc:
                st.error(str(exc))
        if "food_search_results" in st.session_state:
            found = st.session_state["food_search_results"]
            st.caption(f"{found['mode']} results for {found['query']} · retrieved {found['fetched_at']}")
            st.dataframe(pd.DataFrame(found["products"]), hide_index=True)
            st.caption("Copy a result's barcode into the lookup below for pack details.")
    products = cached_products()
    name = st.text_input("Search saved product names", placeholder="Optional offline search")
    matches = [p for p in products if name.lower() in p.get("product_name", "").lower()]
    default = ""
    if matches:
        selection = st.selectbox("Saved examples", matches,
                                 format_func=lambda p: f"{p.get('product_name', 'Unknown')} · {p.get('code', '')}")
        default = selection.get("code", "")
    with st.form("lookup"):
        code = st.text_input("Barcode", value=default)
        offline = st.checkbox("Use saved response (offline)", value=False)
        submitted = st.form_submit_button("Look up pack")
    if submitted:
        try:
            result = lookup_product(code, offline)
        except ValueError as exc:
            st.error(str(exc))
            return
        product = result["product"]
        st.subheader(product.get("product_name") or "Name unavailable")
        st.table({"Field": ["Brand", "Pack size", "Category"],
                  "Value": [product.get("brands") or "Unavailable", product.get("quantity") or "Unavailable",
                            product.get("categories") or "Unavailable"]})
        st.info(result["notice"])
        st.caption(f"Retrieved: {result['fetched_at']} · Open Food Facts · ODbL")
        st.link_button("Source record", result["source_url"])


def unit_page() -> None:
    """Compare two user-entered pack options without storing the input."""
    st.title("Unit Price Compare")
    st.write("Enter two pack sizes of the same product. All prices must use the same currency.")
    with st.form("units"):
        currency = st.selectbox("Currency", ["INR", "EUR", "USD", "GBP"])
        packs = []
        for index, column in enumerate(st.columns(2), 1):
            with column:
                st.subheader(f"Pack {index}")
                price = st.number_input("Price", min_value=.01, value=None, key=f"price{index}")
                quantity = st.number_input("Quantity per pack", min_value=.01, value=None, key=f"quantity{index}")
                unit = st.selectbox("Unit", ["g", "kg", "ml", "l", "count"], key=f"unit{index}")
                count = st.number_input("Number of packs", min_value=1, value=1, key=f"count{index}")
                packs.append({"name": f"Pack {index}", "price": price, "quantity": quantity,
                              "unit": unit, "packs": count, "currency": currency})
        submitted = st.form_submit_button("Compare value")
    if submitted:
        if any(p["price"] is None or p["quantity"] is None for p in packs):
            st.error("Enter a price and quantity for both packs.")
            return
        try:
            result = compare_packs(packs)
        except ValueError as exc:
            st.error(str(exc))
            return
        st.dataframe(pd.DataFrame(result)[["name", "value", "basis", "currency"]], hide_index=True)
        equal = abs(result[0]["value"] - result[1]["value"]) < 1e-9
        st.success("Both packs have the same unit price." if equal else f"{result[0]['name']} has the lower unit price.")


def history_page() -> None:
    """Explore real observations without extrapolating seasonal sale claims."""
    st.title("Buy Timing & History")
    example = st.selectbox("Observation collection", ["India / INR", "International history example / EUR"]) != "India / INR"
    try:
        frame, metadata = load_observations(example)
    except FileNotFoundError:
        st.info("No downloaded observations yet. Follow the data acquisition step in README.md.")
        return
    st.caption(f"Open Prices · ODbL · retrieved {metadata['fetched_at']}")
    if example:
        st.info("Real French-store observations in EUR. This example does not represent Indian prices.")
    options = frame[frame.product_code.notna() & (frame.location_type == "shop")].copy()
    if options.empty:
        st.info("No identified retail-store observations available in this collection.")
        return
    options["label"] = options.product_name.fillna(options.product_code) + " · " + options.product_code
    labels = options.groupby("label").size().sort_values(ascending=False).index.tolist()
    label = st.selectbox("Product", labels)
    product = options[options.label == label]
    location = st.selectbox("Store", product.location_id.unique(),
                            format_func=lambda i: str(product.loc[product.location_id == i, "location_name"].iloc[0]) + f" ({i})")
    unit = st.selectbox("Recorded price basis", product[product.location_id == location].price_per.fillna("UNKNOWN").unique())
    code, currency = product.iloc[0]["product_code"], product.iloc[0]["currency"]
    series = series_for(frame, code, location, currency, unit)
    st.line_chart(series.set_index("date")["price"], y_label=f"Observed price ({currency})")
    st.dataframe(product[product.location_id == location][["date", "price", "currency", "source_url"]], hide_index=True)
    quote = st.number_input(f"Your current quote ({currency})", min_value=.01, value=None)
    if st.button("Compare with history"):
        if quote is None:
            st.error("Enter the quote you want to compare.")
            return
        result = timing_signal(series, quote)
        st.info(result["status"].replace("_", " ").capitalize())
        st.write(result["message"])
        if "median" in result:
            st.metric("Observed historical median", f"{currency} {result['median']:.2f}")
            st.caption(f"{result['days']} prior dates; {result['span_days']} days of coverage; "
                       f"latest prior observation {result['age_days']} days ago.")
    if unit == "UNKNOWN":
        st.warning("The source does not specify the price basis. Confirm the pack and purchase conditions "
                   "before using a comparison; the barcode alone cannot verify unchanged packaging.")
    st.caption("A low historical price does not predict tomorrow's price. Sparse or stale histories abstain "
               "from a timing signal. No sale-calendar dates or future prices are invented.")


def shrink_page() -> None:
    """Show a sourced before/after sequence without inventing exact observation dates."""
    st.title("Shrink Timeline")
    evidence = json.loads((DATA / "evidence/shrink_cases.json").read_text())
    case = st.selectbox("Documented case", evidence["cases"], format_func=lambda c: c["product"])
    result = shrink_change(case["old_quantity"], case["new_quantity"], case["old_price"], case["new_price"])
    columns = st.columns(2)
    columns[0].metric("Quantity reduction", f"{result['quantity_reduction_pct']:.1f}%")
    columns[1].metric("Unit-price increase", f"{result['unit_price_increase_pct']:.1f}%")
    st.table(pd.DataFrame([
        {"Period": case["old_period"], "Quantity (g)": case["old_quantity"], "Price (INR)": case["old_price"]},
        {"Period": case["new_period"], "Quantity (g)": case["new_quantity"], "Price (INR)": case["new_price"]},
    ]))
    st.bar_chart(pd.DataFrame({"Quantity (g)": [case["old_quantity"], case["new_quantity"]]}, index=["Earlier pack", "Reported later pack"]))
    st.caption(f"Reported {evidence['reported_on']} · {evidence['source_name']}")
    st.write(case["notes"])
    st.link_button("Read the evidence", evidence["source_url"])


def catalogue_page(data: pd.DataFrame) -> None:
    """Search both source catalogues without claiming exact cross-platform matches."""
    st.title("Platform Catalogue")
    st.info("Historical catalogue search across Amazon and Flipkart. Search matches can be different "
            "products or variants; this is not a live same-product price aggregator.")
    query = st.text_input("Search product names")
    platforms = st.multiselect("Platforms", ["amazon", "flipkart"], default=["amazon", "flipkart"])
    result = search(data, query, platforms)
    columns = ["platform", "name", "listed_price", "selling_price", "discount_pct", "observed_at"]
    st.caption(f"{len(result):,} matches · INR · displaying up to 500")
    st.dataframe(result[columns].head(500), hide_index=True)
    st.download_button("Download results CSV", export_csv(result[columns]),
                       file_name="historical_catalogue_results.csv", mime="text/csv")
