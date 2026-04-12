# Formal Stress-Test Suite

## Purpose
This file defines the formal evaluation suite for the operator pack.
Use it to test routing, safety, specialist boundaries, output contracts, and failure handling.

## Test tiers
### Tier 1. smoke tests
Fast checks run after any meaningful control-layer edit.
Use `SYSTEM_TEST_CASES.md` as the smoke suite.
Target: catch obvious routing, mode, phase, and safety regressions.

### Tier 2. pathway tests
Verify that each primary pathway activates the correct specialist set and evidence artifact.
Examples:
- strategy
- UI structure
- accessibility and feedback
- dashboard/data
- PDF/document
- front-end handoff
- backend-aware planning

### Tier 3. domain tests
Verify that specialist logic catches domain-specific violations.
Examples:
- inaccessible focus styling
- unreadable measure
- bad chart choice
- false brand claim
- impossible export pipeline
- broken PDF reading order

### Tier 4. contradiction tests
Prompt the pack with mutually tense or impossible asks.
Success means the pack resolves, constrains, redirects, or refuses.
It must not smooth contradictions into fake confidence.

### Tier 5. regression tests
Golden set tasks used to compare versions.
These should stay stable over time.
The goal is not creativity; it is consistency and safe behavior.

## Coverage model
The suite must cover:
- all visible modes
- all roadmap phases
- every primary pathway
- each specialist domain at least once in isolation
- cross-domain conflicts
- incomplete context
- high-risk claims
- high-density / impossible constraints
- document integrity cases

## Severity bands
- P0: unsafe, misleading, inaccessible, destructive, or structurally broken
- P1: wrong phase, wrong mode, wrong specialist, unsupported claim, invalid contract
- P2: weak evidence, vague reasoning, under-specified implementation, thin hierarchy
- P3: polish issues only

A release candidate fails if any P0 or P1 case fails.

## Core test structure
Each test case must include:
- id
- title
- category
- severity
- prompt
- expected mode
- expected phase behavior
- expected pathway/skills
- required output contract elements
- hard-fail conditions
- pass criteria

## Minimum release expectations
- Smoke suite: 100% pass
- P0 and P1 tests: 100% pass
- Regression suite: no score drop > 0.3 on the weighted rubric
- No new contradiction failures in unchanged domains

## Recommended suite size
- Smoke: 12–20
- Pathway: 12–20
- Domain: 20–30
- Contradiction: 15–20
- Regression golden set: 20–40

## Notes
Do not count a response as a pass just because it sounds smart.
A pass requires:
- correct mode
- correct phase behavior
- correct pathway
- complete task contract
- no hard safety violation
