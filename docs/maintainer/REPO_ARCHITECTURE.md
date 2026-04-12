# Repository Architecture

DesignPilot now separates **source** from **distribution**.

## Primary layers
- `src/` — modular source of truth for operator logic, runtime overlays, schemas, skills, templates, libraries, and knowledge summaries.
- `dist/` — generated operator-facing deploy artifacts and release metadata.
- `docs/operator/` — human-facing operator entry docs.
- `docs/maintainer/` — maintainer workflow, compiler behavior, and repo structure rules.
- `evals/` — internal regression, benchmark, and external review storage.
- `proof/` — public-facing release cards, trust notes, and traceability artifacts.
- `config/` — manifests, profiles, tiers, budgets, and precedence metadata.
- `scripts/` — generation, validation, packaging, and maintenance automation.
