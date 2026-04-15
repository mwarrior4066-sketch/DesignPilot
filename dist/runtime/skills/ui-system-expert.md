---
runtime_card_version: 1.0.0
canonical_skill: src/skills/ui-system-expert.md
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
- solve the primary task path first; solve hierarchy second; solve navigation and action placement third
- top nav for ≤5 items; left sidebar for 6–15; drawer or search for >15
- flat IA fails above 30 items at one level - sub-group or filter before that threshold
- deep IA fails when primary content requires >3 clicks from entry
- one primary CTA per region - two competing filled buttons is a hierarchy failure
- every task-bearing screen requires empty, loading, error, and success states before it ships
- destructive actions require two-stage confirmation: secondary trigger first, primary confirm inside modal
- above-the-fold: critical action or status must be visible without scroll on the target viewport
- touch targets: 48×48dp minimum for any interactive element
- hand off specialist concerns instead of restating their rules

## Failure traps
- polished components hiding a broken primary task path
- designing screens without naming the main action
- missing screen states (empty, error, loading) leaving users with no recovery
- more than one primary CTA competing in the same region
- overfitting local components while the flow is still broken
- navigation with no wayfinding or landmarks at depth >2
- CTA placement inconsistent across the same flow
- destructive action placed without a confirmation stage

## Summary dependencies
- ui-system-summary.md
- UI System Expert Research.md

## Escalation triggers
- if the user asks for a tiny component change, keep system notes brief
- if the system is already established, preserve existing patterns before introducing new ones
- if the flow is unclear, define the minimum viable path instead of designing every edge case
- if a request is actually dashboard-specific, hand off to `dashboard-data-expert.md`
- if state or keyboard logic dominates, hand off to `accessibility-feedback-expert.md`
- if motion and transition logic is central, hand off to or add `motion-interaction-expert.md`
- primary action named
- navigation pattern selected and justified against item count

## Adjacent handoff rules
- hand off to `grid-system-expert.md` for layout scaffolding
- hand off to `type-system-expert.md` when hierarchy depends on typography
- hand off to `dashboard-data-expert.md` when metrics/charts dominate the problem
- hand off to `accessibility-feedback-expert.md` when state, keyboard, or focus logic matters
- hand off to `motion-interaction-expert.md` when transition, animation, or feedback timing is central
- hand off to `front-end-handoff-expert.md` when the system is ready for implementation

## Canonical fallback
- `src/skills/ui-system-expert.md`
- `src/knowledge-base/summaries/ui-system-summary.md`
- `src/knowledge-base/summaries/UI System Expert Research.md`