---
runtime_card_version: 1.0.0
canonical_skill: skills/grid-system-expert.md
last_generated: 2026-04-11
overlay: true
---
# grid-system-expert.md

## Activation conditions
- the task is about columns, gutters, margins, baseline logic, modular layout, or breakpoints
- the user is creating a new layout system rather than extending an existing one
- the task is really about inferring a legacy layout from screenshots or PDFs
- the task is only about typography or color with no layout-system choice

## Non-activation conditions
- the task is really about inferring a legacy layout from screenshots or PDFs
- the task is only about typography or color with no layout-system choice

## Core decision rules
- choose the grid from the medium and content type
- prefer the simplest grid that can still support the content
- use 12-column systems for flexible web/editorial/dashboard contexts when appropriate
- use 4/8/12 responsive contraction where it fits the medium
- baseline rhythm matters when text continuity is a real requirement

## Failure traps
- defaulting to 12 columns without reason
- equal columns where hierarchy clearly wants asymmetry
- ignoring baseline rhythm where body text continuity matters
- using fresh grid rules when the source layout should be preserved instead

## Summary dependencies
- grid-mediums-summary.md

## Escalation triggers
- manuscript or two-column editorial structures may beat a generic 12-column grid for long reading
- posters or expressive compositions may prioritize hierarchy and focal alignment over equal-column regularity
- dashboards may combine a global grid with local microgrids
- if the medium is clear but the content is sparse, choose the safest medium default
- if the layout must be inferred from a source, hand off to `layout-reconstruction-expert.md`
- medium
- columns
- gutters

## Adjacent handoff rules
- hand off to `layout-reconstruction-expert.md` for legacy inference
- hand off to `type-system-expert.md` when measure and leading constrain the grid
- hand off to `dashboard-data-expert.md` for dense-data local grid decisions

## Canonical fallback
- `skills/grid-system-expert.md`
- `knowledge-base/summaries/grid-mediums-summary.md`