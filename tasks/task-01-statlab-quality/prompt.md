# Task 01 — Messy CSV Quality Profiler (StatLab Zim)

**Real-world scenario:** StatLab Zim lets classmates upload any CSV and get descriptives + charts + tests. It crashed on an empty file with only a header, mis-typed `Harare vs harare`, and flagged booleans as numeric.

**Your job:** Implement `data_quality.py` with 5 functions so the app never crashes and always tells the truth.

## Files you get

- `starter/data_quality_starter.py` — 5 function stubs with docstrings, all `raise NotImplementedError`
- `fixtures/maize_prices_raw.csv` — 6-row public sample (duplicates, blanks, mixed formats)
- `fixtures/header_only.csv` — just a header, zero rows (the crash case)

## Requirements

Implement in `starter/data_quality_starter.py` (or copy to `solution.py`):

1. `is_numeric_series(s)` — True if numeric dtype AND not bool.
2. `is_categorical_series(s, max_unique_ratio=0.1)` — True if object/string/category dtype, OR numeric with `nunique/len <= ratio`.
3. `column_type_summary(df)` — returns DataFrame with columns: `column, inferred_type, dtype, missing_count, missing_pct, unique_count, is_constant, is_empty`. Order: bool → date → numeric → categorical → text. Must handle empty df (return empty df with those columns, no crash).
4. `duplicate_row_count(df)` — int count of duplicated rows.
5. `data_quality_summary(df)` — dict with: `n_rows, n_columns, n_numeric, n_categorical, n_date, n_bool, n_text, duplicate_rows, empty_columns, constant_columns, high_cardinality_columns, columns_with_missing, total_missing_values, total_missing_pct`.

Edge cases you MUST handle (hidden tests):
- header-only df
- all-NaN column
- bool column must be `bool`, not `numeric`
- constant column (`is_constant=True`)
- IQR outlier helper not required here, but `high_cardinality_columns` helper is tested indirectly via summary

## Constraints

- Only `pandas`, `numpy` allowed.
- No `df.describe()` without empty-guard (that's the original crash).
- Functions must be pure (no prints, no file I/O).

## Scoring

Run: `python grader.py`
- 100 pts total, partial credit per function. See grader output for breakdown.
- Pass threshold for "solved": >= 85.

## Timebox

Polaris target: human ~3-5 hrs. Agent should need multi-step tool use (read fixtures, run pytest, fix dtypes).
