# Repository Architecture

Last updated: 2026-04-14 (v4 restructure)

## Guiding principle

**Source files live in `src/`. Generated files live in `dist/`. Tests live in `tests/`. Documentation for humans lives in `docs/`.**

Generated artifacts never live in `src/`. If a file is produced by a script, it belongs in `dist/`.

---

## Top-level structure

```
dp_fixed/
├── config/              Configuration for the compile pipeline
├── dist/                Generated artifacts — do not edit manually
│   └── runtime/         Everything a model loads at task time
├── docs/                Human-readable documentation
│   ├── maintainer/      For people maintaining the pack
│   ├── operator/        For people deploying the pack
│   └── proof/           Evidence and claim boundary documentation
├── examples/            Known-good model output examples (used by evals)
├── proof/               Release validation artifacts and trust signals
├── scripts/             Build, test, and maintenance scripts
├── src/                 Source files — edit these, not dist/
│   ├── knowledge-base/  Research docs and summaries
│   ├── operator/        Core operator system prompt files
│   ├── runtime/boot/    Minimal bootstrap files
│   ├── schemas/         JSON schemas (contracts, aliases, routing)
│   ├── skills/          Canonical skill card sources
│   └── templates/       Output templates
└── tests/               Test suite
    ├── evals/           Eval fixtures (input to validate_examples.py)
    ├── fixtures/        Input prompts for each eval
    ├── golden_outputs/  Known-good and known-bad model outputs
    ├── live_outputs/    Batch run results
    └── reports/         Analysis documents
```

---

## dist/runtime/ — what the model loads

```
dist/runtime/
├── task_launchers/      One launcher per task (primary model entry point)
├── summaries/           23 runtime summary cards
├── skills/              21 runtime skill overlay cards (compiled from src/skills/)
├── contracts/           17 task contract JSON cards (compiled from src/schemas/task_contracts.json)
├── contracts_lite/      17 lightweight markdown contract cards
├── route_cards/         18 route cards (markdown, for lightweight path)
├── routes/              18 route cards (JSON, for compile pipeline)
├── starters/            11 starter prompts for common tasks
├── loading/             Token budget registry and hydration trace schema
├── START_HERE.md        Front door for normal use
└── TASK_CHOOSER.md      Route selection guide
```

---

## Source of truth for each concern

| What | Source of truth | Generated output |
|------|----------------|-----------------|
| Task contracts | `src/schemas/task_contracts.json` | `dist/runtime/contracts/`, `dist/runtime/contracts_lite/` |
| Section aliases | `src/schemas/section_aliases.json` | Used by `runtime_validator.py` directly |
| Routing | `src/schemas/routing_registry.json` | `dist/runtime/routes/`, `dist/runtime/route_cards/` |
| Skill cards | `src/skills/*.md` | `dist/runtime/skills/` |
| Knowledge summaries | `src/knowledge-base/summaries/*.md` | `dist/runtime/summaries/` |
| System prompt | `src/operator/core/MASTER_CHAT_OPERATOR.md` + kernel files | `dist/DESIGNPILOT_DEPLOY.md` |
| Session zero | `scripts/compile_designpilot.py` `build_session_zero()` | `dist/SESSION_ZERO.md` |
| Task launchers | `src/operator/core/` + contracts + skills | `dist/runtime/task_launchers/` |
| Validator logic | `scripts/runtime_validator.py` | — (runs directly) |

---

## How to make changes

### Add a new task
1. Add entry to `src/schemas/task_contracts.json`
2. Add route entry to `src/schemas/routing_registry.json`
3. Create or update relevant skill card in `src/skills/`
4. Run `python3 scripts/compile_designpilot.py`
5. Verify `python3 scripts/validate_examples.py` passes

### Update a contract
1. Edit `src/schemas/task_contracts.json`
2. Recompile: `python3 scripts/compile_designpilot.py`
3. Run `python3 scripts/validate_examples.py`

### Update a skill card
1. Edit `src/skills/SKILL_NAME.md`
2. Recompile to regenerate `dist/runtime/skills/`

### Add a section alias
1. Edit `src/schemas/section_aliases.json`
2. No recompile needed — validator reads this directly

### Run cross-model batch tests
```bash
python3 scripts/run_batch_parallel.py
```

### Generate missing comparative reports
```bash
python3 scripts/generate_missing_reports.py
```

### Archive old batch runs
```bash
python3 scripts/archive_batch_runs.py
```
