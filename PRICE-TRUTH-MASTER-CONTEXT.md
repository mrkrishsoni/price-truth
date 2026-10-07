# PRICE TRUTH — MASTER CONTEXT & TRACKING FILE
**Purpose:** Single running record of everything decided, built, and planned for this project across all conversations. Read this file first before acting on any new request. New information gets *appended* to the end under a new dated section — earlier sections are not rewritten, so history is preserved.

**Last updated:** Initial consolidation (from batch of uploaded files, first pass)

---

## 1. PROJECT IDENTITY

- **Name:** Price Truth
- **One-line pitch:** A web application that verifies whether e-commerce discounts are real and whether FMCG products have secretly shrunk in pack size — using real Amazon/Flipkart data, a live public API, and explainable ML (SHAP).
- **Context:** Final-year M.Sc. Data Science academic project, also intended as a portfolio piece for recruiters.
- **Team:**
  - Swagata Bhowmik (B053)
  - Charvi Rathod (B049)
  - Yashwi Shah (B036)
- **Course:** M.Sc. Data Science, 3rd Semester
- **Institution:** NMIMS Nilkamal School of Mathematics, Applied Statistics & Analytics

---

## 2. HOW THE PROJECT IDEA WAS CHOSEN (decision history)

Two ideas were evaluated:
- **Idea A — "Price Truth":** Detect fake/inflated e-commerce discounts + predict good times to buy, using real historical pricing data.
- **Idea B — "Pack Truth":** FMCG shrinkflation tracking (pack sizes shrinking at same price).

**Decision:** Idea A is the primary project. Idea B is folded in as one feature/module ("Shrink Timeline") inside Price Truth, not a separate project.

**Reasoning:**
- Price Truth has stronger, more complete real datasets; Pack Truth needs manual primary data to be credible.
- Price Truth = deeper actual data science (anomaly detection, seasonality modeling) vs. Pack Truth being closer to data storytelling.
- Price Truth has a clearer business model (affiliate + B2B API).
- Price Truth is closer to real problems e-commerce/FANG companies work on — matters for recruiter appeal.
- The "did your snack shrink?" hook from Pack Truth is kept as an opening anecdote and as the Shrink Timeline feature, not discarded.

**Key scoping honesty (stated openly, not hidden):** No available dataset tracks a single product's price daily over time — they're snapshots. So price/timing predictions are made at the **category level** (e.g., "this category tends to see its biggest discount during Diwali"), not per-exact-product-per-exact-date.

---

## 3. THE PROFESSOR'S RUBRIC (source of truth for all requirements)

From `prompt-for-ai.md` — Prof. (Dr.) Yogesh Naik's course evaluation slides:

### Course Evaluation — 100 marks total

| Distribution of ICA | Marks | Due Date | Focus Area |
|---|---|---|---|
| S1: Business Need (Lit Review/Products) | 10 | 24 Jul 26 | Deck justifying why the Application/App |
| S1: Wireframe / Prototype | 10 | 7 Aug 26 | Prototype demonstrating UX/UI for all screens |
| S2: Project Presentation (Deck) | 20 | 21 Aug 26 | Detailed deck: Application need; Development approach & features; Challenges (tech & otherwise); Limitations & future scope |
| S3: Lab work | 40 | 2 Oct 26 | Codebase (10); Frameworks w/ justification (10); Code quality (10); NFRs achieved (10) |
| S3: Working Demo | 20 | 16 Oct 26 | App should work (video as backup) |

**Note on dates:** Some later planning documents (e.g. FINAL-WORKFLOW-GUIDE.md) refer to "August 21st, 2026" as the due date for a bundle of 3 deliverables (Word doc, Wireframe URL, PPT) — this appears to treat S1 Wireframe + S2 Presentation (and a Business Need write-up) as being submitted together on Aug 21, rather than on the original separate Jul 24 / Aug 7 dates. **This date discrepancy has not been explicitly reconciled — flag to user if it matters.**

### The 5 explicit questions professor wants addressed (recurring across all planning docs):
1. **Req #1:** Web application or website? (justify which, and why)
2. **Req #2:** Comparative analysis of what exists in the market today
3. **Req #3:** Whose problem are we solving (user personas)
4. **Req #4:** Business need
5. **Req #5:** Business flow of the application

Plus bonus/expected content:
- Functional Requirements (FR list)
- Non-Functional Requirements — 9 categories: Performance, Scalability, Portability, Usability, Compatibility, Security, Reliability, Maintainability, Availability

---

## 4. PROBLEM STATEMENT

**Problem 1 — Fake/inflated discounts:** E-commerce platforms show an inflated "original price" next to today's price to make discounts look bigger than they are (e.g., shown as ~~₹5,000~~ → ₹2,500 "50% OFF", but real recent price was ₹2,600, so real discount ≈ ₹100/4%). No easy way for shoppers to verify this today.

**Problem 2 — Shrinkflation:** FMCG companies reduce pack size instead of raising price, especially at fixed price points (₹5/₹10/₹20). Invisible to consumers without historical data. Examples used throughout materials:
- Lay's Classic: 100g → 85g at same ₹20 (15% less product)
- Parle-G: 125g → 100g at same ₹20 (20% less product)
- Maggi: 4-pack → 3-pack at same ₹40 (25% less product)
- Britannia 50-50: 100g → 85g at same ₹15

**Why it's a genuine gap:** UK & EU legally require unit pricing (price per kg/liter) displayed; India has no such requirement and no accessible consumer tool fills this gap.

**Supporting stat used throughout:** ~70% of Indian shoppers cite "discount" as their primary purchase driver, yet have no discount-authenticity verification tool.

---

## 5. MARKET CONTEXT / BUSINESS NEED (Req #4)

- India e-commerce market size: **₹7.8 lakh crore** (~$100B USD)
- Growth rate: **25% YoY**
- Online shoppers: **300M+**
- Trust crisis context: 2022 Consumer Affairs Ministry investigations into fake festive-sale discounts; 2023 inflated-MRP exposés; growing social media awareness of pricing tricks.
- Regulatory gap: UK/EU mandate unit pricing; India does not.
- Opportunity framed as: **first-mover advantage** for a transparency-first pricing verification platform in India ("FIRST — no existing Indian solution").

---

## 6. TARGET USERS / PERSONAS (Req #3)

Used consistently across every deliverable:

1. **Priya, 28 — Budget-conscious online shopper**
   - Problem: "I see 70% off but don't know if it's real. I waste time checking multiple tabs."
   - Pain point: Information asymmetry
   - Solution: Instant ML verification + explanation

2. **Rajesh, 45 — Grocery buyer / homemaker**
   - Problem: "My regular biscuit pack feels lighter but costs the same ₹20. Am I imagining it?"
   - Pain point: Shrinkflation is invisible without historical data
   - Solution: Visual shrink timeline (historical pack-size tracking)

3. **Aarav, 23 — Student / young professional**
   - Problem: "I want to buy a laptop. Should I wait for the next sale?"
   - Pain point: No data-driven purchase-timing signal
   - Solution: Category-level buy-timing predictions

**Secondary/future users:** Small D2C sellers (future B2B pricing API), researchers/academics.

---

## 7. SOLUTION — 5 CORE MODULES

1. **True Discount Checker** ⭐ (core feature)
   - Input: category, listed price, discounted price (optional product URL)
   - Process: ML anomaly detection (XGBoost) + SHAP explainability, compares against category's real historical price spread
   - Output: verdict (verified real deal / inflated discount) + confidence % + SHAP feature-level breakdown

2. **Live Pack Lookup**
   - Input: barcode or product name
   - Process: live call to Open Food Facts API
   - Output: real-time brand, weight, category data

3. **Unit Price Comparison**
   - Input: product across multiple pack sizes
   - Process: computes price per 100g/ml
   - Output: best-value pack size identified

4. **Buy Timing Signal**
   - Input: product category
   - Process: category-level seasonal model against Indian sale calendar (Big Billion Days, Republic Day Sale, Diwali, Prime Day)
   - Output: "buy now" or "typically drops during [window]"

5. **Shrink Timeline**
   - Input: well-known FMCG product
   - Process: plots documented pack-size changes at same price over years (primary + cited data)
   - Output: visual shrink history

All verified products link out to Amazon, Flipkart, Meesho, Myntra (plain links now; affiliate-tagged links once affiliate programs approve).

---

## 8. SHAP EXPLAINABILITY (the differentiator)

- **What:** SHapley Additive exPlanations — game-theoretic method showing how much each feature contributed to a specific model prediction relative to baseline.
- **Why it matters for this project:** Turns the True Discount model from a black box into something defensible — "why was this flagged?" gets a real, data-grounded answer instead of "the model said so."
- **Illustrative example used throughout materials (hand-set numbers for demo, NOT yet a trained model):**

| Feature | Contribution | Direction |
|---|---|---|
| Price gap vs. 90-day real average | +0.31 | Toward "flagged" |
| Claimed discount vs. category norm | +0.28 | Toward "flagged" |
| Review count (low) | +0.09 | Toward "flagged" |
| Category price volatility | +0.06 | Toward "flagged" |
| Seller rating (moderate) | −0.04 | Toward "genuine" |

- **Planned production implementation:**
```python
import shap
import xgboost as xgb

model = xgb.XGBClassifier()
model.fit(X_train, y_train)  # y = "is this discount genuine or inflated"

explainer = shap.TreeExplainer(model)
shap_values = explainer(X_test)
shap.plots.waterfall(shap_values[0])
```

- **Explicit honesty flag:** The SHAP waterfall currently shown in the HTML proposal/mockups uses illustrative, hand-set numbers. Production version must use a real trained model, not hardcoded values.

---

## 9. COMPETITIVE ANALYSIS (Req #2)

| Solution | What they do | Coverage | Limitations | Price Truth advantage |
|---|---|---|---|---|
| CamelCamelCamel | Amazon price history | US only | No India support, no ML | India-focused + ML + SHAP |
| Keepa | Browser extension, price graphs | Global (paid) | Subscription required, no fraud detection | Free + SHAP explainability |
| PriceBaba / MySmartPrice | Multi-platform price comparison | India | Current prices only, no historical analysis | Historical + predictive |
| BigBasket / Amazon (partial) | Inconsistent unit pricing | India | Not mandatory, no shrinkflation tracking | Systematic tracking |
| News articles | One-off shrinkflation stories | Ad-hoc | No consumer-facing tool | Dedicated systematic platform |

**Unique value props emphasized:** SHAP explainability (shows *why*, not just "suspicious"); shrinkflation tracking (no other Indian tool does this systematically); cross-platform (Amazon + Flipkart); legal data sourcing (no ToS violations); category-level predictive buy signals.

---

## 10. WEB APPLICATION vs WEBSITE (Req #1)

