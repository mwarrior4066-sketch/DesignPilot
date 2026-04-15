# Maintainer Guide

## Core maintainer loop
Before changing surfaces, resolve ownership in `config/authority_manifest.yaml` and `src/operator/governance/CONTROL_AUTHORITY_MAP.md`.

1. edit or add source modules in `src/`
2. update `config/deploy_manifest.yaml` or `config/profile_map.yaml` if profile membership changes
3. run `python3 scripts/compile_designpilot.py`
4. run runtime and mirror generation
5. run lint and regression validation
6. package the release

Do not hand-edit files in `dist/` except for debugging. Regenerate them from source.

## Validation defaults
- `python3 scripts/run_validation_suite.py` is the authoritative default maintainer validation pass and now includes integrity sync by default.
- Use `python3 scripts/run_validation_suite.py --fast` only for intentionally shortened local checks.
- Run `python3 scripts/package_release.py` for the full release-authority pipeline.
- Use `python3 scripts/clean_distribution_noise.py --version <pack-version>` to remove cache artifacts and stale release attempt files before debugging integrity problems.
