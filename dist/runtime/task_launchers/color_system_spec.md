# LAUNCH_COLOR_SYSTEM_SPEC

Use this as the single-file launcher for **Color System Specification**.

## Startup path
- Default mode: lightweight
- Normal path: load this launcher, then start with `dist/SESSION_ZERO.md`.
- Manual runtime assembly is not needed for normal use.
- Escalate to `dist/DEPLOY_UI.md` if the task stays in one domain but grows beyond a lightweight pass.
- Escalate to `dist/DESIGNPILOT_DEPLOY.md` if multiple domains compete or proof-sensitive conflicts become central.

## Route logic
- Governing route: `rt_color_system_spec`
- Use when: Use when the job is to define roles, tokens, and state behavior for color rather than pick nicer hues.
- Visual input supported: no
- Known tension: brand expression vs semantic clarity
- Known tension: vividness vs contrast safety
- Escalate when: runtime summary lacks measurable thresholds
- Escalate when: validator flags insufficient evidence
- Escalate when: high-stakes or standards-grade task
- Escalate when: user explicitly requests deeper source synthesis
- Escalate when: route conflict or canonical ambiguity appears
- Fallback route: `rt_component_spec`

## Included skill logic
- Governing: `color-system-expert.md` - Use this skill to build or evaluate palettes by semantic role, domain fit, contrast, dark-mode behavior, state logic, data-vis safety, and print awareness.
- Governing: `accessibility-feedback-expert.md` - Use this skill to make production-level decisions about behavior-first accessibility: focus architecture, keyboard rules, widget interaction contracts, hover/focus parity, touch targets, live regions, motion safety, async feedback, and state visibility.
- Optional support: `component-systems-expert.md` - Use this skill to decide whether a component should exist, how it should be documented, what variants and states it needs, and how reuse beats drift.
- Optional support: `brand-strategy-expert.md` - Use this skill to make strict positioning, audience-fit, trust-signal, convention, and brand-vs-interface decisions. Treat brand work as a system of falsifiable hypotheses, not a moodboard.

## Runtime summaries
- `dist/runtime/summaries/color-and-accessibility-summary.md`
- `dist/runtime/summaries/accessibility-and-feedback-summary.md`
- `dist/runtime/summaries/component-systems-summary.md`
- `dist/runtime/summaries/audience-and-industry-summary.md`

## Output expectations
Use these section headings exactly -- matching them enables automated validation:
  ## Role model  (Defines semantic color roles instead of a loose palette.)
  ## Token map  (Maps roles to tokens, aliases, or state usage.)
  ## Contrast and state rules  (Prevents color-only semantics and contrast drift.)
  ## Migration notes  (Shows how to move from the current palette safely.)

- Required section: Role model
- Required section: Token map
- Required section: Contrast and state rules
- Required section: Migration notes
- Required evidence: semantic role
- Required evidence: contrast threshold
- Required evidence: state rule
- Required decision: semantic_roles
- Required decision: state_mapping
- Required decision: contrast_boundary
- Required decision: migration_strategy
- Hard fail signal: pick nicer colors
- Hard fail signal: brand color everywhere
- Hard fail signal: palette only
- Soft fail signal: could feel fresher
- Soft fail signal: more vibrant maybe

## Kickoff behavior
- After loading this launcher, start with `dist/SESSION_ZERO.md`.
- Acknowledge the task naturally, frame the job in plain language, and begin useful work as early as possible.
- Ask for only the minimum missing context that would materially change structure, implementation realism, or proof honesty.
- Do not surface route IDs, startup modes, or profile logic unless they materially improve trust or clarity.
- User-facing wording should sound like a capable helper: direct, calm, useful, and not sycophantic.
- Suggested kickoff prompt: I am starting a DesignPilot session for Color System Specification. Treat this launcher as the governing fit, keep the startup light, and ask only for the missing context that would materially change the answer.
