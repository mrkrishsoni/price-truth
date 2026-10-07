# Image 5 — Readiness and product boundaries

## Task and output

Generate ONE finished presentation image directly in this chat, using the image-generation tool. This file contains instructions, not text to reproduce in full. Do not return only a description or another prompt. Do not generate other slides. If image generation is unavailable, state that clearly.

Use landscape 16:9, ideally 1920 × 1080 or the highest supported landscape resolution. Make it readable at normal presentation size. After generating this image, wait for the next uploaded prompt.

## Shared design system

This image belongs to a five-image Price Truth presentation. Use the same design system even when this prompt is opened in a new chat.

- White/off-white background: #F8FAFC.
- White cards: #FFFFFF.
- Main headings and important numbers: deep navy #16324F.
- Teal accents: #0F766E.
- Secondary blue: #4F7CAC.
- Thin borders: #D6DFE8.
- Body text: charcoal #202B38.
- Secondary text: slate #536274.
- Limitations: dark amber #92400E, optionally on pale amber #FFFBEB.

Aim for soft background contrast with strong text readability. Use a clean sans-serif font, rounded cards, restrained shadows, generous spacing and consistent alignment. No dark backgrounds, gradients, neon colours, stock imagery, fake screenshots or decorative graphs. Use colour sparingly; include words to communicate status.

Visual reference: https://price-truth.netlify.app/ . If a prototype screenshot is attached, follow its visual character while retaining this light palette. If the reference is inaccessible or no screenshot is attached, proceed with this fully specified design system; do not claim to have inspected the site.

Place the project name “PRICE TRUTH” at the upper left, one strong takeaway headline beneath it, and a small image number at the bottom right. Use compact tables as the main content, with large bold result cards where specified. The layout should feel like a polished academic presentation, not a dense report page or an app screenshot. Keep numerical columns aligned and labels concise. Preserve mandatory content; avoid extra prose.

## Accuracy and generation checks

The facts below concern a local historical price-assessment application and its recorded code-review snapshot. Do not invent results, functionality, logos, certifications or claims about marks. Do not treat historical data as live offers, R² as classification accuracy, or unmeasured requirements as passed. The presentation summarizes evidence; it does not replace the report.

Use exact values, denominators, units and scope labels provided below. If the concise report is also attached and contains a genuine contradiction, flag it before generating instead of silently inventing a resolution. Do not change values just to fit.

Before displaying the image, check the rendered text and numbers for misspellings, missing rows, clipping and overlap. Keep limitations readable rather than hiding them in tiny footnotes. Use clear typography for decimal points, percentages and the rupee symbol. If a prior slide is attached, match its visual treatment.

## Story role and headline

Close the story with a credible demonstration scope and explicit remaining work.

Headline: **NFRs: measured evidence and remaining gaps**

## Required content

Main table:

| NFR | Target | Numerical evidence / gap |
|---|---|---|
| Performance | Page <3 s; assessment <2 s | First page 3.044 s; repeat 1.029 s; assessment + SHAP 0.926 s |
| Scalability | 100 concurrent users | No concurrent-user benchmark; 29 sequential warm calls only |
| Usability | Use without a manual | 3 browser flows recorded; no user-study success rate |
| Security | HTTPS; no PII storage | Local HTTP; security percentage not measured |
| Reliability | 99% uptime | Actual uptime percentage not measured |
| Portability | Desktop/tablet/mobile | 2 viewport sizes: 1440×1000 and 390×844; no mobile page overflow |
| Maintainability | Modular code | 13 production/script files; 13/13 MI grade A |
| Availability | 24/7 access | Local only; availability percentage not measured |
| Compatibility | 4 named browsers | 1/4 tested = 25% browser test coverage; Chrome only |

Two prominent timing cards:
- **0.035 s** — warm assessment p95, 29 sequential calls
- **1.47% over budget** — first page 3.044 s versus 3 s; target missed

Short scope note: “25% is browser test coverage, not a compatibility success score. Unmeasured is not 0%.”

Security qualification: “Raw CSVs retain reviewer fields; processed model features exclude them.”

Evidence: reports/browser_initial_check.json, browser_check.json, performance.json and radon-mi.json. Percent over time budget calculated from original unrounded timing, not rounded slide values. These are 19 September 2026 snapshot results, rechecked against saved evidence on 24 September; no new benchmark is claimed.

Closing statement:
**A working historical-price demonstration with measured review evidence.**

## Composition

Use a wide central table with restrained, labelled status styling. Give both numerical cards comparable weight. Make the missed load-time target visible. Evidence filenames and generation instructions need not appear in the image. Keep both scope and security qualifications readable. Put the closing statement on a subtle pale strip. Footer: **05 / 05**.

Do not claim production readiness, public availability, verified fraud detection or completion of the entire consumer product. The latency values have different scopes; do not combine them into a single speed result. Generate this single image now.
