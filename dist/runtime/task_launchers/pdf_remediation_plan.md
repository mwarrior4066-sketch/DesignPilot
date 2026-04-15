# LAUNCH_PDF_REMEDIATION_PLAN

Use this as the single-file launcher for **PDF Remediation Plan**.

## Startup path
- Default mode: profile-only or full
- Normal path: load this launcher, then start with `dist/SESSION_ZERO.md`.
- Manual runtime assembly is not needed for normal use.
- Escalate to `dist/DEPLOY_UI.md` if the task stays in one domain but grows beyond a lightweight pass.
- Escalate to `dist/DESIGNPILOT_DEPLOY.md` if multiple domains compete or proof-sensitive conflicts become central.

## Route logic
- Governing route: `rt_pdf_remediation`
- Use when: Prioritize semantic preservation and verification over surface patching.
- Visual input supported: yes
- Known tension: visual fidelity vs semantic repair
- Known tension: speed vs safe preservation
- Escalate when: runtime summary lacks measurable thresholds
- Escalate when: validator flags insufficient evidence
- Escalate when: high-stakes or standards-grade task
- Escalate when: user explicitly requests deeper source synthesis
- Escalate when: route conflict or canonical ambiguity appears
- Fallback route: `rt_ui_structure_critique`

## Included skill logic
- Governing: `document-accessibility-expert.md` - Use this skill to preserve or restore document accessibility: tagging, reading order, artifacts, Unicode mapping, OCR remediation, and extraction fidelity.
- Governing: `pdf-layout-expert.md` - Use this skill to edit, repair, or rebuild PDFs while preserving frame logic, baseline rhythm, visual hierarchy, and layout integrity.
- Optional support: `layout-reconstruction-expert.md` - Use this skill to infer, reconstruct, normalize, and extend existing layouts from screenshots, PDFs, and legacy designs.
- Optional support: `color-system-expert.md` - Use this skill to build or evaluate palettes by semantic role, domain fit, contrast, dark-mode behavior, state logic, data-vis safety, and print awareness.

## Runtime summaries
- `dist/runtime/summaries/pdf-document-accessibility-summary.md`
- `dist/runtime/summaries/pdf-layout-summary.md`
- `dist/runtime/summaries/layout-reconstruction-summary.md`
- `dist/runtime/summaries/color-and-accessibility-summary.md`

## Output expectations
Use these section headings exactly -- matching them enables automated validation:
  ## Current failure state  (Names the real accessibility/document integrity problem.)
  ## Remediation sequence  (Orders the steps so semantics are preserved.)
  ## Verification checks  (Shows how success is confirmed.)
  ## Risk controls  (Prevents destructive edits and copy-paste damage.)

- Required section: Current failure state
- Required section: Remediation sequence
- Required section: Verification checks
- Required section: Risk controls
- Required evidence: tagging rule
- Required evidence: reading-order rule
- Required evidence: verification method
- Required decision: semantic_failure
- Required decision: reading_order_or_extraction
- Required decision: verification_method
- Required decision: destructive_shortcut_rejected
- Hard fail signal: flatten the pdf
- Hard fail signal: rasterize the page
- Hard fail signal: just use OCR only
- Soft fail signal: make it accessible somehow

## Kickoff behavior
- After loading this launcher, start with `dist/SESSION_ZERO.md`.
- Acknowledge the task naturally, frame the job in plain language, and begin useful work as early as possible.
- Ask for only the minimum missing context that would materially change structure, implementation realism, or proof honesty.
- Do not surface route IDs, startup modes, or profile logic unless they materially improve trust or clarity.
- User-facing wording should sound like a capable helper: direct, calm, useful, and not sycophantic.
- Suggested kickoff prompt: I am starting a DesignPilot session for PDF Remediation Plan. Treat this launcher as the governing fit, keep the startup light, and ask only for the missing context that would materially change the answer.
