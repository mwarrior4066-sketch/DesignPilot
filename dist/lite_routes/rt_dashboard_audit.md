# rt_dashboard_audit

**Task:** Dashboard Audit

## Route fit
- Role: governing
- Lightweight eligible: yes
- Governing route or helper: governing route

## Use when
- Use for KPI hierarchy and chart-logic evaluation, not generic screen cleanup.

## Startup recommendation
- Recommended mode: lightweight
- Default contract: `dist/lite_contracts/dashboard_audit.md`
- Recommended profile if you escalate: `dist/DEPLOY_UI.md`
- Visual input supported: yes

## Governing skills
- `src/runtime/cards/skills/dashboard-data-expert.md` — Use this skill to make production-level decisions about dashboard type, KPI hierarchy, chart choice, density, filters, drill-down, and dense-data readability.
- `src/runtime/cards/skills/ui-system-expert.md` — Use this skill to organize screens, flows, navigation, information architecture, and action hierarchy into a coherent interface system.

## Optional supporting skills
- `src/runtime/cards/skills/accessibility-feedback-expert.md` — Use this skill to make production-level decisions about behavior-first accessibility: focus architecture, keyboard rules, widget interaction contracts, hover/focus parity, touch targets, live regions, motion safety, async feedback, and state visibility.
- `src/runtime/cards/skills/color-system-expert.md` — Use this skill to build or evaluate palettes by semantic role, domain fit, contrast, dark-mode behavior, state logic, data-vis safety, and print awareness.

## Runtime summaries
- `src/knowledge-base/runtime-summaries/dashboard-and-density-summary.md`
- `src/knowledge-base/runtime-summaries/ui-system-summary.md`
- `src/knowledge-base/runtime-summaries/accessibility-and-feedback-summary.md`
- `src/knowledge-base/runtime-summaries/color-and-accessibility-summary.md`

## Contract shape
- Dashboard role
- Key failures
- Evidence and rationale
- Recommended rebuild path

## Escalate when
- runtime summary lacks measurable thresholds
- validator flags insufficient evidence
- high-stakes or standards-grade task
- user explicitly requests deeper source synthesis
- route conflict or canonical ambiguity appears

## Fallback
- Route fallback: `rt_ui_structure_critique`
- Canonical routing fallback: `src/schemas/routing_registry.json`
