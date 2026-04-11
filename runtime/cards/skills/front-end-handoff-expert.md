---
runtime_card_version: 1.0.0
canonical_skill: skills/front-end-handoff-expert.md
last_generated: 2026-04-11
overlay: true
---
# front-end-handoff-expert.md

## Activation conditions
- the task involves React, Next.js, Tailwind, components, tokens, semantic HTML, webfont loading, or design-to-code translation
- the answer must be implementation-aware rather than purely visual
- the architecture is already known or can be kept shallow enough for safe handoff
- the core problem is rendering strategy, state ownership, or server/client boundary placement
- the system is still undefined and only strategy is needed
- the task is only a high-level identity discussion with no code implication

## Non-activation conditions
- the core problem is rendering strategy, state ownership, or server/client boundary placement
- the system is still undefined and only strategy is needed
- the task is only a high-level identity discussion with no code implication

## Core decision rules
- semantics before styling
- token usage before hard-coded values
- component boundaries before page-wide hacks
- accessibility behavior before polish
- implementation-safe font loading before typographic romance
- architecture escalation before false certainty

## Failure traps
- styling before semantics
- missing states
- hard-coded colors or spacing where tokens are clearly needed
- inaccessible interactivity
- visually accurate but structurally brittle code
- pretending gateway handoff solved architecture ownership questions

## Summary dependencies
- front-end-handoff-summary.md
- front-end-architecture-summary.md

## Escalation triggers
- local demo code can be simpler if it does not misrepresent system behavior
- if framework detail is unknown and risk is low, provide framework-agnostic structure first
- if the requested font is not deployable, propose a named substitute or system stack
- if a semantic token is missing, define the alias before using a raw primitive
- if a palette decision is still unresolved, pull semantic roles from `COLOR_LIBRARY` before hard-coding hue values
- if hover is irrelevant on touch, prioritize focus, pressed, and visible feedback
- if a variable font is unavailable, fall back to discrete weights and keep the stack explicit
- if the task includes rendering, hydration, or state-architecture risk, hand off to `front-end-architecture-expert.md`

## Adjacent handoff rules
- hand off to `front-end-architecture-expert.md` when rendering strategy, state ownership, or boundary placement dominate
- hand off to `component-systems-expert.md` when registry or variant questions appear
- hand off to `accessibility-feedback-expert.md` when interactive accessibility needs deeper rules
- hand off to `type-system-expert.md` when the font strategy itself is still unresolved
- hand off to `back-end-aware-planner.md` when data, auth, or export risk appears

## Canonical fallback
- `skills/front-end-handoff-expert.md`
- `knowledge-base/summaries/front-end-handoff-summary.md`
- `knowledge-base/summaries/front-end-architecture-summary.md`