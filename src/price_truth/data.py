"""Normalize real supplied listings and preserve an audit of every exclusion."""
import hashlib
import json
import re
from datetime import UTC, datetime

import pandas as pd

from price_truth.paths import DATA, PROCESSED, REPORTS

SOURCES = {
    "amazon": (DATA / "amazon/amazon.csv", "product_id", "actual_price"),
    "flipkart": (DATA / "flipkart/flipkart_com-ecommerce_sample.csv", "pid", "retail_price"),
}
ROOTS = {
    "Computers&Accessories": "Computers", "Computers": "Computers",
    "Electronics": "Electronics", "Mobiles & Accessories": "Electronics",
    "Cameras & Accessories": "Electronics", "Home&Kitchen": "Home and kitchen",
    "Kitchen & Dining": "Home and kitchen", "Home Furnishing": "Home and kitchen",
    "Clothing": "Clothing", "Jewellery": "Jewellery", "Footwear": "Footwear",
    "OfficeProducts": "Office supplies", "Pens & Stationery": "Office supplies",
    "Beauty and Personal Care": "Personal care", "Health&PersonalCare": "Personal care",
}


def numeric(series: pd.Series) -> pd.Series:
    """Parse source numeric strings; unavailable values stay missing."""
    cleaned = series.str.replace(r"[₹,%\s]", "", regex=True)
    return pd.to_numeric(cleaned, errors="coerce").replace([float("inf"), -float("inf")], float("nan"))


def category_parts(value: str, platform: str) -> list[str]:
    """Read each source's category syntax without executing source text."""
    if platform == "amazon":
        return value.split("|")
    try:
        parsed = json.loads(value)
        return parsed[0].split(" >> ") if isinstance(parsed, list) and parsed else []
    except (ValueError, TypeError, AttributeError):
        return []


def name_group(name: str) -> str:
    """Group matching titles and colour/size variants conservatively for evaluation."""
    value = re.sub(r"\([^)]*\)", "", name.lower())
    value = re.sub(r"\b(black|white|blue|red|green|grey|gray|pink|gold|silver|navy)\b", "", value)
    value = re.sub(r"[^a-z0-9]+", " ", value).strip()
    return value


def normalize(platform: str, raw: pd.DataFrame) -> pd.DataFrame:
    """Map a source to common fields; listed price is not a historical price."""
    _, id_field, list_field = SOURCES[platform]
    amazon = platform == "amazon"
    category_field = "category" if amazon else "product_category_tree"
    parts = raw[category_field].map(lambda v: category_parts(v, platform))
    out = pd.DataFrame({"platform": platform, "source_row": raw.index + 2,
                        "product_id": raw[id_field], "name": raw.product_name,
                        "listed_price": numeric(raw[list_field]),
                        "selling_price": numeric(raw.discounted_price), "currency": "INR"})
    out["key"] = platform + ":" + out.product_id
    out["category_path"] = parts.map(lambda p: " > ".join(p))
    out["category_root"] = parts.map(lambda p: p[0] if p else "Unknown")
    out["category_group"] = out.category_root.map(ROOTS).fillna("Other")
    # Three levels avoid Flipkart's brand/product-name leaves; this is a source category,
    # not a claim that every member is an interchangeable product.
    out["subcategory"] = parts.map(lambda p: " > ".join(p[:3]) if len(p) > 1 else "Unknown")
    out["rating"] = numeric(raw["rating" if amazon else "product_rating"])
    out.loc[~out.rating.between(0, 5), "rating"] = float("nan")
    out["rating_count"] = numeric(raw.rating_count) if amazon else float("nan")
    out["brand"] = "" if amazon else raw.brand
    out["observed_at"] = "" if amazon else pd.to_datetime(raw.crawl_timestamp, utc=True).astype(str)
    out["product_url"] = raw["product_link" if amazon else "product_url"]
    out["name_group"] = out.name.map(name_group)
    return out


def clean_source(frame: pd.DataFrame) -> tuple[pd.DataFrame, pd.DataFrame, dict]:
    """Quarantine ambiguous prices and deduplicate IDs without fabricating recency."""
    bad_price = (frame.listed_price.isna() | frame.selling_price.isna()
                 | (frame.listed_price <= 0) | (frame.selling_price <= 0)
                 | (frame.selling_price > frame.listed_price))
    reasons = pd.Series("", index=frame.index)
    reasons.loc[bad_price] = "invalid_or_missing_price"
    conflicts = frame.groupby("key")[["listed_price", "selling_price"]].nunique().max(axis=1)
    conflict_keys = set(conflicts[conflicts > 1].index)
    reasons.loc[frame.key.isin(conflict_keys)] = "conflicting_prices_without_reliable_history"
    candidates = frame[reasons == ""].copy()
    duplicates = candidates.duplicated("key", keep="first")
    reasons.loc[candidates.index[duplicates]] = "repeated_product_id_first_source_row_retained"
    clean = frame[reasons == ""].copy()
    clean["discount_pct"] = 100 * (1 - clean.selling_price / clean.listed_price)
    excluded = frame[reasons != ""].copy()
    excluded["reason"] = reasons[reasons != ""]
    summary = {"raw_rows": len(frame), "raw_unique_products": frame.key.nunique(),
               "clean_rows": len(clean), "exclusions": reasons[reasons != ""].value_counts().to_dict(),
               "missing_rating": int(clean.rating.isna().sum()),
               "missing_rating_count": int(clean.rating_count.isna().sum()),
               "conflicting_product_ids": sorted(conflict_keys)}
    return clean, excluded, summary


def build_catalogue() -> dict:
    """Write the combined catalogue and source hashes, leaving both originals intact."""
    PROCESSED.mkdir(parents=True, exist_ok=True)
    REPORTS.mkdir(parents=True, exist_ok=True)
    clean_frames, excluded_frames, sources = [], [], {}
    for platform, (path, _, _) in SOURCES.items():
        raw = pd.read_csv(path, dtype=str, keep_default_na=False)
        clean, excluded, summary = clean_source(normalize(platform, raw))
        clean_frames.append(clean)
        excluded_frames.append(excluded)
        sources[platform] = {**summary, "file": str(path.relative_to(DATA.parent)),
                             "sha256": hashlib.sha256(path.read_bytes()).hexdigest()}
    catalogue = pd.concat(clean_frames, ignore_index=True)
    catalogue.to_csv(PROCESSED / "catalogue.csv", index=False)
    pd.concat(excluded_frames, ignore_index=True).to_csv(PROCESSED / "excluded.csv", index=False)
    report = {"generated_at": datetime.now(UTC).isoformat(), "sources": sources,
              "combined_rows": len(catalogue), "synthetic_observations": 0,
              "authenticity_labels": 0,
              "policy": "Keep platforms distinct; no currency conversion, no fabricated dates or ratings; "
                        "quarantine all conflicting price IDs; retain first source row for other duplicate IDs."}
    (REPORTS / "data_audit.json").write_text(json.dumps(report, indent=2))
    return report


def load_catalogue() -> pd.DataFrame:
    """Load generated data, requiring an explicit build if it is missing."""
    frame = pd.read_csv(PROCESSED / "catalogue.csv", dtype={"product_id": str})
    for column in ["brand", "observed_at", "subcategory", "category_path"]:
        frame[column] = frame[column].fillna("")
    return frame


if __name__ == "__main__":
    print(json.dumps(build_catalogue(), indent=2))
