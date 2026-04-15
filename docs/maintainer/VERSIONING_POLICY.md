# Versioning Policy

The pack uses an `X.Y` public release scheme. Internal patch-level work may happen during a release cycle, but the public pack version can omit the patch suffix when those changes ship as one unified release line.

- `1.0` change = major (`X`) change
- `0.1` change = minor (`Y`) change

## Major (`X`)
Use a major bump when compatibility or canonical structure changes.
Examples:
- breaking project filesystem changes
- entrypoint or bootstrap contract changes
- release-line resets

## Minor (`Y`)
Use a minor bump for backward-compatible capability growth or bundled hardening that ships as one public release.
Examples:
- new executable schemas
- new validators
- new examples and benchmark systems
- stronger release gates
- bundled nonbreaking refinements that are released together

## Internal patch work
Patch-level fixes can still happen during development, but they do not need to appear in the public version string when they are folded into the current `X.Y` release line.
Examples:
- editorial cleanup
- metadata correction
- narrow bug fixes
- nonbreaking hardening

## Current release authority
- `PACK_MANIFEST.json` is the only canonical source for the current release version.
- `CHANGELOG.md` records release history and milestone progression.
- project context files, proof files, and indices may mention older versions only as historical milestones, never as the current release state.
- current-facing docs and metadata must match `PACK_MANIFEST.json` exactly.

## Line history
- old `v8.2.x` names normalize to the historical `v1.2.x` line
- `v2.0` marks the start of the current major line
- `v2.1` is the first capability-growth release on that line
