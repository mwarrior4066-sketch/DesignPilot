# Tests

This directory contains static regression fixtures, golden outputs, eval artifacts, scorecards, and live-eval scaffolding.

## Layers
- `fixtures/` prompt inputs
- `golden_outputs/` known pass/fail outputs used to test validator behavior
- `evals/` stored evaluation artifacts
- `scorecards/` rubric definitions
- `live_outputs/` raw live model responses scored by the validator
- `live_evals/` blinded comparative run storage

## Static versus live
- `scripts/run_regression_suite.py` validates the validator and file-backed regression fixtures.
- `scripts/run_live_regression.py` runs the pack against a real model and scores the actual output.
- `scripts/run_comparative.py` runs pack versus baseline and stores blinded comparative records in `live_evals/`.

## v3.0 additions
- realistic `full_prompt` fields in `tests/regression_suite.json`
- live-only suite flags so static fail fixtures are not mistaken for pack-release prompts
- generated storage for live outputs under `tests/live_outputs/` and archived reports under `tests/reports/v2-tests/`
