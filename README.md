# DesignPilot

DesignPilot is a modular AI design operator system for structured, implementation-aware design work.

It is built for people who need more than generic critique, loose inspiration, or one-file prompt packs. Instead of treating all design work the same, DesignPilot is organized around routed task handling, specialist skills, reusable contracts, deploy profiles, validation layers, worked examples, and continuity structures that make outputs more usable, more grounded, and easier to build on over time.

DesignPilot's goal is to improve decision quality, structure, and production usefulness.

---

## Start here

### If you want to use DesignPilot
1. Read `docs/operator/OPERATOR_QUICKSTART.md`
2. Choose a startup mode in `docs/operator/STARTUP_MODES.md`
3. Use `docs/operator/ROUTE_PICKER.md` if you want the lightweight path
4. Send `dist/SESSION_ZERO.md` after loading your chosen startup set

### If you want the lightest startup path
Read:
- `docs/operator/LIGHTWEIGHT_QUICKSTART.md`

### If you want to maintain or extend the system
Read:
- `docs/maintainer/MAINTAINER_GUIDE.md`

---

## What DesignPilot is for

DesignPilot is meant for design work that benefits from stronger structure, better routing, and clearer output standards, especially when the task is more complex than “give me feedback on this screen.”

It is designed to help with:

- UI and UX critique focused on hierarchy, behavior, state logic, and usability
- design-system and component documentation
- dashboard and data-product review
- brand and graphic design decisions that need stronger rationale
- case-study and design-writing work that needs clearer narrative structure and evidence
- implementation-aware reviews that account for front-end and back-end constraints
- accessibility and document-review work where shallow advice is not enough
- project continuity, where one task should build on the last instead of resetting every turn

---

## Startup modes

DesignPilot supports three official startup modes.

### Full mode
Use this for complex or cross-domain work.

This is the broadest startup path. It gives the strongest routing, governance, and fallback coverage, and is the right choice when a task spans multiple domains such as accessibility, UI systems, implementation realism, and communication.

Typical load:
- `dist/DESIGNPILOT_DEPLOY.md`
- one relevant profile
- `dist/SESSION_ZERO.md`

### Profile-only mode
Use this for focused domain work.

This path is lighter than the full kernel and is often enough for concentrated work in a single area.

Available profiles:
- `dist/DEPLOY_CORE.md`
- `dist/DEPLOY_UI.md`
- `dist/DEPLOY_BRAND.md`

Typical load:
- one profile
- `dist/SESSION_ZERO.md`

### Lightweight mode
Use this for route-specific work where you want a much smaller startup footprint.

This path is meant for focused sessions that can be handled with a lightweight runtime layer, one route card, one contract card, and a small number of skill cards.

Typical load:
- `dist/DEPLOY_LITE.md`
- one route card
- one contract card
- one or two skill cards
- `dist/SESSION_ZERO.md`

Related docs:
- `docs/operator/STARTUP_MODES.md`
- `docs/operator/LIGHTWEIGHT_QUICKSTART.md`
- `docs/operator/ROUTE_PICKER.md`

---

## What makes it different

Most prompt packs improve style. DesignPilot is built to improve **decision quality, structure, and follow-through**.

### Route the task before answering
Different kinds of design work need different standards. A dashboard audit should not be handled like brand strategy, and a case-study rewrite should not be handled like a component spec. DesignPilot uses route logic so the system can load the right skill set, output shape, and validation expectations for the task.

### Prefer structure over performance
The goal is not to sound polished for its own sake. The goal is to produce work that is easier to review, easier to implement, and harder to mistake for empty polish.

### Treat proof and validation as part of the system
Examples, fixtures, validation rules, regression checks, and proof artifacts are part of the repo. DesignPilot is not just a pile of prompts. It is maintained more like an operator system with checks, constraints, and release discipline.

### Keep continuity across project work
DesignPilot includes project workspace patterns so longer efforts can preserve roadmap state, context, and project-specific constraints instead of starting over every turn.

