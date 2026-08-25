# 02 — Data Cleaning: Brazilian E-Commerce (Olist)

## Overview
End-to-end cleaning and integration of the [Olist Brazilian E-Commerce dataset](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) —
9 relational tables covering orders, payments, reviews, products, customers, and sellers (2016–2018, ~100k orders).

Goal: produce a single, validated, analysis-ready table while documenting every data quality
decision made along the way — not just the fixes, but the reasoning behind them.

## Source Tables
| Table | Grain (what one row represents) |
|---|---|
| orders | one order |
| order_items | one item within an order |
| order_payments | one payment method applied to an order (split payments possible) |
| order_reviews | one (review, order) pair |
| customers | one customer |
| products | one product |
| sellers | one seller |
| geolocation | one zip-code-prefix → lat/long entry (many rows per prefix, expected) |
| product_category_name_translation | category name lookup (PT → EN) |

## Pipeline
1. **Audit** (`01_audit`) — missingness (with MCAR/MAR/MNAR hypotheses tested via groupby/value_counts,
   not assumed), duplicate/primary-key checks, dtype issues, outlier validation, text quality checks,
   light referential integrity checks.
2. **Clean** (`02_clean_tables.py`) — per-table cleaning functions (`clean_products`, `clean_reviews`,
   `clean_orders`, etc.)
3. **Integrate** (`build_wide_table`) — incremental joins from `orders` outward, with row-count and
   null-count validation after every merge.
4. **Time validation** — checks the logical timestamp sequence (purchase ≤ approved ≤ shipped ≤ delivered)
   and flags violations.
5. **Validate** (`validate_wide_table`) — assertions on row counts, key integrity, and known baseline
   anomaly counts, so future re-runs catch regressions automatically.

## Key Findings
- **Review comments (MAR)**: missing comments correlate with higher review scores — happy customers
  tend to rate without writing anything. Missingness is signal, not noise — preserved via a `has_comment` flag
  rather than imputed.
- **Delivery dates (MNAR)**: missing delivery timestamps correspond to orders that were canceled or
  never fulfilled — the date is missing because the event never happened. Left as null, `was_delivered`
  flag added.
- **19 orphaned `product_id`s**: order_items reference products that don't exist anywhere in the products
  table — a genuine source-data integrity gap, only surfaced after the full join (not visible in
  table-level checks alone).
- **1,662 timestamp anomalies**: orders where `approved_at` occurs after `delivered_carrier_date`, or
  `delivered_carrier_date` after `delivered_customer_date` — logically impossible sequences in the
  source data. Flagged (`has_timestamp_anomaly`), not corrected — no reliable way to know which
  timestamp is wrong.
- **9,068 late deliveries**: real operational outcomes, not a data quality issue — flagged for
  downstream analysis (`delivered_late`), not cleaned.
- **74 product categories, 2 missing translations** (`pc_gamer`, `portateis_cozinha_...`) — manually
  translated and merged in.

## What Was Intentionally Left As-Is
- Timestamp anomalies and late deliveries are flagged, not fixed — correcting them would mean
  fabricating data with no ground truth.
- The final table has one row per (order × item × payment) combination — a deliberate choice for a
  single wide table over multiple narrower views. Any aggregation on this table (e.g. summing `price`)
  must account for this row multiplication to avoid double-counting.

## How to Run
```python
final_df = build_wide_table(orders_clean, order_items_clean, order_payments,
                             reviews_clean, customers, products_clean, sellers)
validate_wide_table(final_df)
log_cleaning_summary(final_df)
```

## PII Note
See [PII considerations](#) section — dataset is pre-anonymized; notes included on what would be
required for real, non-anonymized customer data.