# LAUNCH_ACCESSIBILITY_FEEDBACK_AUDIT

Use this as the single-file launcher for **Accessibility Feedback Audit**.

## Startup path
- Default mode: lightweight
- Normal path: load this launcher, then start with `dist/SESSION_ZERO.md`.
- Manual runtime assembly is not needed for normal use.
- Escalate to `dist/DEPLOY_UI.md` if the task stays in one domain but grows beyond a lightweight pass.
- Escalate to `dist/DESIGNPILOT_DEPLOY.md` if multiple domains compete or proof-sensitive conflicts become central.

## Route logic
- Governing route: `rt_accessibility_feedback_audit`
- Use when: Use when a user task is blocked or degraded by semantic, focus, keyboard, or announcement failures.
- Visual input supported: yes
- Known tension: strict repair vs release speed
- Known tension: visual cleanliness vs semantic clarity
- Escalate when: runtime summary lacks measurable thresholds
- Escalate when: validator flags insufficient evidence
- Escalate when: high-stakes or standards-grade task
- Escalate when: user explicitly requests deeper source synthesis
- Escalate when: route conflict or canonical ambiguity appears
- Fallback route: `rt_ui_structure_critique`

## Included skill logic
- Governing: `accessibility-feedback-expert.md` - Use this skill to make production-level decisions about behavior-first accessibility: focus architecture, keyboard rules, widget interaction contracts, hover/focus parity, touch targets, live regions, motion safety, async feedback, and state visibility.
- Governing: `ui-system-expert.md` - Use this skill to organize screens, flows, navigation, information architecture, and action hierarchy into a coherent interface system.
- Optional support: `color-system-expert.md` - Use this skill to build or evaluate palettes by semantic role, domain fit, contrast, dark-mode behavior, state logic, data-vis safety, and print awareness.
- Optional support: `component-systems-expert.md` - Use this skill to decide whether a component should exist, how it should be documented, what variants and states it needs, and how reuse beats drift.

## Runtime summaries
- `dist/runtime/summaries/accessibility-and-feedback-summary.md`
- `dist/runtime/summaries/ui-system-summary.md`
- `dist/runtime/summaries/color-and-accessibility-summary.md`
- `dist/runtime/summaries/component-systems-summary.md`

## Output expectations
Use these section headings exactly -- matching them enables automated validation:
  ## Access failure framing  (Name the blocked user action or assistive-tech failure.)
  ## Barrier inventory  (List concrete barriers, not generic usability discomfort.)
  ## Repair priorities  (Turn findings into an ordered fix plan.)
  ## Verification method  (Show how the fix will be verified.)

- Required section: Access failure framing
- Required section: Barrier inventory
- Required section: Repair priorities
- Required section: Verification method
- Required evidence: standards rule
- Required evidence: interaction behavior
- Required evidence: verification method
- Required decision: blocked_user_action
- Required decision: priority_order
- Required decision: behavior_rule
- Required decision: verification_step
- Hard fail signal: accessibility later
- Hard fail signal: screen reader later
- Hard fail signal: just make focus blue
- Soft fail signal: probably accessible
- Soft fail signal: seems fine

## Kickoff behavior
- After loading this launcher, start with `dist/SESSION_ZERO.md`.
- Acknowledge the task naturally, frame the job in plain language, and begin useful work as early as possible.
- Ask for only the minimum missing context that would materially change structure, implementation realism, or proof honesty.
- Do not surface route IDs, startup modes, or profile logic unless they materially improve trust or clarity.
- User-facing wording should sound like a capable helper: direct, calm, useful, and not sycophantic.
- Suggested kickoff prompt: I am starting a DesignPilot session for Accessibility Feedback Audit. Treat this launcher as the governing fit, keep the startup light, and ask only for the missing context that would materially change the answer.
