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
- Default contract: `dist/lite_contracts/pdf_remediation_plan.md`
- Recommended profile if you escalate: `dist/DEPLOY_UI.md`
- Visual input supported: yes

## Governing skills
- `src/runtime/cards/skills/document-accessibility-expert.md` — Use this skill to preserve or restore document accessibility: tagging, reading order, artifacts, Unicode mapping, OCR remediation, and extraction fidelity.
- `src/runtime/cards/skills/pdf-layout-expert.md` — Use this skill to edit, repair, or rebuild PDFs while preserving frame logic, baseline rhythm, visual hierarchy, and layout integrity.

## Optional supporting skills
- `src/runtime/cards/skills/layout-reconstruction-expert.md` — Use this skill to infer, reconstruct, normalize, and extend existing layouts from screenshots, PDFs, and legacy designs.
- `src/runtime/cards/skills/color-system-expert.md` — Use this skill to build or evaluate palettes by semantic role, domain fit, contrast, dark-mode behavior, state logic, data-vis safety, and print awareness.

## Runtime summaries
- `src/knowledge-base/runtime-summaries/pdf-document-accessibility-summary.md`
- `src/knowledge-base/runtime-summaries/pdf-layout-summary.md`
- `src/knowledge-base/runtime-summaries/layout-reconstruction-summary.md`
- `src/knowledge-base/runtime-summaries/color-and-accessibility-summary.md`

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
