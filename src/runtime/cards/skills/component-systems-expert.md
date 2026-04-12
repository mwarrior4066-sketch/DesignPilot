---
runtime_card_version: 1.0.0
canonical_skill: src/skills/component-systems-expert.md
last_generated: 2026-04-11
overlay: true
---
# component-systems-expert.md

## Activation conditions
- the task is about component creation, registry checks, variants, sizes, state coverage, or design-system governance
- the user is asking “should this be a new component?” or “what should this component support?”
- the issue is actually page flow or information architecture
- the task is only a visual styling pass with no component implication

## Non-activation conditions
- the issue is actually page flow or information architecture
- the task is only a visual styling pass with no component implication

## Core decision rules
- prefer reuse and composition before invention
- a new component needs a new behavior or semantic job, not just a new visual treatment
- every interactive component needs documented states
- every component should include a when-to-use and when-not-to-use rule

## Failure traps
- duplicate components solving the same task
- visual variants pretending to be new components
- missing states
- no when-not-to-use guidance
- component decisions made without accessibility or responsive behavior

## Summary dependencies
- component-systems-summary.md

## Escalation triggers
- a local-only edge component is allowed when the behavior is genuinely unique
- incubating components may exist, but should not be treated as default recommendations
- if the registry is unclear, prefer stable existing components or primitive composition
- if a new variant adds no new behavior, fold it into an existing pattern
- if documentation is incomplete, block the component from being treated as production-ready
- component purpose
- when-to-use / when-not-to-use
- reuse vs new-component decision

## Adjacent handoff rules
- hand off to `accessibility-feedback-expert.md` for state and interaction requirements
- hand off to `front-end-handoff-expert.md` for code-ready translation
- hand off to `ui-system-expert.md` when the real issue is task flow, not component choice

## Canonical fallback
- `src/skills/component-systems-expert.md`
- `src/knowledge-base/summaries/component-systems-summary.md`