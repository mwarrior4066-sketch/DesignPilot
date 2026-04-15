# AI Operator Pack Validation & Stress Testing

## Purpose
This source document supports the operator pack’s formal stress-test suite and runtime validation layer. It should be loaded when the pack itself is being hardened, audited, revised, or compared across versions.

## Why validation needs its own domain
Large operator packs fail less often when they are treated as systems with explicit control layers, specialist boundaries, and deterministic validation gates. A pack cannot rely on “the reasoning seemed fine.” It must check:
- whether the correct mode was chosen
- whether the roadmap phase was respected
- whether the correct specialist pathway activated
- whether the output matched the expected task contract
- whether domain rules were violated
- whether the evidence burden was met
- whether contradictions were resolved instead of polished over

## Core objective
Validation should distinguish between:
- structurally valid output
- semantically correct output
- safe partial output
- misleadingly polished but invalid output

The last category is the most dangerous because it often survives superficial review.

## Failure taxonomy
Important failure classes for design operator packs include:
- **specification drift**: the output gradually departs from the original constraints
- **context rot**: earlier important rules are buried by later context
- **sycophancy**: the operator agrees with unsafe or weak user requests instead of correcting them
- **tool or argument rot**: the reasoning is close but malformed at execution boundaries
- **miscoordination**: the wrong specialist owns the decision or the right specialist is missing
- **silent domain failures**: the answer looks plausible but violates accessibility, document integrity, feasibility, or proof rules
- **contract drift**: the answer no longer matches the required deliverable shape even if the content is partly good

## Stress-test architecture
A formal suite should test the pack at multiple levels.

### Tier 1 - smoke tests
Fast checks for mode, phase, routing, and obvious safety failures.

### Tier 2 - pathway tests
Verify that requests activate the correct specialist pathway and evidence artifact.

### Tier 3 - domain tests
Check that specialist rules catch domain-specific violations, such as:
- hidden focus
- inaccessible color
- unreadable type
- impossible dashboard density
- unsupported brand claim
- backend-heavy request treated as only visual
- broken PDF reading order or tagging

### Tier 4 - contradiction tests
Feed the system mutually tense or impossible asks and verify that it constrains, redirects, or refuses instead of smoothing them together.

### Tier 5 - regression tests
Maintain a golden set of stable prompts with known expected behavior. Compare score and failure safety over time.

## Runtime validation layer
The runtime validation layer should run after a draft exists but before it is accepted.

Recommended validation order:
1. mode
2. phase
3. pathway
4. output contract
5. domain rules
6. evidence/provenance
7. contradiction handling
8. pass / revise / escalate decision

## Hard fail classes
Always hard fail when the output:
- violates accessibility minimums by default
- presents off-phase production work as valid without naming the risk
- destroys document structure when document behavior matters
- makes unsupported hard claims in high-stakes contexts
- uses the wrong output mode in a materially different way
- treats impossible implementation as feasible
- contradicts the governing route while sounding polished

## Soft fail classes
Soft fail when the answer is salvageable but thin:
- structurally incomplete
- weakly evidenced
- under-specified
- too broad for the ask
- not yet aligned with the smallest correct pathway
- correct in verdict but poor in actionability or explanation depth

## Rubric logic
Use weighted rubrics only after hard gates pass. A good general scoring model checks:
- mode correctness
- phase correctness
- pathway correctness
- output contract completeness
- domain rule compliance
- evidence quality
- contradiction handling
- clarity and directness

## Domain-specific validation
Each specialist domain should own deep rules, but the central validation layer should know what to check at a high level.

Examples:
- accessibility: focus, target size, motion, state visibility
- color: role map, contrast, dark-mode logic, color-only meaning
- typography: readable size, measure, hierarchy, no shrink-to-fit shortcuts
- dashboards: dashboard type, KPI hierarchy, chart choice, density, filter/drill-down logic
- documents: frame logic, reading order, tags/artifacts, OCR/extraction behavior
- backend planning: feasibility verdict, auth/data/export/realtime implications
- brand strategy: audience fit, trust burden, claim support
- case study/content: correct writing mode, visible problem/process/solution/outcome chain, evidence framing

## Contradiction handling
A strong pack does not merge impossible asks into one smooth answer. It should:
- identify the contradiction
- name the governing constraint
- offer a safe narrower path if possible
- refuse or redirect when the conflict is fundamental

## Escalation logic
A pack should not endlessly self-revise.

Practical rule:
- pass if hard gates pass and the score is strong
- auto-revise up to two times if only soft fails remain
- constrain scope if a safe partial answer is possible
- ask for clarification only if a material source-of-truth gap remains
- escalate or refuse if the task is destructive, regulated, unsupported, or materially ambiguous after revision attempts

## Golden-set and release discipline
A version should not ship because it “feels better.” It should ship only if:
- smoke tests pass
- no P0/P1 failures remain
- regression scores do not materially drop
- generated surfaces remain synchronized with source truth
- release identity reflects material artifact changes

## Validation blind spots to watch
- files exist but semantically disagree
- summaries drift from source docs
- lite path is present but not actually usable by operators
- proof structure visually overstates evidence maturity
- reports contain stale metrics copied from earlier builds

## DesignPilot stance
Validation is not a final cosmetic check. It is the discipline that keeps a large operator pack from becoming elaborate but unreliable.


## Review checklist for DesignPilot
This knowledge base should be used to ask:
- Which failure classes are most likely for this route or release?
- What should be checked structurally before weighted scoring begins?
- Which domain-specific validator rules are mandatory here?
- When should the system auto-revise, constrain, or escalate instead of polishing?
- Are release artifacts synchronized enough to trust the reported result?

## Success conditions
A strong validation discipline makes the package harder to fool with smooth but invalid output. It should improve both safety and maintainability by exposing failure modes before they become part of the public surface.
