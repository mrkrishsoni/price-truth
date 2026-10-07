"""Process-wide cached data and model, plus a background warm-up of SHAP and PDF export."""
import json
import threading

import streamlit as st

from price_truth.data import load_catalogue
from price_truth.model import load_model
from price_truth.paths import REPORTS


@st.cache_data(show_spinner="Loading catalogue…")
def catalogue():
    """Cache read-only catalogue data across reruns and sessions."""
    return load_catalogue()


@st.cache_resource(show_spinner="Loading model…")
def model():
    """Cache the trusted locally generated model across sessions."""
    return load_model()


@st.cache_data
def report(name: str) -> dict | None:
    """Read a saved evaluation report, or None when it is absent."""
    path = REPORTS / name
    return json.loads(path.read_text()) if path.exists() else None


def _warm() -> None:
    """Pay one-off import and font-cache costs before the first visitor asks for them."""
    try:
        from price_truth.exports import assessment_pdf
        from price_truth.model import assess

        frame, bundle = load_catalogue(), load_model()
        row = frame.iloc[0].to_dict()
        result = assess(bundle, row, row["selling_price"], row["listed_price"])
        assessment_pdf(row, result, row["selling_price"], row["listed_price"])
    except Exception:  # noqa: BLE001 - warm-up is an optimisation; real calls report their own errors.
        pass


@st.cache_resource
def start_warmup() -> threading.Thread:
    """Start the warm-up once per server process."""
    thread = threading.Thread(target=_warm, name="price-truth-warmup", daemon=True)
    thread.start()
    return thread
