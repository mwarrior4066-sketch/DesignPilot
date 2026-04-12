# Skill Synchronization Protocol (SSP)

## Standard frontmatter block
Every runtime skill file in `src/skills/` must begin with this YAML block:

```yaml
---
skill_version: 1.0.0
source_reference:
  - src/knowledge-base/summaries/example-summary.md
  - src/knowledge-base/source-docs/example-source.md
last_updated: 2026-04-09
synchronized: true
canonical_owner: true
domain: example-domain
---
```

### Field meanings
- `skill_version`: semantic version for the skill file itself.
- `source_reference`: ordered list of summary/source docs that ground the skill.
- `last_updated`: last date the skill logic was synchronized.
- `synchronized`: `true` only when the skill has been checked against its source references.
- `canonical_owner`: `true` when the skill is the canonical owner of that logic domain.
- `domain`: short machine-readable domain label.

## Versioning schema
- **MAJOR** = breaking logic change or source replacement
- **MINOR** = substantive new capability or domain logic
- **PATCH** = maintenance, wording, formatting, or cleanup

## Staleness triggers
A skill or summary should be treated as stale when:
1. its logic clearly predates a newer source document
2. a canonical summary contradicts a source doc
3. a control file changes a runtime contract the skill depends on
4. a human flags a project strategy change that invalidates its assumptions
5. the file is missing the standard frontmatter block
6. `synchronized: false`

## Re-sync workflow
1. Read the changed source doc or control file.
2. Compare current skill/summary logic against the new source.
3. Update only the canonical owner file for that logic.
4. Bump version according to change severity.
5. Refresh the frontmatter block.
6. Note the sync in `CHANGELOG.md`.

## Runtime rule
Do not duplicate source logic across multiple skills just to “keep them updated.”
Update the canonical owner and let routing/reference maps point to it.

## Validation rule
A skill file is non-compliant if it lacks the frontmatter block or if `source_reference` is empty.


## Enforcement
After any sync or edit affecting `src/skills/` or `src/knowledge-base/summaries/`, run `python3 lint_pack.py`.
Use `--strict` when the pack is under release or CI review.
