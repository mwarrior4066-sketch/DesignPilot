# Changelog

## v2.5.0 — color and typography knowledge refresh
- added a new digital `COLOR_LIBRARY` alongside the existing Pantone library so digital/system palette work no longer has to route through print-aware sources
- refreshed `FONT_LIBRARY` with stronger script-coverage, variable-font, dense-data, and deployment guidance
- added new source docs derived from the uploaded color and typography research and normalized them against current official documentation
- updated color and type summaries, skills, and loading logic so semantic roles, domain-fit, chart palette types, script coverage, and current font deployment caveats are handled earlier and more explicitly


## v2.5.0 — startup unification, degraded-mode safety, visual input, and lighter execution
- made `MASTER_CHAT_OPERATOR.md` the only canonical startup authority and demoted `SYSTEM_PRECEDENCE.md` back to conflict resolution only
- added `DEGRADED_MODE_PROTOCOL.md` plus load-state validation hooks in `runtime_validator.py`
- replaced always-visible route headers with a trace-visibility policy that defaults to recoverable trace
- added `VISUAL_INPUT_PROTOCOL.md` and visual pre-pass metadata for screenshot, mockup, and page-image tasks
- added `LIGHTWEIGHT_RESPONSE_PROTOCOL.md` and task-weight metadata so small asks can skip unnecessary overhead safely
- hardened validation against hollow compliance, fake tradeoffs, low-alignment recommendations, and overconfident visual claims
- added `QUICKSTART.md` and live-eval scaffolding under `tests/live_evals/`

## v2.4.2 — runtime overlay optimization without capability loss
- added a generated `runtime/` overlay with thin boot files, per-route cards, per-contract cards, and per-skill cards
- added `knowledge-base/runtime-summaries/` and indexed source-doc section maps so deep evidence escalates by section before full-doc load
- updated control authority and knowledge-loading rules so schemas stay canonical and mirrors become maintenance/debug-only
- added capability-preservation validation and runtime token-budget metadata for overlay hydration auditing
- kept all existing skills, routes, contracts, summaries, source docs, templates, and proof artifacts intact

## v2.4.1 — designer comprehension layer
- added `ADAPTIVE_EXPLANATION_PROTOCOL.md` and extended `SESSION_CONTEXT.md` with live explanation-tier state
- added `DESIGNER_RESPONSE_FILTER_PROTOCOL.md` as a cross-cutting response transformation layer
- added `text-humanization-expert.md`, `text_humanization_revision`, and `text-humanization-template.md`
- added summaries and source docs for adaptive explanation, response filtering, and humanization
- added examples, evals, and regression cases for tier compliance, next-step guidance, and humanization drift risks
