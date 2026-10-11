"""Starter — Task 01: implement these 5 functions. All raise NotImplementedError."""

from __future__ import annotations

import pandas as pd


def is_numeric_series(s: pd.Series) -> bool:
    """Return True if numeric (excluding bool)."""
    raise NotImplementedError


def is_categorical_series(s: pd.Series, max_unique_ratio: float = 0.1) -> bool:
    """Heuristic: object/string/category → True; numeric with few uniques → True."""
    raise NotImplementedError


def column_type_summary(df: pd.DataFrame) -> pd.DataFrame:
    """See prompt.md for required columns + empty-df guard."""
    raise NotImplementedError


def duplicate_row_count(df: pd.DataFrame) -> int:
    """Return number of duplicate rows (excluding first occurrence)."""
    raise NotImplementedError


def data_quality_summary(df: pd.DataFrame) -> dict:
    """High-level dict summary. See prompt.md for keys."""
    raise NotImplementedError
