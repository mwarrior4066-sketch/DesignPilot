# Runtime Precedence

## Runtime-first overlay
Use the generated runtime overlay as the first hop for token-efficient execution:
1. route card
2. contract card
3. skill cards
4. runtime summary
5. full summary only on escalation
6. indexed source-doc section before full source-doc load

## Canonical fallback rule
The runtime overlay is an optimization layer only. It is never the sole source of truth.

If the overlay conflicts with a canonical source, the canonical source wins.

## Debug-only files
Do not load these at runtime unless debugging, maintaining, or explaining the pack itself:
- `ROUTE_CATALOG.md`
- `OUTPUT_CONTRACTS_BY_TASK.md`
- `SKILL_REFERENCE_MAP.md`
- `RUNTIME_VALIDATION_LAYER.md` as prose explanation only
- `PACK_QUALITY_RUBRIC.md`
- `VALIDATION_RUBRICS.md`