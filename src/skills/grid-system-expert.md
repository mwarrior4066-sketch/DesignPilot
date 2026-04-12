---
skill_version: 1.0.0
source_reference:
  - src/knowledge-base/summaries/grid-mediums-summary.md
last_updated: 2026-04-09
synchronized: true
canonical_owner: true
domain: grid-system
---

# Grid System Expert

## Purpose
Use this skill to choose new grid systems by medium and content type: web, app, slide, editorial, dashboard, and document layouts.

## Activate when
- the task is about columns, gutters, margins, baseline logic, modular layout, or breakpoints
- the user is creating a new layout system rather than extending an existing one

## Do not activate when
- the task is really about inferring a legacy layout from screenshots or PDFs
- the task is only about typography or color with no layout-system choice

## Read these first
- `src/knowledge-base/summaries/grid-mediums-summary.md`
- `src/knowledge-base/summaries/pdf-layout-summary.md` when print/PDF is involved

## Decision rules
- choose the grid from the medium and content type
- prefer the simplest grid that can still support the content
- use 12-column systems for flexible web/editorial/dashboard contexts when appropriate
- use 4/8/12 responsive contraction where it fits the medium
- baseline rhythm matters when text continuity is a real requirement

## Default actions
- classify the medium
- classify the content type
- define margins, columns, gutters, and baseline or breakpoint behavior
- define where asymmetry is justified
- note when the grid is strict vs intentionally broken by exception zones

## Exception rules
- manuscript or two-column editorial structures may beat a generic 12-column grid for long reading
- posters or expressive compositions may prioritize hierarchy and focal alignment over equal-column regularity
- dashboards may combine a global grid with local microgrids

## Fallback logic
- if the medium is clear but the content is sparse, choose the safest medium default
- if the layout must be inferred from a source, hand off to `layout-reconstruction-expert.md`

## Failure traps
- defaulting to 12 columns without reason
- equal columns where hierarchy clearly wants asymmetry
- ignoring baseline rhythm where body text continuity matters
- using fresh grid rules when the source layout should be preserved instead

## Evidence required
Use some combination of:
- medium
- columns
- gutters
- margins
- baseline or breakpoint rule
- asymmetry / exception-zone note

## Handoff to other skills
- hand off to `layout-reconstruction-expert.md` for legacy inference
- hand off to `type-system-expert.md` when measure and leading constrain the grid
- hand off to `dashboard-data-expert.md` for dense-data local grid decisions

## Output expectations
- medium-appropriate grid
- explicit margins/columns/gutters
- exceptions named, not hand-waved
