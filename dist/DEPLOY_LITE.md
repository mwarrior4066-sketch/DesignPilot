# DEPLOY_LITE

DesignPilot lite mode is the narrow startup path for bounded single-route work.
Use it when one route clearly governs the task and loading a full profile or the kernel would be unnecessary overhead.

## What lite mode is for
- single-domain tasks with one honest governing route
- low-to-medium risk work where the output shape is already known
- sessions where you want DesignPilot discipline without loading the whole package

## Preferred operator path
1. `dist/runtime/START_HERE.md` if you are starting fresh
2. one single-file launcher from `dist/runtime/task_launchers/` when the task type is known
3. `dist/SESSION_ZERO.md`

## Manual fallback load order
Use this only when you are maintaining the pack or debugging a launcher.
1. `dist/DEPLOY_LITE.md`
2. one route card from `dist/runtime/route_cards/`
3. the matching contract card from `dist/runtime/contracts_lite/`
4. only the governing skill cards and truly needed supporting skill cards
5. `dist/SESSION_ZERO.md`

## What lite mode keeps
- DesignPilot identity and claim-boundary honesty
- one-governing-route discipline
- explicit escalation when the task stops being safely bounded
- canonical fallback to source schemas, source skills, and full summaries

## What lite mode does not try to do
- replace the kernel for compound work
- settle cross-domain routing conflicts by itself
- carry the full governance surface for remediation, architecture, or release-sensitive work
- hide uncertainty when the correct answer is to escalate

## Lite operating rules
- stay inside one honest route
- use the route card to decide the task fit before loading extra skills
- use the contract card to define what done looks like
- add supporting skills only when they materially change the answer
- fail closed and escalate rather than improvising missing logic

## Escalate to a profile or the kernel when
- more than one route could honestly govern the task
- architecture, remediation, release readiness, or proof sensitivity becomes central
- accessibility semantics, PDF structure, or back-end feasibility are high-stakes
- the route card or contract card marks the task as unsafe for lightweight execution
- the answer would otherwise hide uncertainty or overclaim confidence

## Canonical fallback sources
- routing: `src/schemas/routing_registry.json`
- contracts: `src/schemas/task_contracts.json`
- skills: `src/skills/*.md`
- summaries: `src/knowledge-base/summaries/*.md`

## Source anchors behind lite mode
- `src/runtime/boot/core_bootstrap.md`
- `src/runtime/boot/runtime_precedence.md`
- `src/operator/protocols/LIGHTWEIGHT_RESPONSE_PROTOCOL.md`
- `src/operator/protocols/DEGRADED_MODE_PROTOCOL.md`
- `src/operator/governance/SYSTEM_PRECEDENCE.md`
