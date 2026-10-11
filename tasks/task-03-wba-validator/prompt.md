# Task 03 — Curated DB Validator (Who Builds Africa)

**Real-world scenario:** Open database of foreign participation in African infrastructure. Every claim needs source + verbatim + evidence-strength. PRs add CSVs; bad rows must fail CI with clear errors, soft issues warn.

**Your job:** Implement `validate.py` as a module with `validate(base_dir, vocab) -> (errors, warns)`.

## You get
- `starter/validator_starter.py` — stub
- `fixtures/curated/` — 6 tiny CSVs (`projects, organizations, participation_records, contracts, claims, dates`) with 8 seeded bugs
- `fixtures/vocabularies.yaml` — allowed enums

## Requirements
1. Check: missing `id`, bad `country_iso3` (`^[A-Z]{3}$`), invalid `sectors/role/location_precision/evidence_strength/precision` vs vocab.
2. `value_original` without `currency` → error; bad currency format → error.
3. `location_precision in {exact, approximate}` but missing lat/lon → warn; lat/lon outside Africa bbox `(-35,-25,38,62)` → warn.
4. Missing `verbatim_quote` → warn; missing `claim_text/source_id/role/org_id` → error.
5. Duplicate `(canonical_name.lower, country_iso3)` projects → warn; duplicate org names → warn.
6. Return `(errors, warns)` lists of strings; CLI exits 1 on errors, 0 otherwise.

## Scoring
`python grader.py` — 100 pts, 8 hidden bug-injection tests + exit-code test. No LLM judge.

Timebox: human 3-4 hrs.
