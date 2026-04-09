# Design Expert v8.2: Operational Manual

Design Expert v8.2 is a modular operator pack for design, design systems, accessibility, document work, implementation planning, and validation-aware outputs.

## Deployment & setup
1. Point the agent to `root `CHAT_BOOTSTRAP_PROMPT.md``.
2. Ensure the environment can read local files.
3. Use models with enough context to support routed summaries and deep source retrieval when needed.

## Repository map
- `/skills` = specialist logic
- `/templates` = reusable deliverable scaffolds
- `/knowledge-base` = source docs, summaries, media, and indices
- root control files = routing, validation, contracts, and governance

## Governance
- `KNOWLEDGE_BASE_CONTRACT.md` defines knowledge ownership.
- `KNOWLEDGE_BASE_CHECKLIST.md` is the readiness audit.
- `SKILL_SYNC_PROTOCOL.md` defines staleness and re-sync rules.
- `CHANGELOG.md` is the single history file.

## Runtime principle
The pack should hydrate in tiers, not by loading the entire repository at startup.


## Governance Check
Run `python3 lint_pack.py` from the pack root to verify skill and summary freshness metadata before release.


## Packaging Note
All runtime files except the bootstrap prompt live inside `DesignExpert_Pack/`. Start from the root `CHAT_BOOTSTRAP_PROMPT.md`.



## Machine-readable library indexes
Use `libraries/PANTONE_LIBRARY.json` and `libraries/FONT_LIBRARY.json` for fast lookup. Only load the markdown companions when nuance or caveats are needed.
