# DesignPilot Integrity Pass Handoff

Current release line: v3.0.

This bundle is the integrity-hardened DesignPilot release for v3.0.

Use `HANDOFF_MANIFEST.json` for key artifact verification. Its `full_build_manifest` field points to `dist/manifest.json` for compiled bundle verification.

Primary operator files:
- `dist/runtime/START_HERE.md`
- `dist/runtime/TASK_CHOOSER.md`
- `dist/DEPLOY_LITE.md`
- `docs/operator/DEPLOYMENT_GUIDE.md`

Credibility files:
- `proof/PROOF_STATUS.md`
- `proof/benchmarks/README.md`
- `proof/reviews/README.md`
- `proof/receipts/README.md`

Validation files:
- `dist/lightweight_validation_report.json`
- `dist/integrity_validation_report.json`
- `dist/validation_suite_report.json`
- `dist/release_consistency_report.json`
- `dist/build_metrics.json`
- `dist/manifest.json`
