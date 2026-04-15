# DesignPilot

Current stable release: v3.0.

DesignPilot is a modular AI design operator for structured, implementation-aware design work.

This README is the public GitHub overview for human readers.
It explains what the project is, what it is good at, and where to look next.
It is not the runtime startup file for the AI.
For AI or operator startup, use `QUICKSTART.md`.

---

## What DesignPilot is

DesignPilot is built for design work that needs more than generic feedback, loose inspiration, or a one-file prompt.
It routes different kinds of work through different decision layers so the output is more structured, more grounded, and more usable in production.

It is designed to improve:
- decision quality
- structural clarity
- implementation realism
- continuity across multi-step project work
- resistance to generic filler and unsupported confidence

---

## What it helps with

DesignPilot is most useful for work like:
- UI and UX critique
- dashboards and data-product review
- component and design-system documentation
- accessibility-aware review
- brand and graphic design decisions that need stronger rationale
- case studies, process writing, and portfolio explanations
- implementation-aware front-end and back-end design reviews
- project continuity where one task should build on the last

---

## What makes it different

DesignPilot's main differentiator is structured task framing with route-specific section contracts and rationale requirements. Instead of asking the model for generic design advice, it forces the answer to name the decision being made, the reason behind it, the tradeoff, and the evidence burden. That produces outputs that are easier to review, revise, and turn into implementation work.

Its implementation-awareness claim is strongest for backend feasibility, backend architecture, API reliability and security, frontend implementation review, component specification, and dashboard audit work. Those tasks involve code-adjacent systems, failure modes, state behavior, or measurable design constraints. For brand, graphic critique, prose revision, and case-study work, DesignPilot primarily improves structure, rationale quality, and claim discipline. Implementation grounding is not the primary value in those routes.

### It routes the task before answering
A dashboard audit, a case-study rewrite, and a brand positioning question should not be handled the same way. DesignPilot uses routes, contracts, skills, and validation layers so the answer shape matches the job.

### It is built for structure, not just style
The goal is not to sound polished for its own sake. The goal is to produce work that is easier to review, easier to implement, and harder to mistake for empty polish.

### It treats proof and validation as part of the system
The repo includes regression fixtures, validation rules, examples, proof notes, and release receipts. It is maintained more like an operator system than a loose prompt pack.

### It keeps continuity across project work
DesignPilot includes workspace and continuity patterns so longer efforts can preserve state, next steps, and project-specific constraints instead of starting over every turn.
---

## How to use this repo

### If you are a human reading this on GitHub
Start here:
- scan this README for project fit
- read `proof/PROOF_STATUS.md` if you want to evaluate credibility
- inspect `docs/maintainer/` if you want to understand the architecture
- inspect `projects/designpilot/` if you want to see the continuity and proof stack in context

### If you want to run the system with an AI
Do not use this README as startup material.
Use `QUICKSTART.md`.
That file is the AI-facing startup surface and points to the correct runtime entry path.

---

## Repository map

- `QUICKSTART.md` - AI-facing startup instructions
- `dist/` - compiled deploy artifacts and runtime startup files
- `src/` - source-of-truth logic, skills, protocols, and knowledge
- `docs/operator/` - operator-facing usage docs
- `docs/maintainer/` - maintainer-facing architecture and system docs
- `proof/` - proof notes, boundaries, and release receipts
- `tests/` - regression fixtures and evaluation checks
- `scripts/` - compile, validation, and packaging tooling
- `projects/` - continuity workspace and flagship project records

---

## Credibility path

If you want to judge how trustworthy the pack is, start with:
- `proof/PROOF_STATUS.md`
- `docs/proof/CLAIM_BOUNDARIES.md`
- `proof/benchmarks/README.md`
- `proof/reviews/README.md`
- `proof/receipts/README.md`

DesignPilot is careful about claim boundaries.
Internal structure and validation are not the same thing as outcome proof.
The repo includes real evidence surfaces, but they support different strengths of claim and should be read that way.

---

## Who this is for

DesignPilot is especially useful for:
- solo product designers
- design students building stronger process and critique habits
- designers who want clearer structure for specs, audits, and case studies
- people using AI for design work but trying to avoid generic filler and fake confidence
- anyone building a more serious design operator instead of a one-file prompt pack

