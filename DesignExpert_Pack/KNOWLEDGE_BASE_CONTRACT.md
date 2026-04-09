# Knowledge Base Governance Contract v1.0

## 1. Directory architecture
- `/knowledge-base/source-docs/` = human-provided or canonical converted sources. Treat as **read-only**.
- `/knowledge-base/source-media/` = preserved media extracted from source docs. Treat as **read-only**.
- `/knowledge-base/summaries/` = AI-usable distilled references derived from source docs.
- `/knowledge-base/indices/` = AI-managed navigation maps for fast retrieval.

## 2. Population protocol
- The pack is not knowledge-ready unless `/knowledge-base/source-docs/` contains foundational project or standards documents.
- Every canonical summary should point back to a matching source doc.
- Visual-first sources that matter for interpretation, such as Pantone references, must remain preserved as visuals.

## 3. Runtime ownership
- The operator may read from `source-docs`, `source-media`, `summaries`, and `indices`.
- The operator must not rewrite `source-docs` or `source-media` during runtime.
- The operator should prefer `summaries` before `source-docs` unless deep reference is required.
- The operator should check `KNOWLEDGE_BASE_CHECKLIST.md` when auditing pack readiness or diagnosing stale knowledge.
