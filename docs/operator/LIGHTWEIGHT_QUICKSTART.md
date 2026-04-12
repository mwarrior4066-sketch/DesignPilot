# Lightweight Quickstart

Use this path when the task is narrow enough that one route can govern it honestly.
Start broad, then narrow.

## 1. Confirm the task is a lightweight fit
Use lightweight mode when:
- one route clearly governs the task
- the output shape is bounded
- the job is not architecture-heavy, remediation-heavy, or release-sensitive

If that is not true, use a profile or the full kernel instead.

## 2. Pick the route from the task type
Start with `docs/operator/ROUTE_PICKER.md`.
Choose the route that best matches the governing job.

Example route:
- `dist/lite_routes/rt_ui_structure_critique.md`

## 3. Load the lite bootstrap and matching contract
Load:
- `dist/DEPLOY_LITE.md`
- `dist/lite_routes/rt_ui_structure_critique.md`
- `dist/lite_contracts/ui_structure_critique.md`

## 4. Add only the skill cards that materially matter
Governing cards for `rt_ui_structure_critique`:
- `src/runtime/cards/skills/ui-system-expert.md`
- `src/runtime/cards/skills/grid-system-expert.md`

Optional supporting cards:
- `src/runtime/cards/skills/type-system-expert.md`
- `src/runtime/cards/skills/accessibility-feedback-expert.md`

## 5. Start with session zero
Send the prompt in `dist/SESSION_ZERO.md`.

## 6. Escalate early instead of patching around missing logic
Switch to a profile or the kernel when:
- more than one route could govern the task
- architecture or proof sensitivity becomes central
- the route or contract explicitly says lightweight is unsafe
- the answer would otherwise depend on hidden assumptions

## Shortcut
Use a prebuilt starter from `dist/lite_starters/` if one matches your task.
