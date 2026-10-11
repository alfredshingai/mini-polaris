## calibration — task-01 (statlab quality profiler)
- human / reference (Alfred shipped `statlab-zim/src/data_quality.py`): 100/100, ~42 min
- blank starter: 0/100 (`NotImplementedError`) — grader not gameable
- agent run A (muse-spark, fresh solve from prompt only, ~6 min, 3 tool calls): 100/100
- agent run B (same, re-run after starter restore): N/A — starter correctly scores 0 until solved
- top failure modes (expected for weaker models): bool-vs-numeric (`is_bool_dtype` guard), header-only crash via `df.describe()`, high-cardinality heuristic (`max_unique_ratio`)
- verdict: SOLVED band (>=85). Good discriminator: trivial stub fails, real implementation passes.
