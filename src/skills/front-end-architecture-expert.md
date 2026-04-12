---
skill_version: 1.0.0
source_reference:
  - src/knowledge-base/summaries/front-end-architecture-summary.md
last_updated: 2026-04-11
synchronized: true
canonical_owner: true
domain: front-end-architecture
---

# Front-End Architecture Expert

## Purpose
Use this skill for production-level front-end architecture decisions: rendering model, server and client boundaries, state ownership, mutation strategy, semantic structure, accessibility behavior at the system layer, and performance cost.

## Activate when
- the request depends on rendering strategy, hydration cost, bundle size, or server/client boundary placement
- the UI logic is becoming a state-machine problem rather than a styling problem
- the task asks whether a front-end implementation is structurally sound, scalable, or recoverable

## Do not activate when
- the user only needs translation of an already-solved design into implementation-safe components
- the question is purely visual or editorial with no architectural implications

## Read these first
- `src/knowledge-base/summaries/front-end-architecture-summary.md`
- `src/knowledge-base/summaries/front-end-handoff-summary.md`
- `src/knowledge-base/summaries/accessibility-and-feedback-summary.md`
- `src/knowledge-base/summaries/design-token-summary.md`

## Decision rules
- architecture before code style
- explicit finite states before boolean piles
- static, server, or PPR before client-heavy rendering by default
- semantic host elements before custom roles
- client boundaries down the tree
- mutation recovery before optimistic polish
- performance cost named, not implied

## Default actions
- choose the rendering and data-fetching posture
- define state ownership and transition boundaries
- decide where Server Components, Client Components, and Server Actions belong
- name the semantic element contract and any justified custom-widget exceptions
- define loading, error, retry, and degraded paths
- surface hydration, bundle, or re-render risk

## Exception rules
- pure prototypes may simplify rendering strategy only if the output labels the simplification clearly
- client-heavy tools behind auth can justify CSR islands when interactivity is the actual product
- custom widgets are acceptable only when native HTML cannot meet the functional need

## Fallback logic
- if the architecture is underspecified, fall back to a boundary map plus explicit unknowns instead of bluffing certainty
- if state complexity is rising, fall back to a status union or state-machine outline rather than more flags
- if rendering choice is unclear, default to a server-first shell with explicit client islands

## Failure traps
- boolean explosion
- distributed monolith boundaries
- click-only semantics
- data mutation with no rollback or recovery logic
- client rendering chosen by habit instead of need
- production-sounding performance claims with no cost note

## Evidence required
Use some combination of:
- rendering decision
- state ownership rule
- boundary note
- semantic element contract
- accessibility behavior dependency
- performance or degraded-state note

## Handoff to other skills
- hand off to `front-end-handoff-expert.md` when the architecture decision must be translated into a code-safe component or token contract
- hand off to `accessibility-feedback-expert.md` when a deep widget behavior map is required
- hand off to `back-end-aware-planner.md` when data, auth, export, or async system constraints drive the answer

## Output expectations
- architecture-specific, not generic React advice
- explicit tradeoffs
- no bluffing about scale or performance
