# Price Truth — current engineering review

Generated: 2026-10-06T15:42:21.813641+00:00

Historical submission reports are preserved separately; these results apply to this source manifest.

## Ruff

0 violations under configured rules (command exited successfully).

## PyTest

| Measure | Value |
| --- | --- |
| name | pytest |
| errors | 0 |
| failures | 0 |
| skipped | 0 |
| tests | 150 |
| time | 27.685 |
| timestamp | 2026-10-06T21:11:36.493281+05:30 |
| hostname | Mac.lan |

## Coverage

| Measure | Count | Percentage |
| --- | --- | --- |
| Statements | 910/1060 | 85.85% |
| Branches | 203/268 | 75.75% |

Coverage scope: price_truth package; scripts and app.py are outside this denominator.

## Mutmut

| Outcome | Count |
| --- | --- |
| killed | 327 |
| survived | 57 |
| total | 384 |
| no_tests | 0 |
| skipped | 0 |
| suspicious | 0 |
| timeout | 0 |
| check_was_interrupted_by_user | 0 |
| segfault | 0 |

Kill rate: 85.16% (327/384). Scope: calculations, catalogue, history only.

## Radon CC

| File | Block | CC | Rank |
| --- | --- | --- | --- |
| src/price_truth/exports.py | assessment_pdf | 4 | A |
| src/price_truth/forecast.py | forecast_next_day | 14 | C |
| src/price_truth/forecast.py | _predict | 3 | A |
| src/price_truth/forecast.py | _errors | 2 | A |
| src/price_truth/evidence_store.py | accumulated_observations | 7 | B |
| src/price_truth/evidence_store.py | archive_snapshot | 6 | B |
| src/price_truth/evidence_store.py | history_readiness | 3 | A |
| src/price_truth/ui.py | lookup_page | 13 | C |
| src/price_truth/ui.py | assessment_panel | 8 | B |
| src/price_truth/ui.py | unit_page | 8 | B |
| src/price_truth/ui.py | history_page | 8 | B |
| src/price_truth/ui.py | checker_page | 2 | A |
| src/price_truth/ui.py | shrink_page | 1 | A |
| src/price_truth/ui.py | catalogue_page | 1 | A |
| src/price_truth/observations.py | validate_observations | 15 | C |
| src/price_truth/observations.py | pack_changes | 10 | B |
| src/price_truth/observations.py | evidence_url | 7 | B |
| src/price_truth/observations.py | read_csv | 3 | A |
| src/price_truth/observations.py | daily_series | 2 | A |
| src/price_truth/cache.py | read_json | 3 | A |
| src/price_truth/cache.py | fresh | 3 | A |
| src/price_truth/cache.py | write_json | 2 | A |
| src/price_truth/offers.py | compare_observed_offers | 10 | B |
| src/price_truth/calculations.py | compare_packs | 8 | B |
| src/price_truth/calculations.py | unit_price | 6 | B |
| src/price_truth/calculations.py | positive | 3 | A |
| src/price_truth/calculations.py | discount_percent | 2 | A |
| src/price_truth/calculations.py | shrink_change | 1 | A |
| src/price_truth/model.py | train_model | 5 | A |
| src/price_truth/model.py | assess | 5 | A |
| src/price_truth/model.py | baseline | 2 | A |
| src/price_truth/model.py | features | 1 | A |
| src/price_truth/model.py | split_groups | 1 | A |
| src/price_truth/model.py | preprocessing | 1 | A |
| src/price_truth/model.py | metrics | 1 | A |
| src/price_truth/model.py | load_model | 1 | A |
| src/price_truth/price_api.py | fetch_observations | 12 | C |
| src/price_truth/price_api.py | valid_cache | 9 | B |
| src/price_truth/price_api.py | normalize | 6 | B |
| src/price_truth/workspace.py | food_workspace | 20 | C |
| src/price_truth/workspace.py | imported_history | 10 | B |
| src/price_truth/workspace.py | history_panel | 9 | B |
| src/price_truth/workspace.py | workspace_page | 6 | B |
| src/price_truth/workspace.py | observation_form | 5 | A |
| src/price_truth/workspace.py | offers_panel | 4 | A |
| src/price_truth/workspace.py | use_pack_for_comparison | 1 | A |
| src/price_truth/external.py | search_products | 12 | C |
| src/price_truth/external.py | lookup_product | 11 | C |
| src/price_truth/external.py | get_json | 2 | A |
| src/price_truth/external.py | cached_products | 2 | A |
| src/price_truth/data.py | normalize | 9 | B |
| src/price_truth/data.py | category_parts | 5 | A |
| src/price_truth/data.py | build_catalogue | 2 | A |
| src/price_truth/data.py | load_catalogue | 2 | A |
| src/price_truth/data.py | numeric | 1 | A |
| src/price_truth/data.py | name_group | 1 | A |
| src/price_truth/data.py | clean_source | 1 | A |
| src/price_truth/catalogue.py | safe_url | 9 | B |
| src/price_truth/catalogue.py | export_csv | 4 | A |
| src/price_truth/catalogue.py | search | 3 | A |
| src/price_truth/history.py | timing_signal | 7 | B |
| src/price_truth/history.py | load_observations | 4 | A |
| src/price_truth/history.py | series_for | 1 | A |
| app.py | main | 14 | C |
| app.py | catalogue | 1 | A |
| app.py | model | 1 | A |
| scripts/concurrency_check.py | main | 8 | B |
| scripts/review_current.py | metrics_sections | 6 | B |
| scripts/review_current.py | source_manifest | 4 | A |
| scripts/review_current.py | execute | 2 | A |
| scripts/review_current.py | collect_checks | 2 | A |
| scripts/review_current.py | benchmark | 2 | A |
| scripts/review_current.py | collect_mutations | 1 | A |
| scripts/review_current.py | table | 1 | A |
| scripts/review_current.py | render_report | 1 | A |
| scripts/review_current.py | main | 1 | A |
| scripts/fetch_real_data.py | fetch_prices | 6 | B |
| scripts/fetch_real_data.py | main | 5 | A |
| scripts/data_feasibility.py | main | 5 | A |
| scripts/browser_current.py | main | 7 | B |
| scripts/browser_current.py | check_workspace | 2 | A |
| scripts/browser_current.py | check_viewports | 2 | A |
| scripts/browser_check.py | main | 3 | A |
| scripts/model_audit.py | main | 4 | A |
| scripts/model_development.py | main | 5 | A |
| scripts/model_development.py | estimator | 1 | A |
| scripts/model_development.py | experiments | 1 | A |
| tests/test_model.py | test_shap_reconstructs_actual_prediction | 5 | A |
| tests/test_model.py | test_training_pipeline_on_real_data | 5 | A |
| tests/test_model.py | test_missing_rating_does_not_break_inference | 2 | A |
| tests/test_model.py | test_invalid_quote_and_sparse_category | 2 | A |
| tests/test_model.py | bundle | 1 | A |
| tests/test_workspace_evidence.py | test_manual_observation_validation_and_clear | 16 | C |
| tests/test_workspace_evidence.py | test_forecast_chronological_holdout_and_future_gate | 7 | B |
| tests/test_workspace_evidence.py | test_workspace_quote_comparison_uses_confirmed_session_evidence | 7 | B |
| tests/test_workspace_evidence.py | test_forecast_abstains_for_constant_sparse_stale_and_bad_history | 6 | B |
| tests/test_workspace_evidence.py | test_workspace_real_assessment_and_empty_import | 5 | A |
| tests/test_workspace_evidence.py | test_csv_preserves_identity_and_labels_evidence | 4 | A |
| tests/test_workspace_evidence.py | test_price_api_filters_identity_and_contributor_fields | 4 | A |
| tests/test_workspace_evidence.py | test_cache_corruption_is_a_miss_and_write_replaces | 4 | A |
| tests/test_workspace_evidence.py | test_pack_change_needs_confirmation_and_identity | 3 | A |
| tests/test_workspace_evidence.py | test_daily_series_requires_same_pack_and_aggregates_dates | 3 | A |
| tests/test_workspace_evidence.py | records | 2 | A |
| tests/test_workspace_evidence.py | test_import_bounds_and_schema | 2 | A |
| tests/test_workspace_evidence.py | test_pdf_export_is_generated_in_memory | 2 | A |
| tests/test_workspace_evidence.py | test_import_rejects_entire_invalid_batch | 1 | A |
| tests/test_workspace_evidence.py | trend | 1 | A |
| tests/test_workspace_evidence.py | test_pack_changes_rejects_ambiguous_same_day_evidence | 1 | A |
| tests/test_search.py | test_search_success_and_timeout | 4 | A |
| tests/test_search.py | test_real_saved_name_search | 3 | A |
| tests/test_search.py | test_invalid_search | 1 | A |
| tests/test_services.py | test_history_sparse_stale_and_future | 6 | B |
| tests/test_services.py | test_real_history_stays_in_one_store_currency_and_product | 5 | A |
| tests/test_services.py | test_history_filters_incompatible_or_unproven_observations | 5 | A |
| tests/test_services.py | test_timing_quartile_boundaries | 5 | A |
| tests/test_services.py | test_offline_and_timeout_use_real_cache | 4 | A |
| tests/test_services.py | test_collection_selection_and_metadata | 4 | A |
| tests/test_services.py | test_success_saves_real_response | 3 | A |
| tests/test_services.py | test_literal_search_and_empty_platforms | 3 | A |
| tests/test_services.py | test_safe_link_and_export | 3 | A |
| tests/test_services.py | test_history_same_day_median_and_sorting | 3 | A |
| tests/test_services.py | test_search_multiple_words_case_and_platform | 3 | A |
| tests/test_services.py | test_timing_same_day_quote_excluded_and_short_span | 3 | A |
| tests/test_services.py | test_reject_unsafe_links | 2 | A |
| tests/test_services.py | test_history_default_unit_matches_explicit_unit | 2 | A |
| tests/test_services.py | test_history_includes_today_but_excludes_zero_prices | 2 | A |
| tests/test_services.py | test_history_freshness_exact_boundary | 2 | A |
| tests/test_services.py | test_export_neutralizes_spreadsheet_formula_prefixes | 2 | A |
| tests/test_services.py | test_malformed_and_credential_links_are_not_exposed | 2 | A |
| tests/test_services.py | test_both_source_retailer_links_remain_available | 2 | A |
| tests/test_services.py | test_invalid_barcode_never_calls_network | 1 | A |
| tests/test_services.py | test_not_found_and_missing_cache | 1 | A |
| tests/test_calculations.py | test_multipack_and_dimension | 4 | A |
| tests/test_calculations.py | test_compare_rank_and_no_mutation | 4 | A |
| tests/test_calculations.py | test_discount_from_actual_amazon_listing | 3 | A |
| tests/test_calculations.py | test_unit_conversions | 3 | A |
| tests/test_calculations.py | test_comparison_respects_multipack_count | 3 | A |
| tests/test_calculations.py | test_reported_vim_shrinkage | 3 | A |
| tests/test_calculations.py | test_shrinkage_accounts_for_price_change | 3 | A |
| tests/test_calculations.py | test_positive_preserves_amount | 2 | A |
| tests/test_calculations.py | test_currency_normalization | 2 | A |
| tests/test_calculations.py | test_blank_currencies_cannot_be_compared | 2 | A |
| tests/test_calculations.py | test_reject_nonpositive_or_nonfinite | 1 | A |
| tests/test_calculations.py | test_reject_inverted_discount | 1 | A |
| tests/test_calculations.py | test_discount_rejects_invalid_prices | 1 | A |
| tests/test_calculations.py | test_invalid_pack_counts | 1 | A |
| tests/test_calculations.py | test_invalid_units_and_amounts | 1 | A |
| tests/test_calculations.py | packs | 1 | A |
| tests/test_calculations.py | test_reject_mixed_or_missing_currency | 1 | A |
| tests/test_calculations.py | test_reject_mixed_dimensions_and_single_pack | 1 | A |
| tests/test_calculations.py | test_shrink_rejects_invalid_values | 1 | A |
| tests/test_data.py | test_catalogue_invariants | 6 | B |
| tests/test_data.py | test_raw_hashes_and_partition | 4 | A |
| tests/test_data.py | test_evaluation_groups_do_not_overlap | 4 | A |
| tests/test_data.py | test_conflicting_actual_source_prices_are_quarantined | 3 | A |
| tests/test_data.py | test_numeric_missing_is_not_zero | 3 | A |
| tests/test_data.py | test_category_rejects_invalid_structure | 2 | A |
| tests/test_data.py | test_no_target_leakage_in_features | 1 | A |
| tests/test_app.py | test_checker_runs_real_model | 4 | A |
| tests/test_app.py | test_unit_comparison_flow | 3 | A |
| tests/test_app.py | test_offline_lookup_flow | 3 | A |
| tests/test_app.py | application | 2 | A |
| tests/test_app.py | test_pages_render | 2 | A |
| tests/test_evidence_store.py | test_repeated_collection_never_manufactures_history | 6 | B |
| tests/test_evidence_store.py | test_schema_corrupt_and_wrong_identity_caches_are_not_evidence | 2 | A |
| tests/test_evidence_store.py | snapshot | 1 | A |
| tests/test_evidence_store.py | test_incomplete_archive_is_explicit_error | 1 | A |
| tests/test_offers.py | test_comparison_respects_dates_packs_and_conditions | 4 | A |
| tests/test_offers.py | test_same_day_price_conflict_and_ties | 2 | A |
| tests/test_offers.py | quotes | 1 | A |
| tests/test_offers.py | test_incompatible_quotes_rejected | 1 | A |

