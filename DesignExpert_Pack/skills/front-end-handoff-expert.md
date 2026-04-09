---
skill_version: 1.0.0
source_reference:
  - knowledge-base/summaries/front-end-handoff-summary.md
last_updated: 2026-04-09
synchronized: true
canonical_owner: true
domain: front-end-handoff
---

# Front-End Handoff Expert

## Purpose
Use this skill to translate design decisions into implementation-safe front-end structure without losing tokens, states, accessibility, typography behavior, or system coherence.

## Activate when
- the task involves React, Next.js, Tailwind, components, tokens, semantic HTML, webfont loading, or design-to-code translation
- the answer must be implementation-aware rather than purely visual

## Do not activate when
- the system is still undefined and only strategy is needed
- the task is only a high-level identity discussion with no code implication

## Read these first
- `knowledge-base/summaries/front-end-handoff-summary.md`
- `knowledge-base/summaries/design-token-summary.md`
- `knowledge-base/summaries/accessibility-and-feedback-summary.md`
- `knowledge-base/summaries/typography-summary.md`
- `libraries/FONT_LIBRARY.json`, `libraries/FONT_LIBRARY.md`

## Decision rules
- semantics before styling
- token usage before hard-coded values
- component boundaries before page-wide hacks
- accessibility behavior before polish
- implementation-safe font loading before typographic romance
- feasibility notes before false certainty

## Default actions
- define component boundaries
- identify the tokens needed for spacing, color, type, motion, and state
- include required states for interactive components
- include reduced-motion handling for non-essential motion
- prefer WOFF2 for webfonts
- use `font-display: swap` unless there is a strong reason not to
- note preload only for primary families or critical cuts
- surface implementation risk instead of bluffing

## Exception rules
- local demo code can be simpler if it does not misrepresent system behavior
- if framework detail is unknown and risk is low, provide framework-agnostic structure first
- if the requested font is not deployable, propose a named substitute or system stack

## Fallback logic
- if a semantic token is missing, define the alias before using a raw primitive
- if hover is irrelevant on touch, prioritize focus, pressed, and visible feedback
- if a variable font is unavailable, fall back to discrete weights and keep the stack explicit
- if the task includes live data, auth, export, or risky architecture, hand off to `back-end-aware-planner.md`

## Failure traps
- styling before semantics
- missing states
- hard-coded colors or spacing where tokens are clearly needed
- inaccessible interactivity
- loading many static font files when one variable WOFF2 would do
- visually accurate but structurally brittle code

## Evidence required
Use some combination of:
- component boundary
- token usage
- state matrix
- keyboard/focus behavior
- reduced-motion behavior
- font loading / fallback logic
- feasibility constraint

## Handoff to other skills
- hand off to `component-systems-expert.md` when registry or variant questions appear
- hand off to `accessibility-feedback-expert.md` when interactive accessibility needs deeper rules
- hand off to `type-system-expert.md` when the font strategy itself is still unresolved
- hand off to `back-end-aware-planner.md` when data, auth, or export risk appears

## Output expectations
- code-aware but system-faithful
- no ad hoc exceptions presented as architecture
- accessibility and font deployment accounted for when relevant
