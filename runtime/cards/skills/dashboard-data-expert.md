---
runtime_card_version: 1.0.0
canonical_skill: skills/dashboard-data-expert.md
last_generated: 2026-04-11
overlay: true
---
# dashboard-data-expert.md

## Activation conditions
- the task involves dashboards, scorecards, analytics, monitoring screens, or dense operational UI
- the user is choosing metrics, charts, filters, table density, or KPI hierarchy
- the task is generic page layout with no metrics or analytics behavior
- the request is only a branding or poster composition task

## Non-activation conditions
- the task is generic page layout with no metrics or analytics behavior
- the request is only a branding or poster composition task

## Core decision rules
- map every metric to a decision
- determine whether the dashboard is strategic, analytical, or operational before designing it
- keep the summary plane decision-oriented
- use the simplest valid chart for the data relationship
- density is earned, not default

## Failure traps
- graveyard of KPIs
- dashboard looks “minimal” but hides essential decisions
- pie charts used for too many categories
- filters with no mental model
- color overload in charts
- summary plane used as an archive instead of a decision surface

## Summary dependencies
- dashboard-and-density-summary.md

## Escalation triggers
- crisis interfaces may justify temporarily higher density
- analytical workspaces may exceed strategic dashboard density if filters, grouping, and drill-down remain clear
- narrow mobile views may need card or stacked fallbacks instead of full table parity
- if the dashboard is too dense, group, filter, or drill down
- if the chart choice is ambiguous, prefer bar or line over clever novelty
- if the data is sparse, use empty states that explain what is missing and what the user can do next
- dashboard type
- KPI hierarchy

## Adjacent handoff rules
- hand off to `ui-system-expert.md` for page-level structure
- hand off to `color-system-expert.md` for chart-safe palette rules
- hand off to `accessibility-feedback-expert.md` for filter/accessibility behavior
- hand off to `front-end-handoff-expert.md` for implementation-safe output

## Canonical fallback
- `skills/dashboard-data-expert.md`
- `knowledge-base/summaries/dashboard-and-density-summary.md`