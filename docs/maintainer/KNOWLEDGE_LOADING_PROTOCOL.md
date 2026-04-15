# Knowledge Loading Protocol

Load the minimum necessary material.
Do not flood the context window.

## Runtime-first loading order
1. current user request and uploaded project files
2. `src/runtime/boot/core_bootstrap.md`
3. `src/runtime/boot/runtime_precedence.md`
4. selected route card in `dist/runtime/routes/`
5. selected contract card in `dist/runtime/contracts/`
6. only the required skill cards in `dist/runtime/skills/`
7. only the mapped runtime summaries in `src/knowledge-base/summaries/`
8. canonical summary only on escalation
9. indexed source-doc section only on escalation
10. full source doc only when section-level escalation is insufficient or the task is explicitly high-stakes

## Escalation rules
Escalate from runtime summary to canonical summary when:
- the runtime summary lacks measurable thresholds
- two runtime summaries conflict
- the validator flags missing evidence classes or insufficient evidence
- the user asks for deeper explanation
- the task is high-stakes or standards-grade

Escalate from canonical summary to indexed source-doc section when:
- the answer needs exact operational rules
- the summary lacks source-specific nuance
- a comparison, exception, or standards reference is required
- the task needs section-level evidence, not just a summary restatement

Escalate from indexed source-doc section to full source doc only when:
- the section map is insufficient
- the task is standards-grade
- the user explicitly wants full-source synthesis
- cross-section reasoning is required

## Specialist loading rules
- load `accessibility-and-feedback-summary.md` or its runtime summary before touching state, focus, motion, or touch-target decisions
- load `dashboard-and-density-summary.md` or its runtime summary before touching dashboard hierarchy, charts, or KPI density
- load `layout-reconstruction-summary.md` or its runtime summary before inferring a legacy grid from screenshots or PDFs
- load `document-presentation-architecture-summary.md` or its runtime summary before fixing deck structure, wayfinding, dead zones, or repeated chrome/page-role failures
- load `pdf-document-accessibility-summary.md` or its runtime summary before giving PDF tagging, artifact, or reading-order advice
- load `component-systems-summary.md` or its runtime summary before creating new components or variants
- for typography: runtime summary -> `typography-summary.md` -> `typeface-database-summary.md` -> `FONT_LIBRARY.json` -> `FONT_LIBRARY.md` -> full typography source docs only if deeper rationale, script coverage, or implementation detail is required
- for color: runtime summary -> `color-and-accessibility-summary.md` -> `COLOR_LIBRARY.json` -> `COLOR_LIBRARY.md` -> `accessibility-and-feedback-summary.md` when state logic matters -> `pantone-production-summary.md` only when print-aware -> `PANTONE_LIBRARY.json` -> `PANTONE_LIBRARY.md` -> full color source docs only if thresholds, domain nuance, or print tradeoffs need deeper detail

## Progressive disclosure model
### Level 1 - Runtime cards
Always prefer:
- route card
- contract card
- required skill cards

### Level 2 - Runtime summaries
Load when the governing skills need decision rules, defaults, exceptions, or failure traps.

### Level 3 - Canonical summaries
Load when runtime summaries are insufficient.

### Level 4 - Indexed source sections
Load only the relevant section when the summary still lacks evidence.

### Level 5 - Full source docs
Load only for explicit, high-stakes, or cross-section reasoning tasks.

## Anti-bloat rules
- never load all skills
- never load all summaries
- never load the full source-doc layer by default
- never load a human-readable mirror when schema or runtime card would suffice
- prefer the summary that matches the task, not the newest or longest summary
- if a specialist skill exists, let it own the decision before borrowing adjacent rules
- do not use dashboard rules for generic UI when there is no dashboard
- do not use PDF accessibility rules for regular UI work
- do not use layout reconstruction rules when the user is clearly asking for a new layout, not an inferred one
- load more than 3 skill cards only with an explicit justification note
- for pack-maintenance, evaluation, or hardening tasks: use `validation-and-stress-testing-summary.md` -> `RUNTIME_VALIDATION_LAYER.md` -> `FORMAL_STRESS_TEST_SUITE.md` -> `AI Operator Pack Validation & Stress Testing.md`

## Project operations
Project filesystem and logging protocols are lightweight control files. Load them only when project-state persistence or filesystem organization is relevant.