## Radon MI

MI is an index, not percent maintainability.

| File | MI | Rank |
| --- | --- | --- |
| src/price_truth/exports.py | 57.61 | A |
| src/price_truth/forecast.py | 42.03 | A |
| src/price_truth/evidence_store.py | 45.71 | A |
| src/price_truth/paths.py | 67.73 | A |
| src/price_truth/ui.py | 24.65 | A |
| src/price_truth/observations.py | 34.43 | A |
| src/price_truth/cache.py | 55.71 | A |
| src/price_truth/__init__.py | 100.0 | A |
| src/price_truth/offers.py | 50.97 | A |
| src/price_truth/calculations.py | 42.83 | A |
| src/price_truth/model.py | 34.07 | A |
| src/price_truth/price_api.py | 39.67 | A |
| src/price_truth/workspace.py | 25.08 | A |
| src/price_truth/external.py | 36.72 | A |
| src/price_truth/data.py | 43.12 | A |
| src/price_truth/catalogue.py | 51.84 | A |
| src/price_truth/history.py | 44.55 | A |
| app.py | 44.0 | A |
| scripts/concurrency_check.py | 44.1 | A |
| scripts/review_current.py | 35.6 | A |
| scripts/fetch_real_data.py | 47.48 | A |
| scripts/data_feasibility.py | 47.58 | A |
| scripts/review.py | 81.86 | A |
| scripts/browser_current.py | 42.55 | A |
| scripts/browser_check.py | 58.84 | A |
| scripts/model_audit.py | 49.41 | A |
| scripts/model_development.py | 42.99 | A |
| tests/test_model.py | 45.59 | A |
| tests/test_workspace_evidence.py | 22.33 | A |
| tests/test_search.py | 52.6 | A |
| tests/test_services.py | 23.23 | A |
| tests/test_calculations.py | 35.15 | A |
| tests/test_data.py | 42.58 | A |
| tests/test_app.py | 49.54 | A |
| tests/test_evidence_store.py | 48.76 | A |
| tests/test_offers.py | 54.05 | A |

