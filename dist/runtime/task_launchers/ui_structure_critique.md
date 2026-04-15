# LAUNCH_UI_STRUCTURE_CRITIQUE

Use this as the single-file launcher for **UI Structure Critique**.

## Startup path
- Default mode: lightweight
- Normal path: load this launcher, then start with `dist/SESSION_ZERO.md`.
- Manual runtime assembly is not needed for normal use.
- Escalate to `dist/DEPLOY_UI.md` if the task stays in one domain but grows beyond a lightweight pass.
- Escalate to `dist/DESIGNPILOT_DEPLOY.md` if multiple domains compete or proof-sensitive conflicts become central.

## Route logic
- Governing route: `rt_ui_structure_critique`
- Use when: Prefer this route when the user wants structural diagnosis before polish.
- Visual input supported: yes
- Known tension: density vs readability
- Known tension: brand expression vs task clarity
- Escalate when: runtime summary lacks measurable thresholds
- Escalate when: validator flags insufficient evidence
- Escalate when: high-stakes or standards-grade task
- Escalate when: user explicitly requests deeper source synthesis
- Escalate when: route conflict or canonical ambiguity appears
- Fallback route: `rt_case_study_rewrite`

## Included skill logic
- Governing: `ui-system-expert.md` - Use this skill to organize screens, flows, navigation, information architecture, and action hierarchy into a coherent interface system.
- Governing: `grid-system-expert.md` - Use this skill to choose new grid systems by medium and content type: web, app, slide, editorial, dashboard, and document layouts.
- Optional support: `type-system-expert.md` - Use this skill to choose, compare, pair, substitute, and deploy typefaces intelligently across UI, editorial, brand, dashboards, presentations, print, accessibility-sensitive, and multilingual systems.
- Optional support: `accessibility-feedback-expert.md` - Use this skill to make production-level decisions about behavior-first accessibility: focus architecture, keyboard rules, widget interaction contracts, hover/focus parity, touch targets, live regions, motion safety, async feedback, and state visibility.

## Runtime summaries
- `dist/runtime/summaries/ui-system-summary.md`
- `dist/runtime/summaries/grid-mediums-summary.md`
- `dist/runtime/summaries/typography-summary.md`
- `dist/runtime/summaries/typeface-database-summary.md`
- `dist/runtime/summaries/accessibility-and-feedback-summary.md`

## Output expectations
Use these section headings exactly -- matching them enables automated validation:
  ## Problem framing  (Sets the user-task and failure frame.)
  ## Findings  (Surface real structural failures instead of taste comments.)
  ## Recommendations  (Convert critique into concrete structural action.)
  ## Tradeoffs  (Show what is preserved and what can flex first.)

- Required section: Problem framing
- Required section: Findings
- Required section: Recommendations
- Required section: Tradeoffs
- Required evidence: task logic
- Required evidence: hierarchy rule
- Required evidence: layout constraint
- Required decision: structural_failure
- Required decision: hierarchy_winner
- Required decision: intervention_order
- Required decision: tradeoff_resolution
- Required decision: visual_confidence_boundary
- Hard fail signal: looks great as-is
- Hard fail signal: just make it prettier
- Hard fail signal: finalize the UI now
- Soft fail signal: could maybe
- Soft fail signal: might want to consider

## Kickoff behavior
- After loading this launcher, start with `dist/SESSION_ZERO.md`.
- Acknowledge the task naturally, frame the job in plain language, and begin useful work as early as possible.
- Ask for only the minimum missing context that would materially change structure, implementation realism, or proof honesty.
- Do not surface route IDs, startup modes, or profile logic unless they materially improve trust or clarity.
- User-facing wording should sound like a capable helper: direct, calm, useful, and not sycophantic.
- Suggested kickoff prompt: I am starting a DesignPilot session for UI Structure Critique. Treat this launcher as the governing fit, keep the startup light, and ask only for the missing context that would materially change the answer.
