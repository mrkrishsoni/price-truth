# Price Truth — final review submission

## What is finished

The historical price-assessment workflow is implemented: real Amazon/Flipkart data, cleaning, trained model, held-out evaluation, real SHAP, user inputs and output export. The unit-price comparator is a second working demonstration. The broader application and its tests are included as reviewed supporting code.

Ruff, PyTest, Mutmut and Radon have already been executed. Their results are in `reports/`; the main eight-page Word report is `PRICE-TRUTH-CONCISE-REPORT.docx`. You do not need to visit a review website or obtain new results for this unchanged version.

Recorded results: 98 passing tests; 0 Ruff violations under the configured rules; 305/375 scoped mutants killed; all four Radon metric families collected. Source hashes were checked against the review manifest before packaging. The document was rendered and every page visually inspected.

## Files

- `PRICE-TRUTH-CONCISE-REPORT.docx`: main eight-page report with separate tool tables for submission.
- `PRICE-TRUTH-FINAL-CODE-REVIEW.docx`: original detailed supporting report.
- `price-truth/`: runnable application source, tests, real datasets, trusted local model, requirements and raw review evidence inside the ZIP.
- `PYTHON-CODE-LISTING.txt`: readable listing of the 19 reviewed Python files, including paths and line numbers. Run the original `.py` files, not this listing.
- `PACKAGE-MANIFEST.json`: hashes and included file inventory for the archive.

## Demonstrate

1. Open a terminal in the project root. Run `.venv/bin/python -m streamlit run app.py`, then open `http://localhost:8501`. For a fresh environment follow README.md; the ZIP does not contain a portable virtual environment.
2. Select **Discount Checker**. Keep the first Amazon listing and its original prices, then click **Assess price**. Explain that the estimate uses historical listings.
3. Show the predicted range, actual SHAP chart and JSON download. SHAP explains a model prediction; it is not proof of a genuine/fake discount.
4. Open **Unit Price Compare**, enter two actual pack options and show normalized unit prices. Inputs are user quotes, not new training data.
5. Open the Word report: show model evaluation, PyTest results, one killed and one surviving mutation, Radon metrics and the NFR table.

## Likely questions

| Question | Answer supported by the implementation |
|---|---|
| Are the training data real? | Yes. Both supplied CSVs are preserved, hashed and audited; 21,267 listings remain after cleaning. |
| Does 0.9576 R-squared mean 95.76% fraud accuracy? | No. This is price regression. The data has no verified fraud labels. |
| Why histogram gradient boosting? | It had the lowest validation mean absolute log error among the tested tree candidates. Baseline and random forest results are included. |
| How is leakage reduced? | Related normalized titles are grouped before splitting; preprocessing is fitted after the split. Residual variant leakage remains possible. |
| Is SHAP real? | Yes. TreeExplainer runs on the fitted estimator. Tests check that contributions and the base value add to the log prediction. |
| Did mutation testing cover the model? | No. It covers calculations, catalogue and history. Model training/SHAP have PyTest tests, not Mutmut coverage. |
| Why did 70 mutants survive? | Some change messages; others reveal remaining gaps, including a default-unit call. They are disclosed, not excluded to inflate the score. |
| Is it deployed and tested with 100 users? | No. Local browser and sequential latency checks are available; public uptime/concurrency are unverified. |

## What is outside today's submission

Final redesign, a unified live-offer dashboard, verified discount-authenticity classification, reliable future-price forecasting, public deployment and unmeasured NFRs are not represented as complete. None is a hidden dependency for the selected local workflow or the finished review report.

The only immediate user steps are to open the report, rehearse the local workflow and submit/present it according to the teacher's process. Changes to code afterward require fresh review results. Raw dataset redistribution rights should be checked before public publication; this archive was assembled locally and has not been uploaded anywhere.
