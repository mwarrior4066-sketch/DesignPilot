# v2 Tests — Catalog

This directory contains all test outputs produced during DesignPilot v2.x development and v3.0 validation.
Raw model outputs are compressed as `raw_outputs.tar.gz` within each batch folder.
Scores in this catalog use the **v3.0 patched validator** throughout, so all numbers are comparable.

---

## Directory structure

```
v2-tests/
  batch/            ← Cross-model batch runs (6 providers × 19–20 tests)
  single-model/     ← Single-model regression runs (Sonnet, Haiku)
  MASTER_SUMMARY.html  ← HTML overview from the run_batch_parallel scoring system
```

---

## Batch runs

| Batch | Date | Providers | Tests | v3.0 score | Composite | Notes |
|---|---|---|---|---|---|---|
| `batch-20260414-0148` | 2026-04-14 01:48 | 6 | 19 | composite only | 80.5 | Partial — deepseek/mistral API issues |
| `batch-20260414-0203` | 2026-04-14 02:03 | 6 | 19 | composite only | 80.8 | Partial — mistral API issue |
| `batch-20260414-0215` | 2026-04-14 02:15 | 6 | 19 | composite only | 76.6 | Partial — gemini/mistral low |
| `batch-20260414-0253` | 2026-04-14 02:53 | 6 | 19 | composite only | 79.3 | Developing run |
| `batch-20260414-0319` | 2026-04-14 03:19 | 1 | 19 | composite only | 87.5 | Mistral only |
| `batch-20260414-0346` | 2026-04-14 03:46 | 1 | 19 | composite only | 89.7 | Mistral only |
| `batch-20260414-0609` | 2026-04-14 06:09 | 6 | 19 | 83/114 (73%) | 79.6 | First full 6-provider scored run |
| `batch-20260414-0734` | 2026-04-14 07:34 | 6 | 19 | 81/114 (71%) | 82.1 | Full run |
| `batch-20260414-0844` | 2026-04-14 08:44 | 6 | 19 | 78/114 (68%) | 83.2 | Full run — 19 tests |
| `batch-20260414-2121` | 2026-04-14 21:21 | 6 | 19 | 90/114 (79%) | — | Diagnostic batch used to identify validator bugs |
| `batch-20260414-2308` | 2026-04-14 23:08 | 6 | 20 | 106/120 (88%) | 81.6 | Validation run — first post-patch batch |
| `batch-20260415-0008` | 2026-04-15 00:08 | 6 | 20 | 104/120 (87%) | 87.3 | Latest full run — pack v3.0 |

> **v3.0 score** = structural validator pass rate using the patched v3.0 runtime_validator.py.
> **Composite** = batch run's own 60/40 rubric score (structural validator + LLM rubric judge).
> Batches 0148–0346 have composite scores only — raw output files were not retained.

---

## Single-model runs

| Run | Model | Notes |
|---|---|---|
| `live-run-v2.8-haiku` | claude-haiku-4-5 | Haiku regression run from v2.8 development |
| `live-run-v2.8-sonnet` | claude-sonnet-4-6 | Sonnet regression run from v2.8 development — 16/19 pass (84%) |

---

## Score progression (v3.0 validator)

All six scored batches evaluated with the same patched validator for direct comparison.
Improvements from batch-0609 to batch-0008 reflect pack refinements, not validator changes.

| Batch | Claude | DeepSeek | Gemini | Mistral | OpenAI | xAI | Total |
|---|---|---|---|---|---|---|---|
| `batch-20260414-0609` | 18/19 | 16/19 | 3/19 | 16/19 | 15/19 | 15/19 | **83/114 (73%)** |
| `batch-20260414-0734` | 15/19 | 13/19 | 14/19 | 15/19 | 9/19 | 15/19 | **81/114 (71%)** |
| `batch-20260414-0844` | 16/19 | 14/19 | 7/19 | 16/19 | 13/19 | 12/19 | **78/114 (68%)** |
| `batch-20260414-2121` | 18/19 | 12/19 | 14/19 | 18/19 | 13/19 | 15/19 | **90/114 (79%)** |
| `batch-20260414-2308` | 19/20 | 17/20 | 17/20 | 19/20 | 17/20 | 17/20 | **106/120 (88%)** |
| `batch-20260415-0008` | 19/20 | 19/20 | 17/20 | 18/20 | 15/20 | 16/20 | **104/120 (87%)** |

---

## Key events

- **batch-20260414-2121** — Identified 7 validator bugs suppressing scores from ~79% to 39%.
  The same outputs scored 39% pre-patch and 79% post-patch. This confirmed the failures were
  validator defects, not model quality issues.

- **batch-20260414-2308** — First validation run with patched validator. 88% pass rate.
  All 6 providers cleared the 70% gate.

- **batch-20260415-0008** — First run with pack v3.0 (renamed from v2.9).
  Pass-05 and pass-06 failures traced to false positives in `positively_present()` and
  overclaim rules — both fixed. Pass-07 prompt updated to require explicit tradeoff.

---

## File format

Each `batch/<id>/raw_outputs.tar.gz` contains:
```
<provider>/pass-NN_pack.md   ← Raw model output for each test
```

Each batch folder also contains the scoring artifacts produced during the run:
- `summary.json` — per-provider composite scores
- `comparative_report.json` — cross-provider comparison
- `comparative_report.html` — rendered HTML report
- `run_context.json` — pack version, run metadata

---

## Validator

All v3.0 scores in this catalog were produced by `scripts/runtime_validator.py` at pack v3.0.
The validator is deterministic — re-running it against any preserved raw_outputs.tar.gz
will produce the same scores shown here.

To rescore a batch:
```bash
tar -xzf tests/v2-tests/batch/<id>/raw_outputs.tar.gz -C /tmp/run/
python scripts/runtime_validator.py  # via run_batch_parallel.py or manual scoring
```
