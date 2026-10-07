# PRICE TRUTH — BUILD PHASE HANDOFF DOCUMENT
**Purpose:** Everything needed to actually *build* Price Truth (not just plan/pitch it), starting from a clean context in a new chat. This is the execution companion to `PRICE-TRUTH-MASTER-CONTEXT.md` (the historical decision log covering Deliverables 1–3, now submitted). Read this whole file before starting work in the next chat — it is designed to be self-sufficient.

**Where we are:** Deliverables 1–3 (Business Need doc, Wireframe/Prototype, Presentation — 40/100 marks) are submitted (Aug 21, 2026). What remains is the real engineering work:
- **S3 Lab Work** — 40 marks, due **Oct 2, 2026**: Codebase (10), Frameworks with justification (10), Code quality (10), NFRs achieved (10)
- **S3 Working Demo** — 20 marks, due **Oct 16, 2026**: the application should actually work (video allowed as backup)

That's 60 of the remaining 60 marks. Everything below is organized to get there.

---

## PHASE 0 — PROJECT IDENTITY (context, don't re-derive)

- **Project:** Price Truth — ML-powered web app that (a) flags whether an e-commerce discount is genuine or inflated, and (b) tracks shrinkflation (FMCG pack-size shrinkage at constant price).
- **Team / Group 11:** Swagata Bhowmik (B053) — technical lead (ML, data pipeline, backend); Charvi Rathod (B049) — product/UX, business model; Yashwi Shah (B036) — data curation, frontend, testing.
- **Course:** M.Sc. Data Science, 3rd Semester, NMIMS Nilkamal School of Mathematics, Applied Statistics & Analytics. Professor: Dr. Yogesh Naik.
- **Professor's 5 core requirements** (already satisfied in Deliverables 1–3, but the build must stay consistent with them):
  1. Web application, not static website (dynamic input → ML processing → results)
  2. Comparative analysis vs. CamelCamelCamel / Keepa / PriceBaba / BigBasket
  3. Named user personas: Priya (28, online shopper), Rajesh (45, grocery buyer/budget-conscious parent), Aarav (23, student)
  4. Business need: ₹7.8 lakh crore Indian e-commerce market, 25% YoY growth, 300M+ shoppers, no existing Indian tool
  5. Business flow / architecture: User → Frontend → Backend → ML Layer (SHAP) → Data Layer → Results

---

## PHASE 1 — LOCK THE SCOPE (do this first, in the next chat, before writing any code)

Several things drifted across the planning phase and need a single, final decision before building, or the codebase will not match the submitted documents:

### 1a. Which 5 features are actually being built?
Two versions exist in submitted materials:
- **Original 5** (Deliverable 1 PDF, most planning docs): True Discount Checker, Live Pack Lookup (Open Food Facts API), Unit Price Comparison, Buy Timing Signal, Shrink Timeline
- **Updated 5** (the final Deliverable 3 presentation): True Discount Checker, Shrinkflation Timeline, Unit Price Comparator, Buy Timing Signal, **Cross-Platform Price Aggregator** (replaces Live Pack Lookup)

**Recommendation:** Build the **original 5** (with Live Pack Lookup) as the primary MVP, since it's the version backed by a real, working, no-auth-required live API (Open Food Facts) and matches the majority of submitted written documentation (the Business Need PDF). "Cross-Platform Price Aggregator" would require live scraping or paid APIs from Amazon/Flipkart/BigBasket, which the project has *explicitly and repeatedly* ruled out for ToS-compliance reasons (see Phase 0 honesty commitments below). If the professor references the newer presentation's 5th feature, frame Live Pack Lookup as a limited-scope demonstration of what a "Cross-Platform Aggregator" would need (i.e., don't over-promise scraping you won't build).

**→ Confirm this decision explicitly with Charvi/Yashwi before starting Phase 2.**

