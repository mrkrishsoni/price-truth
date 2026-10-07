"""Live-search schema and honest cached fallback using retrieved product records."""
import json

import pytest
import requests

from price_truth import external


def test_real_saved_name_search():
    """A downloaded search is usable offline and carries attribution."""
    result = external.search_products("Maggi", offline=True)
    assert result["mode"] == "cached"
    assert result["products"] and result["source_url"].startswith("https://search.openfoodfacts.org")


@pytest.mark.parametrize("query", ["", "x", "x" * 101])
def test_invalid_search(query):
    """Bound query size before network use."""
    with pytest.raises(ValueError):
        external.search_products(query)


def test_search_success_and_timeout(monkeypatch, tmp_path):
    """Use retrieved hits as the response fixture and then simulate an outage."""
    saved = external.search_products("Maggi", offline=True)
    monkeypatch.setattr(external, "EXTERNAL", tmp_path)
    monkeypatch.setattr(external, "get_json", lambda *a, **k: {"hits": saved["products"]})
    result = external.search_products("Maggi")
    assert result["mode"] == "live" and len(result["products"]) == len(saved["products"])
    def timeout(*args, **kwargs):
        raise requests.Timeout()
    monkeypatch.setattr(external, "get_json", timeout)
    assert external.search_products("Maggi")["mode"] == "cached"
    with pytest.raises(ValueError, match="unavailable"):
        external.search_products("unknown query")
    cache = next((tmp_path / "search").glob("*.json"))
    assert json.loads(cache.read_text())["query"] == "Maggi"
