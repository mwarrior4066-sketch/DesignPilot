# Dashboard Audit Example
Fixture: tests/fixtures/dashboard-audit.prompt.md
Validation result: tests/evals/dashboard-audit.eval.json

## Input Prompt
Audit an operations dashboard that currently shows 14 KPIs, 6 charts, and a large table on the first view. Managers say they cannot tell whether they should act or just observe.

## Selected Route and Loaded Skills
- Route: `rt_dashboard_audit`
- Task contract: `dashboard_audit`
- Mode: AUDIT
- Phase: strategy
- Skills: `dashboard-data-expert.md`, `ui-system-expert.md`

## Final Output
### Dashboard role
This is trying to act like an executive summary, an operational triage screen, and a reporting archive at the same time. That role collision is the root failure because the first view cannot decide whether it should guide action, summarize status, or store reporting context.

### Key failures
- KPI cards are equal weight, so high-severity signals do not rise above passive metrics.
- Six charts on first view forces chart reading before action framing. That increases cognitive load without improving decision speed.
- The large table appears before the user knows whether the current state is healthy, risky, or blocked.
- The empty-state and filter logic are missing, so users cannot tell when data is absent versus when no issue exists.

### Evidence and rationale
The primary question for an operations dashboard is “Do I need to intervene now?” A first view with 14 KPIs cannot answer that quickly. The safer pattern is a triage stack: status summary, exceptions, then drill-down. The obvious alternative is to preserve the full KPI wall and restyle it, but that would still force users to scan before they know the governing question. The tradeoff is breadth versus clarity. Breadth loses first because intervention latency is the more important threshold.

### Recommended rebuild path
1. Reclassify the dashboard as an operational triage view.
2. Reduce the first view to a status band, 3–5 critical KPIs, and one exceptions table.
3. Move trend charts into secondary drill-down views.
4. Add explicit filter, empty-state, and “data freshness” treatments so confidence is not inferred blindly.
5. Keep one export path, but do not let reporting needs set the first-view layout.

## Why This Passed
- It identifies the dashboard-type mismatch.
- It uses a rebuild order rather than a loose list of improvements.
- It connects density to decision speed.
- It includes one explicit tradeoff and a governing question.

## What Would Have Failed
- “Use better colors” or “make the charts more engaging.”
- Adding yet another chart to “clarify trends.”
- Treating the first view like a complete reporting surface.

## Revision Pass
The shallow draft only suggested grouping the charts. The corrected version redefined the dashboard role first, because layout changes without role clarity would keep the same failure in a cleaner wrapper.
