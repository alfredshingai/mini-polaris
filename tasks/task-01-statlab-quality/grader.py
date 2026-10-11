"""Deterministic grader for Task 01 — 100 pts, no LLM judge. Run: python grader.py"""
import importlib.util
import pathlib
import sys

import pandas as pd
import numpy as np

HERE = pathlib.Path(__file__).parent
CANDIDATE = HERE / "starter" / "data_quality_starter.py"
# grader also accepts solution.py in same dir if agent copies file
ALT = HERE / "solution.py"
TARGET = str(CANDIDATE if CANDIDATE.exists() else ALT)

spec = importlib.util.spec_from_file_location("dq", TARGET)
dq = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dq)

score, total = 0, 100
def check(name, cond, pts):
    global score
    status = "PASS" if cond else "FAIL"
    if cond:
        score += pts
    print(f"[{status}] {name} (+{pts if cond else 0}/{pts})")
    return cond

# 1. is_numeric_series — 15 pts
check("numeric int is numeric", dq.is_numeric_series(pd.Series([1, 2, 3])) is True, 5)
check("bool is NOT numeric", dq.is_numeric_series(pd.Series([True, False])) is False, 5)
check("string is NOT numeric", dq.is_numeric_series(pd.Series(["a", "b"])) is False, 5)

# 2. is_categorical_series — 15 pts
check("object dtype is categorical", dq.is_categorical_series(pd.Series(["Harare ", "harare", "Bulawayo"])) is True, 5)
check("low-card numeric is categorical", dq.is_categorical_series(pd.Series([1, 1, 2, 2, 1, 2] * 10)) is True, 5)
check("high-card numeric is NOT categorical", dq.is_categorical_series(pd.Series(range(100))) is False, 5)

# 3. column_type_summary — 35 pts
df = pd.DataFrame({
    "price": [10.0, 20.0, None],
    "market": ["Harare ", "harare", None],
    "flag": [True, False, True],
    "day": pd.to_datetime(["2024-01-01", "2024-01-02", "2024-01-03"]),
})
try:
    summ = dq.column_type_summary(df)
    check("summary has 8 cols", list(summ.columns) == ["column","inferred_type","dtype","missing_count","missing_pct","unique_count","is_constant","is_empty"], 5)
    check("bool typed as bool", summ.set_index("column").loc["flag","inferred_type"] == "bool", 5)
    check("date typed as date", summ.set_index("column").loc["day","inferred_type"] == "date", 5)
    check("missing counted", summ.set_index("column").loc["price","missing_count"] == 1, 5)
except Exception as e:
    print(f"[FAIL] summary normal case raised {e} (+0/20)")

try:
    empty = pd.DataFrame(columns=["a", "b"])
    esumm = dq.column_type_summary(empty)
    check("header-only no crash + right cols", list(esumm.columns)[:3] == ["column","inferred_type","dtype"], 10)
    check("header-only 2 rows", len(esumm) == 2, 5)
except Exception as e:
    print(f"[FAIL] header-only crashed: {e} (+0/15)")
    print("HINT: original StatLab bug was df.describe() on empty frame.")

# 4. duplicates — 10 pts
ddf = pd.DataFrame({"a": [1, 1, 2], "b": ["x", "x", "y"]})
try:
    check("dup count == 1", dq.duplicate_row_count(ddf) == 1, 10)
except Exception as e:
    print(f"[FAIL] dup raised {e}")

# 5. data_quality_summary — 25 pts
try:
    s = dq.data_quality_summary(df)
    check("summary keys", all(k in s for k in ["n_rows","n_columns","n_numeric","n_categorical","n_date","n_bool","duplicate_rows","total_missing_values"]), 10)
    check("n_rows==3", s.get("n_rows") == 3, 5)
    check("total_missing==2", s.get("total_missing_values") == 2, 5)
    check("empty summary no crash", isinstance(dq.data_quality_summary(pd.DataFrame(columns=["a"])), dict), 5)
except Exception as e:
    print(f"[FAIL] quality summary raised {e}")

print(f"\nSCORE: {score}/{total} — {'SOLVED (>=85)' if score >= 85 else 'NOT SOLVED'}")
sys.exit(0 if score >= 85 else 1)
