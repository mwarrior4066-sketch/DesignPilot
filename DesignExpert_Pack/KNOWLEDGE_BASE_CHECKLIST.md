# Pre-Deployment Readiness Checklist

| Category | Checkpoint | Status (Y/N) |
|---|---|---|
| Integrity | Are source docs present in `/knowledge-base/source-docs/`? | [ ] |
| Integrity | Are preserved visual sources kept where markdown would lose meaning? | [ ] |
| Coverage | Does each major source domain have a matching summary? | [ ] |
| Metadata | Do summaries identify their source domain clearly? | [ ] |
| Cleanliness | Is `/knowledge-base/indices/` free of duplicate nav maps? | [ ] |
| Sync | Are skills and summaries aligned with the latest source docs? | [ ] |

## Final status
- Ready
- Ready with warnings
- Not ready


## Governance Enforcement
- Run `python3 lint_pack.py` from the pack root before release.
- Use `python3 lint_pack.py --strict` for CI or pre-commit enforcement.
- The linter treats `synchronized: false` and missing frontmatter as hard errors.
