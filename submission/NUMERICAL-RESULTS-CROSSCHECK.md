# Slide numerical evidence — checked 24 September 2026

These are saved results from the 19 September review, not a fresh benchmark. All 19 reviewed source-file hashes still match reports/review_manifest.json. The actual generated slide images were not supplied; this check covers the slide prompts and source evidence. The Word report already contained all 13 production/script MI scores; slide 4 previously omitted them.

## Maintainability Index (MI)

Source: reports/radon-mi.json. MI is a 0–100 index, not a percentage of maintainability or an achievement rate. The installed Radon mi_rank implementation assigns A above 19, B above 9 through 19, C at or below 9. Therefore low-looking scores such as 25.01 can still be A.

| Production/script module | MI score | Rank |
|---|---:|:---:|
| ui.py | 25.01 | A |
| scripts/review.py | 34.05 | A |
| model.py | 34.07 | A |
| external.py | 38.76 | A |
| calculations.py | 42.83 | A |
| data.py | 43.12 | A |
| history.py | 44.55 | A |
| app.py | 45.59 | A |
| scripts/fetch_real_data.py | 47.48 | A |
| catalogue.py | 55.75 | A |
| scripts/browser_check.py | 58.84 | A |
| paths.py | 67.73 | A |
| __init__.py | 100.00 | A |

Package filenames are under src/price_truth/, except app.py. The unweighted mean across these 13 files is 49.06, calculated from unrounded scores; it is not Radon's project-wide MI. It includes the trivial __init__.py file, so per-file scores are more informative. “13/13 = 100% rank A” describes the fraction of files, not perfect code quality. Maximum CC 40/E remains a separate finding.

## Model errors and valid percentages

“MA” was interpreted as model accuracy/MAE; the project has regression metrics, not a classification-accuracy result.

| Metric | Selected model | Baseline | Interpretation |
|---|---:|---:|---|
| Test MAE | INR 356.82 | INR 373.27 | Currency error; 4.41% relative reduction |
| Test log MAE | 0.273049 | 0.305961 | 10.76% relative reduction |
| Median absolute percentage error | 20.16% | 23.39% | Median error; not mean MAPE or accuracy |
| Test R² | 0.957552 | 0.958382 | Baseline slightly higher; not classification accuracy |
| Empirical interval coverage | 89.76% | — | Nominal target 90%; shortfall 0.24 percentage points |

Source: reports/model_evaluation.json. Error reduction = (baseline − selected) / baseline × 100, using unrounded inputs. Test set: 4,269 rows. Do not calculate “accuracy” as 100 minus median percentage error.

## Non-functional requirements (NFRs)

| NFR | Target | Numerical evidence | What can be concluded |
|---|---|---|---|
| Performance | Page <3 s; assessment <2 s | First page 3.043983 s; repeat 1.028876 s; first assessment + SHAP 0.925734 s | First page exceeded 3 s by 1.47%; measured assessment passed |
| Scalability | 100 concurrent users | 29 warm sequential calls; p95 0.034736 s | No concurrency result; no capacity percentage |
| Usability | No manual needed | 3 recorded browser flows | No user-study success rate; flow checks do not prove usability |
| Security | HTTPS; no PII storage | Local HTTP; no security score measured | Raw CSV reviewer fields retained; excluded from processed model features |
| Reliability | 99% evaluation-window uptime | No uptime window measured | 99% is a target, not a result |
| Portability | Desktop/tablet/mobile | 1440×1000 and 390×844 viewports; no mobile page overflow | Two emulated viewport sizes; no physical-device or tablet validation |
| Maintainability | Modular code | 13 production/script files; 13/13 rank A; mean CC 4.66 | 100% of these files rank A, not 100% maintainability |
| Availability | 24/7 access | Local app only; no availability measurement | No achieved uptime/availability percentage |
| Compatibility | Chrome, Firefox, Safari, Edge | 1/4 named browsers tested = 25% | Browser test coverage only; other three untested |

Sources: reports/browser_initial_check.json, browser_check.json, performance.json, radon-mi.json and CODE-REVIEW-REPORT.md. No overall NFR achievement percentage is justified: these requirements have different criteria and several have no measurement. “Not measured” does not mean 0% or failure. Browser/device counts must not be presented as success rates.

## Other measured percentages

| Metric | Calculation | Result |
|---|---|---:|
| Test-case pass rate | 98/98 | 100% |
| Package statement coverage | 462/526 | 87.83% |
| Package branch coverage | 74/98 | 75.51% |
| Scoped mutation kill rate | 305/375 | 81.33% |
| Scoped mutation survival rate | 70/375 | 18.67% |

Sources: reports/pytest.xml, coverage.json and mutation.json. Ruff has zero configured-rule violations; no arbitrary “Ruff quality percentage” is assigned. Coverage is for price_truth; mutation testing covers calculations, catalogue and history only.

## Updated prompts

- Image 2: added baseline median percentage error and relative MAE/log-MAE reductions.
- Image 4: added all 13 actual MI scores, with the index-versus-percentage distinction.
- Image 5: replaced generic readiness labels with nine NFR target/evidence rows and valid derived comparisons.
- PRICE-TRUTH-IMAGE-PROMPTS.zip contains the updated five prompts. No source code or original raw results changed.
