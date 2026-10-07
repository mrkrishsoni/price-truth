# Image 2 — Held-out model results

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

Continue from real data to measured model performance.

Headline: **Price estimates tested on held-out data**

Model label:
**Histogram gradient boosting**
Small subtitle: “Selected using validation log MAE”

## Required content

Main table:

| Test metric | Selected model | Baseline |
|---|---:|---:|
| MAE | ₹356.82 | ₹373.27 |
| Log MAE | 0.273049 | 0.305961 |
| R² | 0.957552 | 0.958382 |
| Median absolute percentage error | 20.16% | 23.39% |

Compact comparison strip: **MAE reduced 4.41% • Log MAE reduced 10.76% versus baseline**.
These are relative error reductions: (baseline − selected) / baseline × 100, calculated from the unrounded saved results. They are not accuracy percentages. Source: reports/model_evaluation.json, test and baseline_test fields.

Three prominent result cards:
- **4,269** — test listings
- **20.16%** — median absolute percentage error
- **89.76%** — empirical interval coverage

Readable qualifier:
“Interval target: 90%. Lower MAE/log MAE is better. Baseline has slightly higher R².”

Scope strip:
**Historical price regression—not fraud-classification accuracy.**

## Composition

Place the model label above the main table and use three cards below it. Highlight selected-model MAE without suggesting it wins every metric. Keep the R² qualification plainly visible. Footer: **02 / 05**.

Do not label 89.76% as prediction accuracy or 20.16% as average error; preserve the exact metric meanings. Generate this single image now.
