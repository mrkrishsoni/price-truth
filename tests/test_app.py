"""End-to-end widget interactions using Streamlit's official AppTest harness."""
import pytest
from streamlit.testing.v1 import AppTest

from price_truth.paths import ROOT


def application(page="Overview"):
    """Load a page through the same entrypoint users run."""
    app = AppTest.from_file(str(ROOT / "app.py"), default_timeout=30).run()
    if page != "Overview":
        app.sidebar.radio[0].set_value(page).run()
    return app


@pytest.mark.parametrize("page", ["Overview", "Discount Checker", "Live Pack Lookup", "Unit Price Compare",
                                  "Buy Timing & History", "Shrink Timeline", "Platform Catalogue", "Evidence & Methods"])
def test_pages_render(page):
    """Every navigation destination must load without a Python exception."""
    app = application(page)
    assert not app.exception


def test_checker_runs_real_model():
    """Submitting the quote displays computed metrics and an explanation chart."""
    app = application("Discount Checker")
    app.button[0].click().run()
    assert not app.exception
    assert len(app.metric) == 3
    assert len(app.get("plotly_chart")) == 1


def test_unit_comparison_flow():
    """Entering comparable packs produces a best-value result."""
    app = application("Unit Price Compare")
    app.number_input(key="price1").set_value(10)
    app.number_input(key="quantity1").set_value(100)
    app.number_input(key="price2").set_value(15)
    app.number_input(key="quantity2").set_value(200)
    app.button[0].click().run()
    assert not app.exception
    assert "Pack 2" in app.success[0].value


def test_offline_lookup_flow():
    """The real saved example can be displayed without network access."""
    app = application("Live Pack Lookup")
    app.checkbox[1].check()
    app.button[1].click().run()
    assert not app.exception
    assert "Offline" in app.info[0].value
