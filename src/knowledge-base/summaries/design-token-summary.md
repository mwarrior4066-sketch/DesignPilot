---
summary_version: 1.0.0
source_reference:
  - src/knowledge-base/source-docs/AI Design Operator Pack Research.md
  - src/knowledge-base/source-docs/AI Design Operator Pack Improvement Brief.md
last_updated: 2026-04-09
synchronized: true
domain: design-tokens
---

# Design Token Summary

Primary sources: AI Design Operator Pack Research and token architecture references.

## Use this summary when
- the task needs tokens, semantic aliases, design-to-code translation, or system-level variable naming

## Core rules
- use primitive -> semantic -> component layers
- prefer flat human-readable names
- semantic aliases should shield components from raw values
- do not name tokens by value
- stateful components need stateful token or rule coverage

## Failure conditions
- hard-coded values in component code
- token names like `spacing-16px` or `border-red`
- missing dark-mode aliases
- components using primitives directly

## Evidence to return
- alias chain
- token naming pattern
- component/state mapping
