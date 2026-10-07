# Image 3 — Testing and mutation results

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

Move from model evaluation to evidence that the implemented code was reviewed.

Headline: **Code quality backed by executed checks**

## Required content

Main table:

| Check | Recorded result | Scope |
|---|---|---|
| Ruff | 0 violations | Configured rules |
| PyTest | 98 passed | Six test files |
| Statement coverage | 87.83% | price_truth package |
| Branch coverage | 75.51% | price_truth package |
| Mutmut | 305/375 killed | Three modules |

Two bold result cards:
- **81.33%** — mutation kill rate
- **70** — surviving mutants

Readable scope note:
“Mutation: calculations, catalogue and history. Coverage excludes scripts and app.py; AppTest exercises app.py.”

## Composition

Give the table most of the image. Put the two result cards below it with equal visual prominence. Use a neutral or amber accent for surviving mutants; do not hide them. Scope note must be legible at presentation size. Footer: **03 / 05**.

Do not imply zero defects, full-project mutation coverage, full-project statement coverage or 100% code coverage. Generate this single image now.

