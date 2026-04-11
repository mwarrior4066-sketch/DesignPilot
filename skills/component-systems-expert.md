---
skill_version: 1.0.0
source_reference:
  - knowledge-base/summaries/component-systems-summary.md
last_updated: 2026-04-09
synchronized: true
canonical_owner: true
domain: component-systems
---

# Component Systems Expert

## Purpose
Use this skill to decide whether a component should exist, how it should be documented, what variants and states it needs, and how reuse beats drift.

## Activate when
- the task is about component creation, registry checks, variants, sizes, state coverage, or design-system governance
- the user is asking “should this be a new component?” or “what should this component support?”

## Do not activate when
- the issue is actually page flow or information architecture
- the task is only a visual styling pass with no component implication

## Read these first
- `knowledge-base/summaries/component-systems-summary.md`
- `knowledge-base/summaries/accessibility-and-feedback-summary.md`

## Decision rules
- prefer reuse and composition before invention
- a new component needs a new behavior or semantic job, not just a new visual treatment
- every interactive component needs documented states
- every component should include a when-to-use and when-not-to-use rule

## Default actions
- classify the component type
- check whether an existing component or primitive composition can solve it
- define the required variants, sizes, and states
- define accessibility and responsive expectations
- define whether the component is stable, local-only, or incubating

## Exception rules
- a local-only edge component is allowed when the behavior is genuinely unique
- incubating components may exist, but should not be treated as default recommendations

## Fallback logic
- if the registry is unclear, prefer stable existing components or primitive composition
- if a new variant adds no new behavior, fold it into an existing pattern
- if documentation is incomplete, block the component from being treated as production-ready

## Failure traps
- duplicate components solving the same task
- visual variants pretending to be new components
- missing states
- no when-not-to-use guidance
- component decisions made without accessibility or responsive behavior

## Evidence required
Use some combination of:
- component purpose
- when-to-use / when-not-to-use
- reuse vs new-component decision
- required variants and states
- accessibility requirement
- implementation readiness note

## Handoff to other skills
- hand off to `accessibility-feedback-expert.md` for state and interaction requirements
- hand off to `front-end-handoff-expert.md` for code-ready translation
- hand off to `ui-system-expert.md` when the real issue is task flow, not component choice

## Output expectations
- reusable system logic
- no variant sprawl without reason
- state coverage explicit
