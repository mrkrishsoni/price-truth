# CODE REVIEW REPORT — SPEC & REFERENCE NOTES
**Purpose:** Not a to-do list for building the Price Truth app itself (see `PRICE-TRUTH-BUILD-HANDOFF.md` for that). This file is specifically about the **Code Review Report** artifact that will need to be produced once the codebase exists — capturing what the professor wants, and what a strong example submission looks like, so Price Truth's own report can be shaped correctly from the start rather than retrofitted later.

**Status: reference/planning only — no work has been started on this yet, per instruction.**

---

## 1. THE PROFESSOR'S EXPLICIT INSTRUCTION ON FORMAT (most important thing in this file)

Stated directly, in the user's own words, and worth preserving verbatim-in-spirit because it should override any generic "how to write a report" instinct:

> He doesn't want everything to be textual that he is going to read. He wants the snippet of the code, the flow, and the metrics — the tools used, and the numbers they produced. He's much more interested in **tables** than in paragraphs or bullet points. He wants **numerical values, numbers, metrics, and results** — not prose.

**Translation into concrete rules for the Price Truth Code Review Report:**
- Default to **tables** for anything that can be tabulated (tool output, metrics, file/module breakdowns, NFR checklists) — this is the primary content format, not an occasional supplement.
- Minimize prose. Where explanation is unavoidable, keep it to short captions/notes attached to a table, not standalone paragraphs.
- Every claim should be backed by an actual number from an actual tool run — not a qualitative description ("the code is clean") without a metric next to it ("0 critical Ruff violations").
- Short code snippets are fine (and expected) to illustrate a specific point (e.g., a type stub, a key function signature) — but snippets should be short/illustrative, not full file dumps.
- Include the actual commands run (e.g., `pytest tests/ -v`) so the numbers are traceable/reproducible, not just asserted.

---

## 2. PROFESSOR'S TOOL RECOMMENDATIONS (from `code_review_tool.jpeg` — his own lecture slide)

Slide title: **"Code Review Tools – A Few Recommendations"**

| Tool | Type | Purpose |
|---|---|---|
| **Ruff** | Python linter (by Astral) | Style/syntax/import checking — PEP-8 compliance, fast |
| **PyTest** | Testing framework | Unit test execution and reporting |
| **Mutmut** | Mutation testing system for Python | Tests the tests — checks whether the test suite actually catches injected bugs |
| **Radon** | Complexity/metrics tool | Cyclomatic Complexity, Maintainability Index, Raw Metrics, Halstead Metrics |

**These 4 tools are the expected toolkit** — Price Truth's own Code Review Report should run all four against its real codebase once built, and report results in the same tabular style shown below. (This matches what `PRICE-TRUTH-BUILD-HANDOFF.md`'s Phase 6 already anticipated for "Code quality" marks — this file adds the specific tool list and the professor's format preference on top of that.)

---

## 3. REFERENCE EXAMPLE: A CLASSMATE'S SUBMISSION (Group — "Neuro-CX")

This is **not our project** — it's a different team's Lab Work Code Review submission (a "Neuroplasticity-Inspired GRU Recommendation System," Python/FastAPI/PyTorch stack), shared purely as a structural/format example of what a strong, professor-approved submission looks like. Noting its shape here so Price Truth's own report can follow the same skeleton, swapping in Price Truth's actual codebase/numbers.

### 3.1 Document header block (metadata table, not prose)
They open with a simple field/value table: Module (S4: Lab Work), Date, Live Demo URL, Team names, Stack. **Adopt this pattern** — a one-glance metadata table at the top of our own report.

### 3.2 Section 1 — Codebase [10 Marks]
- **Repository structure**: an actual file-tree diagram (monospace block) showing the real folder/file layout, with a one-line comment against each file explaining its role. Not described in prose — shown as a tree.
- **Size & Scope table**: columns = Layer | Files | SLOC | Key Responsibility. One row per architectural layer (their layers: Data Pipeline, Model, Evaluation, API, Frontend, Tests), plus a TOTAL row. This is exactly the "numbers over prose" instruction in action.
- **Frameworks & Justification table**: columns = Framework/Library | Version | Role | Justification. One row per dependency (PyTorch, FastAPI, Uvicorn, Pandas+PyArrow, scikit-learn, Gradio, PyTest, Ruff, Radon, Vanilla JS). Justification column is one terse sentence each, not a paragraph.

