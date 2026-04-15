# Surface Boundaries

## Operator surface
- `dist/DESIGNPILOT_DEPLOY.md`
- one profile file from `dist/`
- `dist/SESSION_ZERO.md`
- `docs/operator/OPERATOR_QUICKSTART.md`
- `docs/operator/PROFILE_GUIDE.md`

## Maintainer surface
- `config/authority_manifest.yaml`
- `src/`
- `config/`
- `scripts/`
- `tests/`
- `evals/`
- `proof/`
- `docs/maintainer/`

The operator should not need to understand tiered hydration or source dependencies to deploy DesignPilot correctly.

## Ownership rule
Generated files in `dist/`, handoff manifests, and proof artifact receipts should be regenerated from source and scripts, not manually patched.
