---
runtime_card_version: 1.0.0
canonical_skill: skills/ui-system-expert.md
last_generated: 2026-04-11
overlay: true
---
# ui-system-expert.md

## Activation conditions
- the task is about screens, flows, navigation, IA, page hierarchy, action placement, or system structure
- the user needs system logic before polish or code
- the task is only a font choice
- the task is only a print-specific PDF repair
- the issue is purely about chart logic or dense-data rules

## Non-activation conditions
- the task is only a font choice
- the task is only a print-specific PDF repair
- the issue is purely about chart logic or dense-data rules

## Core decision rules
- solve the primary task path first
- solve hierarchy second
- solve navigation and action placement third
- hand off specialist concerns instead of restating their rules
- visual polish happens after the system is coherent

## Failure traps
- hiding broken UX under polished components
- designing screens without naming the main action
- overfitting local components while the flow is still broken
- solving dashboard density or accessibility issues with generic UI advice

## Summary dependencies
- ui-system-summary.md

## Escalation triggers
- if the user asks for a tiny component change, keep system notes brief
- if the system is already established, preserve it before introducing new patterns
- if the flow is unclear, define the minimum viable path instead of designing every edge case
- if a request is actually dashboard-specific, hand off to `dashboard-data-expert.md`
- if state requirements dominate the task, hand off to `accessibility-feedback-expert.md`
- primary action
- hierarchy map
- navigation logic

## Adjacent handoff rules
- hand off to `grid-system-expert.md` for layout scaffolding
- hand off to `type-system-expert.md` when hierarchy depends on typography
- hand off to `dashboard-data-expert.md` when metrics/charts dominate the problem
- hand off to `accessibility-feedback-expert.md` when state, motion, or keyboard logic matters
- hand off to `front-end-handoff-expert.md` when the system is ready for implementation

## Canonical fallback
- `skills/ui-system-expert.md`
- `knowledge-base/summaries/ui-system-summary.md`