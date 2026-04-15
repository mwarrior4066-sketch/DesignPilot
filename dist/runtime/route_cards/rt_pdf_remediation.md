# rt_pdf_remediation

**Task:** PDF Remediation Plan

## Route fit
- Role: governing
- Lightweight eligible: no
- Governing route or helper: governing route

## Use when
- Prioritize semantic preservation and verification over surface patching.

## Startup recommendation
- Recommended mode: profile or full
- Default contract: `dist/runtime/contracts_lite/pdf_remediation_plan.md`
- Recommended profile if you escalate: `dist/DEPLOY_UI.md`
- Visual input supported: yes

## Governing skills
- `dist/runtime/skills/document-accessibility-expert.md` - Use this skill to preserve or restore document accessibility: tagging, reading order, artifacts, Unicode mapping, OCR remediation, and extraction fidelity.
- `dist/runtime/skills/pdf-layout-expert.md` - Use this skill to edit, repair, or rebuild PDFs while preserving frame logic, baseline rhythm, visual hierarchy, and layout integrity.

## Optional supporting skills
- `dist/runtime/skills/layout-reconstruction-expert.md` - Use this skill to infer, reconstruct, normalize, and extend existing layouts from screenshots, PDFs, and legacy designs.
- `dist/runtime/skills/color-system-expert.md` - Use this skill to build or evaluate palettes by semantic role, domain fit, contrast, dark-mode behavior, state logic, data-vis safety, and print awareness.

## Runtime summaries
- `dist/runtime/summaries/pdf-document-accessibility-summary.md`
- `dist/runtime/summaries/pdf-layout-summary.md`
- `dist/runtime/summaries/layout-reconstruction-summary.md`
- `dist/runtime/summaries/color-and-accessibility-summary.md`

## Contract shape
- Current failure state
- Remediation sequence
- Verification checks
- Risk controls

## Escalate when
- runtime summary lacks measurable thresholds
- validator flags insufficient evidence
- high-stakes or standards-grade task
- user explicitly requests deeper source synthesis
- route conflict or canonical ambiguity appears

## Fallback
- Route fallback: `rt_ui_structure_critique`
- Canonical routing fallback: `src/schemas/routing_registry.json`
