## calibration — task-02 (sokodata cleaner + ZiG guard)
- human / reference (Alfred shipped `SokoData/.../markets/clean.py`): 100/100, ~90 min
- blank starter: 0/100 (`NotImplementedError`) — grader not gameable
- agent run A (muse-spark, fresh solve from prompt only, ~8 min): 100/100 — schema-drift, dedupe keep=last, text strip, implausible-USD null (price preserved), sort
- expected weaker-model failures: forgetting `SchemaDrift`, `keep=first` vs `last`, nulling `price` instead of `usdprice` only, missing `IMPLAUSIBLE_FACTOR=0.10` post-2024 median logic
- verdict: SOLVED band (>=85). Hardest, most Polaris-like task (multi-step + domain reasoning about ZWL→ZiG).
