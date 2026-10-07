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


def test_confirmation_message_and_result_contract():
    """The full confirmation text is shown and results carry an explicit scope label."""
    with pytest.raises(ValueError, match="^Confirm identical product/pack and the same tax, delivery "
                                         "and purchase conditions.$"):
        compare_observed_offers(quotes(), False, date(2026, 10, 6))
    result = compare_observed_offers(quotes(), True, date(2026, 10, 6))
    assert result.columns.tolist() == ["price_rank", "store", "price", "currency", "date",
                                       "age_days", "source_url", "scope"]
    assert result.index.tolist() == [0, 1]
    assert result.age_days.tolist() == [0, 0]
    assert result.scope.eq("Recent user-supplied quotes; availability and completeness "
                           "unverified").all()


def test_yesterday_counts_and_older_quotes_do_not():
    """Quotes dated yesterday are recent; two days old is not."""
    frame = quotes()
    frame.loc[0, "date"] = "2026-10-05"
    result = compare_observed_offers(frame, True, date(2026, 10, 6))
    assert result.age_days.tolist() == [0, 1]
    frame.loc[0, "date"] = "2026-10-04"
    with pytest.raises(ValueError, match="^Need at least two stores with quotes dated today or "
                                         "yesterday.$"):
        compare_observed_offers(frame, True, date(2026, 10, 6))


def test_latest_quote_per_store_and_duplicate_links():
    """Only each store's latest quote counts; equal-price duplicates keep the first link."""
    frame = quotes()
    extra = {**frame.iloc[0].to_dict(), "date": "2026-10-05", "price": 10}
    duplicate = {**frame.iloc[1].to_dict(), "source_url": "https://example.com/0"}
    frame = pd.concat([frame, pd.DataFrame([extra, duplicate])], ignore_index=True)
    result = compare_observed_offers(frame, True, date(2026, 10, 6))
    assert result.store.tolist() == ["Store B", "Store A"]
    assert result.price.tolist() == [90, 100]
    assert result.source_url.tolist() == ["https://example.com/0", "https://example.com/a"]


def test_equal_prices_order_by_store_and_dense_rank():
    """Ties share a rank, are ordered by store name, and the next price gets the next rank."""
    frame = quotes().iloc[:2].copy()
    frame.loc[0, "store"] = "Store Z"
    frame.loc[1, "price"] = 100
    third = {**frame.iloc[0].to_dict(), "store": "Store C", "price": 120}
    frame = pd.concat([frame, pd.DataFrame([third])], ignore_index=True)
    result = compare_observed_offers(frame, True, date(2026, 10, 6))
    assert result.store.tolist() == ["Store B", "Store Z", "Store C"]
    assert result.price_rank.tolist() == [1, 1, 2]


def test_quantities_must_match_exactly_and_dimension_message():
    """Even a tiny pack difference or a dimension change blocks the comparison."""
    message = "^Quotes must refer to the same total pack quantity and dimension.$"
    frame = quotes().astype({"quantity": float})
    frame.loc[1, "quantity"] = 1.000001
    with pytest.raises(ValueError, match=message):
        compare_observed_offers(frame, True, date(2026, 10, 6))
    frame = quotes()
    frame.loc[1, "unit"] = "ml"
    frame.loc[1, "quantity"] = 1000
    with pytest.raises(ValueError, match=message):
        compare_observed_offers(frame, True, date(2026, 10, 6))
    frame = quotes()
    frame.loc[1, "currency"] = "USD"
    with pytest.raises(ValueError, match="^Select exactly one product, variant and currency.$"):
        compare_observed_offers(frame, True, date(2026, 10, 6))


def test_default_today_and_conflict_message():
    """Without a date, today's quotes are used; conflicts carry the documented message."""
    frame = quotes().iloc[:2].copy()
    frame["date"] = date.today().isoformat()
    assert len(compare_observed_offers(frame, True)) == 2
    frame = quotes()
    frame.loc[2, "date"] = "2026-10-06"
    with pytest.raises(ValueError, match="^Reconcile conflicting latest prices for a store before "
                                         "ranking quotes.$"):
        compare_observed_offers(frame, True, date(2026, 10, 6))
