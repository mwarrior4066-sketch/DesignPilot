# Compiler Guide

`compile_designpilot.py` is the first source-to-artifact compiler for DesignPilot.

## Outputs
- `dist/DESIGNPILOT_DEPLOY.md`
- `dist/DEPLOY_CORE.md`
- `dist/DEPLOY_UI.md`
- `dist/DEPLOY_BRAND.md`
- `dist/SESSION_ZERO.md`
- `dist/manifest.json`
- `dist/tier_profile.yaml`
- `dist/validation_report.json`

This release implements the kernel-plus-profile model. It does not yet perform fully dynamic on-demand retrieval.
