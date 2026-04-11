# DesignPilot v2.5.0

This repository keeps the README close to the top of the GitHub page by grouping operator authority files under `operator/` and automation under `scripts/`.

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

## Repo map
- `operator/` — startup authority, route docs, governance, and project protocols
- `scripts/` — maintenance, packaging, validation, and continuity automation
- `schemas/` — canonical machine-readable contracts and route maps
- `runtime/` — token-efficient boot aides, cards, and loading metadata
- `examples/` — worked examples that double as trust and regression artifacts
- `tests/` — fixtures, evals, live-eval scaffolding, scorecards, and regression suites
- `projects/` — canonical project workspaces, including `projects/designpilot/`
- `knowledge-base/` — source docs, indices, summaries, and runtime summaries
- `skills/`, `templates/`, `libraries/` — capability, templates, and reference libraries

## Getting started
Read `QUICKSTART.md` first.
Then start from `operator/core/MASTER_CHAT_OPERATOR.md`.

## Release flow
Run these before packaging:
```bash
python3 scripts/generate_runtime_overlay.py
python3 scripts/generate_human_mirrors.py
python3 scripts/refresh_source_registry.py
python3 scripts/refresh_project_continuity.py
python3 scripts/validate_examples.py
python3 scripts/lint_pack.py . --strict
python3 scripts/run_regression_suite.py
python3 scripts/validate_project_workspace.py
python3 scripts/package_release.py
```
