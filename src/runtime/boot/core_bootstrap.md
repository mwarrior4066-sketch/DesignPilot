# Core Runtime Bootstrap

This is the thin runtime aide for the pack.
It is not a competing startup authority.
The single startup authority remains `src/operator/core/MASTER_CHAT_OPERATOR.md`.

## Default startup chain
1. `src/runtime/boot/core_bootstrap.md`
2. `src/runtime/boot/runtime_precedence.md`
3. selected route card in `src/runtime/cards/routes/`
4. selected contract card in `src/runtime/cards/contracts/`
5. required skill cards in `src/runtime/cards/skills/`
6. required runtime summaries in `src/knowledge-base/runtime-summaries/`

## Safe fallback
If any runtime overlay artifact is missing, stale, or ambiguous, fall back immediately to the canonical authority:
- routing: `src/schemas/routing_registry.json`
- contracts: `src/schemas/task_contracts.json`
- skills: `src/skills/*.md`
- summaries: `src/knowledge-base/summaries/*.md`
- source docs: `src/knowledge-base/source-docs/*`

## Runtime promises
- no capability loss
- no source-doc deletion
- no summary deletion
- mirrors are debug-only unless explicitly requested