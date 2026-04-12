# rt_layout_reconstruction_plan

**Task:** Layout Reconstruction Plan

## Route fit
- Role: governing
- Lightweight eligible: no
- Governing route or helper: governing route

## Use when
- Use when structure must be inferred from an existing artifact instead of redesigned from scratch.

## Startup recommendation
- Recommended mode: profile or full
- Default contract: `dist/lite_contracts/layout_reconstruction_plan.md`
- Recommended profile if you escalate: `dist/DEPLOY_UI.md`
- Visual input supported: yes

## Governing skills
- `src/runtime/cards/skills/layout-reconstruction-expert.md` — Use this skill to infer, reconstruct, normalize, and extend existing layouts from screenshots, PDFs, and legacy designs.
- `src/runtime/cards/skills/grid-system-expert.md` — Use this skill to choose new grid systems by medium and content type: web, app, slide, editorial, dashboard, and document layouts.

## Optional supporting skills
- `src/runtime/cards/skills/pdf-layout-expert.md` — Use this skill to edit, repair, or rebuild PDFs while preserving frame logic, baseline rhythm, visual hierarchy, and layout integrity.
- `src/runtime/cards/skills/document-accessibility-expert.md` — Use this skill to preserve or restore document accessibility: tagging, reading order, artifacts, Unicode mapping, OCR remediation, and extraction fidelity.

## Runtime summaries
- `src/knowledge-base/runtime-summaries/layout-reconstruction-summary.md`
- `src/knowledge-base/runtime-summaries/grid-mediums-summary.md`
- `src/knowledge-base/runtime-summaries/pdf-layout-summary.md`
- `src/knowledge-base/runtime-summaries/pdf-document-accessibility-summary.md`

## Contract shape
- Source constraints
- Reconstruction assumptions
- Rebuild sequence
- Verification checkpoints

## Escalate when
- runtime summary lacks measurable thresholds
- validator flags insufficient evidence
- high-stakes or standards-grade task
- user explicitly requests deeper source synthesis
- route conflict or canonical ambiguity appears

## Fallback
- Route fallback: `rt_pdf_remediation`
- Canonical routing fallback: `src/schemas/routing_registry.json`