### 3.3 Section 2 — Code Quality (mapped 1:1 to the 4 professor-recommended tools)
- **2.1 Ruff**: states the exact command run (`py -m ruff check src/ app.py`), then a table: Category | Violations Found | Status. Ends with a one-line summary claim backed by the table (e.g., "0 critical, 1 cosmetic").
- **2.2 PyTest**: states the exact command (`py -m pytest tests/ -v`), then a result line ("44/44 PASSED, 2.66s"), then a table: Test File | Class | Tests | Coverage Area, broken down per test class, with a TOTAL row.
- **2.3 Mutmut**: explains briefly *why* a manual/adapted approach was used (their WSL/Windows tooling constraint) — this is a good model for us too if a tool doesn't run cleanly in our environment: state the constraint honestly, then show what was actually verified. Table: Mutant Type | Operator | Target | Killed by Test? | Kill Mechanism — one row per mutation type tested, ending with an estimated overall mutation score.
- **2.4 Radon** (four sub-tables, all numeric):
  - (a) Cyclomatic Complexity table: Module | CC | Grade | Assessment, plus an overall average + grade
  - (b) Maintainability Index table: Module | MI Score | Grade — every file listed, sorted by score
  - (c) Raw Metrics table: Metric | Value | Interpretation (Total LOC, LLOC, SLOC, docstring lines, comment ratio)
  - (d) Halstead Metrics table (for key modules only, not every file): Module | Vocabulary | Volume | Difficulty | Effort | Est. Bugs

### 3.4 Section 3 — NFRs Achieved [10 Marks] — a single master table
One row per NFR, columns: **NFR | ISO 25010 category | Target | Achieved | Evidence**. This is the single most important table in their whole report — it directly answers "did you hit your NFRs" with a target-vs-actual-vs-proof structure, and explicitly tags each NFR to an ISO/IEC 25010 quality category (Performance, Reliability, Maintainability, Security, Usability, Portability, etc.) — worth mirroring precisely, since it visibly ties back to a recognized software-quality standard rather than an invented rubric.

Their 12 NFR rows (as a pattern to adapt, not to copy the numbers): Inference Latency, API Availability, Test Pass Rate, CC Complexity, Maintainability, Linting, Modularity, Type Safety, Scalability, Security, Usability, Deployability.

### 3.5 Section 4 — Summary
Short — 4 bullet highlights (testing, linting, complexity, NFRs), each restating a number already shown earlier in a table, plus a two-line closing statement. Notably, even the "prose" section is really just numbers restated in sentence form — reinforcing the professor's stated preference.

---

## 4. WHAT THIS MEANS FOR PRICE TRUTH'S EVENTUAL CODE REVIEW REPORT

