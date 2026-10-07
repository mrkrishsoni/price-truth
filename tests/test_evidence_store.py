"""Collection integrity checks; controlled fixtures never become shipped observations."""
from datetime import UTC, datetime

import pytest

from price_truth.cache import write_json
from price_truth.evidence_store import accumulated_observations, archive_snapshot, history_readiness
from price_truth.price_api import fetch_observations


def snapshot(retrieved="2026-01-02T00:00:00+00:00", price=10):
    """A clearly labelled test-only observation with no contributor identity."""
    return {"source": "https://example.com/test-prices", "license": "test fixture",
            "fetched_at": retrieved, "observations": [
                {"id": 1, "product_code": "00001234", "location_id": 1, "currency": "INR",
                 "price_per": "UNIT", "date": "2026-01-01", "price": price,
                 "duplicate_of": None, "proof_id": 1, "location_type": "shop"}]}


def test_repeated_collection_never_manufactures_history(tmp_path):
    """Repeated retrieval is not a new observed day; corrected values keep an audit trail."""
    original = archive_snapshot(snapshot(), tmp_path)
    assert archive_snapshot(snapshot(), tmp_path) == original
    archive_snapshot(snapshot("2026-01-03T00:00:00+00:00", 12), tmp_path)
    frame, metadata = accumulated_observations(tmp_path)
    assert metadata["snapshots"] == 2 and len(frame) == 1
    assert frame.iloc[0].price == 12 and frame.iloc[0].date == "2026-01-01"
    readiness = history_readiness(frame).iloc[0]
    assert readiness.distinct_dates == 1 and readiness.history_status == "insufficient_history"
    assert not readiness.forecast_authorized


def test_incomplete_archive_is_explicit_error(tmp_path):
    """A broken archive cannot silently disappear from a reported collection."""
    (tmp_path / "broken.json").write_text("{")
    with pytest.raises(ValueError, match="Invalid archived"):
        accumulated_observations(tmp_path)
    with pytest.raises(ValueError):
        archive_snapshot({**snapshot(), "fetched_at": "2026-01-01"}, tmp_path)


def test_schema_corrupt_and_wrong_identity_caches_are_not_evidence(tmp_path, monkeypatch):
    """Valid JSON alone does not establish a valid cache or product identity."""
    from price_truth import price_api
    monkeypatch.setattr(price_api, "EXTERNAL", tmp_path)
    path = tmp_path / "price_cache/00001234.json"
    for record in [{"fetched_at": datetime.now(UTC).isoformat()},
                   {**snapshot(), "complete_query": True,
                    "observations": [{**snapshot()["observations"][0], "product_code": "99999999"}]}]:
        write_json(path, record)
        with pytest.raises(ValueError, match="No saved"):
            fetch_observations("00001234", offline=True)
