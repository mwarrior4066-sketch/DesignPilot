# DesignPilot

DesignPilot is a modular AI design operator system for structured design work.

It is built for people who need more than inspiration or generic critique. Instead of acting like a vague creative assistant, DesignPilot is organized to help with concrete design tasks such as UI audits, component specs, dashboard reviews, design-system decisions, brand positioning, layout reconstruction, case-study writing, front-end handoff, and accessibility review.

The project combines route-based task handling, specialist skills, reusable templates, reference libraries, validation rules, worked examples, and test scaffolding so outputs stay more structured, more grounded, and more useful across follow-up work.

## What DesignPilot is for

DesignPilot is meant for design work that benefits from explicit reasoning and stronger structure, especially when the task is more complex than “give me feedback on this screen.”

It is designed to help with:
- UI and UX critique that focuses on hierarchy, behavior, state logic, and usability
- design-system and component documentation
- brand and graphic design decisions that need clearer rationale
- case-study and design-writing work that needs stronger structure and evidence
- implementation-aware reviews that account for front-end and back-end constraints
- accessibility and document-review work where shallow advice is not enough
- project continuity, where one task should build on the last instead of resetting every turn

## What makes it different

Most prompt packs improve style. DesignPilot is trying to improve decision quality.

The system is built around a few core ideas:

### 1. Route the task before answering
Different kinds of design work need different standards. A dashboard audit should not be handled like brand strategy, and a case-study rewrite should not be handled like a component spec. DesignPilot uses route logic so the system can load the right skill set and output shape for the task.

### 2. Prefer structure over performance
The goal is not to sound smart. The goal is to produce work that is easier to use, easier to review, and harder to mistake for empty polish.

### 3. Treat proof as part of the system
Examples, fixtures, validation rules, and regression checks are part of the repo. The project is not just a collection of prompts. It is organized more like a maintained operator system with evidence, constraints, and checks.

### 4. Keep continuity across project work
DesignPilot includes project workspace patterns so longer efforts can preserve context, roadmap state, and project-specific constraints instead of starting over every time.

## What is in this repository

The repository is organized so a new person can understand the system without reading every file at the root.

### Core areas
- `operator/` — startup authority, routing logic, governance rules, and project protocols
- `skills/` — specialist expert layers for different kinds of design and implementation work
- `templates/` — reusable output formats for specs, audits, roadmaps, case studies, and validation
- `libraries/` — structured reference libraries for color, fonts, and Pantone data
- `schemas/` — routing, task-contract, and validation definitions
- `runtime/` — runtime loading and execution support files
- `knowledge-base/` — source summaries, source docs, indices, and runtime summaries
- `examples/` — worked examples that show what strong outputs look like
- `tests/` — regression fixtures, eval scaffolding, scorecards, and live-eval support
- `projects/` — project workspaces and continuity structures
- `scripts/` — maintenance, validation, packaging, and continuity tooling

## What kinds of work it covers

DesignPilot includes specialist coverage for:
- UI systems
- UX research
- component systems
- dashboard and data products
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

## How to start

If you are trying to use the system, begin here:

1. Read `QUICKSTART.md`
2. Open `operator/core/MASTER_CHAT_OPERATOR.md`
3. Review the relevant skill in `skills/` for the kind of task you are doing
4. Check `templates/` and `examples/` to see the expected output shape

If you are trying to evaluate credibility rather than just use it, also review:
- `examples/`
- `tests/`
- `schemas/validation_rules.json`
- `scripts/lint_pack.py`
- `scripts/run_regression_suite.py`

## Who this is for

DesignPilot is most useful for:
- solo product designers
- design students building stronger process and critique habits
- designers who want clearer structure for specs, audits, and case studies
- people using AI for design work but trying to avoid generic filler and fake confidence
- anyone building a more serious design operator rather than a one-file prompt pack

## What it is not

DesignPilot is not a no-thinking design generator.

It is not a replacement for product judgment, user research, engineering review, accessibility testing, or real-world validation. It is also not pretending to prove outcomes it cannot measure. The repo is built to strengthen reasoning, structure, and continuity, but output quality still depends on the task, the evidence provided, and the discipline of the person using it.

## Project status

This repository reflects a more mature DesignPilot system than its earliest versions. It includes stronger runtime control, clearer startup authority, better handling for visual-input-led tasks, broader specialist coverage, and a more usable GitHub structure.

The project is still best understood as an actively refined operator system, not a finished software product.

## In plain English

DesignPilot is a serious design prompt system that tries to make AI outputs more structured, more specialized, and more useful for real design work.
