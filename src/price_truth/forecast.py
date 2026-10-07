"""Chronological next-day price evaluation with evidence gates and baseline comparison."""
from datetime import date

import numpy as np
import pandas as pd


def _predict(prices: np.ndarray, method: str) -> float:
    """Fit on prior observations only; estimate the next day, never a sale-calendar event."""
    if method == "last_price":
        return float(prices[-1])
    if method == "rolling_median":
        return float(np.median(prices[-7:]))
    window = prices[-14:]
    slope, intercept = np.polyfit(np.arange(len(window)), window, 1)
    return max(.01, float(intercept + slope * len(window)))


def _errors(prices: np.ndarray, start: int, end: int, method: str) -> list[float]:
    """Perform expanding-window one-step predictions with no future observations."""
    return [abs(float(prices[i]) - _predict(prices[:i], method)) for i in range(start, end)]


def forecast_next_day(series: pd.DataFrame, today: date | None = None) -> dict:
    """Gate on consecutive, recent daily observations; reserve final 10 days for testing."""
    today = today or date.today()
    data = series[["date", "price"]].copy()
    data["date"] = pd.to_datetime(data.date, errors="coerce")
    data["price"] = pd.to_numeric(data.price, errors="coerce")
    if (data.isna().any().any() or not np.isfinite(data.price).all()
            or data.price.le(0).any() or data.date.duplicated().any()):
        return {"status": "invalid_history", "reason": "Need unique dates and finite positive prices."}
    data = data.sort_values("date")
    if len(data) < 40:
        return {"status": "insufficient_history", "reason": "At least 40 consecutive daily observations required.",
                "observed_days": len(data)}
    if not data.date.diff().dropna().eq(pd.Timedelta(days=1)).all():
        return {"status": "irregular_history", "reason": "Missing days are not fabricated or interpolated."}
    age = (today - data.date.iloc[-1].date()).days
    if age < 0 or age > 1:
        return {"status": "stale_history", "reason": "Last observation must be today or yesterday.", "age_days": age}
    prices = data.price.to_numpy(dtype=float)
    n = len(prices)
    methods = ["last_price", "rolling_median", "local_trend"]
    validation = {m: float(np.mean(_errors(prices, n-20, n-10, m))) for m in methods}
    selected = min(methods, key=validation.get)
    errors = _errors(prices, n-10, n, selected)
    baseline = _errors(prices, n-10, n, "last_price")
    mae, baseline_mae = float(np.mean(errors)), float(np.mean(baseline))
    improves = selected != "last_price" and mae < baseline_mae
    return {"status": "evaluated" if improves else "baseline_preferred",
            "reason": "One-step historical backtest; not a guaranteed buying recommendation.",
            "selected_on_validation": selected, "validation_mae": validation,
            "test_mae": mae, "baseline_test_mae": baseline_mae, "test_predictions": len(errors),
            "beats_baseline_on_test": improves, "forecast_date": (data.date.iloc[-1] + pd.Timedelta(days=1)).date().isoformat(),
            "next_day_estimate": _predict(prices, selected) if improves else None,
            "observed_days": n, "age_days": age}
