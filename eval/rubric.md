# Rubric philosophy — deterministic, partial-credit, anti-hackable

1. No LLM-as-judge. Every point comes from a pytest assert on hidden fixtures.
2. Each task 100 pts, split by sub-skill (see each grader.py).
3. Solved = >=85. Partial 60-84 = "progressing". <60 = "failed".
4. Hidden fixtures never committed to public `fixtures/` — graders load them from private dir in CI (template in `eval/run_all.py`).
5. Anti-memorization: fixtures use Harare/ZiG/WFP realism that isn't in SWE-bench; USD-guard threshold (0.10) and NATURAL_KEY are documented so agent must read prompt, not guess.
6. Calibration required: every task ships `calibration.md` with human minutes + 2 model runs + top 3 failure modes.
