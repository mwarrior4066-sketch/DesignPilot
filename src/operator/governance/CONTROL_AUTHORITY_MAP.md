# Control Authority Map

## Canonical machine-readable authorities
- route selection and pathway metadata: `src/schemas/routing_registry.json`
- task-level output requirements: `src/schemas/task_contracts.json`
- validation rules and failure taxonomy: `src/schemas/validation_rules.json`
- executable output validation: `runtime_validator.py`
- example quality enforcement: `validate_examples.py`
- source resolvability: `SOURCE_REFERENCE_REGISTRY.json`

## Canonical release authorities
- current release version: `PACK_MANIFEST.json`
- release history and milestone chronology: `CHANGELOG.md`
- project context files may preserve older milestone language, but they may not override the current release defined by the manifest

## Canonical control docs
- startup authority: `MASTER_CHAT_OPERATOR.md`
- conflict resolution: `SYSTEM_PRECEDENCE.md`
- degraded-mode behavior: `DEGRADED_MODE_PROTOCOL.md`
- visual-input behavior: `VISUAL_INPUT_PROTOCOL.md`
- lightweight execution behavior: `LIGHTWEIGHT_RESPONSE_PROTOCOL.md`
- response trace policy: `RESPONSE_PROTOCOL.md`

## Runtime-first overlay authorities
These files exist to reduce default token load. They are generated overlays, not canonical truth.
- startup aides: `src/runtime/boot/core_bootstrap.md`, `src/runtime/boot/runtime_precedence.md`
- per-route runtime cards: `src/runtime/cards/routes/*.json`
- per-contract runtime cards: `src/runtime/cards/contracts/*.json`
- per-skill runtime cards: `src/runtime/cards/skills/*.md`
- per-summary runtime layer: `src/knowledge-base/runtime-summaries/*.md`
- source-doc section escalation index: `src/knowledge-base/indices/source_doc_sections.json`
- route-to-summary loading map: `src/knowledge-base/indices/runtime_summary_map.json`

## Human-readable mirrors — maintenance/debug only
These files remain valuable, but they are no longer runtime-first loading targets.
- route catalog: `ROUTE_CATALOG.md`
- output contract catalog: `OUTPUT_CONTRACTS_BY_TASK.md`
- skill reference map: `SKILL_REFERENCE_MAP.md`
- validation rulebook: `RUNTIME_VALIDATION_LAYER.md`
- quality rubric mirror: `PACK_QUALITY_RUBRIC.md`
- validation rubric notes: `VALIDATION_RUBRICS.md`

## Fail-safe rule
If any runtime overlay artifact is stale, missing, or ambiguous:
1. fall back to canonical schema
2. then canonical skill
3. then canonical summary
4. then indexed source-doc section
5. then full source doc only if still required

The runtime overlay may optimize hydration.
It may not silently remove or replace capability.

## Project continuity and proof
- canonical project shape: `PROJECT_FILE_SYSTEM_PROTOCOL.md`
- project continuity rules: `PROJECT_STATE_PROTOCOL.md`
- workspace liveness checks: `validate_project_workspace.py`
- flagship proof stack: `projects/designpilot/`
