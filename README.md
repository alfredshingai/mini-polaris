# mini-polaris

Realistic, long-horizon software-engineering eval tasks — in the style of Google DeepMind's Polaris team.

> Polaris engineers design tasks that test a model's ability to complete real-world SWE work: a prompt + a grader/rubric that assigns a numerical score. One good task takes ~1 week from ideation to approval.

This repo is my proof I can do that work: 3 tasks mined from my own shipped bugs, each with starter code, hidden fixtures, deterministic grader, and calibration report.

Built by Alfred Shingai — Data Analyst & Builder, Harare.
Portfolio: https://alfredshingai.dev | GitHub: https://github.com/alfredshingai

## Tasks

| # | Task | Source bug | Skills tested |
|---|------|------------|---------------|
| 01 | `task-01-statlab-quality` — Messy CSV quality profiler | StatLab Zim crashed on header-only file | pandas dtypes, empty states, bool vs numeric, IQR outliers |
| 02 | `task-02-sokodata-cleaner` — WFP price cleaner + ZiG guard | False price spikes across ZWL→ZiG redenomination | schema-drift, natural-key dedupe, groupby-median USD guard |
| 03 | `task-03-wba-validator` — Curated DB validator | Claims without sources, map without DB | multi-file CSV validation, vocab enums, errors vs warns, exit codes |

Each task dir has:
```
prompt.md        # what the agent (human or Gemini) sees
starter/         # broken/incomplete code to fix
fixtures/        # public fixtures (hidden fixtures stay private for grading)
grader.py        # deterministic rubric → 0-100 score
solution/        # reference solution (not shown to agent)
calibration.md   # human time + model attempts + failure modes
```

## Quickstart

```bash
python -m pytest tasks/task-01-statlab-quality/grader.py -v
python eval/run_all.py --task task-01-statlab-quality
```

## Rubric philosophy

- No LLM-as-judge. All points from deterministic pytest checks.
- Partial credit per sub-skill (see `eval/rubric.md`).
- Hidden fixtures test: empty file, bool columns, high-cardinality, IQR zero-variance, schema drift, implausible-USD edge.

## Calibration

See `docs/methodology.md` for how tasks were mined, piloted, and scored against 2 agents (human + Gemini/Claude).

## Why this matters for Polaris

My day job is turning WFP PDFs + 12 CSV dialects + ZiG chaos into SokoData (486 markets, 31 commodities, 22 datasets). That's exactly Polaris's bet: fewer, harder, real tasks beat synthetic pipelines.
