# Knowledge Loading Protocol

Load the minimum necessary material.
Do not flood the context window.

## Default loading order
1. current user request and uploaded project files
2. active mode and phase
3. mapped summary files
4. mapped skill files
5. libraries when a lookup or fallback is needed
6. source docs only when summaries are insufficient or the task is high-stakes

## Escalation rules
Escalate from summary to source doc when:
- the task is high-stakes
- the summary lacks measurable thresholds
- two summaries conflict
- the answer requires exact operational rules
- the answer needs document-specific or source-specific nuance
- the answer needs a full comparison database, licensing nuance, or standards-grade wording

## Specialist loading rules
- load `accessibility-and-feedback-summary.md` before touching state, focus, motion, or touch-target decisions
- load `dashboard-and-density-summary.md` before touching dashboard hierarchy, charts, or KPI density
- load `layout-reconstruction-summary.md` before inferring a legacy grid from screenshots or PDFs
- load `pdf-document-accessibility-summary.md` before giving PDF tagging, artifact, or reading-order advice
- load `component-systems-summary.md` before creating new components or variants
- for typography: use `typography-summary.md` -> `typeface-database-summary.md` -> `FONT_LIBRARY.json` -> `FONT_LIBRARY.md` -> full typeface database doc
- for color: use `color-and-accessibility-summary.md` -> `pantone-production-summary.md` when print-aware -> `accessibility-and-feedback-summary.md` when state logic matters -> `PANTONE_LIBRARY.json` for fast structured print-color selection -> `PANTONE_LIBRARY.md` for caveats and examples -> full color research doc or Pantone production source doc if thresholds or print tradeoffs need deeper detail

## Progressive disclosure model
### Level 1 — Metadata
Always available:
- task type
- active mode
- active phase
- active skill names

### Level 2 — Instructions
Load when a skill is active:
- decision rules
- defaults
- exceptions
- failure traps
- evidence requirements

### Level 3 — Resources
Load on demand:
- libraries
- templates
- source docs
- dense research summaries

## Anti-bloat rules
- never load all skills
- never load all summaries
- never load the full source-doc layer by default
- prefer the summary that matches the task, not the newest or longest summary
- if a specialist skill exists, let it own the decision before borrowing adjacent rules
- do not use dashboard rules for generic UI when there is no dashboard
- do not use PDF accessibility rules for regular UI work
- do not use layout reconstruction rules when the user is clearly asking for a new layout, not an inferred one
- for pack-maintenance, evaluation, or hardening tasks: use `validation-and-stress-testing-summary.md` -> `RUNTIME_VALIDATION_LAYER.md` -> `FORMAL_STRESS_TEST_SUITE.md` -> `AI Operator Pack Validation & Stress Testing.md`
