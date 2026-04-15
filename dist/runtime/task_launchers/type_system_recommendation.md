# LAUNCH_TYPE_SYSTEM_RECOMMENDATION

Use this as the single-file launcher for **Type System Recommendation**.

## Startup path
- Default mode: lightweight
- Normal path: load this launcher, then start with `dist/SESSION_ZERO.md`.
- Manual runtime assembly is not needed for normal use.
- Escalate to `dist/DEPLOY_UI.md` if the task stays in one domain but grows beyond a lightweight pass.
- Escalate to `dist/DESIGNPILOT_DEPLOY.md` if multiple domains compete or proof-sensitive conflicts become central.

## Route logic
- Governing route: `rt_type_system_recommendation`
- Use when: Use when the job is to define a repeatable type system instead of suggest a single font.
- Visual input supported: no
- Known tension: brand personality vs reading efficiency
- Known tension: density vs legibility
- Escalate when: runtime summary lacks measurable thresholds
- Escalate when: validator flags insufficient evidence
- Escalate when: high-stakes or standards-grade task
- Escalate when: user explicitly requests deeper source synthesis
- Escalate when: route conflict or canonical ambiguity appears
- Fallback route: `rt_ui_structure_critique`

## Included skill logic
- Governing: `type-system-expert.md` - Use this skill to choose, compare, pair, substitute, and deploy typefaces intelligently across UI, editorial, brand, dashboards, presentations, print, accessibility-sensitive, and multilingual systems.
- Governing: `accessibility-feedback-expert.md` - Use this skill to make production-level decisions about behavior-first accessibility: focus architecture, keyboard rules, widget interaction contracts, hover/focus parity, touch targets, live regions, motion safety, async feedback, and state visibility.
- Optional support: `graphic-design-expert.md` - Use this skill for posters, campaigns, editorial composition, presentation slides, image/text balance, visual hierarchy, and distance-driven communication when the output is more graphic-communication-driven than product-UI-driven.
- Optional support: `ui-system-expert.md` - Use this skill to organize screens, flows, navigation, information architecture, and action hierarchy into a coherent interface system.

## Runtime summaries
- `dist/runtime/summaries/typography-summary.md`
- `dist/runtime/summaries/typeface-database-summary.md`
- `dist/runtime/summaries/accessibility-and-feedback-summary.md`
- `dist/runtime/summaries/graphic-design-format-summary.md`
- `dist/runtime/summaries/ui-system-summary.md`

## Output expectations
Use these section headings exactly -- matching them enables automated validation:
  ## Reading context  (Defines where the type system will be read and at what density.)
  ## Scale and role map  (Maps text roles to scale, weight, and hierarchy rules.)
  ## Readability rules  (Names line length, contrast, spacing, or emphasis boundaries.)
  ## Adoption guidance  (Shows how to phase the new type system into the artifact.)

- Required section: Reading context
- Required section: Scale and role map
- Required section: Readability rules
- Required section: Adoption guidance
- Required evidence: readability rule
- Required evidence: role map
- Required evidence: adoption boundary
- Required decision: reading_context
- Required decision: role_hierarchy
- Required decision: readability_boundary
- Required decision: adoption_sequence
- Hard fail signal: use inter at 12px
- Hard fail signal: just tighten tracking
- Hard fail signal: pick a nicer font
- Soft fail signal: feels too loose
- Soft fail signal: could be sharper

## Kickoff behavior
- After loading this launcher, start with `dist/SESSION_ZERO.md`.
- Acknowledge the task naturally, frame the job in plain language, and begin useful work as early as possible.
- Ask for only the minimum missing context that would materially change structure, implementation realism, or proof honesty.
- Do not surface route IDs, startup modes, or profile logic unless they materially improve trust or clarity.
- User-facing wording should sound like a capable helper: direct, calm, useful, and not sycophantic.
- Suggested kickoff prompt: I am starting a DesignPilot session for Type System Recommendation. Treat this launcher as the governing fit, keep the startup light, and ask only for the missing context that would materially change the answer.
