# Price Truth

A functional Python web application for explaining observed product prices, looking up food packs, comparing unit prices, and showing sourced price/pack history. Built for Group 11's NMIMS M.Sc. Data Science project.

The active completion record is [PROJECT-COMPLETION.md](PROJECT-COMPLETION.md). September submission evidence is preserved; new checks are in `reports/current/`.

## Run the existing local build

From the project folder:

```bash
.venv/bin/python -m streamlit run app.py
```

Open `http://localhost:8501`. The current workspace already includes the cleaned catalogue, trained model, real API caches, and source evidence, so the demo can run without downloading data again. Live barcode/name search needs internet; use the explicitly labeled saved examples when offline.

## Set up a fresh environment

Python 3.12 is recommended. On macOS/Linux:

```bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
.venv/bin/python -m price_truth.data
.venv/bin/python -m price_truth.model
.venv/bin/python -m streamlit run app.py
```

On Windows use `.venv\Scripts\python.exe` in place of `.venv/bin/python`. Mutmut needs a Unix environment (WSL on Windows). The initial development environment reused preinstalled scientific packages; pinned direct dependencies are in `requirements.txt` and review dependencies in `requirements-dev.txt`.

Keep the user-supplied files at `datasets/amazon/amazon.csv` and `datasets/flipkart/flipkart_com-ecommerce_sample.csv`. Raw files are never overwritten by the pipeline.

Refresh public evidence when needed:

```bash
.venv/bin/python scripts/fetch_real_data.py
```

This performs read-only public API calls and writes attributed snapshots under `datasets/external`. It does not scrape Amazon/Flipkart, create accounts, or upload user data. Price histories remain separate from the training catalogue. The search page saves its own successful queries as offline fallbacks.

## Feature status

| Feature | Implemented behavior |
|---|---|
| Product Workspace | Connected listing assessment, barcode history, pack-to-comparison transfer, manual/CSV observations and exports |
| Discount Checker | Select an actual catalogue product, enter a quote, receive a calibrated snapshot-price estimate and real SHAP waterfall; export JSON and PDF |
| Live Pack Lookup | Live barcode lookup and product-name search; real dated cached fallback |
| Unit Price Compare | Validate quantities/currencies, normalize g/kg/ml/l/count and multipacks, rank two variants |
| Buy Timing & History | Show real observations by barcode/store/currency and compare a quote; abstain when evidence is sparse or stale |
| Shrink Timeline | Two cited Indian pack-change cases with quantity and unit-price calculations |
| Platform Catalogue | Literal search across both historical catalogues and safe CSV export |
| Evidence & Methods | Display source audit and held-out model evaluation |

The model estimates prices, not discount authenticity. The supplied catalogues have no verified fraud labels or usable per-product histories. Flipkart prices are from 2015–2016 and Amazon's dates are unknown. The current price-history examples are sparse/stale, so no current buying forecast is promised. Read [data sources and limitations](docs/DATA-SOURCES.md).

## Architecture

```text
app.py → src/price_truth/ui.py → independent feature functions
                                   ├─ data.py → supplied CSVs → processed catalogue
                                   ├─ model.py → trained tree model + real SHAP
                                   ├─ external.py → read-only APIs + dated caches
                                   ├─ calculations.py → discounts / unit prices / shrinkage
                                   ├─ history.py → comparable dated observations
                                   └─ catalogue.py → search / safe links / CSV exports
```

Observation uploads and manual entries are validated atomically and held in Streamlit session memory; download CSV to retain them. Closing/restarting a session can lose unsaved observations. They are labelled user-supplied and never silently included in model training. Pack changes require confirmation of variant continuity and reject ambiguous same-day evidence.

The next-day forecasting engine requires at least 40 consecutive recent daily observations, selects a method on chronological validation, evaluates ten later predictions against persistence, and withholds an estimate if the baseline wins. The current INR data does not qualify. Synthetic data is used only in clearly labelled tests.

The interface is intentionally simple. Restyle `app.py`, `ui.py`, and `.streamlit/config.toml` later without rewriting the data or model logic.

## Review and tests

```bash
.venv/bin/python scripts/review.py
```

The runner writes Ruff, PyTest/coverage, Radon CC/MI/raw/Halstead, scoped Mutmut, timings and a source-hash manifest to `reports/current/`. Read the [current review](reports/current/CODE-REVIEW-REPORT.md). Mutation scope is calculations, catalogue and history; it is not a whole-application mutation score. The original [submission report](reports/CODE-REVIEW-REPORT.md) and `submission/BASELINE-2026-09-19-SOURCE-EVIDENCE.zip` preserve the earlier version.

Additional checks:

```bash
.venv/bin/python scripts/model_audit.py
.venv/bin/python scripts/data_feasibility.py
.venv/bin/python scripts/browser_current.py
```

The data audit makes bounded public API requests and saves a separate current snapshot. The browser check needs the local app running and Chrome (macOS detection, or `PRICE_TRUTH_CHROME` for another executable); otherwise install Playwright Chromium. `PRICE_TRUTH_URL` can override localhost. Viewport emulation is not physical-device testing.

## Deployment preparation

A non-root Dockerfile with a Streamlit health check is provided. Docker is unavailable on the development machine, so the image is **not build-verified**. On a machine with Docker:

```bash
docker build -t price-truth .
docker run --rm -p 8501:8501 price-truth
```

Use HTTPS at the hosting proxy. Container caches and session observations are ephemeral unless storage is deliberately configured. Supply source attribution and verify dataset redistribution rights before public hosting. No credentials or public site changes are included. Claude's current handoff is [docs/CLAUDE-UI-HANDOFF.md](docs/CLAUDE-UI-HANDOFF.md).

## Demo route

1. Overview: explain real catalogue sizes and snapshot dates. Open Product Workspace for the connected journey; use My observations for real sourced manual/CSV records.
2. Discount Checker: submit the initial Wayona listing; inspect the actual SHAP chart and export.
3. Live Pack Lookup: use a saved barcode offline; optionally search `Maggi` live or use saved search results.
4. Unit Price Compare: enter two real pack options and compare price per 100g/ml.
5. History: show the INR evidence and explain why sparse data produces abstention; switch to the separate EUR example to show a longer real history.
6. Shrink Timeline: inspect a reported case and open its source.
7. Evidence & Methods: show the real evaluation and review report.

## Remaining external work

Public deployment, measured uptime, a true 100-user load test, Firefox/Safari/Edge verification, physical-device testing, a demo video, and optional final visual redesign have not been claimed complete. No public site has been replaced. [PROJECT-COMPLETION.md](PROJECT-COMPLETION.md) tracks current acceptance gates. Reliable current Indian buying forecasts and verified live retailer comparisons still require suitable data access.
