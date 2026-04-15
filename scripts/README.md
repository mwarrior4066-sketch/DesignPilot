# Scripts

29 scripts in this directory. Most are internal. This is the current map.

---

## Tier 1 - User scripts

| Script | What it does | When to use it |
|--------|-------------|----------------|
| `run_batch_parallel.py` | Cross-model test runner across supported providers | After meaningful pack changes, for quality signals |
| `compile_designpilot.py` | Rebuilds `dist/` artifacts from `src/` sources | After any edit to `src/` |
| `run_validation_suite.py` | Runs all local validators in sequence | Before packaging or sharing a changed pack |
| `run_regression_suite.py` | Runs the full 45-test static regression suite | After validator, contract, or fixture changes |
| `package_release.py` | Full release gate and package builder | Before tagging or handing off a version |

---

## Tier 2 - Maintenance scripts

| Script | What it does |
|--------|-------------|
| `check_alias_drift.py` | Scans batch outputs for section-name gaps and suggests alias additions |
| `run_cross_model_suite.py` | Single-provider version of the batch runner |
| `run_rubric_eval.py` | Standalone rubric scoring for one output file |
| `run_live_parallel.py` | Claude-only quick regression check |
| `run_live_regression.py` | Live regression against the current deploy |
| `run_comparative.py` | Side-by-side comparison of two outputs |
| `validate_examples.py` | Checks structured examples and runtime overlay assets |
| `validate_integrity_sync.py` | Checks compiled runtime/source/report synchronization |
| `validate_lightweight_path.py` | Validates the lightweight deploy path |
| `validate_project_workspace.py` | Validates project workspace structure and continuity state |
| `validate_release_consistency.py` | Checks pack, proof, handoff, and continuity release-line alignment |
| `generate_missing_reports.py` | Generates missing comparative reports and rebuilds the master summary |
| `archive_batch_runs.py` | Compresses or archives old batch run outputs |
| `generate_human_mirrors.py` | Regenerates human-readable contract mirrors from task contracts |
| `refresh_proof_status.py` | Updates proof status artifacts |
| `refresh_project_continuity.py` | Updates project workspace continuity files |
| `refresh_source_registry.py` | Refreshes the source document registry |
| `clean_distribution_noise.py` | Removes cache and bundle noise artifacts |

---

## Tier 3 - Internal scripts

| Script | Called by |
|--------|----------|
| `runtime_validator.py` | Regression, examples, live, and batch validators |
| `generate_runtime_overlay.py` | `compile_designpilot.py` |
| `generate_integrity_artifacts.py` | `package_release.py` |
| `lint_pack.py` | `run_validation_suite.py`, `package_release.py` |
| `_authority.py` | `_validation.py` |
| `_validation.py` | Validation scripts |

---

## Common workflows

**After editing source files:**
```bash
python3 scripts/compile_designpilot.py
python3 scripts/run_validation_suite.py
python3 scripts/run_regression_suite.py
python3 scripts/validate_release_consistency.py
```

**After a batch run to generate the master summary:**
```bash
python3 scripts/generate_missing_reports.py
```

**To compress old test data:**
```bash
python3 scripts/archive_batch_runs.py --dry-run
python3 scripts/archive_batch_runs.py
```

**To find section alias gaps:**
```bash
python3 scripts/check_alias_drift.py
```
