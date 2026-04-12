# Lightweight Pass Report v2.6.0

## Goal
Productize the lightweight startup path so it becomes a first-class operator mode rather than an improvised runtime-only path.

## Implemented
- Added `dist/DEPLOY_LITE.md`
- Added human-readable route companions in `dist/lite_routes/`
- Added human-readable contract companions in `dist/lite_contracts/`
- Added prebuilt starter packs in `dist/lite_starters/`
- Added `dist/lite_index.json`
- Added operator docs:
  - `docs/operator/STARTUP_MODES.md`
  - `docs/operator/LIGHTWEIGHT_QUICKSTART.md`
  - `docs/operator/ROUTE_PICKER.md`
  - updated `docs/operator/OPERATOR_QUICKSTART.md`
  - updated `docs/operator/PROFILE_GUIDE.md`
- Added `scripts/validate_lightweight_path.py`
- Wired lightweight validation into:
  - `scripts/run_regression_suite.py`
  - `scripts/package_release.py`
- Updated root `README.md` and `AGENTS.md` to expose the three startup modes
- Added lightweight examples in `examples/lightweight/`

## Current lightweight metrics
- `DEPLOY_LITE.md`: 283 words
- Lite route docs: 18
- Lite contract docs: 17
- Lite starter packs: 11

## Validation
- lightweight validation: PASS
- examples: PASS
- lint: PASS
- regression suite: PASS
- workspace validation: PASS
- release packaging: PROMOTE
