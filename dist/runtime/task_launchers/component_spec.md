# LAUNCH_COMPONENT_SPEC

Use this as the single-file launcher for **Component Specification**.

## Startup path
- Default mode: lightweight
- Normal path: load this launcher, then start with `dist/SESSION_ZERO.md`.
- Manual runtime assembly is not needed for normal use.
- Escalate to `dist/DEPLOY_UI.md` if the task stays in one domain but grows beyond a lightweight pass.
- Escalate to `dist/DESIGNPILOT_DEPLOY.md` if multiple domains compete or proof-sensitive conflicts become central.

## Route logic
- Governing route: `rt_component_spec`
- Use when: Use when a reusable system component needs state-safe documentation.
- Visual input supported: no
- Known tension: flexibility vs implementation simplicity
- Known tension: expressiveness vs token consistency
- Escalate when: runtime summary lacks measurable thresholds
- Escalate when: validator flags insufficient evidence
- Escalate when: high-stakes or standards-grade task
- Escalate when: user explicitly requests deeper source synthesis
- Escalate when: route conflict or canonical ambiguity appears
- Fallback route: `rt_ui_structure_critique`

## Included skill logic
- Governing: `component-systems-expert.md` - Use this skill to decide whether a component should exist, how it should be documented, what variants and states it needs, and how reuse beats drift.
- Governing: `front-end-handoff-expert.md` - Use this skill as the gateway that translates design decisions into implementation-safe front-end structure without losing tokens, states, accessibility, typography behavior, or system coherence. It is not the owner of deep front-end architecture decisions.
- Optional support: `accessibility-feedback-expert.md` - Use this skill to make production-level decisions about behavior-first accessibility: focus architecture, keyboard rules, widget interaction contracts, hover/focus parity, touch targets, live regions, motion safety, async feedback, and state visibility.
- Optional support: `color-system-expert.md` - Use this skill to build or evaluate palettes by semantic role, domain fit, contrast, dark-mode behavior, state logic, data-vis safety, and print awareness.

## Runtime summaries
- `dist/runtime/summaries/component-systems-summary.md`
- `dist/runtime/summaries/front-end-handoff-summary.md`
- `dist/runtime/summaries/front-end-architecture-summary.md`
- `dist/runtime/summaries/accessibility-and-feedback-summary.md`
- `dist/runtime/summaries/color-and-accessibility-summary.md`

## Output expectations
Use these section headings exactly -- matching them enables automated validation:
  ## Purpose and scope  (Defines when the component exists and where it stops.)
  ## Anatomy  (Names the governed parts.)
  ## State matrix  (Shows interaction and edge states.)
  ## Accessibility and implementation notes  (Prevents front-end drift.)

- Required section: Purpose and scope
- Required section: Anatomy
- Required section: State matrix
- Required section: Accessibility and implementation notes
- Required evidence: state rule
- Required evidence: aria or keyboard rule
- Required evidence: implementation boundary
- Required decision: component_boundary
- Required decision: state_coverage
- Required decision: accessibility_behavior
- Required decision: implementation_boundary
- Hard fail signal: states TBD
- Hard fail signal: accessibility later
- Soft fail signal: basic component
- Soft fail signal: simple usage

## Kickoff behavior
- After loading this launcher, start with `dist/SESSION_ZERO.md`.
- Acknowledge the task naturally, frame the job in plain language, and begin useful work as early as possible.
- Ask for only the minimum missing context that would materially change structure, implementation realism, or proof honesty.
- Do not surface route IDs, startup modes, or profile logic unless they materially improve trust or clarity.
- User-facing wording should sound like a capable helper: direct, calm, useful, and not sycophantic.
- Suggested kickoff prompt: I am starting a DesignPilot session for Component Specification. Treat this launcher as the governing fit, keep the startup light, and ask only for the missing context that would materially change the answer.
