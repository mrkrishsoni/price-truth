# Reference-format check: Group 6 vs Price Truth

Reviewed all eight pages of the user-provided `GROUP_6_Code_Review_Final.pdf`, including rendered pages. Its structure was used as a checklist; its model, values, architecture and achievement claims were not transferred. This comparison is preparation material, not part of Price Truth's numerical evidence.

| Reference element | Price Truth report location | Coverage |
|---|---|---|
| Identity, stack and local demo | Page 1 | Project-specific metadata |
| Repository structure | Page 1 | Actual reviewed files |
| Size & Scope | Page 1, separate table | Layer, files, SLOC, responsibility |
| Frameworks & Justification | Page 2, separate table | Library, installed version, role, reason |
| Ruff | Page 3, separate table | Configured categories, violations, status and command |
| PyTest | Page 3, separate tables | Six suites, case counts, results and scoped coverage |
| Mutmut | Page 4, separate tables | Real operators, targets, killed/survived examples and totals |
| Radon CC | Page 5, separate table | Module means, maxima and grades |
| Radon MI | Page 5, separate table | All 13 production/script files |
| Radon raw metrics | Page 6, separate table | LOC, LLOC, SLOC, comments, multiline strings, blanks |
| Documentation/type-checking | Page 6 | AST docstring counts; static type checker not run |
| Radon Halstead | Page 6, separate table | Vocabulary, volume, difficulty, effort, estimated bugs |
| NFRs | Page 7, separate table | Nine actual requirements, targets, status, evidence |
| Summary and model evidence | Page 8, separate tables | Measured outcomes, limits and held-out model results |
| Reproduction commands | Pages 3, 4, 6 and 8 | Tool commands and application launch |

## Important project-specific differences

- Price Truth is tabular price regression with Tree SHAP, not a GRU recommender. Its held-out price errors and interval coverage are the relevant model results.
- Native Mutmut reports 81.33% killed in three scoped modules. This is not comparable to a manual sampled estimate from another project.
- Price Truth's nine documented NFR categories govern its report. The other project's twelve rows are not twelve additional mandatory requirements for this app.
- A report can address an NFR fully while recording that its target is unachieved or unmeasured. This is a reporting-completeness claim, not an engineering-completion claim.
- Dataset row count does not establish concurrent-user capacity. Local startup does not establish 99% uptime. Type hints do not establish static type correctness.
- The reference labels its module S4, while Price Truth's supplied handoff says S3. The concise report uses “Lab Work” rather than silently copying the conflicting number. Use the instructor's official submission label in any upload form.
- The reference is an example, not an independently confirmed marking guarantee. The revised report covers its relevant structural elements but cannot guarantee full marks.

## Result

No relevant top-level review section in the reference is missing from the revised eight-page report. Remaining gaps concern actual product evidence and code improvements, explicitly listed in REMAINING-WORK.md. The original Python code and its recorded tool results remain unchanged.
