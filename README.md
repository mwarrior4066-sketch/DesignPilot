# Design Expert Pack v2.5.0

This release revises the v2.4.2 runtime-overlay system so it is faster, less over-scaffolded, safer under partial loads, and more credible when working from screenshots or other visual inputs.

## What is new in v2.5.0
- made `MASTER_CHAT_OPERATOR.md` the only canonical startup authority
- moved `SYSTEM_PRECEDENCE.md` back to conflict resolution only
- added `DEGRADED_MODE_PROTOCOL.md` with explicit partial-load behavior and stop conditions
- replaced mandatory visible trace with a trace-visibility policy that defaults to recoverable trace
- added `VISUAL_INPUT_PROTOCOL.md` plus visual pre-pass metadata for screenshot- and mockup-led tasks
- added `LIGHTWEIGHT_RESPONSE_PROTOCOL.md` so small asks do not pay the full runtime overhead tax
- hardened `runtime_validator.py` against hollow compliance, fake tradeoffs, and overconfident visual claims
- added `QUICKSTART.md` and live-eval scaffolding

## Core directories
- `schemas/` — canonical machine-readable contracts and route maps
- `runtime/` — token-efficient boot aides, cards, and loading metadata
- `examples/` — worked examples that double as trust and regression artifacts
- `tests/fixtures/` — prompt and artifact fixtures
- `tests/scorecards/` — rubric definitions
- `tests/live_evals/` — blinded comparative evaluation scaffolding
- `tests/evals/` — stored evaluation results and benchmark traces
- `projects/` — canonical project workspaces

## Getting started
Read `QUICKSTART.md` first.
Then start from `MASTER_CHAT_OPERATOR.md`.

## Release flow
Run these before packaging:
```bash
python3 generate_runtime_overlay.py
python3 generate_human_mirrors.py
python3 refresh_source_registry.py
python3 refresh_project_continuity.py
python3 validate_examples.py
python3 lint_pack.py . --strict
python3 run_regression_suite.py
python3 validate_project_workspace.py
python3 package_release.py
```