### 1b. Frontend framework: Streamlit vs. the existing static HTML/JS prototype?
- All Lab Work planning docs (roadmap, tech stack, architecture diagrams) assume **Streamlit** (Python-native, fastest path to a real ML-backed app, free Streamlit Cloud hosting).
- The *already-live* Deliverable 2 prototype (`index.html` + `dashboard.html` at https://price-truth.netlify.app/) is static HTML/CSS/JS with **simulated/hardcoded data only** — explicitly built with "no real ML model execution, no real API calls, no backend" per its own build prompt.
- **Recommendation:** Build the real, ML-backed application in **Streamlit** as a *separate, new deliverable* for Lab Work/Demo — don't try to retrofit real ML into the static Netlify site. Reuse the Netlify site's visual language (whichever palette you pick — see 1c) as inspiration for the Streamlit UI, but the Streamlit app is the "real" product from here on.

### 1c. Pick ONE color palette and stop drifting
Five different palettes appeared across the project's history:
1. Navy #1E3A5F / Coral #FF6B6B / Green #2ECC71 / Amber #F39C12 (original Business Need doc + most PPT prompts)
2. Pastel: soft blue #6B8DBF / peach #FFB5A7 / mint #B4E7CE / butter #FFE8A3 / lavender #E0D4F7 (live `dashboard.html`)
3. Darker coral #C0392B / teal #1F7A5C / amber #B9700E / navy #151C24 ("ultimate" PPT prompt)
4. Coral #FF6B6B / Teal #1F7A5C / Navy #1E3A5F / Amber #F39C12 (ChatGPT visual prompt)
5. Purple/lavender gradient + coral/salmon + mint checkmarks, shield logo, "Powered by AI" tagline (final Deliverable 3 PDF — **this is the newest and most polished, likely the best "official" brand going forward**)

**Recommendation:** Adopt palette #5 (the final presentation's purple/lavender/coral "Price Truth — Truth. Transparency. Trust." identity with the shield logo) as the single canonical brand for the Streamlit app, since it's the newest, most-refined, and represents what a professor/interviewer will have most recently seen. Document this choice once and stop re-deriving it.

### 1d. Honesty commitments to preserve from planning (do not violate these when building)
- No live scraping of Amazon/Flipkart (ToS compliance) — only Kaggle static datasets + the one live, no-auth Open Food Facts API.
- Predictions are **category-level**, not per-exact-SKU-per-exact-date (datasets are snapshots, not time-series).
- Don't literally claim "92% ML accuracy" or "2.5M+ products tracked" in the actual demo/codebase unless the trained model and data pipeline genuinely produce those numbers — those were pitch-deck framing in the final presentation, not verified engineering facts. Report real numbers from your real trained model.
- SHAP explainability must come from an actual `shap.TreeExplainer` on an actual trained model — not hardcoded/simulated bar values (the mockups used illustrative numbers; the real app must not).

---

## PHASE 1e — FULL REQUIREMENTS TO BUILD AGAINST (don't lose these)

### Functional Requirements (from the submitted Business Need doc — the codebase should trace back to these)
| ID | Requirement | Priority |
|---|---|---|
| FR1 | User input — accept product price, category, barcode | HIGH |
| FR2 | Discount verification — ML model flags suspicious discounts | HIGH |
| FR3 | SHAP explanation — feature-level explanation per verdict | HIGH |
| FR4 | API integration — live query to Open Food Facts | HIGH |
| FR5 | Unit price calculation — price per 100g/ml | MEDIUM |
| FR6 | Buy timing prediction — category-level seasonal analysis | MEDIUM |
| FR7 | Shrink timeline display — visual history of pack-size changes | MEDIUM |
| FR8 | Results display — verdict + buy links out to Amazon/Flipkart/Meesho/Myntra | HIGH |
| FR9 | Authentication (optional, future — do not build unless time permits) | LOW |
| FR10 | Data export — download results as PDF (future — do not build unless time permits) | LOW |

Buy-out links (FR8): plain hyperlinks for now; affiliate-tagged versions (Amazon Associates / Flipkart Affiliate) are a stated future step once accounts are approved — don't block the MVP on affiliate approval.

### Non-Functional Requirements — all 9 categories (the Lab Work rubric grades "NFRs achieved" — measure every one of these for real, don't just restate targets)
| Category | Target | Implementation |
|---|---|---|
| Performance | <3s page load, <2s prediction | `@st.cache_resource` for the model, `@st.cache_data` for datasets |
| Scalability | 100 concurrent users | Stateless design, Streamlit's own session handling |
| Usability | Non-technical users, no manual needed | Clean UI, tooltips, pre-filled example inputs |
| Security | HTTPS, no PII/data storage | Streamlit Cloud's managed HTTPS; don't add accounts/storage |
| Reliability | 99% uptime (during evaluation window) | Cloud hosting; check the live link daily before the demo |
| Portability | Desktop, tablet, mobile | Streamlit's responsive layout; spot-check on a phone |
| Maintainability | Modular code | Separate file per module (see Phase 4 repo structure) |
| Availability | 24/7 accessible | Cloud infrastructure (Streamlit Cloud free tier) |
| Compatibility | Chrome, Firefox, Safari, Edge | Cross-browser smoke test before the demo |

### Limitations to state openly in the Lab Work write-up (this project's stated academic-integrity stance — don't paper over these)
- Public datasets are price *snapshots*, not daily time-series per SKU → predictions are category-level, not per-product-per-exact-date.
- Live scraping of Amazon/Flipkart is deliberately excluded (ToS risk) — only Kaggle static datasets + the one live, no-auth Open Food Facts API.
- Affiliate commission requires platform approval (not guaranteed, takes time) → plain hyperlinks used initially.
- Open Food Facts is crowdsourced — field completeness varies; the app should degrade gracefully (clear "data not available" states) rather than error out on missing fields.
- Any SHAP values shown must come from a real trained model at inference time — the illustrative numbers used in every mockup/pitch deck to date (e.g., "+0.31, +0.28...") were hand-set for demo purposes, not computed.
- Don't literally claim "92% ML accuracy" or "2.5M+ products tracked" (numbers that appeared in the final pitch deck) in the actual codebase/report unless your real trained model and real dataset genuinely produce them — report your actual measured numbers instead.

---

## PHASE 2 — DATA (build this before any modeling)

### Datasets to acquire
| Source | Size (as documented) | Role | Status |
|---|---|---|---|
| Amazon Sales Dataset (Kaggle) | ~1,465 products | Core training data for True Discount Checker | Not yet confirmed downloaded |
| Flipkart E-commerce Dataset (Kaggle) | ~20,000 listings | Cross-platform validation | Not yet confirmed downloaded |
| Flipkart Retail Product Dataset (Kaggle) | 5.7M+ records | Optional scale-up once pipeline validated | Not yet confirmed downloaded |
| Flipkart Product Review Dataset (Kaggle) | 194,276 rows | Reserved for a *future* sentiment/quality-drift feature — not part of the MVP, don't build against it yet | Not yet confirmed downloaded |
| Open Food Facts API | Global, live, no auth | Live Pack Lookup module | API confirmed reachable in planning; not yet integrated in real code |
| Self-collected primary data | 30–40 in-store photos (MRP + weight labels) | Shrink Timeline evidence | Not yet collected (needs manual store visits — assign to a team member) |

### Data tasks (in order)
1. Download Amazon + Flipkart Kaggle datasets; store raw copies untouched.
2. Write a cleaning/merging script: standardize category names across platforms, remove duplicates/nulls/outliers, align price fields, unify currency/units.
3. Feature engineering for the discount-detection model: price gap vs. rolling category average, claimed discount % vs. category norm, review count, seller rating, category price volatility (these 4–5 features are exactly what the SHAP mockups already assume — build the real pipeline to actually produce them).
4. Build a labeled target for "genuine vs. inflated discount" — since no dataset comes pre-labeled with this, you'll need a **heuristic/rule-based labeling pass** (e.g., flag discounts where claimed price is >X standard deviations above the category's realistic price range) to bootstrap training labels, and be upfront about this in the write-up (this is a legitimate, common approach for anomaly-style labels — document it as a limitation/methodology choice, not hide it).
5. Test Open Food Facts API calls (barcode lookup, product-name search) and cache sample responses for offline demo reliability (don't depend on live internet during the actual demo presentation — always have a cached fallback).
6. Collect the 30–40 shrinkflation reference photos/data points (can supplement with cited public shrinkflation reporting if store visits aren't feasible in time — cite sources).

---

## PHASE 3 — MODELING

### True Discount Checker (flagship feature)
- **Algorithm:** Anomaly-style binary classifier — XGBoost (as documented everywhere) or start simpler with Isolation Forest / a rule-based baseline first, then upgrade to XGBoost once labels exist.
- **Input features:** price gap vs. category rolling average, claimed discount % vs. category norm, review count, seller rating, category price volatility (matches every SHAP mockup already shown to the professor — keep these consistent).
- **Output:** binary verdict (genuine / flagged) + probability/confidence score.
- **Explainability:** `shap.TreeExplainer(model)` → `shap_values` → waterfall plot per prediction. This must be REAL, computed at inference time, not hardcoded.

### Buy Timing Signal
- Category-level seasonal model (e.g., simple seasonal decomposition or Prophet) against known Indian sale calendar events (Republic Day Sale, Big Billion Days/Diwali, Prime Day). Keep this simple — a lookup table of "category X historically drops during event Y" is an acceptable, honestly-scoped MVP if a full time-series model is too much for the timeline; state the simplification openly.

### Unit Price Comparison
- Pure calculation, no ML needed: price ÷ pack size, normalized to price-per-100g/ml, across variants of the same product.

### Shrink Timeline
- Data visualization only (no ML) — plot documented pack-size-over-time data points per product.

### Live Pack Lookup
- Direct Open Food Facts API call + display — no ML, just integration.

**Minimum Viable Model bar for Lab Work grading:** you need *at least one* real trained model with real SHAP explainability wired end-to-end (True Discount Checker) to satisfy "Codebase" and "Frameworks with justification" marks credibly. The other 4 modules can be simpler (rule-based/calculation/API-only) and still legitimately count as part of "5 core features," since the original Business Need document already frames them at varying levels of ML-sophistication.

---

## PHASE 3b — VISUAL REFERENCE FOR THE REAL UI

`Price_Truth.png` (an infographic image shared early in planning, fully transcribed in `price-truth-image-prompt.md`) contains a detailed "Website Preview" dashboard mockup that is the richest UI reference on record — use it as the layout target for the Streamlit app's main dashboard view, adapted to whichever palette Phase 1c settles on:
- Top nav: logo + tagline, search bar, dark-mode toggle, login button
- Left sidebar: Dashboard, Discount Checker, Buy Timing Signal, Shrink Timeline, Live Product Lookup, Unit Price Comparator, History, Saved Products, Settings, About Us
- 4 main widget panels in a 2×2 grid: True Discount Checker (genuineness gauge + SHAP top-reasons bars), Buy Timing Signal (countdown + confidence + prediction chart), Shrinkflation Timeline (quantity-over-time + % shrinkage), Unit Price Comparator (best-value highlight)
- Below that: Product Details card + SHAP Explainability bar chart side by side
- Bottom row: "Buy From Verified Platforms" (Amazon/Flipkart/Myntra/Meesho buttons) + "Recent Activity" feed

This was always a concept mockup, not literal spec — but it's a good north star for what "done" looks like visually, and it's the mockup the professor has effectively already seen (via the Business Need doc's figure references and the final presentation).

---

## PHASE 4 — APPLICATION (Streamlit)

### Architecture (already documented, now actually build it)
```
User Input → Streamlit Frontend → Python Backend (functions/modules) → ML Layer (XGBoost + SHAP) → Data Layer (cleaned CSVs + Open Food Facts API) → Results Display
```

### Suggested repo structure
```
price-truth/
├── app.py                     # Streamlit entrypoint, page routing between 5 modules
├── modules/
│   ├── discount_checker.py    # True Discount Checker UI + inference call
│   ├── pack_lookup.py         # Open Food Facts API integration
│   ├── unit_price.py          # Unit price comparison calculator
│   ├── buy_timing.py          # Seasonal buy-timing lookup/model
│   └── shrink_timeline.py     # Shrinkflation timeline visualization
├── ml/
│   ├── train_discount_model.py
│   ├── model.pkl              # trained XGBoost model artifact
│   └── shap_explainer.py
├── data/
│   ├── raw/                   # untouched Kaggle downloads
│   ├── processed/             # cleaned/merged datasets
│   └── shrink_evidence/       # photos/data for shrink timeline
├── tests/                     # unit tests — needed for "code quality" marks
├── requirements.txt
└── README.md
```

### Non-functional requirements to actually implement (not just claim)
| NFR | Target (as promised in Deliverable 1) | How to actually satisfy it |
|---|---|---|
| Performance | <3s page load, <2s prediction | Cache the trained model with `@st.cache_resource`; cache data loads with `@st.cache_data` |
| Scalability | 100 concurrent users | Stateless design, no server-side session state beyond Streamlit's own; document this as the scaling strategy |
| Usability | No manual needed | Tooltips, pre-filled example inputs, clear empty states |
| Security | No PII stored, HTTPS | Streamlit Cloud provides HTTPS by default; don't add any user accounts/storage that would need securing |
| Reliability | 99% uptime (during evaluation window) | Deploy early, test the live link daily before Oct 16 |
| Portability | Desktop/tablet/mobile | Streamlit is responsive by default; spot-check on a phone browser |
| Maintainability | Modular code | The `modules/` structure above; keep functions small and documented |

### Code quality checklist (10 marks — don't skip)
- Docstrings on every function/module
- `requirements.txt` pinned to specific versions
- At least a handful of unit tests (`tests/`) — e.g., test the unit-price calculation, test the data-cleaning function on a small fixture
- Consistent naming, no dead/commented-out code left in
- A clear `README.md`: setup instructions, how to run, architecture diagram, known limitations

---

## PHASE 5 — DEPLOYMENT & DEMO PREP

- Deploy the real Streamlit app to **Streamlit Community Cloud** (free tier) — this becomes the "working demo" URL, separate from the existing static Netlify prototype.
- Decide whether to keep both live (static Netlify prototype = original wireframe submission record; new Streamlit app = the real working product) or consolidate — recommend keeping both, and being explicit in the demo about which is which.
- Prepare a **backup demo video** (rubric explicitly allows this) in case of live-deploy issues on demo day — screen-record a full walkthrough of all 5 modules well before Oct 16.
- Rehearse a script that maps every demo action back to the 5 professor requirements and the FR/NFR list, so the demo doubles as evidence for the Lab Work write-up.

---

## PHASE 6 — WRITE-UP FOR LAB WORK SUBMISSION (40 marks)

Map directly to the 4 graded components:
1. **Codebase (10):** the repo itself, well-organized per Phase 4's structure.
2. **Frameworks with justification (10):** a short doc/section explaining *why* XGBoost (interpretable, handles tabular data well, works with SHAP TreeExplainer efficiently), *why* Streamlit (fastest path from Python ML code to a deployed web UI, free hosting, matches team's Python skill set vs. learning a JS framework), *why* SHAP specifically (model-agnostic-enough but optimized for trees, produces the exact waterfall visualization already promised to the professor in Deliverables 1 & 3).
3. **Code quality (10):** the checklist in Phase 4.
4. **NFRs achieved (10):** a short table (like Phase 4's) showing target vs. actual measured result for each NFR — e.g., actually time the page load and prediction latency and report real numbers, don't just restate the target.

---

## APPENDIX A — BUSINESS CONTEXT (not needed to write code, but part of "everything" — keep for the write-up/demo narration)

**Business model (as submitted):** affiliate commissions (Amazon Associates/Flipkart Affiliate, 4–8%, plain links until approved) as the primary near-term revenue stream; a future B2B pricing-insights API for small D2C sellers as the secondary stream; premium alert subscriptions and a "Verified Honest Seller" badge as longer-term ideas. None of this needs to be *built* for Lab Work/Demo — it's pitch-deck material — but keep it available in case the demo narration or write-up references "how this becomes a real product."

**Go-to-market (pitch framing, not a build task):** soft launch as the college project itself → content marketing around the shrinkflation story → affiliate program applications → public launch (Product Hunt-style) → scale. Not relevant to the codebase; only relevant if asked about future scope during the demo.

## APPENDIX B — ORIGINAL PHASE ROADMAP (from the submitted Business Need document — cross-check against Phase 1–6 above so nothing silently drops)
| Phase | Original dates | Deliverables |
|---|---|---|
| 1: Planning | Aug 10–23 | Requirements, mockups, architecture (✅ done — this is Deliverables 1–3) |
| 2: Data | Aug 24–Sep 6 | Download, clean, merge datasets |
| 3: ML Models | Sep 7–20 | Discount detector, SHAP integration |
| 4: App Dev | Sep 21–Oct 4 | Streamlit UI, API integration |
| 5: Testing | Oct 5–11 | Feature testing, deployment |
| 6: Demo | Oct 12–16 | Documentation, video, presentation |

This original timeline has almost certainly already slipped relative to today's date — Phase 2 (Data) was supposed to start Aug 24 and Lab Work is due Oct 2, so **the very first thing to establish in the next chat is how much of Phases 2–4 above is realistically still possible before Oct 2**, and compress/triage accordingly (this is exactly why Phase 1 of this handoff exists — to lock scope fast rather than relitigate it).

---

## OPEN QUESTIONS TO RESOLVE AT START OF NEXT CHAT
1. Confirm Phase 1a (which 5 features), 1b (Streamlit vs. static), 1c (which palette) with teammates before writing code.
2. Has anyone actually downloaded the Kaggle datasets yet, or does Phase 2 start from zero?
3. Realistic time budget: Oct 2 (Lab Work) is the harder deadline — is there enough runway for real model training, or should the team start Phase 2/3 immediately?
4. Who owns which module (per the team-role split already documented: Swagata = ML/backend, Charvi = product/UX decisions + business-facing write-up, Yashwi = data curation/frontend/testing)?
5. Should the existing static Netlify prototype be retired, kept as-is, or updated to link to the new real Streamlit app?

---

## REFERENCE: WHERE THE FULL HISTORY LIVES
Everything about *how* Deliverables 1–3 were produced (every draft, every dead-end, every color-scheme iteration, the full professor rubric verbatim, all persona/competitive-analysis/business-model content already written and submitted) is preserved in `PRICE-TRUTH-MASTER-CONTEXT.md` (append-only log, 5 appends). That file is the historical record; this file is the forward execution plan. Bring both into the next chat if deep historical detail is ever needed, but this file alone should be enough to start building.
