# Task 02 — WFP Price Cleaner + ZiG Guard (SokoData)

**Real-world scenario:** WFP publishes maize prices across 486 African markets. Columns drift, duplicates appear on `(date, market_id, commodity_id, pricetype, priceflag)`, and Zimbabwe's 2024 ZWL→ZiG redenomination makes local-currency series incomparable. WFP's `usdprice` for pre-2024 rows is often garbage (e.g. $0.0017/kg rice).

**Your job:** Implement `clean_prices(df)` that enforces the warehouse contract.

## You get
- `starter/cleaner_starter.py` — stub + constants (`PRICE_COLUMNS`, `NATURAL_KEY`, `VALID_FLAGS`)
- `fixtures/wfp_sample.csv` — 12 rows with drift, dupes, bad USD

## Requirements
1. Raise `SchemaDrift` if any of `PRICE_COLUMNS` missing.
2. Strip text cols, coerce `date` (errors→NaT), numeric ids/prices (errors→NaN), add `country="ZW"`.
3. Drop rows missing `date/market_id/commodity_id/price`; keep only `priceflag in {"actual","aggregate"}`.
4. `drop_duplicates(subset=NATURAL_KEY, keep="last")`, sort by NATURAL_KEY.
5. `_null_implausible_usd`: ref = median `usdprice` per `commodity_id` over `date >= 2024-01-01`; null any `usdprice < 0.10 * ref`. Commodities with no post-2024 rows untouched. Never touch `price`.

## Scoring
`python grader.py` — 100 pts: schema-drift (20), nulls/flags (20), dedupe (20), USD guard (30), sort/stability (10). Hidden tests use ZWL-era fixtures.

Timebox: human 4-6 hrs. This is the hardest, most Polaris-like task.
