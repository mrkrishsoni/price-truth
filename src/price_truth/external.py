"""Read-only Open Food Facts integration with explicit cached fallback."""
import hashlib
import json
import re
from datetime import UTC, datetime
from pathlib import Path

import requests

from price_truth.cache import fresh, read_json, write_json
from price_truth.paths import EXTERNAL

HEADERS = {"User-Agent": "PriceTruthAcademic/0.1 (https://price-truth.netlify.app/)"}


def get_json(url: str, params: dict | None = None) -> dict:
    """Read a public API using a bounded request; never silently accept HTML."""
    response = requests.get(url, params=params, headers=HEADERS, timeout=(5, 15))
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, dict):
        raise ValueError("The API returned an unexpected response.")
    return payload


def lookup_product(code: str, offline: bool = False, cache_dir: Path | None = None) -> dict:
    """Fetch a numeric barcode, falling back only to a previously saved real response."""
    code = code.strip()
    if not re.fullmatch(r"[0-9]{8,14}", code):
        raise ValueError("Enter a barcode containing 8 to 14 digits.")
    cache_dir = cache_dir or EXTERNAL / "off"
    path = cache_dir / f"{code}.json"
    cached = read_json(path)
    if fresh(cached) and not offline:
        return {**cached, "mode": "cached", "notice": "Recently retrieved response (one-hour cache)."}
    if offline:
        if not cached:
            raise ValueError("This barcode is not in the offline cache. Try a live lookup.")
        return {**cached, "mode": "cached", "notice": "Offline saved response"}
    url = f"https://world.openfoodfacts.org/api/v2/product/{code}.json"
    try:
        result = get_json(url, {"fields": "code,product_name,brands,quantity,product_quantity,"
                              "product_quantity_unit,categories,countries,last_modified_t"})
    except (requests.RequestException, ValueError) as exc:
        if cached:
            return {**cached, "mode": "cached",
                    "notice": f"Live lookup unavailable ({type(exc).__name__}); showing saved data."}
        raise ValueError("Live lookup is unavailable and no cached record exists.") from exc
    if result.get("status") != 1 or not result.get("product"):
        raise ValueError("No product found for this barcode.")
    record = {"product": result["product"], "source_url": url,
              "fetched_at": datetime.now(UTC).isoformat(), "license": "ODbL"}
    write_json(path, record)
    return {**record, "mode": "live", "notice": "Live Open Food Facts response"}


def cached_products() -> list[dict]:
    """Expose saved names for offline browsing without inventing product information."""
    directory = EXTERNAL / "off"
    return [json.loads(path.read_text())["product"] for path in sorted(directory.glob("*.json"))]


def search_products(query: str, offline: bool = False) -> dict:
    """Search the official full-text API, retaining a dated real-response fallback."""
    query = query.strip()
    if not 2 <= len(query) <= 100:
        raise ValueError("Use between 2 and 100 characters for a product search.")
    cache = EXTERNAL / "search" / (hashlib.sha256(query.lower().encode()).hexdigest() + ".json")
    cached = read_json(cache)
    if fresh(cached) and not offline:
        return {**cached, "mode": "cached"}
    if offline:
        if not cached:
            raise ValueError("No saved results for this search. Try the barcode examples below.")
        return {**cached, "mode": "cached"}
    url = "https://search.openfoodfacts.org/search"
    try:
        response = get_json(url, {"q": query, "page_size": 10})
        hits = response["hits"]
        if not isinstance(hits, list):
            raise ValueError("Unexpected search response.")
    except (requests.RequestException, ValueError, KeyError) as exc:
        if cached:
            return {**cached, "mode": "cached"}
        raise ValueError("Live search is unavailable. Use a saved barcode example below.") from exc
    products = [{"code": h.get("code"), "product_name": h.get("product_name_en") or h.get("product_name"),
                 "brands": h.get("brands"), "quantity": h.get("quantity")}
                for h in hits if re.fullmatch(r"\d{8,14}", str(h.get("code", "")))]
    result = {"query": query, "products": products, "source_url": url,
              "fetched_at": datetime.now(UTC).isoformat(), "license": "ODbL"}
    write_json(cache, result)
    return {**result, "mode": "live"}
