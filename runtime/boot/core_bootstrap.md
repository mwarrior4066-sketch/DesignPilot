# Core Runtime Bootstrap

This is the thin runtime aide for the pack.
It is not a competing startup authority.
The single startup authority remains `MASTER_CHAT_OPERATOR.md`.

## Default startup chain
1. `runtime/boot/core_bootstrap.md`
2. `runtime/boot/runtime_precedence.md`
3. selected route card in `runtime/cards/routes/`
4. selected contract card in `runtime/cards/contracts/`
5. required skill cards in `runtime/cards/skills/`
6. required runtime summaries in `knowledge-base/runtime-summaries/`

## Safe fallback
If any runtime overlay artifact is missing, stale, or ambiguous, fall back immediately to the canonical authority:
- routing: `schemas/routing_registry.json`
- contracts: `schemas/task_contracts.json`
- skills: `skills/*.md`
- summaries: `knowledge-base/summaries/*.md`
- source docs: `knowledge-base/source-docs/*`

## Runtime promises
- no capability loss
- no source-doc deletion
- no summary deletion
- mirrors are debug-only unless explicitly requested