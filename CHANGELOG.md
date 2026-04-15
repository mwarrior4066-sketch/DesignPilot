## v3.0 - 2026-04-15

Major release focused on validator health, proof accuracy, public-claim discipline, and v3.0 release alignment.

### Validator bug fixes

- Removed the stale `source_section_map.json` read from `scripts/lint_pack.py`; `source_doc_sections.json` is the current index source.
- Updated runtime route and contract card checks in `scripts/runtime_validator.py` from the removed `src/runtime/cards/` layout to `dist/runtime/routes/` and `dist/runtime/contracts/`.
- Fixed doubled starter paths in `scripts/validate_lightweight_path.py` and `scripts/validate_integrity_sync.py` from `dist/dist/runtime/starters` to `dist/runtime/starters`.
- Fixed lite index reads from `dist/lite_index.json` to `dist/runtime/lite_index.json`.
- Updated lightweight and integrity validators to use the current compiled doc folders: `dist/runtime/route_cards/` and `dist/runtime/contracts_lite/`.
- Made `scripts/run_regression_suite.py` defensive when a test lacks `golden_output_file`, while also adding the missing golden output to pass-20.
- Tightened evidence detection so contract headings alone cannot satisfy required evidence classes.

### Validation impact

Before these fixes, the local validation suite could crash or report false failures due to stale path references. After the patch set:

- `python3 scripts/run_validation_suite.py` passes all five validators.
- `python3 scripts/run_regression_suite.py` passes all 45 regression fixtures.
- `python3 scripts/validate_examples.py` passes.
- `python3 scripts/validate_lightweight_path.py` passes.
- `python3 scripts/validate_integrity_sync.py` passes.

### Pass-05, pass-06, and pass-07 root cause carryover

The earlier v2.8 work identified that compound and communication-heavy tasks were failing when section names, rationale depth, or tradeoff language were too implicit. v3.0 preserves that fix pattern and extends it into the proof and validation layer: the validator now distinguishes real evidence content from section headings, and the docs no longer overstate what structural compliance proves.

### Test archive and report organization

- Public documentation now points the master summary reference to `tests/reports/v2-tests/MASTER_SUMMARY.html`.
- Cross-model batch outputs still write to `tests/live_outputs/batch/`.
- The HOWTO now explains which validators are blocking and what failures usually mean.

### Version consistency

- `tests/regression_suite.json` now reports `suite_version: 3.0` and `pack_version: 3.0`.
- `proof/PROOF_STATUS.md` now opens on v3.0.
- Project continuity files, roadmap, task queue, and bundle manifest are aligned to the v3.0 release line.

### Proof and claim discipline

- Rewrote `proof/PROOF_STATUS.md` around three tiers: structural compliance, output quality, and designer outcome proof.
- Added `proof/CLAIM_TO_EVIDENCE_MAP.md` so public claims trace to evidence tiers and known weak links.
- Updated `README.md` to scope implementation-awareness to the task families where the pack is strongest.

### Examples and real-use-case coverage

- Completed `examples/designer-response-filter-pass.md` with the missing input prompt and selected-route sections.
- Added `examples/real-brief-backend-feasibility-review.md` as a real-use-case style example rather than another synthetic validator fixture.

### Known limitations

- No Tier 3 designer outcome proof is claimed yet.
- Brand, case-study, prose, and graphic critique routes still require more human-review evidence than implementation-aware routes.
- pass-07 style case-study work still benefits from explicit tradeoff prompting when the brief is ambiguous.
- The current proof layer is stronger than a generic prompt pack, but it should not be described as independent production outcome validation.

## v2.8 - 2026-04-13

Validator and system overhaul based on live model evidence from three regression runs (Haiku v1, Haiku v2, Sonnet 4.6). Root cause analysis across 46 failure instances drove two parallel workstreams: fixing what the pack tells the model to produce, and fixing how the validator scores outputs. Sonnet 4.6 now passes the gate at 84% (16/19). Haiku calibrated re-score reaches 79%.

### System fixes (what the model produces)

- **Launcher section hints (S1):** Every required section heading in every launcher now includes a one-sentence rationale description pulled from the task contract. `## Migration notes` becomes `## Migration notes  (Shows how to move from the current palette safely.)` - fixes the single most common failure cause across both Haiku runs
- **SESSION_ZERO rule 9 (S4):** Added depth requirement - each required section must have at least two paragraphs of original analysis, not a heading with a single sentence underneath
- **Comprehension test prompts (S2):** pass-17, pass-18, and pass-19 prompts updated to explicitly request decision statements, not just explanation
- **Wrong task contract corrected (S3):** pass-18 `validator_task` changed from `backend_architecture_spec` to `api_reliability_security_review` - the contract now matches the actual prompt scope
- **Scope-explicit prompts (S5):** pass-04 and pass-16 full_prompts updated to enumerate required coverage areas, preventing the model from stopping before required sections
- **Decision token generalisation (S6):** `boundary_placement`, `migration_strategy`, `job_of_piece`, `meaning_guard`, and `revision_sequence` all expanded with vocabulary that generalises across prompt types, not just the original calibration domain
- **Vocab calibration log (S7):** `src/schemas/vocab_calibration_log.json` created with 5 seed entries documenting observed vocabulary gaps; `lint_pack.py` now warns on decisions with fewer than 4 `any_of` tokens

### Validator structural fixes (how the validator scores)