## Radon raw

| File | LOC | SLOC | Comments |
| --- | --- | --- | --- |
| src/price_truth/exports.py | 41 | 36 | 0 |
| src/price_truth/forecast.py | 57 | 46 | 0 |
| src/price_truth/evidence_store.py | 64 | 51 | 0 |
| src/price_truth/paths.py | 10 | 7 | 0 |
| src/price_truth/ui.py | 236 | 212 | 0 |
| src/price_truth/observations.py | 110 | 91 | 0 |
| src/price_truth/cache.py | 38 | 28 | 0 |
| src/price_truth/__init__.py | 2 | 0 | 0 |
| src/price_truth/offers.py | 36 | 30 | 0 |
| src/price_truth/calculations.py | 59 | 41 | 0 |
| src/price_truth/model.py | 180 | 149 | 0 |
| src/price_truth/price_api.py | 76 | 63 | 0 |
| src/price_truth/workspace.py | 272 | 247 | 1 |
| src/price_truth/external.py | 92 | 76 | 0 |
| src/price_truth/data.py | 136 | 107 | 2 |
| src/price_truth/catalogue.py | 38 | 27 | 0 |
| src/price_truth/history.py | 54 | 42 | 0 |
| app.py | 97 | 82 | 0 |
| scripts/concurrency_check.py | 67 | 56 | 0 |
| scripts/review_current.py | 145 | 112 | 0 |
| scripts/fetch_real_data.py | 64 | 54 | 0 |
| scripts/data_feasibility.py | 52 | 44 | 0 |
| scripts/review.py | 5 | 3 | 0 |
| scripts/browser_current.py | 75 | 60 | 0 |
| scripts/browser_check.py | 58 | 49 | 1 |
| scripts/model_audit.py | 48 | 40 | 0 |
| scripts/model_development.py | 95 | 81 | 0 |
| tests/test_model.py | 55 | 38 | 0 |
| tests/test_workspace_evidence.py | 215 | 164 | 0 |
| tests/test_search.py | 38 | 26 | 0 |
| tests/test_services.py | 218 | 152 | 0 |
| tests/test_calculations.py | 159 | 99 | 0 |
| tests/test_data.py | 78 | 53 | 0 |
| tests/test_app.py | 51 | 34 | 0 |
| tests/test_evidence_store.py | 52 | 37 | 0 |
| tests/test_offers.py | 49 | 34 | 0 |

