---
summary_version: 1.0.0
source_reference:
  - knowledge-base/source-docs/Dashboard Expert Research.md
last_updated: 2026-04-09
synchronized: true
domain: dashboard-data
---

# Dashboard and Density Summary

## Purpose
Canonical summary for dashboard taxonomy, KPI hierarchy, chart choice, density, filter/drill-down logic, and dense-data accessibility.

## Use when
- the task involves dashboards, scorecards, analytics, monitoring screens, metric cards, charts, or dense operational UI

## Dashboard types
- strategic: executive, low-density, 3 to 7 primary metrics, 5-second scan
- analytical: denser, exploratory, stronger filters and drill-down
- operational: real-time or near-real-time, faster scan, clear state visibility

## Default rules
- every metric should map to a real decision or action
- keep the summary plane decision-oriented, not exhaustive
- top-left carries the most critical KPI/status information
- use bar charts for categorical comparison, line charts for time series, and simple numeric KPI blocks for single top metrics
- use drill-down and progressive disclosure instead of packing everything into one plane

## Key thresholds
- primary summary view should usually show 3 to 7 main metrics
- avoid more than about 7 color intensities in one visualization
- dashboards should pass a quick “system health in 5 seconds” check
- dense dashboards should still avoid horizontal scrolling as the default summary behavior

## Exceptions
- crisis or incident dashboards may allow temporarily higher density
- analytical workspaces may exceed strategic dashboard density if navigation and filters stay clear
- mobile may need card or stacked fallbacks instead of full table parity

## Failure patterns
- graveyard of KPIs
- decorative chart junk
- wrong chart for the data type
- filters with no mental model
- no drill-down path
- empty states that explain nothing
- dashboard looks minimal but hides essential decisions

## Hand off to
- `ui-system-expert.md` for page-level structure
- `color-system-expert.md` for chart-safe and contrast-safe palettes
- `accessibility-feedback-expert.md` for interactive filter/accessibility behavior
- `front-end-handoff-expert.md` when implementation structure is needed
