---
skill_version: 1.0.0
source_reference:
  - src/knowledge-base/summaries/dashboard-and-density-summary.md
last_updated: 2026-04-09
synchronized: true
canonical_owner: true
domain: dashboard-data
---

# Dashboard Data Expert

## Purpose
Use this skill to make production-level decisions about dashboard type, KPI hierarchy, chart choice, density, filters, drill-down, and dense-data readability.

## Activate when
- the task involves dashboards, scorecards, analytics, monitoring screens, or dense operational UI
- the user is choosing metrics, charts, filters, table density, or KPI hierarchy

## Do not activate when
- the task is generic page layout with no metrics or analytics behavior
- the request is only a branding or poster composition task

## Read these first
- `src/knowledge-base/summaries/dashboard-and-density-summary.md`
- `src/knowledge-base/summaries/ui-system-summary.md`

## Decision rules
- map every metric to a decision
- determine whether the dashboard is strategic, analytical, or operational before designing it
- keep the summary plane decision-oriented
- use the simplest valid chart for the data relationship
- density is earned, not default

## Default actions
- classify the dashboard type
- rank metrics by user decision value
- assign the top-left and top-center hierarchy
- choose charts based on data type, not style preference
- move lower-value detail into drill-down, filtering, or secondary views

## Exception rules
- crisis interfaces may justify temporarily higher density
- analytical workspaces may exceed strategic dashboard density if filters, grouping, and drill-down remain clear
- narrow mobile views may need card or stacked fallbacks instead of full table parity

## Fallback logic
- if the dashboard is too dense, group, filter, or drill down
- if the chart choice is ambiguous, prefer bar or line over clever novelty
- if the data is sparse, use empty states that explain what is missing and what the user can do next

## Failure traps
- graveyard of KPIs
- dashboard looks “minimal” but hides essential decisions
- pie charts used for too many categories
- filters with no mental model
- color overload in charts
- summary plane used as an archive instead of a decision surface

## Evidence required
Use some combination of:
- dashboard type
- KPI hierarchy
- chart rule
- density threshold
- filter/drill-down rule
- empty-state or mobile fallback rule

## Handoff to other skills
- hand off to `ui-system-expert.md` for page-level structure
- hand off to `color-system-expert.md` for chart-safe palette rules
- hand off to `accessibility-feedback-expert.md` for filter/accessibility behavior
- hand off to `front-end-handoff-expert.md` for implementation-safe output

## Output expectations
- metrics tied to decisions
- chart choice justified
- density controlled
- drill-down or grouping used instead of brute-force overload