---

## What it is not

DesignPilot is not a no-thinking design generator.
It is not a replacement for product judgment, user research, engineering review, accessibility testing, or real-world validation.
It is meant to strengthen reasoning, structure, continuity, and production usefulness, not pretend to automate the entire job.

## Pack health

Latest validated run: `batch-20260414-0844`

| Provider     | Composite | Pass rate | Gate |
|-------------|-----------|-----------|------|
| claude       | 91        | 100%       | ✓    |
| mistral      | 87        | 95%       | ✓    |
| deepseek     | 81        | 84%       | ✓    |
| xai          | 81        | 74%       | ✓    |
| openai       | 80        | 90%       | ✓    |
| gemini       | 79        | 89%       | ✓    |

*Composite = 60% validator + 40% rubric judge, 0–100. Gate = ≥ 70% pass rate.*  
Full history: `tests/reports/v2-tests/MASTER_SUMMARY.html`
DesignPilot is a modular AI design operator pack built to make AI-assisted design work more structured, more specialized, and more useful than a generic prompt.

It is designed for people who want stronger critique, clearer output shape, better continuity across follow-up work, and more grounded handling of design tasks that usually fall apart when treated like one undifferentiated request.

Instead of acting like a vague creative assistant, DesignPilot is organized as a maintained operator system with routed task handling, specialist skill layers, reusable contracts, deploy profiles, validation rules, examples, continuity patterns, and proof infrastructure.

---

## Overview

Most prompt packs mostly change tone.

DesignPilot is built to improve:
- decision quality
- output structure
- implementation realism
- task routing
- continuity across project work
- resistance to generic filler
- clarity around what “done” looks like

It is meant for design work that benefits from stronger structure and explicit standards, especially when the task is more complex than “give me feedback on this screen.”

DesignPilot is especially useful for:
- UI and UX critique
- design-system decisions
- component specifications
- dashboard and data-product review
- brand positioning
- graphic design direction
- layout reconstruction
- case-study writing
- front-end handoff
- implementation-aware planning
- accessibility and document-review work

---

## What DesignPilot is

DesignPilot is an AI design operator system.

In practice, that means it is a pack you upload to an AI model so the model follows a more structured design workflow instead of answering with generic advice.

The system is built around a few core ideas:

### Route the task before answering
A dashboard audit should not be handled like brand strategy. A case-study rewrite should not be handled like a component spec. DesignPilot uses route logic so the model can handle different types of work with different standards, output shapes, and validation expectations.

### Prefer structure over performance
The goal is not to sound impressive. The goal is to produce work that is easier to review, easier to use, and less likely to collapse into empty polish.

### Keep continuity across project work
DesignPilot includes project and continuity patterns so the model can preserve constraints, decisions, roadmap state, and working context across longer efforts instead of resetting every turn.

### Treat proof and validation as part of the system
The repository includes validation logic, examples, build artifacts, proof scaffolding, and release discipline because DesignPilot is intended to behave more like a maintained operator system than a one-file prompt.

### Separate the operator surface from the maintainer surface
The pack now supports operator-friendly startup paths through compiled deploy artifacts and startup docs, while preserving a modular source-of-truth structure for maintainers.

---

## Who it is for

DesignPilot is most useful for:
- solo product designers
- design students trying to build stronger process and critique habits
- designers who want clearer structure for audits, specs, and case studies
- people using AI for design work but trying to avoid generic filler and fake confidence
- anyone building or studying a more serious design operator instead of a one-file prompt pack

---

## What it is not

DesignPilot is not a no-thinking design generator.

It does not replace:
- product judgment
- user research
- engineering review
- accessibility testing
- real-world validation

It is designed to improve the quality, structure, and usefulness of AI-assisted design work, not remove the need for judgment.

It also does not claim proof it does not have. The repo includes internal validation and proof scaffolding, but external evaluation maturity is still a separate track from architecture and packaging improvements.

---

## Quick start

For most people, the normal use path is simple:

1. download the pack
2. upload the zip or repo files into an AI chat
3. tell the model to follow DesignPilot
4. give it your task

Example:

```text
Follow DesignPilot.

I need a critical review of a B2B dashboard settings page. Focus on hierarchy, control grouping, state clarity, and implementation realism.
