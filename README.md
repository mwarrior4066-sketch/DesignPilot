# DesignPilot

A modular, roadmap-driven AI design operator pack for production-level UX, UI, brand, graphic, document, accessibility, and implementation work.

## What this is

DesignPilot is an AI operator pack built around:
- a small control layer
- specialist skill files
- compact knowledge summaries
- deep source docs
- strict routing
- output validation
- stress-test and governance tooling

It is designed to help an AI behave more like a disciplined design operator than a generic chat assistant.

## Core capabilities

The pack supports work across:
- UX and UI design
- grid and layout systems
- typography and font selection
- color systems and Pantone-aware print logic
- accessibility and interaction feedback
- dashboards and dense-data interfaces
- brand strategy and audience fit
- case studies and design rationale writing
- PDF/document accessibility and layout
- front-end handoff
- back-end-aware feasibility planning
- component systems and state logic

## Repository structure

The repository is intentionally split into:
- `CHAT_BOOTSTRAP_PROMPT.md` at the root
- `DesignExpert_Pack/` for the full operator system

Root-level files may also include repository support files such as:
- `LICENSE`
- `.gitignore`
- `lint_pack.py`
- CI / hook / tooling files
- docs for humans

Those files do **not** replace the bootstrap entry point.

## How an AI should start

The runtime entry point is always:

`CHAT_BOOTSTRAP_PROMPT.md`

The AI should read that file first, then enter `DesignExpert_Pack/` and follow the tiered hydration sequence from there.

## Runtime model

The pack uses a tiered loading approach:
1. load the control core
2. read the user request
3. route intent
4. load only the needed skills
5. load only the needed summaries or templates
6. validate output before treating it as acceptable

This keeps cold-start overhead low and reduces unnecessary context bloat.

## Main control files

Inside `DesignExpert_Pack/`, the most important control files are:
- `MASTER_CHAT_OPERATOR.md`
- `TASK_ROUTER.md`
- `SESSION_CONTEXT.md`
- `SYSTEM_PRECEDENCE.md`
- `MODE_SYSTEM.md`
- `RESPONSE_PROTOCOL.md`
- `KNOWLEDGE_LOADING_PROTOCOL.md`

## Governance

The pack includes governance and maintenance logic:
- `SKILL_SYNC_PROTOCOL.md`
- `KNOWLEDGE_BASE_CONTRACT.md`
- `KNOWLEDGE_BASE_CHECKLIST.md`
- `lint_pack.py`

Run the linter from the repository root:

```bash
python3 lint_pack.py