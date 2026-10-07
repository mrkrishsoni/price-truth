# Image 4 — Scope and maintainability

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

Explain the amount of reviewed code, measured maintainability, and the remaining complexity issue.

Headline: **Maintainability measured—with gaps visible**

## Required content

Table A — Actual Maintainability Index (MI), 0–100 score, NOT percent:

| Module | MI score | Grade |
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

Package file names without a directory prefix are inside src/price_truth/, except app.py. Source: reports/radon-mi.json; review snapshot 19 September 2026.

Table B — Radon metrics:

| Measure | Result |
|---|---|
| Mean cyclomatic complexity | 4.66 / A |
| Maximum cyclomatic complexity | 40 / E — scripts/review.py |
| Files with MI grade A | 13/13 = 100% of production/script files |
| Raw source lines | 1,017 production/scripts + 361 tests |
| Halstead: model.py | Volume 493.63; effort 3,004.67 |

Two bold result cards, if space allows without shrinking tables:
- **4.66 / A** — mean CC across 47 blocks
- **40 / E** — maximum CC; refactoring target

Readable qualification:
“MI is a 0–100 index, not a percentage. Radon grade A means MI >19. 100% refers only to files ranked A.”

Small scope line: “19 reviewed files • 1,378 SLOC • maximum CC 40/E remains a refactoring target.”

## Composition

Give the full MI table about 60% of the content width and the compact Radon summary the rest. Omit optional cards if needed; never omit MI rows. Preserve readability rather than squeezing long entries into tiny cells. The average and maximum complexity should both stand out. Footer: **04 / 05**.

These are slide-level summaries, not a replacement for the separate detailed Radon tables in the report. Do not describe all functions as low-complexity or treat Halstead effort as measured development time. Generate this single image now.
