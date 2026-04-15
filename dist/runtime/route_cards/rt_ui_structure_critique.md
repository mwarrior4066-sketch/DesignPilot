# rt_ui_structure_critique

**Task:** UI Structure Critique

## Route fit
- Role: governing
- Lightweight eligible: yes
- Governing route or helper: governing route

## Use when
- Prefer this route when the user wants structural diagnosis before polish.

## Startup recommendation
- Recommended mode: lightweight
- Default contract: `dist/runtime/contracts_lite/ui_structure_critique.md`
- Recommended profile if you escalate: `dist/DEPLOY_UI.md`
- Visual input supported: yes

## Governing skills
- `dist/runtime/skills/ui-system-expert.md` - Use this skill to organize screens, flows, navigation, information architecture, and action hierarchy into a coherent interface system.
- `dist/runtime/skills/grid-system-expert.md` - Use this skill to choose new grid systems by medium and content type: web, app, slide, editorial, dashboard, and document layouts.

## Optional supporting skills
- `dist/runtime/skills/type-system-expert.md` - Use this skill to choose, compare, pair, substitute, and deploy typefaces intelligently across UI, editorial, brand, dashboards, presentations, print, accessibility-sensitive, and multilingual systems.
- `dist/runtime/skills/accessibility-feedback-expert.md` - Use this skill to make production-level decisions about behavior-first accessibility: focus architecture, keyboard rules, widget interaction contracts, hover/focus parity, touch targets, live regions, motion safety, async feedback, and state visibility.

## Runtime summaries
- `dist/runtime/summaries/ui-system-summary.md`
- `dist/runtime/summaries/grid-mediums-summary.md`
- `dist/runtime/summaries/typography-summary.md`
- `dist/runtime/summaries/typeface-database-summary.md`
- `dist/runtime/summaries/accessibility-and-feedback-summary.md`

## Contract shape
- Problem framing
- Findings
- Recommendations
- Tradeoffs

## Escalate when
- runtime summary lacks measurable thresholds
- validator flags insufficient evidence
- high-stakes or standards-grade task
- user explicitly requests deeper source synthesis
- route conflict or canonical ambiguity appears

## Fallback
- Route fallback: `rt_case_study_rewrite`
- Canonical routing fallback: `src/schemas/routing_registry.json`
