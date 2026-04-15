# LAUNCH_LAYOUT_RECONSTRUCTION_PLAN

Use this as the single-file launcher for **Layout Reconstruction Plan**.

## Startup path
- Default mode: profile-only or full
- Normal path: load this launcher, then start with `dist/SESSION_ZERO.md`.
- Manual runtime assembly is not needed for normal use.
- Escalate to `dist/DEPLOY_UI.md` if the task stays in one domain but grows beyond a lightweight pass.
- Escalate to `dist/DESIGNPILOT_DEPLOY.md` if multiple domains compete or proof-sensitive conflicts become central.

## Route logic
- Governing route: `rt_layout_reconstruction_plan`
- Use when: Use when structure must be inferred from an existing artifact instead of redesigned from scratch.
- Visual input supported: yes
- Known tension: exact preservation vs practical reconstruction
- Known tension: speed vs verification rigor
- Escalate when: runtime summary lacks measurable thresholds
- Escalate when: validator flags insufficient evidence
- Escalate when: high-stakes or standards-grade task
- Escalate when: user explicitly requests deeper source synthesis
- Escalate when: route conflict or canonical ambiguity appears
- Fallback route: `rt_pdf_remediation`

## Included skill logic
- Governing: `layout-reconstruction-expert.md` - Use this skill to infer, reconstruct, normalize, and extend existing layouts from screenshots, PDFs, and legacy designs.
- Governing: `grid-system-expert.md` - Use this skill to choose new grid systems by medium and content type: web, app, slide, editorial, dashboard, and document layouts.
- Optional support: `pdf-layout-expert.md` - Use this skill to edit, repair, or rebuild PDFs while preserving frame logic, baseline rhythm, visual hierarchy, and layout integrity.
- Optional support: `document-accessibility-expert.md` - Use this skill to preserve or restore document accessibility: tagging, reading order, artifacts, Unicode mapping, OCR remediation, and extraction fidelity.

## Runtime summaries
- `dist/runtime/summaries/layout-reconstruction-summary.md`
- `dist/runtime/summaries/grid-mediums-summary.md`
- `dist/runtime/summaries/pdf-layout-summary.md`
- `dist/runtime/summaries/pdf-document-accessibility-summary.md`

## Output expectations
Use these section headings exactly -- matching them enables automated validation:
  ## Source constraints  (Defines what must be preserved from the source artifact.)
  ## Reconstruction assumptions  (Makes inferred structure explicit instead of pretending certainty.)
  ## Rebuild sequence  (Shows the ordered reconstruction plan.)
  ## Verification checkpoints  (Protects against drift and silent geometry errors.)

- Required section: Source constraints
- Required section: Reconstruction assumptions
- Required section: Rebuild sequence
- Required section: Verification checkpoints
- Required evidence: grid inference
- Required evidence: preservation boundary
- Required evidence: verification checkpoint
- Required decision: preserved_elements
- Required decision: inference_boundary
- Required decision: reconstruction_order
- Required decision: verification_method
- Required decision: visual_confidence_boundary
- Hard fail signal: redraw it from scratch
- Hard fail signal: eyeball the spacing
- Hard fail signal: just clean it up
- Soft fail signal: approximate it
- Soft fail signal: close enough

## Kickoff behavior
- After loading this launcher, start with `dist/SESSION_ZERO.md`.
- Acknowledge the task naturally, frame the job in plain language, and begin useful work as early as possible.
- Ask for only the minimum missing context that would materially change structure, implementation realism, or proof honesty.
- Do not surface route IDs, startup modes, or profile logic unless they materially improve trust or clarity.
- User-facing wording should sound like a capable helper: direct, calm, useful, and not sycophantic.
- Suggested kickoff prompt: I am starting a DesignPilot session for Layout Reconstruction Plan. Treat this launcher as the governing fit, keep the startup light, and ask only for the missing context that would materially change the answer.
