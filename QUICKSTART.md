# Quickstart

This pack is a routed design operator system, not a generic writing prompt.
It is designed to choose one governing route, load only the needed domain logic, and block polished but weak answers.

## Three deployment modes

### 1. Direct operator use
Use when you want the pack to answer normal requests in chat.
Load first:
- `operator/core/MASTER_CHAT_OPERATOR.md`
- `operator/core/TASK_ROUTER.md`
- `operator/core/SESSION_CONTEXT.md`

### 2. Runtime-first use
Use when you want lower token overhead.
Start from `operator/core/MASTER_CHAT_OPERATOR.md`, then use:
- `runtime/boot/core_bootstrap.md`
- `runtime/boot/runtime_precedence.md`

### 3. Maintenance/debug use
Use when you are patching the pack itself.
Start from:
- `operator/core/MASTER_CHAT_OPERATOR.md`
- `operator/governance/SYSTEM_PRECEDENCE.md`
- `operator/governance/CONTROL_AUTHORITY_MAP.md`
- relevant schema files in `schemas/`

## First conversation pattern
- load startup authority
- classify degraded mode if needed
- determine task weight
- run visual pre-pass if images are present
- choose one governing route
- load one contract and only the supporting skill cards you need
- answer directly

## Common failure modes
- overloading too many skills at once
- exposing full operator scaffolding in normal answers
- treating screenshots as proof of unseen behavior
- drifting into style talk before resolving the structural failure
- implying proof or validation without receipts

## What to read next
- `operator/core/MASTER_CHAT_OPERATOR.md`
- `operator/core/TASK_ROUTER.md`
- `operator/protocols/DEGRADED_MODE_PROTOCOL.md`
- `operator/protocols/VISUAL_INPUT_PROTOCOL.md`
- `operator/protocols/LIGHTWEIGHT_RESPONSE_PROTOCOL.md`
