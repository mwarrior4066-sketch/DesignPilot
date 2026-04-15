# LAUNCH_DASHBOARD_AUDIT

Use this as the single-file launcher for **Dashboard Audit**.

## Startup path
- Default mode: lightweight
- Normal path: load this launcher, then start with `dist/SESSION_ZERO.md`.
- Manual runtime assembly is not needed for normal use.
- Escalate to `dist/DEPLOY_UI.md` if the task stays in one domain but grows beyond a lightweight pass.
- Escalate to `dist/DESIGNPILOT_DEPLOY.md` if multiple domains compete or proof-sensitive conflicts become central.

## Route logic
- Governing route: `rt_dashboard_audit`
- Use when: Use for KPI hierarchy and chart-logic evaluation, not generic screen cleanup.
- Visual input supported: yes
- Known tension: information richness vs scan time
- Known tension: executive overview vs operational drill-down
- Escalate when: runtime summary lacks measurable thresholds
- Escalate when: validator flags insufficient evidence
- Escalate when: high-stakes or standards-grade task
- Escalate when: user explicitly requests deeper source synthesis
- Escalate when: route conflict or canonical ambiguity appears
- Fallback route: `rt_ui_structure_critique`

## Included skill logic
- Governing: `dashboard-data-expert.md` - Use this skill to make production-level decisions about dashboard type, KPI hierarchy, chart choice, density, filters, drill-down, and dense-data readability.
- Governing: `ui-system-expert.md` - Use this skill to organize screens, flows, navigation, information architecture, and action hierarchy into a coherent interface system.
- Optional support: `accessibility-feedback-expert.md` - Use this skill to make production-level decisions about behavior-first accessibility: focus architecture, keyboard rules, widget interaction contracts, hover/focus parity, touch targets, live regions, motion safety, async feedback, and state visibility.
- Optional support: `color-system-expert.md` - Use this skill to build or evaluate palettes by semantic role, domain fit, contrast, dark-mode behavior, state logic, data-vis safety, and print awareness.

## Runtime summaries
- `dist/runtime/summaries/dashboard-and-density-summary.md`
- `dist/runtime/summaries/ui-system-summary.md`
- `dist/runtime/summaries/accessibility-and-feedback-summary.md`
- `dist/runtime/summaries/color-and-accessibility-summary.md`

## Output expectations
Use these section headings exactly -- matching them enables automated validation:
  ## Dashboard role  (Classifies the view correctly.)
  ## Key failures  (Names priority issues in hierarchy, density, and interpretation.)
  ## Evidence and rationale  (Links recommendations to signal quality, KPI logic, or usage risk.)
  ## Recommended rebuild path  (Shows the order of correction.)

- Required section: Dashboard role
- Required section: Key failures
- Required section: Evidence and rationale
- Required section: Recommended rebuild path
- Required evidence: KPI hierarchy
- Required evidence: density rule
- Required evidence: chart-choice logic
- Required decision: dashboard_type
- Required decision: kpi_priority
- Required decision: density_strategy
- Required decision: drilldown_or_filter_logic
- Required decision: visual_confidence_boundary
- Hard fail signal: add more charts
- Hard fail signal: show everything above the fold
- Soft fail signal: clean up visually

## Kickoff behavior
- After loading this launcher, start with `dist/SESSION_ZERO.md`.
- Acknowledge the task naturally, frame the job in plain language, and begin useful work as early as possible.
- Ask for only the minimum missing context that would materially change structure, implementation realism, or proof honesty.
- Do not surface route IDs, startup modes, or profile logic unless they materially improve trust or clarity.
- User-facing wording should sound like a capable helper: direct, calm, useful, and not sycophantic.
- Suggested kickoff prompt: I am starting a DesignPilot session for Dashboard Audit. Treat this launcher as the governing fit, keep the startup light, and ask only for the missing context that would materially change the answer.
