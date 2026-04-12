# Maintainer Guide

## Core maintainer loop
1. edit or add source modules in `src/`
2. update `config/deploy_manifest.yaml` or `config/profile_map.yaml` if profile membership changes
3. run `python3 scripts/compile_designpilot.py`
4. run runtime and mirror generation
5. run lint and regression validation
6. package the release

Do not hand-edit files in `dist/` except for debugging. Regenerate them from source.
