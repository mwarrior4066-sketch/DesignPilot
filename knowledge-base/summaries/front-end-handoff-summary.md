---
summary_version: 1.1.0
source_reference:
  - knowledge-base/source-docs/Front-End Handoff Expert Research.md
  - knowledge-base/source-docs/Front-End Architecture Expert Knowledge Base.md
last_updated: 2026-04-11
synchronized: true
domain: front-end-handoff
---

# Front-End Handoff Summary

## Purpose
Canonical summary for translating design decisions into implementation-safe front-end structure. This summary is the gateway layer, not the deep architecture owner.

## Use when
- the user needs React, Next.js, Tailwind, component, token, or implementation handoff help
- the answer must preserve design-system logic while staying safe for code implementation
- the task needs component boundaries, states, or token mapping more than full architectural redesign

## Default rules
- preserve semantics before styling
- preserve tokens before hard-coded values
- define component boundaries before page-wide hacks
- preserve required states, accessibility behavior, and reduced-motion logic
- keep font deployment, fallbacks, and loading safe for the actual medium
- surface when the problem has crossed from handoff into deeper front-end architecture

## Key outputs
- component boundary
- token and state map
- semantic and accessibility notes
- mutation/loading/error UI contract
- font loading or fallback logic
- escalation note when architecture risk appears

## Failure patterns
- code translation that loses the original system logic
- token drift
- missing states or degraded paths
- implementation detail that ignores semantics
- handoff advice pretending to solve rendering or state architecture questions it does not own

## Hand off to
- `front-end-architecture-expert.md` for rendering strategy, state ownership, and server/client boundary decisions
- `component-systems-expert.md` for registry and variant governance
- `accessibility-feedback-expert.md` for deeper widget and keyboard rules
- `back-end-aware-planner.md` when data, auth, export, or async risk appears
