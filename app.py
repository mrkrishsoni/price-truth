"""Price Truth Streamlit entrypoint; business logic lives in the price_truth package."""
import json

import streamlit as st

from price_truth.data import load_catalogue
from price_truth.model import load_model
from price_truth.paths import REPORTS
from price_truth.ui import (
    catalogue_page,
    checker_page,
    history_page,
    lookup_page,
    shrink_page,
    unit_page,
)
from price_truth.workspace import workspace_page

st.set_page_config(page_title="Price Truth", page_icon="₹", layout="wide")


@st.cache_data
def catalogue():
    """Cache read-only catalogue data across reruns."""
    return load_catalogue()


@st.cache_resource
def model():
    """Cache the locally generated model across sessions."""
    return load_model()


def main() -> None:
    """Route the functional application without coupling features to page styling."""
    st.sidebar.title("Price Truth")
    st.sidebar.caption("Truth. Transparency. Trust.")
    page = st.sidebar.radio("Explore", ["Overview", "Product Workspace", "Discount Checker", "Live Pack Lookup",
                                        "Unit Price Compare", "Buy Timing & History",
                                        "Shrink Timeline", "Platform Catalogue", "Evidence & Methods"])
    st.sidebar.caption("Academic prototype · real source data")
    try:
        data = catalogue()
    except FileNotFoundError:
        st.error("The catalogue is not prepared. Follow the setup steps in README.md.")
        return
    if page == "Overview":
        st.title("Know what your price means")
        st.write("Check a discount, compare pack sizes, and explore the evidence behind a price.")
        columns = st.columns(3)
        columns[0].metric("Catalogue listings", f"{len(data):,}")
        columns[1].metric("Platforms", data.platform.nunique())
        columns[2].metric("Generated training records", "0")
        st.info("Catalogue prices are historical snapshots: Flipkart 2015–2016; Amazon date unknown. "
                "They are not live offers or verified fraud labels.")
        st.write("Start with **Product Workspace** in the sidebar to assess a listing, look up a pack, or add your own dated observations.")
        st.write("**Discount Checker:** estimated selling-price range and a computed explanation.\n\n"
                 "**Live Pack Lookup:** barcode data from Open Food Facts, with saved offline examples.\n\n"
                 "**Unit Price Compare:** compare like-for-like pack sizes.\n\n"
                 "**Buy Timing & History:** compare a quote with real dated observations.\n\n"
                 "**Shrink Timeline:** documented quantity changes with source links.")
    elif page == "Product Workspace":
        try:
            workspace_page(data, model)
        except FileNotFoundError:
            st.error("A required data or model file is missing. Follow the setup steps in README.md.")
    elif page == "Discount Checker":
        try:
            checker_page(data, model())
        except FileNotFoundError:
            st.error("The trained model is missing. Follow the training step in README.md.")
    elif page == "Live Pack Lookup":
        lookup_page()
    elif page == "Unit Price Compare":
        unit_page()
    elif page == "Buy Timing & History":
        history_page()
    elif page == "Shrink Timeline":
        shrink_page()
    elif page == "Platform Catalogue":
        catalogue_page(data)
    else:
        st.title("Evidence & methods")
        st.write("The model predicts observed selling prices; it does not prove seller dishonesty. "
                 "There are no generated prices, dates, or authenticity labels in training.")
        for filename in ["data_audit.json", "model_evaluation.json"]:
            path = REPORTS / filename
            if path.exists():
                with st.expander(filename):
                    st.json(json.loads(path.read_text()))
        st.write("Sources: supplied Kaggle Amazon and Flipkart listings; "
                 "[Open Food Facts](https://world.openfoodfacts.org) and "
                 "[Open Prices](https://prices.openfoodfacts.org) (ODbL); "
                 "attributed Bloomberg/Financial Express shrinkflation reporting.")


main()
