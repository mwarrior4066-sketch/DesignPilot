---
runtime_card_version: 1.0.0
canonical_skill: src/skills/front-end-architecture-expert.md
last_generated: 2026-04-11
overlay: true
---
# front-end-architecture-expert.md

## Activation conditions
- the request depends on rendering strategy, hydration cost, bundle size, or server/client boundary placement
- the UI logic is becoming a state-machine problem rather than a styling problem
- the task asks whether a front-end implementation is structurally sound, scalable, or recoverable
- the user only needs translation of an already-solved design into implementation-safe components
- the question is purely visual or editorial with no architectural implications

## Non-activation conditions
- the user only needs translation of an already-solved design into implementation-safe components
- the question is purely visual or editorial with no architectural implications

## Core decision rules
- architecture before code style
- explicit finite states before boolean piles
- static, server, or PPR before client-heavy rendering by default
- semantic host elements before custom roles
- client boundaries down the tree
- mutation recovery before optimistic polish
- performance cost named, not implied

## Failure traps
- boolean explosion
- distributed monolith boundaries
- click-only semantics
- data mutation with no rollback or recovery logic
- client rendering chosen by habit instead of need
- production-sounding performance claims with no cost note

## Summary dependencies
- front-end-architecture-summary.md

## Escalation triggers
- pure prototypes may simplify rendering strategy only if the output labels the simplification clearly
- client-heavy tools behind auth can justify CSR islands when interactivity is the actual product
- custom widgets are acceptable only when native HTML cannot meet the functional need
- if the architecture is underspecified, fall back to a boundary map plus explicit unknowns instead of bluffing certainty
- if state complexity is rising, fall back to a status union or state-machine outline rather than more flags
- if rendering choice is unclear, default to a server-first shell with explicit client islands
- rendering decision
- state ownership rule

## Adjacent handoff rules
- hand off to `front-end-handoff-expert.md` when the architecture decision must be translated into a code-safe component or token contract
- hand off to `accessibility-feedback-expert.md` when a deep widget behavior map is required
- hand off to `back-end-aware-planner.md` when data, auth, export, or async system constraints drive the answer

## Canonical fallback
- `src/skills/front-end-architecture-expert.md`
- `src/knowledge-base/summaries/front-end-architecture-summary.md`