# Operator Quickstart

Start with `dist/runtime/START_HERE.md`.
Choose the narrowest honest startup mode for the task.

## Startup selector
- **Fastest normal path**: `dist/runtime/START_HERE.md` -> one launcher in `dist/runtime/task_launchers/` -> `dist/SESSION_ZERO.md`
- **Full mode**: `dist/DESIGNPILOT_DEPLOY.md` + one profile + `dist/SESSION_ZERO.md`
- **Profile-only mode**: one profile + `dist/SESSION_ZERO.md`
- **Manual lightweight mode**: `dist/DEPLOY_LITE.md` + one route card + one contract card + only the needed runtime skill cards + `dist/SESSION_ZERO.md`

## Read next
- `dist/runtime/START_HERE.md`
- `dist/runtime/TASK_CHOOSER.md`
- `docs/operator/DEPLOYMENT_GUIDE.md`
- `docs/operator/PROFILE_GUIDE.md`
- `docs/operator/ROUTE_PICKER.md`

## Startup authority
- Operator entrypoint: `dist/runtime/START_HERE.md`
- Compiled full-kernel authority: `dist/DESIGNPILOT_DEPLOY.md`
- Source startup authority for maintainers: `src/operator/core/MASTER_CHAT_OPERATOR.md`

## Guardrail
Do not default to the full kernel unless the task is truly compound, cross-domain, remediation-heavy, or proof-sensitive.
