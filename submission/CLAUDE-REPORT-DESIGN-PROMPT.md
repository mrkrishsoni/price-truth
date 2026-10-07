# Claude prompt — Price Truth report design

Attach `PRICE-TRUTH-CONCISE-REPORT.docx` and paste the prompt below. The submission ZIP is optional supporting evidence. This prompt decorates the academic report; the website has a separate UI handoff.

---

Act as an academic report designer. Polish the attached **Price Truth — Code Review Report** into a professional, attractive submission for a 40-mark code-review assignment. Deliver an editable DOCX and a matching print-ready PDF, if your environment supports those formats. Produce the files, not just design advice.

The attached report is the authoritative content source. Improve typography, colour, spacing, alignment and pagination. Preserve its meaning, all table rows, commands, numerical results, team details, dates, evidence references, scope boundaries and limitations. Do not change application code or rerun analyses. If a factual inconsistency appears, flag it separately rather than silently changing a result.

## Visual direction

Use a calm, precise academic style with these colours:

| Role | Colour |
|---|---|
| Title, main headings, table header fill | Deep navy `#16324F` |
| Subheadings and small decorative accents | Teal `#0F766E` |
| Body text | Charcoal `#202B38` |
| Secondary text | Slate `#536274` |
| Alternating table rows | Very light blue-grey `#F3F7FA` |
| Table rules | Pale grey `#D6DFE8` |
| Page background / table header text | White `#FFFFFF` |
| Optional limitation label | Dark amber `#92400E` on pale amber `#FFFBEB` |

Use colour sparingly. Keep the paper white and the document legible in greyscale. No gradients, neon colours, large illustrations, stock photos, emojis, badges implying certification, invented logos or oversized cover page. Do not use green colour to suggest an unmeasured target passed. Always express status in words.

Use Aptos or Calibri consistently, with Consolas for code. Target body text 10–11 pt, table text 9–10 pt and code at least 8 pt. Main headings 16–18 pt, subheadings 12–13 pt, title 24–28 pt. Keep the current portrait page size and approximately one-inch margins. Prefer breathing room and clean page breaks over shrinking type. Aim for the existing eight-page length; a modest increase is acceptable if necessary for readability, without deleting evidence or shrinking tables excessively.

## Structure that must stay separate

Keep the existing sequence and rubric labels:

1. Project identity, repository structure, and a distinct **Size & Scope** table: layer, files, SLOC, responsibility.
2. A distinct **Frameworks & Justification** table: library, installed version, role, justification; retain model-selection rationale.
3. **Ruff**: its own category/rule/result table and command.
4. **PyTest**: its own suite/case/coverage-area table and results/coverage table.
5. **Mutmut**: its own operator/target/outcome/mechanism table, outcome totals and actual mutation excerpts.
6. **Radon**: FOUR DISTINCT TABLES for cyclomatic complexity, maintainability index, raw metrics and Halstead. Preserve the documentation metrics too. Do not merge these into a generic scorecard.
7. **NFRs**: requirement, ISO category, target, actual status, evidence. Keep partial and unmeasured outcomes explicit.
8. Summary and real-data model evaluation, launch/review commands, and limitations.

Use native editable Word tables and heading styles. Repeat table headers if a table crosses pages; avoid splitting individual rows. Keep headings with the following content. Right-align numeric columns where appropriate. Keep code indentation and executable command text intact. Use consistent headers and page numbers. No orphaned rows, clipped text, footer collisions or blank filler pages.

## Facts and qualifications that must remain intact

- 19 reviewed Python files, 1,378 SLOC; 13 production/script files and six test files.
- Ruff: zero violations under the configured rules only.
- PyTest: 98 passed; 87.83% statement coverage and 75.51% branch coverage of the `price_truth` package. Scripts and app.py are outside that coverage denominator; AppTest exercises app.py.
- Mutmut: 305 killed / 375 total = 81.33%; 70 survived. Mutation scope is calculations.py, catalogue.py and history.py, not the full project.
- Mean CC 4.66/A over 47 blocks; maximum CC 40/E remains. MI rank A is not a percentage quality score.
- 21,267 cleaned real listings: Amazon 1,347 and Flipkart 19,920. No synthetic training data.
- Histogram gradient boosting was chosen by validation log MAE. Test MAE INR 356.82 versus baseline INR 373.27; test R-squared 0.957552 versus baseline 0.958382. Do not claim improvement on every metric or convert R-squared to classification accuracy.
- Historical observed-price estimation with actual Tree SHAP; not verified fraud detection, current fair-price estimation or reliable forecasting.
- First page load 3.044 seconds missed the <3-second target. Other timings have distinct scopes and must retain their labels.
- Public deployment, HTTPS validation, concurrent-user capacity, sustained uptime and several usability/compatibility targets remain unverified. Local demonstration is not production readiness.

Do not copy Group 6's project architecture, results or achievement claims. Our report follows a comparable table structure but contains Price Truth's own evidence. Do not promise marks, hide survivors, suppress warnings, invent screenshots or add decorative charts suggesting new measurements.

## Final check and handoff

Compare the redesigned document against the attachment, checking every number, table row, command and limitation. Render and inspect every page for readability, table boundaries, wrapping and consistent spacing. Deliver `PRICE-TRUTH-DESIGNED-REPORT.docx` and its matching PDF, plus a short description of the visual changes. If you cannot generate or inspect a requested format, say so plainly. Do not describe an uninspected file as verified.
