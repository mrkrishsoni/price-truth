# What is complete and what remains

## Completed for the selected submission

- Historical price-assessment workflow: real datasets, cleaning, model training/evaluation, real SHAP, interface and export.
- Unit-price comparison and the included supporting feature pages.
- Actual Ruff, PyTest, Mutmut and Radon execution with saved raw results.
- Concise report, detailed supporting report, original Python files and runnable project package.

## What you need to do now

1. Read `PRICE-TRUTH-CONCISE-REPORT.docx`; use it as the main report. The original 12-page report is supporting detail.
2. Extract the code ZIP and open its `price-truth` directory. Follow README.md if using a fresh environment. No virtual environment is bundled.
3. Run `.venv/bin/python -m streamlit run app.py`. Demonstrate Discount Checker, actual SHAP and Unit Price Compare. Use `START-HERE.md` for the demo sequence and likely questions.
4. Present/submit according to the teacher's required process. No new model or tool execution is necessary for this unchanged reviewed snapshot.

## Known engineering improvements — disclosed, not completed

| Work | Present status |
|---|---|
| Surviving mutation cases | 70 remain; includes message mutations and a default-unit test gap |
| Test coverage | 87.83% statements and 75.51% branches for the package; not 100% |
| Complexity | Report-generation routine has CC 40 / E; refactoring remains |
| Initial page load | 3.044s missed the <3s target; later measured load was 1.029s |

These findings do not prevent demonstration of the selected workflow. They must remain visible in the review; the code is not claimed defect-free.

## Broader product work — outside this submission

- Claude visual redesign and a genuinely connected product-search dashboard.
- Reliable current exact-product offers across retailers, supported by source access and matching.
- More real longitudinal price/pack observations before evaluating forecasts or authenticity claims.
- Public deployment, HTTPS checks, sustained uptime and 100-user load validation.
- Other browsers, tablet/physical-device testing and a user usability study.

The historical model is not a fraud detector. The broader product is not complete. If code changes after submission preparation, rerun the review and update the report rather than retaining stale results.
