# Startup Modes

DesignPilot now supports three official startup modes.

## 1. Full mode
Use for compound or cross-domain work.

Load:
- `dist/DESIGNPILOT_DEPLOY.md`
- one profile file from `dist/`
- `dist/SESSION_ZERO.md`

Use this when:
- multiple domains compete
- proof sensitivity is high
- the task changes release readiness, remediation posture, or architecture direction

## 2. Profile-only mode
Use for focused single-domain work.

Load:
- one of `dist/DEPLOY_CORE.md`, `dist/DEPLOY_UI.md`, or `dist/DEPLOY_BRAND.md`
- `dist/SESSION_ZERO.md`

Use this when:
- the task is clearly inside one domain
- you want stronger domain coverage than lite mode
- you do not need the full kernel body or true cross-domain arbitration

## 3. Lightweight mode
Use for bounded route-specific work.

Load:
- `dist/DEPLOY_LITE.md`
- one route card from `dist/lite_routes/`
- one contract card from `dist/lite_contracts/`
- only the needed skill cards from `src/runtime/cards/skills/`
- `dist/SESSION_ZERO.md`

Use this when:
- the task has one clear governing route
- the output is bounded and low-to-medium risk
- the task does not need deep cross-domain coordination

## Current route coverage
- lightweight-eligible routes: 11
- total routes: 18
- routes that should escalate immediately: 7
