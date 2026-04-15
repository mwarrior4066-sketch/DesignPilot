# Lightweight Quickstart

Use this path when the task is narrow enough that one route can govern it honestly.
Start broad, then narrow.

## 1. Prefer the launcher-first path
Normal operators should start with a single-file launcher rather than assembling route, contract, and skill cards by hand.

Load:
- `dist/runtime/START_HERE.md`
- `dist/runtime/task_launchers/ui_structure_critique.md` or another matching launcher
- `dist/SESSION_ZERO.md`

## 2. Confirm the task is a lightweight fit
Use lightweight mode when:
- one route clearly governs the task
- the output shape is bounded
- the job is not architecture-heavy, remediation-heavy, or release-sensitive

If that is not true, use a profile or the full kernel instead.

## 3. Pick the launcher from the task type
Start with `dist/runtime/TASK_CHOOSER.md`.
Choose the launcher that best matches the governing job.

Example launcher:
- `dist/runtime/task_launchers/ui_structure_critique.md`

## 4. Use manual runtime assembly only as a fallback
If you are debugging, maintaining, or checking launcher internals, the manual path is:
- `dist/DEPLOY_LITE.md`
- `dist/runtime/route_cards/rt_ui_structure_critique.md`
- `dist/runtime/contracts_lite/ui_structure_critique.md`
- the needed runtime skill cards
- `dist/SESSION_ZERO.md`

## 5. Start with session zero
Send the prompt in `dist/SESSION_ZERO.md`.

## 6. Escalate early instead of patching around missing logic
Switch to a profile or the kernel when:
- more than one route could govern the task
- architecture or proof sensitivity becomes central
- the route or contract explicitly says lightweight is unsafe
- the answer would otherwise depend on hidden assumptions
