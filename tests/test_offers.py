"""Prevent misleading comparisons using explicit controlled quote fixtures."""
from datetime import date

import pandas as pd
import pytest

from price_truth.offers import compare_observed_offers


def quotes():
    """Test-only quotes with equivalent quantities and an outdated lower price."""
    row = {"product_id": "00012345", "name": "Test food", "variant": "plain", "currency": "INR",
           "date": "2026-10-06", "price": 100, "quantity": 1000, "unit": "g",
           "store": "Store A", "source_url": "https://example.com/a"}
    return pd.DataFrame([row, {**row, "store": "Store B", "quantity": 1, "unit": "kg", "price": 90},
                         {**row, "store": "Store B", "price": 50, "date": "2026-10-01"}])


def test_comparison_respects_dates_packs_and_conditions():
    """The stale cheap quote cannot win a recent comparison."""
    result = compare_observed_offers(quotes(), True, date(2026, 10, 6))
    assert result.store.tolist() == ["Store B", "Store A"]
    assert result.price.tolist() == [90, 100]
    assert result.price_rank.tolist() == [1, 2]
    with pytest.raises(ValueError, match="Confirm"):
        compare_observed_offers(quotes(), today=date(2026, 10, 6))
    with pytest.raises(ValueError, match="at least two"):
        compare_observed_offers(quotes(), True, date(2026, 10, 8))


@pytest.mark.parametrize("column,value", [("currency", "USD"), ("variant", "other"),
                                         ("quantity", 2), ("unit", "l")])
def test_incompatible_quotes_rejected(column, value):
    """Currencies, variants and sizes cannot be merged into a best-price claim."""
    frame = quotes()
    frame.loc[1, column] = value
    with pytest.raises(ValueError):
        compare_observed_offers(frame, True, date(2026, 10, 6))


def test_same_day_price_conflict_and_ties():
    """Conflicting prices need reconciliation; equal valid prices share rank one."""
    frame = quotes()
    frame.loc[2, "date"] = "2026-10-06"
    with pytest.raises(ValueError, match="conflicting"):
        compare_observed_offers(frame, True, date(2026, 10, 6))
    frame["price"] = 100
    result = compare_observed_offers(frame, True, date(2026, 10, 6))
    assert result.price_rank.tolist() == [1, 1]
