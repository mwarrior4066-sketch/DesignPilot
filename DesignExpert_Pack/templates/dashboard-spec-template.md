# Dashboard Spec Template

Use this when the task is a real dashboard planning/output problem, not a generic page layout.

## Dashboard type
- strategic / analytical / operational:

## Primary user and decision
- user:
- main question they need answered:
- action they can take:

## KPI hierarchy
- top-left:
- top-center:
- supporting metrics:
- secondary detail:
- drill-down destinations:

## Chart logic
- metric:
- chart type:
- why this chart:
- accessibility note:

## Density control
- primary metric count:
- grouped sections:
- drill-down rules:
- empty states:

## Filters
- global filters:
- local filters:
- default filter state:
- reset behavior:

## Mobile fallback
- card / stacked / condensed table / other:

## Example output
### Dashboard type
- strategic / analytical / operational: operational dashboard with executive summary row

### Primary user and decision
- user: cloud operations lead
- main question they need answered: where are compliance failures and cost anomalies increasing right now
- action they can take: drill into flagged assets, assign remediation, export exception report

### KPI hierarchy
- top-left: active critical compliance violations
- top-center: cost anomaly total vs prior 7 days
- supporting metrics: untagged assets, stale backups, overdue remediations
- secondary detail: region breakdown, owner breakdown, recent incident log
- drill-down destinations: asset list view, owner-specific queue, exception export

### Chart logic
- metric: anomaly trend by day
- chart type: line chart
- why this chart: trend over time matters more than exact isolated comparisons
- accessibility note: direct labels on line endpoints, not color-only legend reliance

- metric: violations by team
- chart type: sorted horizontal bar chart
- why this chart: team comparison with long labels needs scan-efficient ranking
- accessibility note: use direct value labels and restrained category colors

### Density control
- primary metric count: 4 in the summary band
- grouped sections: summary KPIs / trend panel / owner or region comparisons / action queue
- drill-down rules: details and raw tables stay one click down, not on the main surface
- empty states: if anomaly feed is empty, show “No active anomalies in selected range” plus data freshness timestamp

### Filters
- global filters: time range, region, environment, owner
- local filters: chart-specific severity filter on incident queue only
- default filter state: last 7 days, all production regions
- reset behavior: one-click reset to operational default

### Mobile fallback
- card / stacked / condensed table / other: summary cards + stacked charts + condensed issue queue cards; no wide data tables on phone