**Position taken:** This is a **Web Application** (specifically framed as a Progressive Web Application, PWA), not a static website.

Justification used consistently:
- Dynamic user interactions (input → real-time results)
- Backend ML processing (anomaly detection, SHAP calculations)
- Live API integration (Open Food Facts)
- Database/data layer (product datasets)
- State management (user sessions)

---

## 11. TECHNICAL ARCHITECTURE / BUSINESS FLOW (Req #5)

**System flow (used in every deck):**
```
User Input
    ↓
Streamlit Frontend
    ↓
Python Backend
    ↓
ML Layer (XGBoost + SHAP)
    ↓
Data Layer (CSV + Open Food Facts API)
    ↓
Results Display
```

**Tech stack:**
- **Data processing:** Python, pandas, NumPy
- **Machine Learning:** scikit-learn (anomaly detection), XGBoost/LightGBM (True Discount classifier), Prophet/statsmodels (seasonal buy-timing model)
- **Explainability:** SHAP (`shap.TreeExplainer`)
- **Frontend:** Streamlit (primary, per later planning docs) — note: earlier `price-truth-project-context.md` describes frontend as HTML5/CSS3/JS + Chart.js/Plotly.js with optional Flask/FastAPI backend. **These two descriptions differ (Streamlit-based app vs. custom HTML/JS site) — later documents (TODAYS-ACTION-PLAN.md, HOW-TO-BUILD-PPT.md, DELIVERABLE docs) consistently settle on Streamlit as the actual build plan; the custom-HTML approach appears to be from the earlier proposal/pitch-deck stage.**
- **APIs:** Open Food Facts (live, working today, no auth needed)
- **Deployment:** Streamlit Cloud (free tier)

**Data sources:**
| Source | Size | Role |
|---|---|---|
| Amazon Sales Dataset (Kaggle) | ~1,465 products | Core training data for True Discount detector |
| Flipkart E-commerce Dataset (Kaggle) | 20,000 listings | Cross-platform validation |
| Flipkart Retail Product Dataset (Kaggle) | 5.7M+ records | Scale-up dataset once pipeline validated |
| Flipkart Product Review Dataset (Kaggle) | 194,276 rows | Reserved for future sentiment/quality-drift feature |
| Self-collected primary data | ~30–40 in-store photos (MRP + weight) | Grounds the Shrink Timeline in first-hand evidence |

**APIs status:**
- Open Food Facts API: ✅ live, usable now, free, no registration
- Amazon Product Advertising API: ⏳ roadmap (needs approved Associates account with sales history)
- Flipkart Affiliate API: ⏳ roadmap (same gating issue)
- Live scraping of Amazon/Flipkart: ❌ deliberately excluded (ToS violation risk)

---

## 12. FUNCTIONAL REQUIREMENTS (FR list)

| ID | Requirement |
|---|---|
| FR1 | User input — accept product price, category, barcode |
| FR2 | Discount verification — ML model flags suspicious discounts |
| FR3 | SHAP explanation — feature-level explanation per verdict |
| FR4 | API integration — live query to Open Food Facts |
| FR5 | Unit price calculation — price per 100g/ml |
| FR6 | Buy timing prediction — category-level seasonal analysis |
| FR7 | Shrink timeline display — visual history of pack-size changes |
| FR8 | Results display — verdict + buy links (Amazon, Flipkart) |
| FR9 | Authentication (optional, future) |
| FR10 | Data export — download results as PDF (future) |

## 13. NON-FUNCTIONAL REQUIREMENTS (9 categories)

| Category | Target | Implementation |
|---|---|---|
| Performance | <3s page load, <2s prediction | Cached ML models, pre-processed data |
| Scalability | 100 concurrent users | Streamlit caching, stateless design |
| Usability | Non-technical users, no manual | Clean UI, tooltips, pre-filled examples |
| Security | HTTPS, no data storage | Streamlit Cloud managed HTTPS |
| Reliability | 99% uptime | Cloud hosting |
| Portability | Desktop, tablet, mobile | Responsive layout |
| Maintainability | Modular code | Separate files per module |
| Availability | 24/7 accessible | Cloud infrastructure |
| Compatibility | Chrome, Firefox, Safari, Edge | Cross-browser tested |

---

## 14. BUSINESS MODEL

| Revenue stream | Description | Est. revenue |
|---|---|---|
| Affiliate commissions (primary, near-term) | Amazon Associates / Flipkart Affiliate, 4–8% on verified-deal clicks | Year 1: ₹2–5 lakh (10K monthly users) |
| B2B Pricing API (secondary) | Small D2C sellers pay for category-level pricing insights, ₹5,000–10,000/mo | Year 2: ₹30 lakh (50 sellers) |
| Premium alerts (future) | Free watchlist; ₹99/month for instant WhatsApp/email alerts | ~₹12 lakh (1,000 premium users) |
| "Verified Honest Seller" badge (future) | ₹10,000/year listing fee | ~₹10 lakh (100 sellers) |

**Total projected revenue (Year 2):** ₹50–60 lakh (~$60–70K USD)

**Go-to-market stages (from PPT-CONTENT-MASTER):** Soft launch (Oct 2026, college project + social media) → Content marketing (viral shrinkflation posts) → Affiliate applications (Jan 2027) → Product Hunt launch (Feb 2027) → Scale (Mar 2027+).

---

## 15. LIMITATIONS (stated openly, not hidden — recurring across docs)

- Public datasets are price *snapshots*, not daily time-series per SKU → predictions are category-level, not per-product-per-exact-date.
- Live scraping of Amazon/Flipkart deliberately excluded (ToS risk).
- Affiliate commission requires platform approval (not guaranteed, takes time) → plain hyperlinks used initially.
- Open Food Facts is crowdsourced — field completeness varies; system should degrade gracefully on missing fields.
- Current SHAP waterfall numbers are illustrative/hand-set, not yet computed from a real trained model.

---

## 16. ROADMAP / TIMELINE

Per `DELIVERABLE-1-WORD-DOCUMENT.md` phase table:
| Phase | Duration | Deliverables |
|---|---|---|
| Phase 1: Planning | Aug 10–23 | Requirements, mockups, architecture |
| Phase 2: Data | Aug 24–Sep 6 | Download, clean, merge datasets |
| Phase 3: ML Models | Sep 7–20 | Discount detector, SHAP integration |
| Phase 4: App Dev | Sep 21–Oct 4 | Streamlit UI, API integration |
| Phase 5: Testing | Oct 5–11 | Feature testing, deployment |
| Phase 6: Demo | Oct 12–16 | Documentation, video, presentation |

**Key milestones referenced across docs:**
- Aug 21, 2026: Business Need doc + Wireframe URL + Presentation (as bundled by later planning docs)
- Oct 2, 2026: Lab work (code + NFRs) — per original rubric
- Oct 16, 2026: Working demo — per original rubric

---

## 17. DELIVERABLES REQUIRED (per FINAL-WORKFLOW-GUIDE.md / START-HERE-REVISED.txt — the "bundle due Aug 21" framing)

| # | Deliverable | Format | Marks |
|---|---|---|---|
| 1 | Business Need / Idea Document | MS Word (.docx + .pdf) | 10 |
| 2 | Wireframe / Prototype | Deployed URL (GitHub Pages / Netlify) | 10 |
| 3 | Project Presentation | PowerPoint (.pptx + .pdf) | 20 |

Requirement-to-location mapping used across the planning docs (note: slide numbers vary between the "9-slide" version and the "33-slide" version — see Section 18 below):
- Req #1 (Web App vs Website) ↔ Word Section 5
- Req #2 (Comparative Analysis) ↔ Word Section 6
- Req #3 (User Personas) ↔ Word Section 4
- Req #4 (Business Need) ↔ Word Section 3
- Req #5 (Business Flow) ↔ Word Section 7
- Bonus: Functional Requirements ↔ Word Section 8
- Bonus: Non-Functional Requirements ↔ Word Section 9

---

## 18. STATUS OF EACH DELIVERABLE (as of last upload batch)

### Deliverable 1 — Word Document (Business Need)
**Status: ✅ Content fully written**, in `DELIVERABLE-1-WORD-DOCUMENT.md` — 13 sections: Executive Summary, Problem Statement, Market Context, Target Users, Solution, Competitive Analysis, Technical Approach, Functional Requirements, Non-Functional Requirements, Business Model, Implementation Roadmap, Limitations & Risks, Conclusion. Just needs copy-paste into Word + formatting + export to PDF.

### Deliverable 2 — Wireframe / Prototype
**Status: Mockups built, not yet deployed.** Three standalone HTML mockups exist:
- `mockup-landing-page.html` — full landing page (hero + search, stats bar, 6 feature cards, CTA, footer). Navy/coral/green/amber palette, Space Grotesk + Inter fonts.
- `mockup-discount-checker.html` — core feature UI: left input form (category, listed price, discounted price, optional URL) + right results panel with verdict banner, product details, **interactive SHAP waterfall bar chart** (5 features, hover tooltips), interpretation callout box, action buttons (View on Amazon/Flipkart, Set Price Alert, Share Result).
- `mockup-mobile-responsive.html` — desktop/tablet/mobile device-frame comparison showing responsive behavior, plus a "Responsive Design Features" info panel (adaptive layouts, touch targets, progressive disclosure, consistent design, smart charts, accessibility).
- Still needed: deploy to GitHub Pages or Netlify Drop to get a live URL; or use screenshots as wireframe evidence if deployment is skipped.

There's also `Price_Truth_Project_Proposal.html` (uploaded, not yet read in full by this session) — described in `price-truth-project-context.md` §14 as the in-depth 14-section professor-facing proposal (already emailed to professor for approval), and a separate `price-truth-dashboard.html` pitch-style dashboard with a **live interactive "True Discount calculator" demo** — mentioned in context doc but not confirmed present in this upload batch.

### Deliverable 3 — PowerPoint Presentation
**Status: Two competing versions of content exist, not yet reconciled or built into an actual .pptx:**

