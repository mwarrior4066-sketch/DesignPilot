# START_HERE

This is the simplest runtime front door for normal use.

## Fastest normal path
1. Open `dist/runtime/TASK_CHOOSER.md` if the task type is not obvious.
2. Load one launcher from `dist/runtime/task_launchers/`.
3. Start with `dist/SESSION_ZERO.md`.

## What this is for
Use this path when you want DesignPilot to help with a real task without manually assembling the system.

## Escalate only when needed
- Use a profile file from `dist/` when the job is clearly inside one domain but grows beyond a lightweight pass.
- Use `dist/DESIGNPILOT_DEPLOY.md` when multiple domains compete or proof-sensitive conflicts matter.
- Use manual lightweight assembly only for debugging, maintenance, or runtime inspection.

## Guardrails
- Do not manually assemble route + contract + skills for normal use.
- Prefer the smallest correct startup path.
- If the task widens, escalate instead of patching around ambiguity.
- DesignPilot improves structure and decision quality, but it does not replace research, engineering review, accessibility testing, or real-world validation.
