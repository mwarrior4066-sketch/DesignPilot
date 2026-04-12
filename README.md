# DesignPilot v2.6.1

DesignPilot is a modular AI design operator system with a **compiled deployment surface** and an official **lightweight startup path**.

This repo now separates:
- `src/` for modular maintainer-facing source files
- `dist/` for generated operator-facing deployment artifacts
- `docs/operator/` for startup modes and quickstarts
- `docs/maintainer/` for compiler, validation, and release workflow
- `evals/` and `proof/` for evidence and trust artifacts

## Startup choices
1. **Full mode** — `dist/DESIGNPILOT_DEPLOY.md` + one profile + `dist/SESSION_ZERO.md`
2. **Profile-only mode** — one profile + `dist/SESSION_ZERO.md`
3. **Lightweight mode** — `dist/DEPLOY_LITE.md` + one route card + one contract card + only the needed skill cards + `dist/SESSION_ZERO.md`

## Fastest operator path
- Read `docs/operator/OPERATOR_QUICKSTART.md`
- Then choose between `docs/operator/STARTUP_MODES.md`, `docs/operator/LIGHTWEIGHT_QUICKSTART.md`, and `docs/operator/PROFILE_GUIDE.md`

## Maintainer path
Read `docs/maintainer/MAINTAINER_GUIDE.md`.