## Halstead

| File | Volume | Estimated effort |
| --- | --- | --- |
| src/price_truth/exports.py | 72.0 | 280.8 |
| src/price_truth/forecast.py | 428.93 | 2964.04 |
| src/price_truth/evidence_store.py | 137.55 | 412.65 |
| src/price_truth/paths.py | 59.79 | 39.86 |
| src/price_truth/ui.py | 664.41 | 4565.15 |
| src/price_truth/observations.py | 410.43 | 1258.06 |
| src/price_truth/cache.py | 33.22 | 66.44 |
| src/price_truth/__init__.py | 0 | 0 |
| src/price_truth/offers.py | 145.71 | 647.62 |
| src/price_truth/calculations.py | 510.04 | 3559.89 |
| src/price_truth/model.py | 493.63 | 3004.67 |
| src/price_truth/price_api.py | 338.83 | 1564.86 |
| src/price_truth/workspace.py | 779.8 | 6037.73 |
| src/price_truth/external.py | 318.15 | 1145.33 |
| src/price_truth/data.py | 548.29 | 4532.54 |
| src/price_truth/catalogue.py | 113.09 | 339.27 |
| src/price_truth/history.py | 543.93 | 3451.88 |
| app.py | 99.91 | 163.49 |
| scripts/concurrency_check.py | 180.0 | 720.0 |
| scripts/review_current.py | 555.01 | 1776.03 |
| scripts/fetch_real_data.py | 120.4 | 318.72 |
| scripts/data_feasibility.py | 240.0 | 886.15 |
| scripts/review.py | 4.75 | 2.38 |
| scripts/browser_current.py | 221.14 | 904.66 |
| scripts/browser_check.py | 64.53 | 129.06 |
| scripts/model_audit.py | 208.59 | 866.43 |
| scripts/model_development.py | 208.08 | 560.21 |
| tests/test_model.py | 274.84 | 1205.75 |
| tests/test_workspace_evidence.py | 1266.15 | 7533.6 |
| tests/test_search.py | 101.95 | 152.93 |
| tests/test_services.py | 1414.6 | 8891.75 |
| tests/test_calculations.py | 320.15 | 640.3 |
| tests/test_data.py | 267.64 | 853.12 |
| tests/test_app.py | 114.2 | 285.5 |
| tests/test_evidence_store.py | 182.68 | 380.58 |
| tests/test_offers.py | 38.04 | 19.02 |

## Local timing

| Measure | Value |
| --- | --- |
| first_assessment_seconds | 9.294358790997649 |
| warm_calls | 29 |
| warm_p95_seconds | 0.03713549120002426 |
| scope | Sequential local assessment including SHAP; not 100-user load or browser latency |

## Requirements still requiring external evidence

Public deployment/HTTPS, monitored uptime, real-user usability, physical devices and 100-user concurrency are not established by these checks. Browser evidence is recorded separately. Forecasts require sufficient recent comparable observations; controlled test fixtures are not market evaluation.
