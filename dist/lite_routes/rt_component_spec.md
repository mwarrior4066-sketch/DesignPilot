# rt_component_spec

**Task:** Component Specification

## Route fit
- Role: governing
- Lightweight eligible: yes
- Governing route or helper: governing route

## Use when
- Use when a reusable system component needs state-safe documentation.

## Startup recommendation
- Recommended mode: lightweight
- Default contract: `dist/lite_contracts/component_spec.md`
- Recommended profile if you escalate: `dist/DEPLOY_UI.md`
- Visual input supported: no

## Governing skills
- `src/runtime/cards/skills/component-systems-expert.md` — Use this skill to decide whether a component should exist, how it should be documented, what variants and states it needs, and how reuse beats drift.
- `src/runtime/cards/skills/front-end-handoff-expert.md` — Use this skill as the gateway that translates design decisions into implementation-safe front-end structure without losing tokens, states, accessibility, typography behavior, or system coherence. It is not the owner of deep front-end architecture decisions.

## Optional supporting skills
- `src/runtime/cards/skills/accessibility-feedback-expert.md` — Use this skill to make production-level decisions about behavior-first accessibility: focus architecture, keyboard rules, widget interaction contracts, hover/focus parity, touch targets, live regions, motion safety, async feedback, and state visibility.
- `src/runtime/cards/skills/color-system-expert.md` — Use this skill to build or evaluate palettes by semantic role, domain fit, contrast, dark-mode behavior, state logic, data-vis safety, and print awareness.

## Runtime summaries
- `src/knowledge-base/runtime-summaries/component-systems-summary.md`
- `src/knowledge-base/runtime-summaries/front-end-handoff-summary.md`
- `src/knowledge-base/runtime-summaries/front-end-architecture-summary.md`
- `src/knowledge-base/runtime-summaries/accessibility-and-feedback-summary.md`
- `src/knowledge-base/runtime-summaries/color-and-accessibility-summary.md`

## Contract shape
- Purpose and scope
- Anatomy
- State matrix
- Accessibility and implementation notes

## Escalate when
- runtime summary lacks measurable thresholds
- validator flags insufficient evidence
- high-stakes or standards-grade task
- user explicitly requests deeper source synthesis
- route conflict or canonical ambiguity appears

## Fallback
- Route fallback: `rt_ui_structure_critique`
- Canonical routing fallback: `src/schemas/routing_registry.json`