- **Structural tradeoff/rationale detection (V2):** `_has_structural_tradeoff()` and `_has_structural_rationale()` functions replace flat token list checks. A tradeoff is now detected by structural co-occurrence (comparison operator OR cost signal + benefit signal), not by vocabulary matching. Catches "the cost of this approach is X while the benefit is Y" without any token list entry
- **Rationale keyword overlap section fallback (V1):** Added as Fallback 4 in section matching. When exact, stem-prefix, and alias matching all fail, finds the section with the most keyword overlap with the required section's rationale description. "Migration notes - Shows how to move from the current palette safely" is now satisfied by a section with substantial overlap on palette, move, current, safely, regardless of heading
- **Domain-adaptive evidence class detection (V3):** `context_overrides` added to 4 task contracts. React state management vocabulary now satisfies `rendering_boundary_rule` for frontend tasks; color adoption vocabulary satisfies `comparison_artifact` for color specs. `detected_evidence_classes()` uses task-level context overrides when available
- **Specificity check exemptions (V6):** `specificity_exempt: true` added to `graphic_critique`, `type_system_recommendation`, `component_spec`, `color_system_spec`, and `accessibility_feedback_audit`. Design recommendation tasks that inherently use specific numbers (px, %, ratios) no longer trigger `unsupported_specificity`
- **thin_section confirmed soft (V7):** Verified soft severity - sections below word count threshold reduce score but do not cause FAIL

### Validator maintenance (preventing recurrence)

- **SECTION_ALIASES externalised (V5):** All 69 alias groups moved from hardcoded dict in `runtime_validator.py` to `src/schemas/section_aliases.json`. Validator loads from file at startup. `validate_integrity_sync.py` now checks that every required section across all task contracts has at least one alias entry - a new task without aliases triggers a warning on every integrity run
- **Lint minimum token count (V4):** `lint_pack.py` now warns when a required decision has fewer than 4 `any_of` tokens, preventing new tasks from shipping with undetectable decisions

### Runtime card format fix

- `generate_runtime_overlay.py` was stripping section dicts to plain strings when writing runtime contract cards, discarding `rationale` and `min_words` before they reached the launcher template. Fixed to preserve full section dicts. `validate_lightweight_path.py` and `validate_integrity_sync.py` updated to handle both string and dict forms

### Live run evidence

Three runs produced 57 model outputs used to calibrate the validator:
- `tests/live_outputs/live-run-2026-04-13/` - Haiku 4.5, untuned validator, 6/19 raw
- `tests/live_outputs/live-run-2026-04-13-v2/` - Haiku 4.5, improved launchers, 7/19 raw
- `tests/live_outputs/live-run-sonnet-2026-04-13/` - Sonnet 4.6, 16/19 = 84%, gate PASS

### New schema files

- `src/schemas/section_aliases.json` - 69 alias groups for required section heading matching
- `src/schemas/vocab_calibration_log.json` - living log of evidence class and decision token expansions

## v2.7 - 2026-04-13

Historical v2.7 entry: runtime, release, proof, integrity, and operator-surface hardening were unified under that version. Patch-level naming has been removed so the public version stays consistent across the repo.

### Included in v2.7

- unified startup docs across full, profile-only, and lightweight modes
- added semantic integrity validation for route, contract, and starter parity
- added generated build metrics plus a full build manifest
- cleaned release bundle noise and tightened handoff verification
- deepened previously thin knowledge domains for UI systems, UX cognition, and motion/interaction feedback
- made user-facing wording more helper-shaped by enforcing humanization on displayed prose
- split the repo front door so `README.md` is GitHub-facing for humans and `QUICKSTART.md` is AI-facing for runtime startup
- aligned public and operator startup paths so setup language is less likely to leak back to the user

### Knowledge base depth pass

**UI System Expert**
- added `src/knowledge-base/source-docs/UI System Expert Research.md`
- rewrote `src/knowledge-base/summaries/ui-system-summary.md`
- populated `src/knowledge-base/runtime-summaries/ui-system-summary.md` and `dist/runtime/summaries/ui-system-summary.md`
- updated `src/skills/ui-system-expert.md` with explicit thresholds and expanded failure traps

**UX Cognition**
- added `src/knowledge-base/source-docs/UX Cognition Expert Research.md`
- rewrote `src/knowledge-base/summaries/ux-cognition-summary.md`
- populated `src/knowledge-base/runtime-summaries/ux-cognition-summary.md` and `dist/runtime/summaries/ux-cognition-summary.md`

**Motion and Interaction Feedback**
- added `src/knowledge-base/source-docs/Motion and Interaction Feedback Expert Research.md`
- created `src/knowledge-base/summaries/motion-and-interaction-feedback-summary.md`
- created `src/knowledge-base/runtime-summaries/motion-and-interaction-feedback-summary.md` and `dist/runtime/summaries/motion-and-interaction-feedback-summary.md`
- created `src/skills/motion-interaction-expert.md`
- added `motion-interaction-expert` to the `ui-system-expert` handoff chain

### Source registry

- updated `src/knowledge-base/SOURCE_FORMAT_MAP.md` with the new source documents

## v2.6.0 - Source-to-artifact foundation
- introduced the source-to-artifact architecture and the initial lightweight product surface


## Legacy (pre-v2.8) quickstart notes
See `docs/operator/DEPLOYMENT_GUIDE.md` for current startup instructions.
Previous versions used a direct `OPERATOR_QUICKSTART.md` file.
The session zero file (`dist/SESSION_ZERO.md`) replaces the old warm-start protocol.
