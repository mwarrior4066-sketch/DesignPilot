# Project State Protocol

The continuity layer distinguishes between four proof states and treats continuity as an artifact-backed system rather than a folder-presence ritual.

## Proof families
- **internal operator proof**: routes, contracts, validation, continuity, and failure-prevention behavior
- **comparative proof**: benchmark deltas, controlled baseline comparisons, and scored output differences
- **external confidence proof**: reviewer confidence, user confidence, live artifact reviews, and production-adjacent trust receipts
- **production outcome proof**: measured outcomes from real usage, implementation receipts, or shipped-system impact

## Required continuity files for every project
- `context/CASE_STUDY_ROADMAP.md`
- `context/ACTIVE_STATE.md`
- `problems_and_solutions/PROJECT_SPECIFIC_ERRORS.md`

## Required roadmap sections
Every project roadmap must include:
- `## Project identity`
- `## Proof state`
- `## Done before`
- `## Just added`
- `## Needed next`
- `## Open risks`
- `## Next validation move`
- `## Pending artifacts`
- `## Release readiness`

## Meaningful update threshold
Refresh continuity only when one of these happens:
- a benchmark run is added, removed, or materially rescored
- a new example or regression meaningfully changes the proven surface
- a proof claim changes class or wording strength
- validator, route, or contract behavior changes materially
- a new research prompt pack is stored
- a major project-specific error or decision is logged
- a handoff-ready artifact becomes exportable

Do **not** refresh continuity for tiny copy edits, formatting cleanup, or mirror regeneration by itself.

## Artifact-driven freshness rules
The roadmap and bundle manifest must carry:
- `Last meaningful update`
- `Artifact freshness anchor`
- artifact counts for benchmark runs, external confidence artifacts, and stored prompt packs

The freshness anchor must reflect the newest meaningful artifact in the project proof surface. If artifacts change and the roadmap or bundle manifest still report older counts or an older anchor, the workspace is stale.

## Required proof behavior for the flagship DesignPilot workspace
- keep a fixed prompt set for repeatable comparisons
- keep a claim-to-proof map that separates proof classes cleanly
- keep benchmark artifacts in `process/reviews/benchmarks/`
- keep a structured trust log and at least one external confidence artifact
- store research prompt packs in `process/research/prompt-packs/`
- refresh the roadmap, active state, and bundle manifest when the proof surface changes

## Release-readiness language
Continuity files must state what is:
- proven enough to say directly
- only safe to say comparatively or cautiously
- not allowed to claim yet

That keeps the case-study layer aligned with the real evidence state.


## Canonical structured state
- `context/state/continuity_evergreen.json` is the evergreen continuity source of truth for project identity, goal, and stable proof boundaries
- `context/state/release_state.json` is the release-specific continuity source of truth for current version, freshness, active next steps, blockers, and proof counts
- human-readable continuity docs are rendered from those structured state files
- workspace validation must check both the structured state and the rendered markdown outputs together
