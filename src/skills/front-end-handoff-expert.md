---
skill_version: 1.1.0
source_reference:
  - src/knowledge-base/summaries/front-end-handoff-summary.md
  - src/knowledge-base/summaries/front-end-architecture-summary.md
last_updated: 2026-04-11
synchronized: true
canonical_owner: true
domain: front-end-handoff
---

# Front-End Handoff Expert

## Purpose
Use this skill as the gateway that translates design decisions into implementation-safe front-end structure without losing tokens, states, accessibility, typography behavior, or system coherence. It is not the owner of deep front-end architecture decisions.

## Activate when
- the task involves React, Next.js, Tailwind, components, tokens, semantic HTML, webfont loading, or design-to-code translation
- the answer must be implementation-aware rather than purely visual
- the architecture is already known or can be kept shallow enough for safe handoff

## Do not activate when
- the core problem is rendering strategy, state ownership, or server/client boundary placement
- the system is still undefined and only strategy is needed
- the task is only a high-level identity discussion with no code implication

## Read these first
- `src/knowledge-base/summaries/front-end-handoff-summary.md`
- `src/knowledge-base/summaries/front-end-architecture-summary.md`
- `src/knowledge-base/summaries/design-token-summary.md`
- `src/knowledge-base/summaries/accessibility-and-feedback-summary.md`
- `src/knowledge-base/summaries/typography-summary.md`
- `src/libraries/FONT_LIBRARY.json`, `src/libraries/FONT_LIBRARY.md`
- `src/libraries/COLOR_LIBRARY.json`, `src/libraries/COLOR_LIBRARY.md` when semantic theme tokens or palette aliases are still unresolved

## Decision rules
- semantics before styling
- token usage before hard-coded values
- component boundaries before page-wide hacks
- accessibility behavior before polish
- implementation-safe font loading before typographic romance
- architecture escalation before false certainty

## Default actions
- define component boundaries
- identify the tokens needed for spacing, color, type, motion, and state
- include required states for interactive components
- include reduced-motion handling for non-essential motion
- prefer WOFF2 for webfonts
- use `font-display: swap` unless there is a strong reason not to
- use high-level CSS font controls before low-level `font-variation-settings` unless a custom axis truly requires it
- surface when the task has crossed into deep front-end architecture or backend risk

## Exception rules
- local demo code can be simpler if it does not misrepresent system behavior
- if framework detail is unknown and risk is low, provide framework-agnostic structure first
- if the requested font is not deployable, propose a named substitute or system stack

## Fallback logic
- if a semantic token is missing, define the alias before using a raw primitive
- if a palette decision is still unresolved, pull semantic roles from `COLOR_LIBRARY` before hard-coding hue values
- if hover is irrelevant on touch, prioritize focus, pressed, and visible feedback
- if a variable font is unavailable, fall back to discrete weights and keep the stack explicit
- if the task includes rendering, hydration, or state-architecture risk, hand off to `front-end-architecture-expert.md`
- if the task includes live data, auth, export, or risky architecture, hand off to `back-end-aware-planner.md`

## Failure traps
- styling before semantics
- missing states
- hard-coded colors or spacing where tokens are clearly needed
- inaccessible interactivity
- visually accurate but structurally brittle code
- pretending gateway handoff solved architecture ownership questions

## Evidence required
Use some combination of:
- component boundary
- token usage
- state matrix
- keyboard/focus behavior
- reduced-motion behavior
- font loading / fallback logic
- escalation or feasibility note

## Handoff to other skills
- hand off to `front-end-architecture-expert.md` when rendering strategy, state ownership, or boundary placement dominate
- hand off to `component-systems-expert.md` when registry or variant questions appear
- hand off to `accessibility-feedback-expert.md` when interactive accessibility needs deeper rules
- hand off to `type-system-expert.md` when the font strategy itself is still unresolved
- hand off to `back-end-aware-planner.md` when data, auth, or export risk appears

## Output expectations
- code-aware but system-faithful
- no ad hoc exceptions presented as architecture
- accessibility and font deployment accounted for when relevant

## Runtime summary

<!-- Auto-generated runtime overlay. Edit src/skills/front-end-handoff-expert.md -- not this section. -->

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
- `src/skills/front-end-handoff-expert.md`
- `src/knowledge-base/summaries/front-end-handoff-summary.md`
- `src/knowledge-base/summaries/front-end-architecture-summary.md`
