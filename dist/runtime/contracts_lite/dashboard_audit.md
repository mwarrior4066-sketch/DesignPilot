# dashboard_audit

**Title:** Dashboard Audit

## Required sections
- Dashboard role
- Key failures
- Evidence and rationale
- Recommended rebuild path

## Required evidence types
- KPI hierarchy
- density rule
- chart-choice logic

## Required decisions
- dashboard_type
- kpi_priority
- density_strategy
- drilldown_or_filter_logic
- visual_confidence_boundary

## Hard-fail signals
- These are output patterns that mean the task is not done yet or is unsafe to accept.
- add more charts
- show everything above the fold

## Soft-fail signals
- These are weak-output signs that usually require revision, specificity, or escalation.
- clean up visually

## Execution boundaries
- Lightweight supported: yes
- Default weight: `standard`
- Allowed modes: AUDIT, PEER
- Allowed phases: strategy, structure, ui

## Canonical source
- `src/schemas/task_contracts.json#dashboard_audit`
