# How to use DesignPilot

## Just want to run it?

For normal AI startup, begin with:
```
QUICKSTART.md
```

The quickstart points the AI to the correct runtime entry path. Do not use `README.md` as operator startup material.

---

## Want to run cross-model tests?

```bash
python3 scripts/run_batch_parallel.py
```

Results appear in `tests/live_outputs/batch/`. The master timeline is at:
```
tests/reports/v2-tests/MASTER_SUMMARY.html
```

---

## Want to change the pack?

Edit files in `src/` first. Rebuild compiled artifacts after source changes:

```bash
python3 scripts/compile_designpilot.py
```

Then verify nothing broke:

```bash
python3 scripts/run_validation_suite.py
python3 scripts/run_regression_suite.py
```

---

## Verify the pack is healthy

| Validator | What it checks | Failure type | Common cause |
|---|---|---|---|
| `run_validation_suite.py` | Runs lint, lightweight path, examples, project workspace, and integrity sync together | Blocking | Any lower-level validator fails |
| `run_regression_suite.py` | Runs all 45 pass/fail fixtures against the runtime validator | Blocking | Validator drift, fixture drift, or a missing golden output |
| `validate_examples.py` | Checks example structure, eval references, and runtime overlay assets | Blocking | Example edited without required sections, eval JSON, or matching compiled route cards |
| `validate_lightweight_path.py` | Checks `DEPLOY_LITE`, launchers, starters, route cards, contract cards, and lite index counts | Blocking | Compile step skipped or paths point to stale runtime locations |
| `validate_integrity_sync.py` | Checks compiled runtime assets, reports, summaries, aliases, and dist/source sync | Blocking unless noted as warning | Stale generated reports, cache artifacts, or source and dist summaries out of sync |

A PASS means the pack is internally consistent. It does not mean real-world design outcomes have been proven.

---

## Want to do a release?

```bash
python3 scripts/package_release.py
```

---

## Where things live

| What | Where |
|------|-------|
| AI startup surface | `QUICKSTART.md` |
| Compiled full deploy prompt | `dist/DESIGNPILOT_DEPLOY.md` |
| Runtime launchers | `dist/runtime/task_launchers/` |
| Skill definitions | `src/skills/` |
| Task contracts | `src/schemas/task_contracts.json` |
| Section name aliases | `src/schemas/section_aliases.json` |
| Test suite | `tests/` |
| Maintainer docs | `docs/maintainer/MAINTAINER_GUIDE.md` |
| Operator docs | `docs/operator/DEPLOYMENT_GUIDE.md` |

---

## The 5 scripts you actually need

| Script | What it does |
|--------|-------------|
| `run_batch_parallel.py` | Run cross-model tests across supported providers |
| `compile_designpilot.py` | Rebuild `dist/` after editing `src/` |
| `run_validation_suite.py` | Run all local validators in one command |
| `run_regression_suite.py` | Check all 45 static regression fixtures |
| `package_release.py` | Validate and package a release |

Everything else in `scripts/` is either called by these five or is a maintenance tool. See `scripts/README.md` for the full map.