**(a) The "9-slide" simplified version** (`DELIVERABLE-3-PPT-9-SLIDES.md`, `FINAL-WORKFLOW-GUIDE.md`) — described as a deliberate simplification "based on your feedback" from a much longer version. Slide list:
1. Title
2. The Problem (fake discounts + shrinkflation, split screen)
3. Market & Business Need (Req #4)
4. Who We're Solving For / personas (Req #3)
5. Our Solution (5-module hub diagram)
6. Competitive Advantage (Req #2)
7. Web Application + Architecture & Business Flow (Req #1 & #5 combined)
8. Requirements & Tech (FR + NFR + stack, 3 columns)
9. Roadmap & Closing

**(b) The "33-slide" full/detailed version** (`PPT-CONTENT-MASTER.md` + `PPT-REQUIREMENTS-CHECKLIST.md` + `COMPLETE-STATUS-REPORT.md` + `START-HERE.md` + `PROGRESS-SUMMARY.md` + `HOW-TO-BUILD-PPT.md` + `EXECUTIVE-SUMMARY.txt`) — full content written for all 33 slides across 8 sections (Introduction, Market Analysis, Solution, Technical, Requirements, Business & Challenges, UI Showcase, Closing). This is the more recent and more thorough set of planning docs (dated Aug 23, 2026 per `COMPLETE-STATUS-REPORT.md` / `EXECUTIVE-SUMMARY.txt`), and treats the 3 HTML mockups above as the visual assets to screenshot into slides 28–30 (UI Showcase section).

**⚠️ Open contradiction to flag to user:** The "9-slide" plan and the "33-slide" plan are two different scopes for the same Deliverable 3, generated at different times (9-slide docs are dated earlier/simpler; 33-slide docs are the latest, dated Aug 23, with mockups built specifically to support it). **It is not yet clear which version the user actually wants built.** The 33-slide version is more recently developed and has purpose-built visual assets (the 3 mockups), suggesting it's the current direction, but this should be confirmed rather than assumed.

**Also present:** `Price_Truth.png` — a polished infographic-style project workflow diagram (6-stage pipeline: Data Sources → Data Processing → ML Pipeline → SHAP → Website Modules → Consumer Benefits, with tech stack icons) plus a separate "Website Preview" dashboard mockup image showing a full working-product UI (Dashboard sidebar, True Discount Checker with genuineness score gauge, Buy Timing Signal, Shrinkflation Timeline, Unit Price Comparator, SHAP explainability bar chart, Product Details, Buy From Verified Platforms panel, Recent Activity feed). This appears to be a separately-generated, more advanced/final-look UI concept image — richer than the 3 individual HTML mockups — and could be another candidate visual asset for the PPT or wireframe deliverable.

---

## 19. FILES INVENTORY (as of this upload batch — 18 files)

| File | Type | Purpose |
|---|---|---|
| `PPT-CONTENT-MASTER.md` | Content | All 33-slide PPT content, full detail |
| `PPT-REQUIREMENTS-CHECKLIST.md` | Checklist | Slide-by-slide validation against rubric, 31-slide breakdown |
| `Price_Truth.png` | Image | Polished workflow infographic + website preview dashboard mockup |
| `Price_Truth_Project_Proposal.html` | HTML | Full 14-section professor-facing proposal (already sent for approval) — not yet read in detail this session |
| `price-truth-project-context.md` | Context doc | Full project handoff/context doc — most authoritative single source of project decisions |
| `_-START-HERE-REVISED.txt` | Guide | Quick-start guide for the "9-slide" / 3-deliverable bundle plan |
| `FINAL-WORKFLOW-GUIDE.md` | Guide | Step-by-step workflow for the 3-deliverable bundle (9-slide PPT version) |
| `DELIVERABLE-3-PPT-9-SLIDES.md` | Content | 9-slide PPT content + Claude/Kimi HTML-generation prompts |
| `DELIVERABLE-1-WORD-DOCUMENT.md` | Content | Full Word doc content, 13 sections, ready to paste |
| `EXECUTIVE-SUMMARY.txt` | Status doc | Summary of "Phase 1 & 2" work completed (33-slide plan era) |
| `COMPLETE-STATUS-REPORT.md` | Status doc | Detailed status report, 33-slide plan, design system specs |
| `START-HERE.md` | Guide | Quick-start guide for the 33-slide plan |
| `mockup-mobile-responsive.html` | HTML asset | Responsive device-comparison mockup |
| `PROGRESS-SUMMARY.md` | Status doc | Screenshot instructions + PPT build sequence for 33-slide plan |
| `mockup-discount-checker.html` | HTML asset | True Discount Checker UI with SHAP waterfall chart |
| `mockup-landing-page.html` | HTML asset | Landing page mockup |
| `HOW-TO-BUILD-PPT.md` | Guide | PowerPoint formatting/build guide for 33-slide plan |
| `TODAYS-ACTION-PLAN.md` | Planning doc | Original 10-hour execution plan (earliest-stage doc, contains open questions to user that may or may not have been answered since) |
| `prompt-for-ai.md` | Source doc | Verbatim professor rubric — the ground-truth requirements document |

---

## 20. OPEN QUESTIONS / THINGS TO CONFIRM WITH USER (not yet resolved as of this pass)

1. **Which PPT scope is final** — the 9-slide simplified deck or the 33-slide detailed deck? (See §18.) They cover the same requirements but at very different depth/length.
2. **Frontend framework discrepancy** — is the actual build going to be Streamlit (as most recent planning docs assume) or a custom HTML/CSS/JS site with Flask/FastAPI backend (as the original `price-truth-project-context.md` describes)?
3. **Due-date framing** — original rubric splits Business Need (Jul 24), Wireframe (Aug 7), and Presentation (Aug 21) across three separate dates; later docs treat all three as due together on Aug 21. Confirm which is actually still accurate/relevant given today's date context.
4. **Deployment status** — have the mockups been deployed anywhere (GitHub Pages/Netlify) yet, or is that still pending?
5. **`TODAYS-ACTION-PLAN.md` open decisions** (UI design method, PPT style, data handling, team division) — unclear if these were ever answered in a past conversation not captured in these files.
6. Whether `Price_Truth.png`'s more advanced "Website Preview" dashboard concept should replace/supplement the 3 simpler HTML mockups as the primary wireframe visual.

---

## APPEND LOG
*(New sections get added below this line as more files/context are shared. Do not edit sections above without being told to.)*

---

### APPEND 1 — Second upload batch (19 files): the "Word Doc Completeness Crisis" saga, Enhanced 14-section content, and full image-prompt breakdown

**Context of this batch:** These files are almost all dated **August 23, 2026**, i.e. *after* the Aug 21 deadline referenced in Batch 1's planning docs. They document a self-contained back-and-forth the user had (in a separate/previous conversation) about whether `PriceTruth-Business-Need-Document.docx` was missing content compared to the original HTML proposal and the `Price_Truth.png` infographic. **This sub-saga is now resolved** (see verdict below) — it's preserved here mainly for continuity/history, not because it's still an open problem.

#### A. The reported issue
User noticed the Word doc "only has 2 problem statements" and worried content was missing vs. `Price_Truth_Project_Proposal.html` (the original professor-facing proposal) and vs. `Price_Truth.png` (the infographic).

#### B. The investigation trail (chronological, all same-day Aug 23)
1. `🚨-URGENT-ACTION-PLAN.md` (4:45 PM) — diagnosed the Word doc as genuinely incomplete (36 KB, only Problem Statement section) vs. an expected 100–300 KB / 25–30 page document. Proposed two fixes: (1) paste a mega-prompt into a **fresh Claude.ai conversation** asking it to generate step-by-step manual Word-formatting instructions (workflow docs like `🔥-COMPLETE-CLAUDE-PROMPT.md`, `📋-COPY-THIS-TO-CLAUDE.md`, `_-COMPLETE-CLAUDE-PROMPT.txt` were built for this — note: this is a *different* usage pattern than the current session, where Claude edits the .docx directly), or (2) manual copy-paste + basic Word styling (`✅-SIMPLE-SOLUTION.md`).
2. `📢-READ-THIS-FIRST.md`, `🎯-YOUR-NEXT-STEPS.md`, `📊-QUICK-VISUAL-SUMMARY.md` (not shown in full this batch, referenced), `CONTENT-COMPARISON-REPORT.md`, `✅-DELIVERABLE-1-STATUS.md`, `✅-FINAL-ANSWER.md`, `VERIFICATION-REPORT.md` — a series of self-generated verification/reassurance documents concluding that **no content was actually missing**: the true content source of record, `DELIVERABLE-1-ENHANCED.md` (1,120 lines, ~8,500 words, **14 sections**), has 143% more words than the original HTML proposal (~3,500 words, 14 sections) and covers 100% of what's depicted in `Price_Truth.png`. The perceived "shortness" was attributed to the Word doc simply not yet having the Enhanced MD's content pasted in / formatted, not to any content being lost.
3. `🖼️-IMAGE-CONTENT-VERIFICATION.md` — line-by-line mapping confirming every element of `Price_Truth.png` (both the 6-stage workflow diagram and the dashboard "Website Preview" mockup) is already described somewhere in the Enhanced MD content. Notes two trivial discrepancies: (a) the image includes "BeautifulSoup" in the tech stack, which the written docs correctly omit/exclude since live scraping was deliberately ruled out; (b) the image's banner has a typo, "FFrom Data to Consumer Empowerment" (double F) — cosmetic only.
4. `🎨-DELIVERABLE-1-VISUAL-APPROACH.txt` — the design system used for formatting the Word doc: cover page, colored headings (Navy #1E3A5F), light-cream callout boxes (#FFF9E6), styled tables, SmartArt diagrams, persona cards, stat boxes.

#### C. Verified current state of the actual .docx files (checked directly in this session, not just taken from the meta-docs)
Three .docx files were uploaded this batch: `PriceTruth-Business-Need-Document.docx`, `PriceTruth-Business-Need-Document__1_.docx` (a duplicate/near-duplicate), and `Price_Truth_Business_Need_Document.docx`. **Direct inspection confirms all three now contain the full 13-section structure** (Executive Summary → Conclusion, matching `DELIVERABLE-1-WORD-DOCUMENT.md`'s outline, not yet the newer 14-section Enhanced outline which adds a standalone "13. Deliverables" section before the Conclusion):

| File | Paragraphs | Tables | Approx. word count (text + tables) |
|---|---|---|---|
| `PriceTruth-Business-Need-Document.docx` | 159 | 17 | ~1,356 |
| `PriceTruth-Business-Need-Document__1_.docx` | 161 | 17 | ~1,359 |
| `Price_Truth_Business_Need_Document.docx` | 151 | **25** | ~1,534 |

**Verdict: the "only 2 problem statements" issue is resolved.** All three current files have all 13 sections with headings, sub-headings, and multiple tables (market stats, personas, competitive analysis, FR/NFR, roadmap, etc.). `Price_Truth_Business_Need_Document.docx` is the most developed of the three (most tables, includes extra content like a "Revenue Funnel" and "Timeline — Gantt-Style View" not present in the other two) and appears to be the latest/best candidate for final submission. Note: none of the three yet include the Enhanced MD's newest additions verbatim as a distinct "13. Deliverables" section — they go straight from Limitations & Risks (12) to Conclusion (13), i.e. they reflect the 13-section `DELIVERABLE-1-WORD-DOCUMENT.md` content, not the slightly-expanded 14-section `DELIVERABLE-1-ENHANCED.md` content. **This is a minor, low-stakes gap, not the "missing content" crisis originally feared.**

#### D. `DELIVERABLE-1-ENHANCED.md` — what's actually new vs. the Batch-1 `DELIVERABLE-1-WORD-DOCUMENT.md`
Confirmed by direct heading comparison: Enhanced version = same 13 sections **plus**:
- More granular subheadings throughout (e.g., "Market Size & Growth", "Consumer Behavior Shifts", "Regulatory Landscape", "Why NOW? (Timing Factors)" as distinct subsections under Market Context)
- Expanded Business Model with 4 named revenue streams (Affiliate Commissions, B2B Pricing API, Premium Alerts, "Verified Honest Seller" Badge) + a new **Cost Structure** and **Unit Economics** subsection
- A new standalone **Section 13: Deliverables** (splitting "Academic" vs "Technical" deliverable lists) that pushes Conclusion to Section 14
- More detailed **Risk Mitigation Strategies** subsection under Roadmap

#### E. Full verbatim breakdown of `Price_Truth.png` (from `price-truth-image-prompt.md`)
This file is the authoritative, exact source-of-truth description of the infographic image (since the image itself can't be "read" as text by whoever wrote this prompt file — though note, in *this* Claude session the image was actually visible directly in Batch 1's message). Key details now on record verbatim:

- **Banner typo confirmed as intentional-to-flag:** "FFrom Data to Consumer Empowerment" (double F) — should be corrected if a cleaned-up version is ever produced.
- **Part 1 (workflow diagram), 6 stages**, each with a distinct header color: Data Sources (blue) → Data Processing (green) → Machine Learning Pipeline (orange) → Explainable AI/SHAP (purple) → Website Modules (pink/magenta) → Consumer Benefits (teal). A "Technologies Used" dark-navy bar sits below, dot-connected to stages 2–5, listing: Python, Pandas, Scikit-learn, XGBoost, SHAP, Streamlit, Plotly, BeautifulSoup, Requests API, Open Food Facts API. (BeautifulSoup here is aspirational/inaccurate — see discrepancy note above.)
- **Part 2 (website preview mockup)** — full dashboard layout with: top nav (logo + tagline "Truth in Every Price", search bar, dark-mode toggle, Login/Signup button); left sidebar with **10 menu items** (Dashboard, Discount Checker, Buy Timing Signal, Shrink Timeline, Live Product Lookup, Unit Price Comparator, History, Saved Products, Settings, About Us — note this is a richer nav than the 5-module framing used everywhere else); 4 top widget panels (True Discount Checker with 96% genuineness gauge + SHAP top-reasons bars; Buy Timing Signal with "10 DAYS TO WAIT" + 78% confidence + price prediction chart; Shrinkflation Timeline with 200g→180g→150g example + 25% total shrinkage; Unit Price Comparator with 3 pack-size options, best value highlighted); a second row with Product Details (Nutella Hazelnut Spread 750g example) + a wide SHAP Explainability bar chart; a third row with "Buy From Verified Platforms" (Amazon/Flipkart/Myntra/Meesho) and "Recent Activity" (3 example checked products with genuineness scores); dark-navy footer with standard links + "© 2024 Price Truth" (note: copyright year says 2024, inconsistent with project's actual 2026 timeline — cosmetic, from whenever this mockup image was first generated).
- **Explicit instruction given to whichever assistant receives this file:** treat this description as the UI/UX and workflow reference for wireframe, prototype, and frontend build guidance going forward.

#### F. Updated file inventory — 19 new files this batch
| File | Type | Purpose |
|---|---|---|
| `_-COMPLETE-CLAUDE-PROMPT.txt` | Prompt | Full 53 KB mega-prompt (all 14 sections pasted in) meant to be pasted into a fresh Claude.ai chat to get manual MS Word formatting instructions |
| `PriceTruth-Business-Need-Document__1_.docx` | Deliverable draft | Near-duplicate of the main docx, 17 tables, 13 sections — confirmed complete |
| `Price_Truth_Business_Need_Document.docx` | Deliverable draft | Most-developed of the 3 docx candidates, 25 tables, 13 sections — likely best submission candidate |
| `PriceTruth-Business-Need-Document.docx` | Deliverable draft | Original docx under investigation, 17 tables, 13 sections — confirmed complete |
| `_-QUICK-VISUAL-SUMMARY.md` | Status doc | Visual HTML-vs-Enhanced-MD comparison (referenced but not read in full this pass) |
| `DELIVERABLE-1-ENHANCED.md` | Content | The newest/most complete Word-doc content source, 14 sections, ~8,500 words — supersedes `DELIVERABLE-1-WORD-DOCUMENT.md` from Batch 1 |
| `PROMPT-FOR-CLAUDE-WORD-DOC.md` | Prompt | The (shorter, 418-line / ~2,279-word) prompt that was flagged as the likely root cause of the incomplete docx — diagnosed as itself incomplete/abbreviated versus the full Enhanced MD |
| `_-COPY-THIS-TO-CLAUDE.md` | Guide | Instructions for using `_-COMPLETE-CLAUDE-PROMPT.txt` with a fresh Claude.ai session |
| `_-COMPLETE-CLAUDE-PROMPT.md` | Prompt | Shorter/markdown version of the mega-prompt, referencing the full content by file path rather than inlining it |
| `_-SIMPLE-SOLUTION.md` | Guide | Backup manual copy-paste + basic-formatting approach (20 min) as an alternative to the Claude-prompt approach |
| `_-URGENT-ACTION-PLAN.md` | Status/diagnosis doc | The original diagnosis of the incomplete Word doc, with two remediation options |
| `_-FINAL-ANSWER.md` | Status doc | Consolidated reassurance doc: confirms no content missing vs HTML or image |
| `_-READ-THIS-FIRST.md` | Guide | Entry-point summary of the whole verification saga |
| `__-IMAGE-CONTENT-VERIFICATION.md` | Verification doc | Section-by-section mapping of `Price_Truth.png` content to Enhanced MD sections |
| `price-truth-image-prompt.md` | Source doc | Verbatim, exact description of every element in `Price_Truth.png` — authoritative reference for wireframe/UI work |
| `_-YOUR-NEXT-STEPS.md` | Guide | Step-by-step action plan for finishing Deliverable 1 |
| `_-DELIVERABLE-1-STATUS.md` | Status doc | Detailed section-by-section completeness check against professor's 5 requirements |
| `CONTENT-COMPARISON-REPORT.md` | Comparison doc | HTML vs Enhanced MD, section-by-section |
| `_-DELIVERABLE-1-VISUAL-APPROACH.txt` | Design doc | Visual/formatting design system for the Word doc (cover page, colors, callout boxes, SmartArt) |
| `VERIFICATION-REPORT.md` | Verification doc | Full pre-submission QA pass: content completeness, professor-requirement coverage, technical accuracy, business-model feasibility, anticipated professor Q&A, risk assessment — concludes 95% confidence, estimated 9–10/10 marks |

#### G. New/updated open questions
1. **Which docx is the final one to submit?** Three near-identical candidates exist (`PriceTruth-Business-Need-Document.docx`, `...__1_.docx`, `Price_Truth_Business_Need_Document.docx`). The third has the most tables/content. Confirm with user which is canonical, or whether they should be merged/rebuilt from `DELIVERABLE-1-ENHANCED.md` (the true current source of truth for content) to fully close the loop.
2. **Section-count mismatch persists at the docx level:** actual docx files still reflect the 13-section structure, not the 14-section Enhanced structure (missing the standalone "Deliverables" section). Low priority, but worth closing if the user wants the docx to fully match Enhanced MD.
3. **Timeline confusion continues:** this whole batch is dated Aug 23, 2026 — two days *after* the Aug 21 deadline referenced throughout Batch 1's planning docs. It's not clear whether the deadline actually shifted, already passed (and this is now catch-up/rework), or whether "August 21" in Batch 1 was itself aspirational/mistaken. **This should be directly confirmed with the user**, since it affects how urgently Deliverables 2 and 3 (still not finalized — see Batch 1 §18) need to be completed.
4. Given this saga, it's worth explicitly checking with the user whether Deliverable 1 is now considered DONE (pick the best docx and move on) or whether they still want it rebuilt from the newer 14-section Enhanced content for full consistency.

---

### APPEND 2 — Third upload batch (20 files): the "page count" saga resolves, and a finished PDF appears

**Context of this batch:** Direct continuation of the Aug 23 saga from Append 1, same day. The concern shifted from "is content missing?" (resolved in Append 1) to **"the document is too long / too short — what's the right length?"** This batch documents that back-and-forth and — importantly — **includes what looks like the actual final, submission-ready PDF.**

#### A. The page-count saga (chronological)
1. `✅-DOCUMENT-CREATED.md` + `create_complete_doc.py` — a Python script (using `python-docx`) was written to programmatically rebuild the Word doc directly from `DELIVERABLE-1-ENHANCED.md`, producing `COMPLETE-Price-Truth-Document.docx` (claimed 14 sections, ~59 KB). This was framed as "the fix" for the earlier incomplete-docx problem, since it removes manual copy-paste error.
2. User reaction (implied by later files): the resulting document was **too long** ("nobody will read 64 pages").
3. `✅-CHECK-WORD-DOCUMENT.md` — separately diagnosed `Price Truth DOC.docx` (30 KB) as **too short/incomplete** (a different, older/parallel file, not the newly-generated COMPLETE version) and pushed the "use `_-COMPLETE-CLAUDE-PROMPT.txt`" fresh-Claude-chat approach again.
4. `📌-USE-THIS-CONDENSED-PROMPT.md` + `_-CONDENSED-VERSION-PROMPT.txt` — pivoted to explicitly asking for a **condensed 10–15 page version** that keeps all 14 section headings and all 5 professor requirements but shortens personas/examples/elaborations. This condensed prompt is fully self-contained (includes all 14 sections' condensed content inline) and ends with a request for step-by-step manual MS Word formatting instructions — same "fresh Claude.ai chat" workflow pattern as Batch 2.
5. `✅-FINAL-CONDENSED-READY.md` — reports `PriceTruth-CONDENSED-FINAL.docx` created (39 KB claimed, actually ~61 KB / ~1,011 words of extractable text + 5 tables on direct inspection) as the "perfect 10–15 page" version, all 14 sections, 6 key tables.
6. `✅-9-PAGE-DOCUMENT-READY.md` — reports a further iteration, `PriceTruth-10-Pages-FINAL.docx` (claimed 9 pages / 1,853 words), this time with **13 sections** (not 14 — no standalone "Deliverables" section break called out) and explicitly **no tables** (confirmed on inspection: 0 tables, all content in prose/paragraph form) — a deliberate move away from tables for a more narrative, shorter feel.
7. `🔥-FINAL-SOLUTION-THAT-WORKS.md` — a self-critical "apology" document acknowledging that **all the automated condensing attempts up to this point were unreliable** ("too short, not actually condensed properly, missing most of the content"). Proposes three fallback options: (1) manual 20-minute copy-paste from the Enhanced MD, (2) just submit the full 25–30 page `COMPLETE-Price-Truth-Document.docx` as-is and stop trying to shorten it, or (3) manually condense by hand, section by section. Recommends **Option 2 (submit the full version)** as the most reliable, arguing academic documents are supposed to be comprehensive and professors want depth, not brevity.

#### B. Direct inspection of the actual files (ground truth, checked this session)

| File | Size (KB) | Paragraphs | Tables | Extractable words (para+table) | Sections (headings) |
|---|---|---|---|---|---|
| `PriceTruth_Condensed.docx` | 19 | 125 | 35 | ~1,241 | 14-section structure, heavily table-based (35 tables!) |
| `PriceTruth-PROPERLY-CONDENSED.docx` | 25 | 322 | 0 | ~1,692 | No heading styles applied at all — plain paragraphs only |
| `Price_Truth_DOC.docx` | 31 | 375 | 20 | ~4,350 | 133 headings — very granular/deep subheading structure, 14 sections |
| `PriceTruth-10-Pages-FINAL.docx` | 61 | 61 | 0 | ~1,855 | 13 sections, no tables (converted to prose) |
| `PriceTruth-CONDENSED-FINAL.docx` | 61 | 136 | 5 | ~1,011 | 14 sections, 5 tables |
| `COMPLETE-Price-Truth-Document.docx` | 61 | 668 | 78 | ~11,524 | 61 headings, 14 sections — this is the "full" version, by far the most content-dense |

**Key finding: file size alone was a misleading signal throughout this whole saga.** Several files are ~60 KB regardless of actual content length, because .docx size is dominated by embedded XML/styles/theme overhead, not just text volume. The meta-docs' repeated size-based diagnoses ("30 KB = incomplete," "59 KB = complete") were an unreliable heuristic — actual extractable word count and heading/table structure (checked directly above) is the only trustworthy signal.

#### C. **The actual resolution: two identical, finished PDFs were uploaded this batch**
`Deliverable_1_-_PriceTrurth_Document.pdf` and `PriceTruth_Business_Need_-_Group_11.pdf` are **byte-identical in content** (same 863 KB size, same text) — the second filename ("Group 11") strongly suggests this is the **actual final submission-formatted file**. Both are:
- **7 pages**, dated **23rd August 2026**
- **13 sections**, Executive Summary → Conclusion (matches the `DELIVERABLE-1-WORD-DOCUMENT.md` / condensed-prompt outline, i.e. no standalone "Deliverables" section split from Conclusion — it's folded in as section 12)
- Written in clean, professional prose paragraphs (not dense bullet lists), with tables used specifically for the persona grid, competitive analysis, data sources, and FR/NFR — i.e., **exactly the middle-ground format the whole saga was searching for**: not the sprawling 25–30 page "full" version, not an overly-condensed bullet skeleton, but readable narrative prose at a normal business-document length.
- Confirmed to include content matching the `_-CONDENSED-VERSION-PROMPT.txt` condensed section content nearly verbatim (e.g. same persona wording, same competitive table, same revenue streams), suggesting this PDF is the **direct output** of that condensing effort, successfully exported to PDF this time.
- All 5 professor requirements are present and easy to locate: Req #1 in Section 5 ("Web Application vs. Website"), Req #2 in Section 6 ("Competitive Analysis"), Req #3 in Section 4 ("Target Users"), Req #4 in Section 3 ("Market Context & Business Need"), Req #5 in Section 5 ("Solution Architecture — Six Stages").

**Conclusion: Deliverable 1 appears to be DONE.** This 7-page PDF (in its two identically-named copies) is the natural end-point of the entire multi-day saga documented across Append 1 and Append 2, and reads as complete, well-scoped, and appropriately concise. Barring the user saying otherwise, **this is the file to treat as final for Deliverable 1** going forward, superseding every intermediate .docx candidate discussed above.

#### D. Two Python build scripts also uploaded (for completeness of file record)
- `create_complete_doc.py` — builds the full/uncondensed Word doc from `DELIVERABLE-1-ENHANCED.md` via `python-docx`; parses markdown headings (`##`/`###`/`####`), bold lines, bullet lists, and pipe-tables into corresponding Word elements; applies Navy (#1E3A5F) heading color.
- `create_10_page_doc.py` and `create_condensed_doc.py` — referenced by filename in this batch's uploads but not shown inline; presumably the corresponding generator scripts for the 9/10-page and condensed variants respectively (same pattern as above, different source content / more aggressive trimming).

#### E. `DELIVERABLE-CONDENSED-CONTENT.md` — referenced but not shown inline this batch; presumably the underlying condensed markdown content source (parallel to `DELIVERABLE-1-ENHANCED.md` for the full version). Not yet read in detail.

#### F. Updated file inventory — 20 new files this batch
| File | Type | Purpose |
|---|---|---|
| `Deliverable_1_-_PriceTrurth_Document.pdf` | **Final deliverable (likely)** | 7-page, 13-section, professionally formatted final PDF — see §C above |
| `PriceTruth_Business_Need_-_Group_11.pdf` | **Final deliverable (likely, duplicate)** | Identical content to above, "Group 11" naming suggests official submission copy |
| `PriceTruth_Condensed.docx` | Draft candidate (superseded) | Early condensed attempt, 35 tables, ~1,241 words — diagnosed as "incomplete" (18 KB) in the saga |
| `PriceTruth-10-Pages-FINAL.docx` | Draft candidate (superseded) | 13-section, 0-table, prose-only 9-page attempt, ~1,855 words |
| `create_10_page_doc.py` | Build script | Generator for the 10-page variant (not shown inline) |
| `PriceTruth-PROPERLY-CONDENSED.docx` | Draft candidate (superseded) | No heading styles applied — a broken/incomplete build, 0 tables |
| `DELIVERABLE-CONDENSED-CONTENT.md` | Content source (not read in detail) | Presumably the condensed-version markdown source content |
| `PriceTruth-CONDENSED-FINAL.docx` | Draft candidate (superseded) | 14-section, 5-table condensed version, ~1,011 words |
| `create_condensed_doc.py` | Build script | Generator for the condensed variant (not shown inline) |
| `COMPLETE-Price-Truth-Document.docx` | Draft candidate (reference/backup) | The "full" 14-section, 78-table, ~11,524-word version built via `create_complete_doc.py` — richest content, but the one judged "too long" |
| `Price_Truth_DOC.docx` | Draft candidate (superseded) | Deep/granular 133-heading structure, 20 tables, ~4,350 words — an intermediate-length attempt |
| `FINAL-PROMPT-FOR-CLAUDE.md` | Prompt | An earlier/alternate full-content prompt (10-page target) for a fresh Claude.ai chat, very similar in structure to the condensed prompt but written before it |
| `_-9-PAGE-DOCUMENT-READY.md` | Status doc | Announces `PriceTruth-10-Pages-FINAL.docx` as done; includes file-comparison table |
| `_-FINAL-SOLUTION-THAT-WORKS.md` | Status/apology doc | Admits automated condensing was unreliable; recommends submitting the full version instead |
| `_-FINAL-CONDENSED-READY.md` | Status doc | Announces `PriceTruth-CONDENSED-FINAL.docx` as done; includes file-comparison table and "files to delete" list |
| `_-USE-THIS-CONDENSED-PROMPT.md` | Guide | Instructions for using `_-CONDENSED-VERSION-PROMPT.txt` with a fresh Claude.ai chat |
| `_-CONDENSED-VERSION-PROMPT.txt` | Prompt | Full self-contained condensed-content prompt (13 sections) — the direct source of what appears in the final PDF (§C) |
| `_-DOCUMENT-CREATED.md` | Status doc | Announces `COMPLETE-Price-Truth-Document.docx` as done (the full/uncondensed version) |
| `create_complete_doc.py` | Build script | Full Python source for the markdown→docx converter used to build the full version |
| `_-CHECK-WORD-DOCUMENT.md` | Diagnostic guide | Checklist-based method for manually verifying whether a given docx is complete (page count, word count, scroll-to-end test) |

#### G. Updated status of open questions from Append 1
1. **Which docx is final?** — **Superseded by a better question and a likely answer.** The real final artifact is not a .docx at all, but the **PDF** (`Deliverable_1_-_PriceTrurth_Document.pdf` / `PriceTruth_Business_Need_-_Group_11.pdf`), which looks genuinely finished and appropriately scoped. Recommend confirming with the user that this PDF is indeed what got/will get submitted, and archiving the many .docx intermediates as historical drafts only.
2. **Section-count mismatch** — resolved in the final PDF's favor: it consistently uses the 13-section structure throughout (no orphaned "14th section" ambiguity).
3. **Timeline confusion** — **partially clarified**: the final PDF's cover page is explicitly dated **"23rd August 2026,"** i.e., the document itself confirms work was still being finalized two days after the "Aug 21, 10 PM" deadline mentioned everywhere else. This means either (a) the deadline genuinely slipped/was extended, or (b) this is post-deadline catch-up. **Still recommend directly asking the user what actually happened with the Aug 21 deadline**, since it materially affects how urgent Deliverables 2 and 3 are.
4. Given the finished PDF, the original Append-1 question ("is Deliverable 1 done, or does it need rebuilding from Enhanced MD?") is likely **answered: it's done, and it deliberately did NOT use the full 14-section Enhanced MD content verbatim — it used a condensed 13-section version instead**, which the saga concluded was the right call for readability.

#### H. New open question from this batch
5. **Confirm submission status:** Was `PriceTruth_Business_Need_-_Group_11.pdf` actually submitted to the professor already, or is it still pending? If already submitted, Deliverable 1 can be marked fully closed in this tracking file. If not yet submitted, it's still the recommended final candidate — no further rework needed unless the user has new concerns.
6. Should the many superseded `.docx` drafts and the `create_*.py` scripts be treated as safe to discard going forward, given the PDF supersedes them? (Recommend keeping `DELIVERABLE-1-ENHANCED.md` and `COMPLETE-Price-Truth-Document.docx` only as content-reference backups, per the "files to keep vs delete" guidance already given by the user's own prior planning docs.)

---

### APPEND 3 — Fourth upload batch (20 files): Deliverable 2 confirmed LIVE, Deliverable 3 lands on a new 6-slide format, and a master submission plan appears

**Context of this batch:** This is the most conclusive batch so far — it contains **actual built artifacts** for Deliverables 2 and 3 (not just plans/prompts), plus a master "how to submit everything" document. Several files are repeats/near-repeats of earlier batches (`Deliverable_1_-_PriceTrurth_Document.pdf` reappears unchanged — the final Deliverable 1 PDF from Append 2, §C, is reconfirmed).

#### A. Deliverable 2 (Wireframe/Prototype) — CONFIRMED LIVE AND BUILT
- **Live URL confirmed: https://price-truth.netlify.app/** — referenced consistently across `README.md`, `ALL-DELIVERABLES-SUMMARY.md`, and `⚡-START-HERE-DELIVERABLE-3.md` as the actual deployed prototype.
- **Real source files present and inspected:**
  - `index.html` (42 KB) — the landing page, built from `DELIVERABLE-2-WIREFRAME-PROMPT.md`'s prompt (a detailed Claude-prompt requesting a "fully interactive, visually stunning wireframe/prototype," explicitly scoped as Deliverable 2, 10 marks, with a specific navy/coral color palette spec at the top of the prompt).
  - `dashboard.html` (34 KB) — a richer interactive dashboard added afterward via `CLAUDE-DASHBOARD-PROMPT.md`, explicitly modeled on the `Price_Truth.png` reference image's "Website Preview" mockup (same 4-widget-panel layout: True Discount Checker with genuineness gauge, Buy Timing Signal, Shrinkflation Timeline, Unit Price Comparator, plus Product Details/SHAP/Platform-links/Recent-Activity sections below) — but explicitly instructed to **only include what's realistically demoable in a static prototype** (no real ML/API/backend/auth — simulated data only).
  - `README.md` — the actual GitHub repo readme, confirms this repo IS Deliverable 2, lists the team, links the live URL, and describes `index.html` + `dashboard.html` as the two pages (landing → "Try Dashboard" click-through).
  - `_gitignore` — confirms the deployed repo is deliberately kept clean: only `.html` files and `README.md` are tracked; every planning artifact (`.docx`, `.pdf`, `.png`, `.jpeg`, `.md` except README, `.py`, `.txt`) is excluded from the actual GitHub repo used for the Netlify deploy. This explains why the live site is minimal/clean despite the huge amount of planning material generated around it.
- **Notable design pivot:** `dashboard.html` uses a **different, softer color palette** than everything else in the project (soft blue `#6B8DBF`, peach `#FFB5A7`, mint `#B4E7CE`, butter `#FFE8A3`, lavender `#E0D4F7`, cream `#FFFBF5` background) — explicitly "pastel," a deliberate departure from the navy/coral/green/amber scheme used in the Word doc, PPT prompts, and original mockups (`mockup-*.html` from Batch 1). **This means the live prototype's visual identity no longer matches the Word doc / PPT visual identity** — worth flagging to the user as a minor brand-consistency gap, though not a functional problem.
- **Conclusion: Deliverable 2 is DONE and live.** No further action needed unless the user wants to reconcile the color-scheme mismatch or add more interactivity.

#### B. Deliverable 3 (Presentation) — landed on a NEW 6-slide dense format, actual .pptx exists
This resolves the open question carried since Batch 1 (§18: "which PPT scope is final — 9-slide or 33-slide?"). **Neither.** The project moved through several more iterations documented in this batch, and arrived at a **third, denser 6-slide format**:

1. `CLAUDE-BEAUTIFUL-DENSE-PROMPT.md` — first dense-format attempt: explicitly reacts against the earlier 9-slide version being "too sparse," instructing "DENSE, not sparse," "NO EMPTY SPACES," dashboard/infographic style, 6 slides combining multiple topics per slide (e.g., Slide 2 combines Market Stats + User Personas + Solution Modules in one dashboard-style grid).
2. `CLAUDE-MAXIMUM-CONTENT-PROMPT.md` — a further-refined version of the same 6-slide dense brief ("FILL EVERY INCH," KPI cards/tables/charts/timelines combined per slide).
3. `⚡-QUICKEST-METHOD.md` + `CLAUDE-TO-CANVA-WORKFLOW.md` — describe a **Claude → screenshot → Canva → export .pptx** workflow as the fastest path to get from generated HTML slides to an actual PowerPoint file, with online-converter and direct-PDF-export fallback options.
4. **Confirmed actual output: `PriceTruth_Presentation.pptx` exists** (324 KB, verified by direct inspection) — **6 slides**, matching the dense-format brief:
   - Slide 1: "PRICE TRUTH" title + problem showcase combined
   - Slide 2: "MARKET, USERS & SOLUTION" (combines Req #4 + Req #3 + solution overview)
   - Slide 3: "COMPETITION, ARCHITECTURE & REQUIREMENTS" (combines Req #2 + Req #5 + FR/NFR)
   - Slide 4: "WEB APPLICATION IN ACTION" (Req #1 + UI demo mockup)
   - Slide 5: "BUSINESS MODEL, TIMELINE & RISK"
   - Slide 6: "TEAM, IMPACT & WHAT'S NEXT"
   
   This is a genuinely different structure from both Batch 1 candidates (the 9-slide one-topic-per-slide version and the 33-slide expanded version) — it deliberately **fuses multiple professor requirements onto single dense slides** rather than giving each its own slide, matching the "dashboard-style, no empty space" design brief.
5. Separately, `⚡-START-HERE-DELIVERABLE-3.md` and `DELIVERABLE-3-QUICK-START.md` / `DELIVERABLE-3-CHECKLIST.md` describe a **parallel, more traditional manual path**: build the original 9-slide version directly in PowerPoint (not via HTML/Canva), inserting screenshots of the mockups and the live Netlify prototype. These docs still reference the Batch-1 9-slide content (`DELIVERABLE-3-PPT-9-SLIDES.md`) as the source, and are seemingly earlier/alternate advice that predates the pivot to the dense 6-slide format.

**Conclusion: Deliverable 3 has a real, finished `.pptx` file (6 slides, dense format), which appears to be the version actually completed.** The manual 9-slide guides in this same batch look like an alternate path that was likely superseded once the dense 6-slide HTML→pptx approach succeeded — but this should be **confirmed with the user**, since both a working 6-slide .pptx AND detailed 9-slide manual instructions exist side-by-side in the same batch with no explicit note saying which one was actually submitted.

#### C. `ALL-DELIVERABLES-SUMMARY.md` — the master submission plan (most authoritative organizational doc so far)
This is a comprehensive, single-source submission checklist covering all three deliverables at once. Key new facts:
- **Submission destination:** a specific **Google Drive folder** (link included in the doc) — the professor's collection point, not email or an LMS.
- **Required folder naming:** a "GROUP 11" folder, with suggested subfolder structure (`1-Business-Need/`, `2-Prototype/`, `3-Presentation/`) and canonical filenames: `PriceTruth-Business-Need-Group11.docx`, `PriceTruth-Presentation-Group11.pptx` (+ PDF backups). This confirms the team's group number is **Group 11** (also seen in the `PriceTruth_Business_Need_-_Group_11.pdf` filename from Append 2).
- **Deliverable 2 submission format clarified:** since it's a live URL rather than a file, the plan is to create a small companion doc/text file stating the URL (`https://price-truth.netlify.app/`), confirming no login is required, and listing the 5 features demonstrated — this companion doc doesn't appear to have been separately created yet in the uploads so far.
- Includes a **draft submission email** to the professor summarizing all three deliverables, team member names, and course/institution details — ready to send once files are finalized.
- Reiterates the "Aug 21st, 2026 by 10 PM" deadline (again inconsistent with the Aug 23-dated PDF from Append 2/3 — **this deadline-date discrepancy is now confirmed to persist across multiple batches and should be directly asked about**, since virtually every planning doc still cites Aug 21 even while work demonstrably continued past that date).
- Gives an expected-marks estimate: Business Need 8–9/10, Prototype 9–10/10, Presentation 18–20/20, total 35–39/40.

#### D. `check_pdf.py` — a small PyPDF2 script the user/assistant used to page-by-page verify the contents of `PriceTruth Business Need - Group 11.pdf`, confirming that PDF was actively being QA-checked (consistent with Append 2's conclusion that this PDF is the final Deliverable 1 artifact).

#### E. Other files in this batch
- `temp-full-html.txt` (585 lines) — appears to be a scratch/temp file, likely a saved copy of generated HTML output from one of the Claude-prompt workflows (not fully read in detail this pass; low priority since the final `index.html`/`dashboard.html`/`.pptx` artifacts already supersede intermediate scratch files).
- `PriceTruth-Business-Need-FINAL.docx` — another Deliverable 1 draft candidate (105 paragraphs, 10 tables, ~1,655 words, no heading styles applied), corresponding to the `FINAL-PROMPT-FOR-CLAUDE.md` 10-page prompt from Append 2. Superseded by the finished PDF per Append 2 §C.
- `Deliverable_1_-_PriceTrurth_Document.pdf` — identical re-upload of the Append-2 final PDF; no new information, just reconfirmation.

#### F. Updated file inventory — 20 files this batch
| File | Type | Purpose |
|---|---|---|
| `temp-full-html.txt` | Scratch file | Likely saved HTML output from a Claude prompt workflow; not fully reviewed |
| `PriceTruth_Presentation.pptx` | **Final Deliverable 3 (likely)** | Real 6-slide dense-format PowerPoint, matches `CLAUDE-BEAUTIFUL-DENSE-PROMPT.md`/`CLAUDE-MAXIMUM-CONTENT-PROMPT.md` brief |
| `CLAUDE-MAXIMUM-CONTENT-PROMPT.md` | Prompt | Refined dense 6-slide PPT prompt ("fill every inch") |
| `_gitignore` | Config | Confirms the live Netlify repo tracks only HTML + README, excludes all planning docs |
| `index.html` | **Final Deliverable 2 asset** | Landing page for the live prototype |
| `dashboard.html` | **Final Deliverable 2 asset** | Interactive dashboard page, pastel color scheme, modeled on `Price_Truth.png`'s UI mockup |
| `CLAUDE-BEAUTIFUL-WIREFRAME-PROMPT.md` | Prompt | (Not read in full detail this pass — presumably an earlier/alternate wireframe prompt, possibly superseded by `DELIVERABLE-2-WIREFRAME-PROMPT.md`) |
| `DELIVERABLE-2-WIREFRAME-PROMPT.md` | Prompt | The actual prompt used to generate `index.html` — navy/coral palette spec, Deliverable-2-scoped |
| `PriceTruth-Business-Need-FINAL.docx` | Draft candidate (superseded) | 10-page target version, 10 tables, no heading styles |
| `Deliverable_1_-_PriceTrurth_Document.pdf` | Final deliverable (reconfirmed) | Identical to Append-2's final PDF |
| `CLAUDE-BEAUTIFUL-DENSE-PROMPT.md` | Prompt | First "dense 6-slide" PPT prompt, reacting against the sparse 9-slide version |
| `⚡-QUICKEST-METHOD.md` | Guide | Condensed Claude→Canva→PPTX workflow summary |
| `CLAUDE-TO-CANVA-WORKFLOW.md` | Guide | Full Claude→screenshot→Canva→export-pptx workflow, includes the original 9-slide HTML prompt reused from Batch 1 |
| `⚡-START-HERE-DELIVERABLE-3.md` | Guide | Alternate manual 9-slide-in-PowerPoint build path, references live Netlify URL + mockup screenshots |
| `ALL-DELIVERABLES-SUMMARY.md` | **Master submission plan** | Google Drive submission instructions, Group 11 naming, folder structure, draft professor email, expected marks |
| `DELIVERABLE-3-CHECKLIST.md` | Checklist | Step-by-step manual 9-slide PPT build checklist |
| `DELIVERABLE-3-QUICK-START.md` | Guide | Manual 9-slide-in-PowerPoint quick-start, offers 9-slide vs 33-slide choice (recommends 9-slide) |
| `README.md` | Repo doc | Actual GitHub README for the live prototype repo — confirms Deliverable 2 identity, live URL, file list |
| `CLAUDE-DASHBOARD-PROMPT.md` | Prompt | The prompt that generated `dashboard.html`, explicitly modeled on `Price_Truth.png`'s dashboard mockup, pastel palette, simulated-data-only constraint |
| `check_pdf.py` | Script | PyPDF2 page-by-page verification script for the final Deliverable 1 PDF |

#### G. Status update: all three deliverables now appear to have real, finished artifacts
| Deliverable | Status | Artifact |
|---|---|---|
| 1. Business Need Document | ✅ Done | `Deliverable_1_-_PriceTrurth_Document.pdf` / `PriceTruth_Business_Need_-_Group_11.pdf` (7 pages, 13 sections) |
| 2. Wireframe/Prototype | ✅ Done, live | https://price-truth.netlify.app/ (`index.html` + `dashboard.html`) |
| 3. Presentation | ✅ Likely done | `PriceTruth_Presentation.pptx` (6 dense slides) — though parallel 9-slide manual instructions also exist unconfirmed as superseded |

#### H. Updated / new open questions
1. **Was the dense 6-slide `.pptx` the one actually submitted**, or did the user end up manually building the 9-slide version instead per the parallel checklist docs in this same batch? Both paths exist with no cross-reference to each other.
2. **Color-scheme inconsistency**: the live prototype (`dashboard.html`) uses a soft pastel palette, while the Word doc, PPT prompts, and original Batch-1 mockups use navy/coral/green/amber. Worth asking whether this is intentional (a deliberate rebrand for the "real" prototype) or worth reconciling.
3. **The Aug 21 vs Aug 23+ deadline discrepancy remains unresolved** across four batches now — every planning doc still says Aug 21, 10 PM, but dated artifacts (the final PDF, this batch's file timestamps) show work continuing after that. Strongly recommend asking the user directly what actually happened with the deadline, since it affects whether any of this is still "urgent" or already submitted/graded.
4. **Has the Google Drive "GROUP 11" folder submission (per `ALL-DELIVERABLES-SUMMARY.md`) actually happened yet?** If yes, this entire project can likely be marked closed in this tracking file, pending only Lab Work (Oct 2) and Working Demo (Oct 16) per the original rubric (Batch 1 §3).
5. The companion "Deliverable 2 details" document (URL + credentials + features list, as templated in `ALL-DELIVERABLES-SUMMARY.md`) doesn't appear to have been created yet — flag as a small remaining task if submission hasn't happened.

---

### APPEND 4 — Fifth upload batch (20 files): mostly a repeat of Append 3, plus one new PPT prompt iteration

**Context:** This batch re-uploads the exact same 19 files already logged in Append 3 (`temp-full-html.txt`, `PriceTruth_Presentation.pptx`, `CLAUDE-MAXIMUM-CONTENT-PROMPT.md`, `_gitignore`, `index.html`, `dashboard.html`, `CLAUDE-BEAUTIFUL-WIREFRAME-PROMPT.md`, `DELIVERABLE-2-WIREFRAME-PROMPT.md`, `PriceTruth-Business-Need-FINAL.docx`, `CLAUDE-BEAUTIFUL-DENSE-PROMPT.md`, `_-QUICKEST-METHOD.md`, `CLAUDE-TO-CANVA-WORKFLOW.md`, `_-START-HERE-DELIVERABLE-3.md`, `ALL-DELIVERABLES-SUMMARY.md`, `DELIVERABLE-3-CHECKLIST.md`, `DELIVERABLE-3-QUICK-START.md`, `README.md`, `CLAUDE-DASHBOARD-PROMPT.md`, `check_pdf.py`) — no new information from these; see Append 3 for full analysis. **One genuinely new file this batch:**

#### `_-FINAL-ULTIMATE-PROMPT.md` — a further (likely final) iteration of the dense PPT prompt
This is a **fourth distinct attempt** at the Deliverable 3 PPT prompt (after the 9-slide version, the 33-slide version, and the "dense 6-slide" `CLAUDE-BEAUTIFUL-DENSE-PROMPT.md` / `CLAUDE-MAXIMUM-CONTENT-PROMPT.md` versions from Append 3). Key differences:
- Explicitly framed as derived from **"your ACTUAL beautiful HTML"** — i.e., this prompt was reverse-engineered from a real, already-generated HTML presentation (very likely `temp-full-html.txt`, the scratch file flagged as unread in Append 3 §E), rather than being an original content brief. This suggests the workflow was: generate HTML → like the result → ask Claude to convert/re-express it as a formal PPT-ready content prompt.
- **Yet another color palette**, different again from both the navy/coral/green/amber scheme (Word doc, original mockups, first two PPT prompts) and the pastel scheme (`dashboard.html`): this one uses **Coral #C0392B, Teal #1F7A5C, Amber #B9700E, Navy #151C24** — darker/more muted tones than either prior palette.
- Retains the "dense, no empty space, 2-3 columns per slide, no two slides look the same" design philosophy from the Append-3 dense prompts.
- Includes a fleshed-out **Roadmap/Deliverables/Limitations slide** with a Gantt-style 10-week timeline, an explicit "What's Delivered" checklist (working live website, 5 modules, SHAP layer, live API, real data, Netlify deployment, GitHub repo, demo video), and an explicit "Honest Limitations" list — content consistent with everything already logged (Batch 1 §15, Append 2) but styled for this particular dense-slide format.
- Ends by explicitly telling the user this is "THIS IS IT" / "the REAL content with REAL story," suggesting this was presented as the definitive, final version of the PPT content — potentially superseding the `CLAUDE-BEAUTIFUL-DENSE-PROMPT.md`/`CLAUDE-MAXIMUM-CONTENT-PROMPT.md` attempts from Append 3, though it's not confirmed whether this prompt is what actually produced the `PriceTruth_Presentation.pptx` file already on record, or a still-later, unused iteration.

**Net effect on tracking:** This adds a **fourth color palette** to the project's visual-identity history (navy/coral/green/amber → pastel blue/peach/mint/lavender → this darker coral/teal/amber/navy), reinforcing the color-scheme inconsistency flagged in Append 3 §H(2). It also reinforces that Deliverable 3's PPT went through **at least four distinct content/design iterations** before whatever was finally exported to `PriceTruth_Presentation.pptx`.

#### Updated open question
7. Given at least four different PPT prompt iterations now on record (9-slide, 33-slide, dense-6-slide v1, dense-6-slide "ultimate"/v2 with yet another palette), **it would help to directly ask the user which prompt actually produced the final `PriceTruth_Presentation.pptx`** — this can't be determined from file timestamps alone, and matters for knowing whether the presentation is truly finalized or whether `_-FINAL-ULTIMATE-PROMPT.md` represents a not-yet-executed "better" version still worth generating.

---

### APPEND 5 — Sixth upload batch: SUBMISSION CONFIRMED, a fifth visual identity appears, and the user's own master doc surfaces

**Context:** Alongside a repeat of already-logged files (`_-FINAL-ULTIMATE-PROMPT.md`, `PriceTruth_Presentation.pptx`, `CLAUDE-MAXIMUM-CONTENT-PROMPT.md`, wireframe/dense/dashboard prompts, `ALL-DELIVERABLES-SUMMARY.md`, checklists, `check_pdf.py`, `PriceTruth-Business-Need-FINAL.docx` — all already covered in Appends 3–4), this batch contains **three genuinely new and highly significant items**: two finished submission-ready PDFs, and the user's own independently-compiled master context document. Together these substantially resolve the open questions carried since Append 3.

#### A. `MASTER-CONTEXT-COMPLETE.md` — the user's (or a prior session's) own consolidated project doc
Dated **August 25, 2026**, "Status: Phase 1 Complete | Ready for Presentation." This is functionally the same kind of document as this tracking file, but compiled independently. Cross-checking it against everything logged so far:

- **Confirms all three deliverables as submitted**: it explicitly states, for each of Deliverables 1, 2, and 3: **"Status: Submitted August 21, 2026."** This is the first direct confirmation on record that the submission actually happened, and that it happened on the original deadline despite planning/refinement work continuing for days afterward (Aug 23–25). **This resolves the long-running "what happened to the Aug 21 deadline" question from Appends 2–4**: the answer appears to be that the team submitted on time, then kept polishing/regenerating improved versions of the deliverables afterward (better Word doc formatting, better PPT designs, etc.) — quite possibly for the team's own portfolio/practice purposes, or in case of a resubmission opportunity, rather than because the original deadline was missed.
- **Contains one internal inconsistency worth flagging**: it describes Deliverable 3 as **"PowerPoint, 33 slides"** with the old 9-section structure from Batch 1 — this does not match either the 6-slide dense `.pptx` (Append 3) or the ~16-slide, entirely new-look PDF also uploaded in this same batch (§B below). This line in `MASTER-CONTEXT-COMPLETE.md` looks like leftover boilerplate copied from the earliest planning phase rather than an accurate description of what was actually submitted — **direct file inspection (as this tracking file has done throughout) remains more reliable than any single meta-document's self-description.**
- **New information not previously on record:**
  - **Explicit team role assignments**: Swagata Bhowmik (B053) — Technical Lead (ML model development, data pipeline, backend API); Charvi Rathod (B049) — Product Manager (persona research, UI/UX, business model/GTM); Yashwi Shah (B036) — Data Analyst (dataset curation, frontend HTML/CSS/JS, user testing).
  - **Product/business success metrics for the (hypothetical) post-academic future**: 500 users in 3 months, 5,000 discount checks, 80%+ task completion, <5s average check time; ₹10,000/month revenue by Month 6 scaling to ₹50,000/month by Month 12, 5% visitor-to-check conversion, 10 B2B API clients by Month 12. (More conservative than the Batch-1 "₹50–60L Year 2" figures — likely a later, more grounded revision.)
  - Confirms the **pastel color palette** (soft blue #6B8DBF, peach #FFB5A7, mint #B4E7CE, butter #FFE8A3, cream #FFFBF5) as "the" brand palette in this doc's telling — though see §B below, since the newest PPT PDF uses yet another, different palette again.
  - A "Key Decisions Log" section exists (append-only, dated-entry format) but was not fully read in this pass — worth reviewing in a future batch if the user wants full decision history reconciled.

#### B. `Deliverable_3_-_PriceTruth_PPT__Updated_.pdf` — a brand-new, fifth visual identity for the presentation
This is a fully rendered, image-rich PDF (viewed directly) — **not** the 6-slide dense `.pptx` logged in Append 3, and **not** any of the navy/coral or pastel-dashboard styles seen before. It appears to be AI-generated infographic-style slide art (consistent with the `_-CHATGPT-VISUAL-PROMPT.md` DALL-E workflow from this batch, or a similar Canva/AI image-slide pipeline), with a cohesive new brand:

- **New tagline/branding**: "Price Truth — Powered by AI" and "Truth. Transparency. Trust." with a shield-and-rupee logo mark.
- **New color identity (a fifth distinct palette for this project)**: soft purple/lavender gradients, coral/salmon accents, mint-green checkmarks — related to but not identical to either the earlier pastel dashboard palette or any navy/coral version.
- **~16 slides**, substantially content-richer and more specific than any prior version, including some **notable content changes/updates** worth flagging:
  - The 5th feature is now called **"Cross-Platform Price Aggregator"** (comparing prices across Amazon/Flipkart/BigBasket/Croma/Tata CLiQ/Reliance Digital) — this appears to **replace "Live Pack Lookup"** as the fifth module in earlier versions (Batch 1 §7, all prior PPT prompts). This is a genuine feature-set change, not just a rename.
  - Uses a **new flagship example throughout: iPhone 14 (128GB)**, MRP ₹79,900 → sold at ₹48,999, "18% OFF, you save ₹8,901," 92% AI confidence — replacing the earlier ₹5,000-headphones and Nutella examples as the primary running example (though the SHAP explainability slide still uses "boAt Rockerz 450 Headphones," ₹5,000→₹2,500, so the two running examples now coexist rather than one fully replacing the other).
  - New stated metrics: **92% ML accuracy** (vs. the "96% confidence" figure used everywhere earlier), **"2.5M+ products tracked across 10+ platforms"** — a big jump from the Batch-1 figures (1,465 Amazon products + 20,000 Flipkart listings). This looks like aspirational/marketing framing for the pitch rather than the actual current dataset size, and is worth flagging as a potential overclaim if presented literally to the professor.
  - Persona labels updated slightly: Rajesh is now "Budget-Conscious Parent" (was "Grocery Buyer"), Aarav is now "Price-Sensitive Student" (consistent). New quantified persona-level stats appear: "10M+ Smart Shoppers Empowered," "₹5,000+ Avg. Annual Savings Per User," "15+ Hours Saved Every Year."
  - Competitive analysis table drops "Keepa" and "News articles" from earlier versions and now compares against **CamelCamel, PriceBaba, and BigBasket** only.
  - Includes a live "Dashboard Demo" link distinct from the main site: **https://price-truth.netlify.app/dashboard** (in addition to the main `https://price-truth.netlify.app/` URL already on record).
  - SHAP explanation slide reframes the model output as a **percentage-based "Final Prediction" (e.g., 50% base value → 78% final = "Likely to be a Real Discount")** rather than the earlier signed-SHAP-value format (+0.31, +0.28, etc.) — a simplified, more presentation-friendly way of showing the same underlying idea.

**This is very likely the actual, final, submitted version of Deliverable 3** — its filename ("Updated") and its polish level (far beyond any HTML/PPT prompt draft) both suggest it superseded the 6-slide `.pptx` and all earlier prompt-based attempts. This resolves the open question from Append 3–4 about "which PPT actually got submitted."

#### C. `Deliverable_2_-_URL_Prototype_Link.pdf` — confirms the actual Deliverable 2 submission format
A minimal, single-page PDF containing only the title "Deliverable 2 – Prototype – Price Truth" and the live URL (`https://price-truth.netlify.app/`) as a hyperlink. This confirms the simplest possible approach was taken for Deliverable 2's file submission — just a URL pointer document, not the more elaborate "features list + tech description" companion doc that `ALL-DELIVERABLES-SUMMARY.md` had templated (Append 3 §C). That more detailed companion doc template appears to have been dropped in favor of this simpler one-pager.

#### D. Updated overall project status
| Deliverable | Status | Final Artifact |
|---|---|---|
| 1. Business Need Document | ✅ **Submitted Aug 21, 2026** | `PriceTruth_Business_Need_-_Group_11.pdf` (7 pages, 13 sections) |
| 2. Wireframe/Prototype | ✅ **Submitted Aug 21, 2026** | `Deliverable_2_-_URL_Prototype_Link.pdf` pointing to https://price-truth.netlify.app/ |
| 3. Presentation | ✅ **Submitted Aug 21, 2026** (best current guess) | `Deliverable_3_-_PriceTruth_PPT__Updated_.pdf` (~16 slides, new purple/coral AI-generated visual identity) |

**All three deliverables (40 of the course's 100 marks) now appear complete and submitted.** Per the original rubric (Batch 1 §3), remaining coursework is: **S3 Lab Work** (codebase + frameworks + code quality + NFRs, 40 marks, due Oct 2, 2026) and **S3 Working Demo** (20 marks, due Oct 16, 2026) — neither of which has any artifacts on record yet.

#### E. Updated open questions
1. **Confirm with the user directly**: is `Deliverable_3_-_PriceTruth_PPT__Updated_.pdf` indeed the final submitted presentation (superseding the 6-slide `.pptx` and all earlier prompt iterations)? This tracking file now assumes yes based on file-naming and polish level, but this is inference, not confirmation.
2. The **new "2.5M+ products tracked" / "92% ML accuracy" claims** in the updated PPT are considerably more ambitious than the actual documented dataset sizes (1,465 + 20,000 records) and modeling status (no model has been confirmed as trained yet per any file in this tracker) — worth checking with the user whether this is intentional pitch-deck framing (common and generally fine for a vision/mockup slide) or something that could raise questions if a professor probes for the actual current dataset/model status versus the aspirational product vision.
3. **The "Cross-Platform Price Aggregator" replacing "Live Pack Lookup" as the 5th module** is a real scope change — worth confirming this is deliberate and not an accidental drift, since it affects what the "5 core features" actually are going forward (e.g., for the eventual Lab Work / Working Demo phases).
4. Given submission is now confirmed for all three deliverables, **should this tracking file shift focus going forward to the Lab Work (Oct 2) and Working Demo (Oct 16) phases** — i.e., actual codebase, trained ML model, and a functioning (not just mocked) application? No artifacts for that phase exist in the uploads yet.
5. The "Key Decisions Log" section of `MASTER-CONTEXT-COMPLETE.md` was not read in full this pass — flag for review if the user wants complete reconciliation of every dated decision entry against this tracker's own append log.

---

## Append 6 — Functional implementation and measured review (September 19, 2026)

This entry supersedes earlier planning-only status where it conflicts with the implementation below; earlier entries remain historical records.

### Authorization and scope

The user authorized building the complete functional project, using real datasets, with freedom to choose/combine datasets and models. Both supplied Amazon and Flipkart datasets were selected. The user confirmed the existing Netlify site as the reference and deferred beautification to a later pass. The earlier instruction to read without implementing was superseded by this explicit build authorization.

### Implemented foundation

| Area | Actual outcome |
|---|---|
| Catalogue | 21,267 cleaned real listings: Amazon 1,347; Flipkart 19,920; original CSV hashes preserved |
| Model | Histogram gradient boosting selected against random forest and category/platform baseline by validation log error |
| Evaluation | Grouped train/validation/calibration/test split; 4,269 held-out test rows; MAE ₹356.82; median absolute percentage error 20.16%; empirical 90% interval coverage 89.76% |
| Explainability | Actual Tree SHAP, additive contributions in log-price space; no invented explanations |
| Core screens | Discount Checker, Live Pack Lookup, Unit Price Compare, Buy Timing & History, Shrink Timeline |
| Additional screens | Historical Platform Catalogue, Overview, Evidence & Methods |
| External evidence | 395 real INR Open Prices observations; separate 8-observation EUR example; four real barcode caches; real saved name-search results; two cited Indian shrink cases |
| UI | Local Streamlit application; styling isolated from core logic |
| Code review | Generated `reports/CODE-REVIEW-REPORT.md`, raw tool evidence, source hashes, exact commands, actual mutation examples and nine-category NFR table |

### Decisions that replace unsupported planning assumptions

- No synthetic observations or bootstrapped genuine/fake labels were created. Supplied data has no verified authenticity labels, usable repeated price histories or seller ratings. Model output is an observed-price estimate, not a fraud verdict or an accuracy percentage.
- Advertised discount and selling price are not model inputs. Listed price remains an input and can bias the estimate if the reference price is inflated; this limitation is displayed and documented.
- Amazon lacks observation dates. Flipkart dates are 2015–2016. These snapshots cannot establish current fair prices. Combining both sources improves some metrics but not every platform's result.
- Current INR histories are sparse; the longer EUR example is stale. Timing logic abstains rather than inventing seasonal predictions. Currencies and stores remain separate.
- Cross-platform search is implemented as historical catalogue discovery; it does not claim verified same-product live offers.
- Shrink cases are attributed secondary reports with approximate reported timing, not fabricated exact event dates or independently inspected packs.
- Source acquisition and license limitations are recorded in `docs/DATA-SOURCES.md`. Confirm rights before redistributing supplied raw CSVs publicly.

### Verification and remaining scope

98 PyTest cases passed; zero configured Ruff violations. Package statement coverage is 462/526 and branch coverage 74/98. Actual scoped Mutmut run killed 305/375 mutants (81.33%); 70 survived and are disclosed. Mutation scope covers calculations, catalogue and history, not the entire application. All four Radon metric families were collected, including higher complexity in report-generation code rather than hiding it.

Actual Chrome verification exercised overview, price assessment with SHAP and catalogue search/export controls at desktop and mobile sizes. No JavaScript errors or mobile horizontal page overflow were observed. Initial visible load was 3.044 seconds (missed the target); a later run was 1.029 seconds. Sequential prediction and SHAP measurements are in `reports/performance.json`; they are not a concurrent-user benchmark.

The local functional base and review report are ready. Public deployment, HTTPS validation, 24/7 availability, 99% evaluation-window uptime, 100 concurrent users, other browsers, physical devices, a usability study, visual polish and demo recording remain unverified or unfinished. No public site has been replaced. `README.md` contains setup and demo steps; `PROGRESS.md` is the current task tracker.
