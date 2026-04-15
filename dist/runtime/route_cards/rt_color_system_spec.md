# rt_color_system_spec

**Task:** Color System Specification

## Route fit
- Role: governing
- Lightweight eligible: yes
- Governing route or helper: governing route

## Use when
- Use when the job is to define roles, tokens, and state behavior for color rather than pick nicer hues.

## Startup recommendation
- Recommended mode: lightweight
- Default contract: `dist/runtime/contracts_lite/color_system_spec.md`
- Recommended profile if you escalate: `dist/DEPLOY_UI.md`
- Visual input supported: no

## Governing skills
- `dist/runtime/skills/color-system-expert.md` - Use this skill to build or evaluate palettes by semantic role, domain fit, contrast, dark-mode behavior, state logic, data-vis safety, and print awareness.
- `dist/runtime/skills/accessibility-feedback-expert.md` - Use this skill to make production-level decisions about behavior-first accessibility: focus architecture, keyboard rules, widget interaction contracts, hover/focus parity, touch targets, live regions, motion safety, async feedback, and state visibility.

## Optional supporting skills
- `dist/runtime/skills/component-systems-expert.md` - Use this skill to decide whether a component should exist, how it should be documented, what variants and states it needs, and how reuse beats drift.
- `dist/runtime/skills/brand-strategy-expert.md` - Use this skill to make strict positioning, audience-fit, trust-signal, convention, and brand-vs-interface decisions. Treat brand work as a system of falsifiable hypotheses, not a moodboard.

## Runtime summaries
- `dist/runtime/summaries/color-and-accessibility-summary.md`
- `dist/runtime/summaries/accessibility-and-feedback-summary.md`
- `dist/runtime/summaries/component-systems-summary.md`
- `dist/runtime/summaries/audience-and-industry-summary.md`

## Contract shape
- Role model
- Token map
- Contrast and state rules
- Migration notes

## Escalate when
- runtime summary lacks measurable thresholds
- validator flags insufficient evidence
- high-stakes or standards-grade task
- user explicitly requests deeper source synthesis
- route conflict or canonical ambiguity appears

## Fallback
- Route fallback: `rt_component_spec`
- Canonical routing fallback: `src/schemas/routing_registry.json`
