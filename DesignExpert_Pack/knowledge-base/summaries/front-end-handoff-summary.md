---
summary_version: 1.0.0
source_reference:
  - knowledge-base/source-docs/Front-End Handoff Expert Research.md
last_updated: 2026-04-09
synchronized: true
domain: front-end-handoff
---

# Front-End Handoff Summary

## Purpose
Canonical summary for turning design decisions into implementation-safe, token-driven, accessible front-end outputs.

## Use when
- the user needs React/Next.js/Tailwind/component guidance
- the answer must translate design into code-ready structure
- design handoff or implementation risk is part of the task

## Default rules
- semantics before styling
- token use before hard-coded values
- component boundaries before page-wide hacks
- state coverage before animation polish
- variable-font and WOFF2 strategy before ad hoc font loading
- reduced-motion path before expressive motion

## Key outputs
- component boundary
- token usage
- accessibility behaviors
- font loading/fallback logic
- feasibility and risk note

## Failure patterns
- design logic lost in translation
- missing states
- hard-coded values where tokens should exist
- inaccessible interactivity
- too many static font files instead of a cleaner variable-font strategy
- visually accurate but structurally brittle code

## Hand off to
- `component-systems-expert.md` for registry/variant decisions
- `accessibility-feedback-expert.md` for interactive accessibility
- `type-system-expert.md` for font strategy
- `back-end-aware-planner.md` for data/auth/export risk
