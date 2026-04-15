# rt_accessibility_feedback_audit

**Task:** Accessibility Feedback Audit

## Route fit
- Role: governing
- Lightweight eligible: yes
- Governing route or helper: governing route

## Use when
- Use when a user task is blocked or degraded by semantic, focus, keyboard, or announcement failures.

## Startup recommendation
- Recommended mode: lightweight
- Default contract: `dist/runtime/contracts_lite/accessibility_feedback_audit.md`
- Recommended profile if you escalate: `dist/DEPLOY_UI.md`
- Visual input supported: yes

## Governing skills
- `dist/runtime/skills/accessibility-feedback-expert.md` - Use this skill to make production-level decisions about behavior-first accessibility: focus architecture, keyboard rules, widget interaction contracts, hover/focus parity, touch targets, live regions, motion safety, async feedback, and state visibility.
- `dist/runtime/skills/ui-system-expert.md` - Use this skill to organize screens, flows, navigation, information architecture, and action hierarchy into a coherent interface system.

## Optional supporting skills
- `dist/runtime/skills/color-system-expert.md` - Use this skill to build or evaluate palettes by semantic role, domain fit, contrast, dark-mode behavior, state logic, data-vis safety, and print awareness.
- `dist/runtime/skills/component-systems-expert.md` - Use this skill to decide whether a component should exist, how it should be documented, what variants and states it needs, and how reuse beats drift.

## Runtime summaries
- `dist/runtime/summaries/accessibility-and-feedback-summary.md`
- `dist/runtime/summaries/ui-system-summary.md`
- `dist/runtime/summaries/color-and-accessibility-summary.md`
- `dist/runtime/summaries/component-systems-summary.md`

## Contract shape
- Access failure framing
- Barrier inventory
- Repair priorities
- Verification method

## Escalate when
- runtime summary lacks measurable thresholds
- validator flags insufficient evidence
- high-stakes or standards-grade task
- user explicitly requests deeper source synthesis
- route conflict or canonical ambiguity appears

## Fallback
- Route fallback: `rt_ui_structure_critique`
- Canonical routing fallback: `src/schemas/routing_registry.json`