A checklist to apply once the real Price Truth codebase exists (do not attempt this yet — the codebase doesn't exist; this is prep only):

- [ ] Header metadata table (module, date, live demo URL, team, stack) — mirror `PRICE-TRUTH-BUILD-HANDOFF.md`'s already-decided tech stack once finalized
- [ ] Repository file-tree diagram with inline role comments (build this straight from the actual `modules/`, `ml/`, `data/`, `tests/` structure already sketched in the build handoff)
- [ ] Size & Scope table by layer (Data Pipeline / ML / API-or-Streamlit-app / Tests), with SLOC counts
- [ ] Frameworks & Justification table — reuse the justifications already drafted in the build handoff's Phase 6 (why XGBoost, why Streamlit, why SHAP) but reformat as a table with version numbers once dependencies are pinned
- [ ] Ruff run + violations table
- [ ] PyTest run + pass/fail table broken down by test file/class
- [ ] Mutmut run (or a manual/adapted mutation check, following the reference example's honest-workaround pattern if native Mutmut has environment issues) + kill-mechanism table
- [ ] Radon: CC table, MI table, Raw Metrics table, Halstead table for key modules
- [ ] A single master NFR table: NFR | ISO 25010 category | Target | Achieved | Evidence — directly built from the 9-category NFR table already in `PRICE-TRUTH-BUILD-HANDOFF.md` Phase 1e, reshaped into this target/achieved/evidence format and tagged to ISO 25010 categories
- [ ] Short numbers-restated summary at the end, no new prose claims

**Net effect:** this doesn't change *what* Price Truth needs to build (that's still the build handoff's job) — it changes *how the results get written up* once built: tool-run tables instead of descriptive paragraphs, everywhere it's possible to tabulate.

---

## 5. OPEN ITEM
Waiting on: more classmate examples (the user mentioned more may be shared) to further pattern-match the expected format before the actual Price Truth codebase/report work begins. Add further reference-example notes here (as new numbered sub-sections under Section 3) rather than overwriting this one, if/when more examples arrive — keep this file as an append-friendly reference log, matching the working style already used for `PRICE-TRUTH-MASTER-CONTEXT.md`.

---

## 6. HOW TO ACTUALLY EXECUTE THIS (current reality check + step-by-step plan)

### 6.1 The blocker: there is no Python codebase yet
Right now Price Truth has: a static HTML/CSS/JS prototype (`index.html` + `dashboard.html`, live on Netlify — no real ML, no backend, simulated data only) plus a large body of planning documents. **All four recommended tools (Ruff, PyTest, Mutmut, Radon) are Python-specific static/dynamic analysis tools — they need actual `.py` files and a real test suite to run against.** There is currently nothing for them to analyze. So the Code Review Report cannot be produced by "running tools on what exists" — a minimum real Python codebase has to be written first, even if it's smaller than the full 5-module vision.

This isn't a detour from `PRICE-TRUTH-BUILD-HANDOFF.md` — it's that document's Phases 2–4 (data, modeling, app), just scoped down to "the smallest slice that is genuinely real code, honestly tested" rather than the full feature set. Lab Work marks (Codebase, Frameworks, Code Quality, NFRs) do not require all 5 modules to be finished — they require *whatever exists* to be real, working, and well-analyzed. A smaller, fully-real, fully-tested codebase scores far better here than a large, half-fake one.

### 6.2 Minimum buildable slice (build this before touching any of the 4 tools)
Prioritize **one vertical slice that's completely real end-to-end** over partial work on all five modules. The natural choice is the **True Discount Checker**, since it's the flagship feature and the one every planning document already assumes has a real trained model + real SHAP output:

1. **Data pipeline** (`src/data_pipeline/` or similar): a script that loads the Amazon/Flipkart Kaggle CSVs, cleans them, engineers the 4–5 features already specified (price gap vs. category average, claimed discount % vs. category norm, review count, seller rating, category price volatility), and produces a bootstrapped genuine/inflated label per the heuristic approach in the Build Handoff's Phase 2.
2. **Model** (`src/model/` or similar): train one real XGBoost classifier on that data; save the trained artifact.
3. **Explainability**: wire up a real `shap.TreeExplainer` against the trained model — this is non-negotiable, since it's the project's headline differentiator and must not be faked.
4. **A thin interface**: even a bare-bones Streamlit page (or a single FastAPI endpoint) that takes an input and returns a verdict + SHAP explanation counts as the "API/backend" layer for review purposes — it does not need the full 5-module UI yet.
5. **Tests** (`tests/`): a real PyTest suite — even 10–15 tests covering the data-cleaning function, the feature-engineering function, and the model's output shape/sanity (this mirrors the reference example's `TestSchema`, `TestCleanData`, `TestGRUBaselineForward`-style test classes) is enough to generate meaningful PyTest, Mutmut, and Radon results.

**This slice alone is enough to run all 4 tools meaningfully and produce a real, non-fabricated report** — the other 4 modules (Live Pack Lookup, Unit Price Comparison, Buy Timing Signal, Shrink Timeline) can be added afterward, or left as "in progress" in the report, which is an honest and acceptable thing to state given the project's own stated academic-integrity stance (see the Limitations list in `PRICE-TRUTH-BUILD-HANDOFF.md`).

### 6.3 Order of operations
1. Build the slice above (Phase 2 + Phase 3 + a thin Phase 4, from the Build Handoff) — this is coding work, not tool-running.
2. Write the PyTest suite alongside it (don't leave tests for last — the reference example's strength was that tests existed for real behaviors, not decorative ones).
3. Run **Ruff** first (`ruff check src/ app.py` or equivalent) — fastest, catches basic issues before anything else.
4. Run **PyTest** (`pytest tests/ -v`) — confirms the tests actually pass.
5. Run **Radon** — three separate commands, all on the same codebase:
   - `radon cc <path> -a` → Cyclomatic Complexity + average grade
   - `radon mi <path>` → Maintainability Index per file
   - `radon raw <path>` → Raw Metrics (LOC, LLOC, SLOC, comments)
   - `radon hal <path>` → Halstead metrics (run this on 3–5 key modules, not every file, per the reference example's pattern)
6. Attempt **Mutmut** last, since it's the most environment-fragile of the four. If it doesn't run cleanly (a real risk on Windows, exactly as the reference example ran into with WSL), fall back to the reference example's own workaround: manually reason through 5–7 mutation types by hand (e.g., "what if `>` became `>=` in the filtering logic — does a real test in the suite catch that?") and present it as a deliberate, disclosed manual analysis rather than a tool failure — this is a legitimate, professor-acceptable substitute, not a cop-out, precisely because the reference example did the same thing openly.

### 6.4 What to send back once results exist
Whatever comes out of each tool run — raw terminal output, screenshots, exported CSVs/JSON (Radon and Mutmut can both export machine-readable output) — send it over as-is. From that, the actual Code Review Report gets built by mapping results directly into the table structures already specified in Section 3/4 of this file (Size & Scope, Frameworks & Justification, Ruff violations table, PyTest results table, Mutmut kill-mechanism table, the four Radon sub-tables, and the master NFR table). No results need to be pre-formatted before sending — raw output is exactly what's needed to fill in real numbers rather than invented ones.

### 6.5 Realistic sequencing given the Oct 2 deadline
Given Lab Work is due Oct 2 and no Python code exists yet, the practical order is: **(1) lock scope** (Build Handoff Phase 1 decisions — which 5 features, Streamlit vs. static, one clear plan) **→ (2) build the one real vertical slice above** **→ (3) run the 4 tools** **→ (4) send results here for the report.** Steps 1–2 are the actual bottleneck; the tool-running and report-writing in steps 3–4 are comparatively fast once real code exists.
