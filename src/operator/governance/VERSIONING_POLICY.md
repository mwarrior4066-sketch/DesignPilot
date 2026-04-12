# Versioning Policy

The pack uses an `X.Y.Z` scheme.

- `1.00` change = major (`X`) change
- `0.10` change = minor (`Y`) change
- `0.01` change = patch (`Z`) change

## Major (`X`)
Use a major bump when compatibility or canonical structure changes.
Examples:
- breaking project filesystem changes
- entrypoint or bootstrap contract changes
- release-line resets

## Minor (`Y`)
Use a minor bump for backward-compatible capability growth.
Examples:
- new executable schemas
- new validators
- new examples and benchmark systems
- stronger release gates

## Patch (`Z`)
Use a patch bump for nonbreaking fixes.
Examples:
- editorial cleanup
- metadata correction
- narrow bug fixes

## Current release authority
- `PACK_MANIFEST.json` is the only canonical source for the current release version.
- `CHANGELOG.md` records release history and milestone progression.
- project context files, proof files, and indices may mention older versions only as historical milestones, never as the current release state.
- current-facing docs and metadata must match `PACK_MANIFEST.json` exactly.

## Line history
- old `v8.2.x` names normalize to the historical `v1.2.x` line
- `v2.0.0` marks the start of the current line
- `v2.1.0` is the first capability-growth release on that line
