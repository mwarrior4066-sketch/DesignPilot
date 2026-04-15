# Receipts

This layer covers **downstream artifact receipt proof**.
It shows what the repo actually compiled, validated, packaged, and handed off.

## Canonical sources
- release reports: `dist/release_quality_report_v3.0.json`
- validation suite outputs: `dist/validation_suite_report.json` and related reports in `dist/`
- integrity receipts: `proof/artifacts/`
- handoff manifests: `HANDOFF_MANIFEST.json`, `HANDOFF_README.md`
- build manifests: `dist/build_metrics.json`, `dist/manifest.json`

## Interpretation rule
Use this layer to verify what shipped and what checks passed.
Do **not** treat build receipts as proof of downstream product success.
