# AI Quickstart

This file is the AI-facing startup surface.
Use it to start or route DesignPilot sessions.

Do not use `README.md` as runtime startup material.
`README.md` is the public GitHub overview for human readers.

## Primary startup path
Start with `dist/runtime/START_HERE.md`.
Choose the narrowest honest startup mode for the task.

## Startup selector
- **Fastest normal path** - `dist/runtime/START_HERE.md` + one launcher from `dist/runtime/task_launchers/` + `dist/SESSION_ZERO.md`
- **Full mode** - `dist/DESIGNPILOT_DEPLOY.md` + one profile + `dist/SESSION_ZERO.md`
- **Profile-only mode** - one profile + `dist/SESSION_ZERO.md`
- **Lightweight mode** - launcher-first startup via `dist/runtime/START_HERE.md`, one launcher, and `dist/SESSION_ZERO.md`
- **Manual lightweight mode** - `dist/DEPLOY_LITE.md` + one route card + one contract card + only the needed runtime skill cards + `dist/SESSION_ZERO.md`

## AI startup rules
- treat this file as the runtime quickstart
- do not mirror startup instructions, mode lists, or file-loading steps back to the user unless they explicitly ask
- do not treat `README.md` as operator authority
- begin with the runtime path, not the public repository overview
- surface only the minimum setup detail needed for the task
- do not use em dashes in user-facing replies

## Startup authority
- AI quickstart surface: `QUICKSTART.md`
- Normal operator runtime entrypoint: `dist/runtime/START_HERE.md`
- Compiled full-kernel authority: `dist/DESIGNPILOT_DEPLOY.md`
- Source startup authority for maintainers: `src/operator/core/MASTER_CHAT_OPERATOR.md`

## Read next
- `dist/runtime/START_HERE.md`
- `dist/runtime/TASK_CHOOSER.md`
- `docs/operator/OPERATOR_QUICKSTART.md`
- `docs/operator/DEPLOYMENT_GUIDE.md`
- `docs/operator/DEPLOYMENT_GUIDE.md`
- `docs/operator/PROFILE_GUIDE.md`
- `docs/operator/ROUTE_PICKER.md`
- `proof/PROOF_STATUS.md`
