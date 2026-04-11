---
summary_version: 1.0.0
source_reference:
  - knowledge-base/source-docs/Front-End Architecture Expert Knowledge Base.md
last_updated: 2026-04-11
synchronized: true
domain: front-end-architecture
---

# Front-End Architecture Summary

## Purpose
Canonical summary for production-level front-end architecture decisions around rendering strategy, state ownership, server and client boundaries, semantic structure, mutation handling, accessibility behavior, and performance cost.

## Use when
- the request needs architectural control, not only code translation
- rendering model, hydration cost, state modeling, or mutation strategy will affect the outcome
- a screen or component risks becoming a distributed monolith or impossible-state UI

## Default rules
- UI is a state machine, not a sequence of boolean flags
- prefer static, server, or PPR strategies before defaulting to heavy client rendering
- move `use client` boundaries down the tree
- use native elements before custom roles and widgets
- keep state as local as possible and use server-state for external data synchronization
- prefer Actions, progressive enhancement, and rollback-safe mutations over manual async spaghetti
- treat bundle, hydration, and rendering cost as explicit tradeoffs

## Key outputs
- rendering decision
- state ownership map
- server and client boundary note
- semantic element contract
- mutation and degraded-state logic
- performance risk note

## Failure patterns
- boolean explosion
- deep prop drilling and boundary collapse
- client-heavy rendering with avoidable hydration cost
- clickable divs and fake semantics
- ad hoc `useEffect` chains for derived state
- production-sounding recommendations with no performance or failure posture

## Hand off to
- `front-end-handoff-expert.md` for translation into code-safe structure and token-aware implementation
- `accessibility-feedback-expert.md` for deep widget behavior and keyboard contracts
- `back-end-aware-planner.md` when permissions, exports, storage, or async work become blockers
