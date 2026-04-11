---
runtime_summary_version: 1.0.0
canonical_summary: knowledge-base/summaries/front-end-architecture-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - knowledge-base/source-docs/Front-End Architecture Expert Knowledge Base.md
---
# Front End Architecture Summary Runtime Summary

## Decision rules
- UI is a state machine, not a sequence of boolean flags
- prefer static, server, or PPR strategies before defaulting to heavy client rendering
- move `use client` boundaries down the tree
- use native elements before custom roles and widgets
- keep state as local as possible and use server-state for external data synchronization
- prefer Actions, progressive enhancement, and rollback-safe mutations over manual async spaghetti
- treat bundle, hydration, and rendering cost as explicit tradeoffs
- rendering decision
- state ownership map
- server and client boundary note
- semantic element contract
- mutation and degraded-state logic

## Failure traps
- boolean explosion
- deep prop drilling and boundary collapse
- client-heavy rendering with avoidable hydration cost
- clickable divs and fake semantics
- ad hoc `useEffect` chains for derived state
- production-sounding recommendations with no performance or failure posture

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `knowledge-base/summaries/front-end-architecture-summary.md`
- `knowledge-base/source-docs/Front-End Architecture Expert Knowledge Base.md`