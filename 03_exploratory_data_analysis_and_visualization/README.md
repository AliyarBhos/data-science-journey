# Olist E-Commerce — Exploratory Data Analysis

Exploratory Data Analysis module on the Brazilian E-Commerce (Olist) dataset, built on top of a prior six-phase data cleaning pipeline (audit → clean → integrate → time validation → productionize → PII/documentation wrap-up).

## Objective

Move beyond cleaning into visualization, trend detection, and storytelling — understanding what drives delivery performance, customer satisfaction, and regional patterns in the dataset.

## Structure

The analysis follows five completed phases:

1. **Missingness & Integrity Audit** — Mapped null values across all tables and confirmed that key gaps (e.g. missing `order_delivered_customer_date`) are structural, tied to order status (canceled/unavailable orders), rather than leftover data quality issues.
2. **Univariate Exploration** — Distributions of price, freight value, and review scores; frequency analysis of product categories and payment types.
3. **Temporal Trends** — Monthly order volume and delivery time trends, computed only on actually-delivered orders to avoid NaT values silently skewing averages.
4. **Bivariate & Correlation Analysis** — Delivery time vs. review score, price vs. freight correlation, order value by payment type.
5. **Geographic Analysis** — Order volume and average delivery time broken down by customer state.


## Key Checks Along the Way

- Every table merge logs row counts before/after to catch NaNs introduced by joins rather than assuming the pre-cleaned state holds.
- Delivery-time metrics are filtered to `order_status == 'delivered'` before aggregation, since including undelivered orders would introduce null durations into the calculation.
- Outlier-heavy numeric fields (price, freight, delivery days) are viewed with quantile clipping for plotting, without discarding the underlying data.

## Tech Stack

- Python, pandas, numpy
- matplotlib, seaborn

## Status

Phases 1–5 complete. 

## Data Source

[Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) (Kaggle)