### Separate the operator surface from the maintainer surface
The repo now supports a cleaner operator-facing entry path through compiled deploy artifacts and startup guides, while preserving the modular source-of-truth structure for maintainers.

---

## Core deploy artifacts

The current deploy surface includes:

- `dist/DESIGNPILOT_DEPLOY.md` — full kernel for broader or cross-domain work
- `dist/DEPLOY_CORE.md` — focused general critique and planning profile
- `dist/DEPLOY_UI.md` — UI systems, structure, components, and implementation-aware UI work
- `dist/DEPLOY_BRAND.md` — brand, positioning, communication, and narrative work
- `dist/DEPLOY_LITE.md` — lightweight startup bootstrap for smaller route-based sessions
- `dist/SESSION_ZERO.md` — onboarding and task-classification entry prompt

---

## Repository structure

The repository is organized so operators do not need to understand the full internal architecture just to use the system, while maintainers still retain the modular source structure.

### Main areas
- `src/` — modular source-of-truth for runtime logic, knowledge, governance, and system building blocks
- `dist/` — compiled deploy artifacts, startup files, manifests, and validation outputs
- `docs/operator/` — operator-facing startup and usage guidance
- `docs/maintainer/` — maintainer-facing architecture, compilation, and system guidance
- `evals/` — eval scaffolding, datasets, and review structures
- `proof/` — proof artifacts, release reports, trust notes, and audit outputs
- `config/` — deploy manifests, profile maps, precedence rules, and runtime settings
- `scripts/` — compiler, validation, packaging, and maintenance tooling
- `examples/` — worked examples and starter references
- `projects/` — project continuity structures and workspace support

---

## What kinds of work it covers

DesignPilot includes specialist coverage for:

- UI systems
- UX research
- component systems
- dashboard and data-product design
- brand strategy
- graphic design
- layout reconstruction
- typography and color systems
- front-end handoff and architecture review
- back-end-aware feasibility planning
- accessibility and document accessibility
- case-study and design-writing work
- text humanization and explanation structure

That does not mean every task is fully automated. It means the repo contains distinct decision layers for these problem types instead of treating all design work as one undifferentiated prompt.

---

## Validation and proof

DesignPilot includes validation, examples, and proof infrastructure because the project is intended to behave more like a maintained operator system than a loose prompt pack.

Key areas include:
- worked examples
- regression fixtures
- runtime and deploy validation
- build manifests
- handoff manifests
- proof artifacts and release reports

DesignPilot is careful about claim boundaries. Internal structure and validation are not the same thing as full external proof. The repo includes proof scaffolding and stronger release discipline, but external evaluation maturity is still a separate track from architecture hardening.

---

## Who this is for

DesignPilot is most useful for:

- solo product designers
- design students trying to build stronger process and critique habits
- designers who want clearer structure for specs, audits, and case studies
- people using AI for design work but trying to avoid generic filler and fake confidence
- anyone building a more serious design operator instead of a one-file prompt pack

---

## What it is not

DesignPilot is not a no-thinking design generator.

It is not a replacement for product judgment, user research, engineering review, accessibility testing, or real-world validation. It is also not pretending to prove outcomes it cannot measure. The repo is designed to strengthen reasoning, structure, continuity, and deployability, but output quality still depends on the task, the evidence provided, and the discipline of the person using it.

---

## Project status

This repository reflects a more mature DesignPilot system than its earlier versions.

It now includes:
- a cleaner GitHub-facing structure
- compiled deploy artifacts
- official startup modes
- a real lightweight runtime path
- stronger validation and integrity checks
- better operator vs maintainer separation
- improved handoff packaging
- a tighter knowledge-base and proof structure

DesignPilot is still best understood as an actively refined operator system, not a finished software product.

---

## In plain English

DesignPilot is a serious AI design operator system that tries to make outputs more structured, more specialized, more grounded, and more useful for real design work.
