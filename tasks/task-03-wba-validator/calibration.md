## calibration — task-03 (wba validator)
- human / reference (Alfred shipped `who_builds_africa/scripts/validate.py` CLI, refactored to `validate()`): 100/100, ~60 min
- blank starter: 0/100 — grader not gameable
- agent run A (muse-spark, fresh solve): 95/100 first pass — missed `coords outside Africa → warn`
  - root cause was a GRADER BUG, not agent bug: fixture used lat=0, lon=0 (Gulf of Guinea) which is INSIDE bbox (-35,-25,38,62), so no-warn was correct
  - fix: fixture changed to London 51.5,-0.1 (truly outside bbox) → agent scores 100/100
  - rubric total also fixed 110 → 100 (`returns 2 lists` now 0-pt gate)
- lesson (Polaris-relevant): bbox calibration + edge-point selection matters; Gulf of Guinea (0,0) is a classic null-island trap
- expected weaker-model failures: errors-vs-warns swap, currency regex, duplicate detection without case-folding
- verdict: SOLVED band (>=85) after fix.
