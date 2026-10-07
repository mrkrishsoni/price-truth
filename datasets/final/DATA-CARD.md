# Price Truth — final dataset card

Version 1.0 · built 7 October 2026 by `scripts/build_final_dataset.py` · generator `src/price_truth/synthetic.py` · parameters `assumptions.json`.

The dataset combines **real** marketplace and food-price records with **synthetic** layers that fill gaps no public source covers (daily price histories, discount-authenticity labels, cross-platform offers). Every row or case carries a `provenance` field: `real` or `synthetic`. The price-estimation model is trained and evaluated on real listings only.

## Tables

| File | Rows | Provenance | Contents |
|---|---|---|---|
| `datasets/processed/catalogue.csv` | 21,267 listings | real | Amazon (1,347, crawled 5 Jan 2023) and Flipkart (19,920, crawled 2015–16): name, category, listed (MRP) and selling price, rating, rating count, brand, URL |
| `price_history.csv.gz` | 523,698 daily rows · 518 products | synthetic | Daily selling price and shown MRP, 1 Jan 2024 – build date, with the sale event in force and whether the seller inflates prices |
| `discount_training.csv.gz` | 29,276 offers · 1,958 products | synthetic | Sampled days with the advertised discount, the product's usual discount, the 30-day pre-promotion low, the real saving and the label `inflated` (5.6% positive) |
| `offers.csv` | 2,283 offers · 518 products | synthetic | Same-product price on up to 8 Indian platforms on the build date, with delivery and platform fees, availability and a search link |
| `food_prices.csv.gz` | 407 real + 60,660 synthetic | mixed | Open Prices INR shop observations plus daily histories for 30 real barcodes at 2 simulated stores, anchored at their real observed price |
| `shrink_cases.json` | 15 cases | 10 real, 5 synthetic | Pack-size reductions: Vim and Haldiram's (Financial Express 2022), Parle-G (ThePrint 2022), Maggi ×7 sizes (Angel One 2026); 5 simulated multi-step timelines with generic product names |

The app generates any listing's history on demand with the same seeded function, so every catalogue product (not only the 518 in the file) has a history that ends today. Past days never change when later days are added.

## Fields recovered from the real data (not synthetic)

- **Amazon observation date:** the `qid` Unix timestamp in each product link → 5 January 2023 for all 1,347 listings.
- **Amazon brand:** the first word of the title (`brand_source = title_first_word`).
- **Flipkart rating count:** `0` where the source says "No rating available"; unknown otherwise.

## How the synthetic layers are generated

For each product, from a seed derived from its key:

1. **Regular price.** It starts at the real catalogue selling price (on the anchor date, 1 Jun 2025). Price revisions follow a category-specific rate (every 10–45 days), plus India CPI drift of 4.3% a year (2023–25 average) and occasional small daily changes. The result is about 3.4 price changes per product per month (assumed range 1–4).
2. **Sale events.** 40 dated events, 2024–2027: Big Billion Days, Great Indian Festival, Prime Day, Republic Day and Independence Day sales, Myntra EORS and Meesho Mega Blockbuster. Dates come from press releases and news reports; 2027 is extrapolated. During an event the price drops by the category's measured extra discount against the prior week: 3–15% for electronics, 5–25% for clothing, and so on (DataWeave, Prime Day India 2024).
3. **Inflating sellers.** 16% of Amazon and 6% of Flipkart products, matching DataWeave's measured share of products whose price was raised during the 2020 festive sales. These sellers raise the price 5–15% for 1–4 weeks before an event, then show an MRP 10–30% higher during it. Their real saving is about 10% of a normal sale's.
4. **Labels.** An offer is `inflated` when its advertised discount is at least 5 points above the product's 90-day median **and** the price is less than 5% below its lowest price in the 30 days before the promotion. The 30-day rule follows EU Omnibus Directive 2019/2161 (Art. 6a), confirmed by CJEU C-330/23. Result: 23% of Amazon and 12% of Flipkart sale-day offers are inflated, against about 0% outside sales.
5. **Offers.** Platforms that sell the category quote the listing's current price × a platform factor: ±4% for Amazon and Flipkart, +3% for Croma and Reliance Digital, about −10% for Meesho, ±8% for fashion sites. Real delivery thresholds and fees apply: Amazon ₹40 below ₹499 plus a ₹5 marketplace fee; Flipkart ₹40 below ₹500 plus ₹3; Myntra ₹99 below ₹1,000.

Every parameter in `assumptions.json` records its source URL, or is marked `assumption` where no citable figure exists.

## Models trained on this dataset

| Model | Data | Held-out result |
|---|---|---|
| Price estimate (gradient boosting) | Real listings only | 4,269 unseen listings: R² 0.962, MAE ₹354, median error 20.5% |
| Discount authenticity (logistic regression, chosen over gradient boosting on validation) | Synthetic labelled offers, split by product | 5,859 offers from unseen products: ROC AUC 0.88, precision 23%, recall 49% at the validation-tuned threshold 0.17 |

The discount model sees only listing information. The history-based rule is the primary check in the app; the model gives a secondary risk score.

## Limitations

- Synthetic rows show realistic *patterns*; they are not observations of what any seller actually charged. Conclusions about real sellers need real price histories.
- The model learns the generator's rules, so its accuracy is accuracy at recovering the simulation, not at detecting real fraud.
- Pre-sale price-rise magnitudes, regular-day discounts for some categories, cross-platform gaps for Croma, Reliance Digital, Tata CLiQ and Ajio, and some sale end dates are assumptions (marked in `assumptions.json`).
- The Maggi shrinkflation figures come from a single outlet.
- Licences: Amazon data CC BY-NC-SA 4.0, Flipkart CC BY-SA 4.0, Open Food Facts/Open Prices ODbL. Derived files keep these terms; non-commercial use with attribution.

## Rebuild

```bash
.venv/bin/python -m price_truth.data      # real catalogue with recovered fields
.venv/bin/python -m price_truth.model     # price model (real data only)
.venv/bin/python scripts/build_final_dataset.py
```
