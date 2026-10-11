# Methodology — how these tasks were built (Polaris-style)

1. **Mine, don't invent:** each task is a real bug I fixed: header-only crash (StatLab), ZiG false spikes (SokoData), source-less claims (WBA). Screenshots + commit links in each `calibration.md`.
2. **Starter = broken, not blank:** agent gets docstrings + constants + fixtures, must read 2-4 files and make 50-150 line change — mirrors Polaris "1 week" realism at small scale.
3. **Grader first:** I wrote reference solution (from my shipped code), then grader, then deleted solution to make starter. Hidden fixtures cover: empty, bool, drift, dupe-key, pre/post-2024 USD, bbox edge.
4. **Calibration:** run human (me, timed) + 2 frontier agents with coding tools; record score, tool calls, failure modes. Template:

```
## calibration — task-01
- human: 42 min, 96/100
- gemini-2.5-pro + tools: 78/100, failed bool-vs-numeric + header-only guard
- claude-sonnet + tools: 85/100, missed high-cardinality
- top failures: ...
```

5. **What this proves for Polaris:** I can scope realism, write rubrics, build deterministic graders, and analyze agent failures — the exact job description.
