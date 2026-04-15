# DesignPilot Pack — Five-Solutions Analysis & Comprehensive Fix Plan

---

## Problem 1 — Pack is 118KB, half of which is a human-readable mirror

The `OUTPUT_CONTRACTS_BY_TASK.md` (56KB) and `RUNTIME_VALIDATION_LAYER.md` (15KB) together account for 71KB — 60% of the deploy. Both are listed in `deploy_manifest.yaml` as `kernel_files` but the `MASTER_CHAT_OPERATOR.md` explicitly says *"do not load human-readable mirrors at runtime."* This bloat causes Gemini Flash to truncate at ~120 tokens, costs all models their first 14,000 tokens of context before any task begins, and makes routing preambles more likely as models try to anchor themselves in a large document.

---

### Solution 1A — Remove OUTPUT_CONTRACTS_BY_TASK and RUNTIME_VALIDATION_LAYER from deploy_manifest.yaml

Simply strike both files from `kernel_files` in the manifest and recompile.

**Pros:** One-line change. No new content to write. Immediately cuts deploy from 118KB to ~42KB. Safe — the contracts live in `task_contracts.json` (read by the validator), in the launchers (read by the model at task time), and in skill cards. The model doesn't need the table-format repeat. RUNTIME_VALIDATION_LAYER is a rulebook for debugging, not for the model to memorize.

**Cons:** If a task runs without a launcher loaded, the model has no contract reference. The validator rules no longer appear in the system prompt, which means the model's self-validation in the "validation gate" step of the MASTER_CHAT_OPERATOR becomes less precise. Any prompt engineering that relied on the model reading the full contract table would break.

---

### Solution 1B — Replace OUTPUT_CONTRACTS_BY_TASK with a compressed decision-token index

Instead of removing it, replace the 56KB human-readable table with a compact reference of only the section names and decision tokens per task — no prose explanations.

```
ui_structure_critique: sections=[Problem framing,Findings,Recommendations,Tradeoffs] decisions=[structural_failure,hierarchy_winner,intervention_order,tradeoff_resolution]
backend_feasibility_review: sections=[Requested capability,Hidden system requirements,Feasibility assessment,Safer implementation path] decisions=[data_dependency,permissions_dependency,system_surface_dependency,blocking_constraint]
...
```

**Pros:** Preserves contract awareness in the model's context. Estimated size: ~4KB for all 17 tasks. Model can self-validate against specific section names and decision IDs without reading a table. Vocabulary-exact reference improves decision token compliance.

**Cons:** Requires writing new content. Loses the "why it exists" rationale columns that help models understand the purpose behind each contract requirement. Requires ongoing maintenance when contracts change.

---

### Solution 1C — Split into domain deploys and never compile a full-stack deploy

Replace `DESIGNPILOT_DEPLOY.md` with three targeted deploys (`DEPLOY_UI.md`, `DEPLOY_BRAND.md`, `DEPLOY_CORE.md`) that each include only the relevant contracts. The manifest already defines these profiles.

**Pros:** Each deploy is ~30–40KB. Models receive only the contracts they need. Eliminates cross-domain noise. Gemini Flash operates comfortably within domain deploys.

**Cons:** Users must know which deploy to load. Breaks single-prompt workflows where the task type is unknown at startup. Adds routing overhead before any task begins. The launcher quickstart path already handles task selection — this would require a pre-task selection step that SESSION_ZERO currently avoids.

---

### Solution 1D — Lazy reference: replace inline contract content with "load on demand" pointers

Replace the output contracts section with a pointer table: *"For task X, load contract from launcher file Y before answering."* The launcher already contains the Output expectations block with required sections.

**Pros:** Near-zero size for the contracts section. Contracts are always current (pulled from launchers). No duplication. Aligns with the tiered hydration model in MASTER_CHAT_OPERATOR.

**Cons:** Requires the model to load launcher files mid-task, which many API contexts don't support. In practice the model would still need all contracts in context for the validation gate step. For non-launcher workflows this creates a gap.

---

### Solution 1E — Compress RUNTIME_VALIDATION_LAYER to a checklist; remove rule prose

Instead of a 200-row table with prose explanations, reduce RUNTIME_VALIDATION_LAYER to a 30-line checklist of rule IDs and their single-line triggers.

```
hr_accessibility_floor: accessible color/keyboard/PDF repair required
hr_wrong_mode: mode mismatch blocks output
sr_tradeoff_visibility: pick a direction and name the sacrifice
sr_typed_evidence_coverage: claims need evidence class receipts
...
```

**Pros:** Reduces from 15KB to ~2KB. Preserves model awareness of validation rules. Faster to scan than the full table. Easier to maintain.

**Cons:** Loses the "human remediation" column that helps the model know how to fix failures. The detailed failure triggers become less precise.

---

### Synthesis for Problem 1

Solutions 1A and 1B address the same bloat from different angles. 1A is fastest and lowest risk; 1B preserves the benefit 1A loses (contract vocabulary in context). Solution 1E addresses the second-largest contributor. Solutions 1C and 1D are architecturally interesting but add complexity that doesn't justify the tradeoff.

**Best synthesis:** Apply 1A for `OUTPUT_CONTRACTS_BY_TASK.md` (full removal — the launchers already carry everything the model needs) + Apply 1B's vocabulary-index idea as a new lightweight addition to MASTER_CHAT_OPERATOR's validation gate section, not as a standalone file + Apply 1E for `RUNTIME_VALIDATION_LAYER.md` (compress to checklist, keep as kernel file but at 2KB not 15KB).

---

## Problem 2 — Models emit routing preambles despite instructions not to

Fourteen of 19 Gemini outputs and several Claude outputs began with `Mode: STANDARD | Phase: AUDIT | Route: ui_structure_critique`. The `RESPONSE_PROTOCOL.md` describes three trace levels and explicitly says compact visible trace is for *"audit or trust-sensitive contexts"* only. SESSION_ZERO rule 5 says *"do not front-load internal architecture, startup modes, route IDs."* But something is still triggering the preamble. Reading the `RESPONSE_PROTOCOL.md` reveals the cause: the "Recommended format" example `Mode: <MODE> | Phase: <PHASE> | Route: <ROUTE>` appears in the document. Models treat documented format examples as templates to follow.

---

### Solution 2A — Remove the preamble format example from RESPONSE_PROTOCOL.md

The compact visible trace format `Mode: <MODE> | Phase: <PHASE> | Route: <ROUTE>` is currently shown as a template. Removing the positive example removes the template the model follows.

**Pros:** Eliminates the instruction that triggers the behavior. Consistent with the operator's stated preference for recoverable trace. One-line change in RESPONSE_PROTOCOL.md.

**Cons:** If a user actually wants compact trace, the model now has no documented format to follow. Debugging becomes harder when trace is needed.

---

### Solution 2B — Add an explicit suppression rule to SESSION_ZERO

Add a rule: *"Do not begin your response with Mode, Phase, Route, or Skills lines. Your first output line must be substantive content."*

**Pros:** SESSION_ZERO runs at task start and carries the most weight of any instruction. An explicit prohibition is clearer than a preference statement. Works even if the preamble format example remains in RESPONSE_PROTOCOL.

**Cons:** Adds a rule where SESSION_ZERO should be minimal. Doesn't fix the source — the format example still exists and will trigger behavior in contexts where SESSION_ZERO isn't loaded.

---

### Solution 2C — Change the preamble format from visible to hidden (comment syntax)

Replace the compact visible trace recommendation with a hidden format: `<!-- route: X | mode: Y | phase: Z -->`. The validator already checks for this format in `has_route_traceability()`.

**Pros:** Preserves traceability for debugging. Eliminates visible token waste. Consistent with "recoverable internal trace" policy. Models that emit HTML comments don't waste the user's screen space or token budget.

**Cons:** Most models don't emit HTML comments in markdown outputs by default. Requires a format change in RESPONSE_PROTOCOL and teaching all models a new pattern. Claude follows this; other models may not.

---

### Solution 2D — Move trace to the SESSION_STATE block (already being stripped by validator)

The validator already strips `[SESSION_STATE]...[/SESSION_STATE]` blocks before validation. Route metadata belongs there, not in visible output. Update the SESSION_STATE_TRACKING_PROTOCOL to instruct models to put route/mode/phase in the SESSION_STATE block only.

**Pros:** Clean separation between content and metadata. Consistent with how Claude already handles SESSION_STATE. No visible preamble. Validator strips it before scoring.

**Cons:** SESSION_STATE is a terminal block — it appears at the end of responses, not the beginning. Some models don't follow the SESSION_STATE format reliably. Requires updating the SESSION_STATE_TRACKING_PROTOCOL and all relevant references.

---

### Solution 2E — Reframe preamble as a "compact header" that only appears when explicitly requested

Change RESPONSE_PROTOCOL to say: compact trace appears *only when* the user includes "debug mode", "show routing", or similar in their prompt. Otherwise default is no visible header.

**Pros:** Preserves trace capability without making it the default. User-controlled. Clean for normal use. Easy to understand.

**Cons:** Requires model to reliably detect intent phrases. In automated batch testing, no prompt triggers debug mode, so this should already work — but the current implementation doesn't respect the "compact trace for trust-sensitive contexts only" rule as written, suggesting the model is ignoring the condition.

---

### Synthesis for Problem 2

Solutions 2A and 2B are complementary — one removes the triggering example, one adds a prohibition. Solution 2C is elegant but fragile across model families. Solution 2D is the architecturally correct destination but requires more refactoring. Solution 2E is already the stated intent but isn't working.

**Best synthesis:** Apply 2A (remove the template example from RESPONSE_PROTOCOL) + 2B (add explicit suppression to SESSION_ZERO) + 2D's SESSION_STATE framing as a *guideline* in RESPONSE_PROTOCOL, not a mandate. This covers all three failure modes: removes the template trigger, adds a hard prohibition at session start, and redirects trace to the existing stripped metadata block.

---

## Problem 3 — Skill cards don't teach the vocabulary the validator contracts require

The skill cards describe *what* good work looks like but don't teach the specific *words* that satisfy evidence class and decision requirements. `brand-strategy-expert.md` says "every serious claim needs proof" — but a model following this rule still fails `implementation_constraint` because it doesn't know to write "trust requires X" or "category convention demands Y." `api-reliability-security-expert.md` says "async lifecycle before long-request optimism" but doesn't teach "202 Accepted", "terminal states", "job lifecycle." The skills and contracts are logically aligned but linguistically disconnected.

---

### Solution 3A — Add a "## Required vocabulary" block to each skill card

Each card gets a new section listing the specific phrases that satisfy its evidence class and decision requirements.

**Pros:** Direct fix. Each skill card becomes self-contained. Models reading the card get both the conceptual rules and the vocabulary they need to satisfy those rules. No new files needed.

**Cons:** Adds ~200–400 chars per skill card. Creates a maintenance dependency — if the validator's token lists change, skill card vocabulary blocks must also update. Risk of over-prescribing vocabulary at the expense of natural expression.

---

### Solution 3B — Create a cross-skill vocabulary manifest loaded once per session

A single new file `VOCABULARY_MANIFEST.md` maps evidence class IDs to their trigger phrases, organized by domain. Loaded as part of the task context alongside the governing skill.

**Pros:** Single source of truth. No duplication across skill cards. Easy to maintain in sync with validator changes. Can be auto-generated from `task_contracts.json`.

**Cons:** Another file that adds to the pack size. Models must remember to use it. Without it, skills still lack vocabulary guidance. Less immediately useful than in-skill vocabulary because it requires cross-referencing.

---

### Solution 3C — Add vocabulary examples directly to the decision rules in skill cards

Rather than a dedicated vocabulary section, embed the vocabulary in the existing "Core decision rules" using parenthetical examples.

```
# Current:
- every serious claim needs proof, scope, or an explicit downgrade to hypothesis

# New:
- every serious claim needs proof, scope, or an explicit downgrade to hypothesis
  (use: "trust requires...", "category convention demands...", "only holds if...",
  "this claim cannot be made without...")
```

**Pros:** Vocabulary is contextual rather than listed abstractly. Less likely to feel like a keyword-stuffing instruction. Adds minimal size. Natural to read.

**Cons:** Increases the length of already-dense decision rules. The parenthetical format may be ignored by models that scan bullet points quickly.

---

### Solution 3D — Map evidence classes to skill output requirements in the task contracts

In `task_contracts.json`, add a `skill_vocabulary_hint` field to each required evidence class entry, pointing to the vocabulary the skill should produce.

```json
{
  "class_id": "implementation_constraint",
  "description": "Uses a real constraint...",
  "skill_vocabulary_hint": ["trust requires", "only holds if", "category convention", "cannot claim without"]
}
```

**Pros:** Machine-readable. Can be surfaced in OUTPUT_CONTRACTS_BY_TASK (if retained) or in the compact vocabulary index. Single source of truth for vocabulary.

**Cons:** Requires schema change. The model reads `task_contracts.json` indirectly through the compiled deploy — this data would only help if surfaced in a place the model reads.

---

### Solution 3E — Add vocabulary guidance to the launcher Output expectations blocks

The launchers already have `## Output expectations` with required section headings. Add a "Required phrases" note under each evidence class requirement.

```markdown
- Required evidence: implementation_constraint
  Use: "trust requires...", "only if...", "category convention...", "cannot proceed without..."
```

**Pros:** Appears at the exact moment the model is preparing to answer a specific task. Vocabulary is task-specific not generic. Launchers are already the most reliable instruction surface.

**Cons:** Same vocabulary appears across multiple launchers — maintenance burden. Adds length to already-updated launchers.

---

### Synthesis for Problem 3

Solutions 3A and 3C are complementary — 3A adds a dedicated vocabulary section, 3C embeds vocabulary in existing rules. 3B is architecturally clean but requires a new file. 3D is the right long-term schema direction. 3E targets the highest-reliability surface.

**Best synthesis:** Apply 3C (embed vocabulary examples in decision rules) in skill cards — low friction, contextual, no new files — plus apply 3E for the three most commonly failing launchers (brand_positioning_pass, api_reliability_security_review, backend_feasibility_review), where vocabulary gaps cause the most failures. Skip 3A, 3B, 3D for now — they can be revisited when the compile process is updated.

---

## Problem 4 — Adaptive Explanation Protocol breaks required sections in tiered answers

Pass-17 fails on every non-Claude provider because all of them use Functional/Integrative/Strategic tier framing — which is exactly what the `ADAPTIVE_EXPLANATION_PROTOCOL.md` instructs. The contract requires `Rendering and mutation strategy` and `Risks and safer path` as standalone sections. When models use tiers, they embed both inside the tier headings and the validator can't find them. The protocol teaches the tier behavior without protecting the contract requirements.

---

### Solution 4A — Add a contract section anchor rule to the protocol itself

Insert a rule in `ADAPTIVE_EXPLANATION_PROTOCOL.md`: *"Contract-required sections must appear as standalone headings even in tiered answers."*

**Pros:** Fixes the problem at its source. One addition to one file. Consistent with how the protocol handles other constraints. The fix applies to all tasks that use tiered explanation.

**Cons:** Models may not read or weight this rule as highly as the tier behavior rules that surround it. The rule competes with the strong tier framing instructions above it.

---

### Solution 4B — Move required sections outside the tier structure by instruction

Update the `frontend_implementation_review` launcher to explicitly place required sections after the tier blocks:

```
Answer using three tiers IF the task is an architectural explanation.
AFTER completing tier framing, output these as standalone sections:
## Rendering and mutation strategy
## Risks and safer path
```

**Pros:** Explicit structural instruction at the task level. Models follow "place X after Y" instructions more reliably than abstract "X must survive restructuring" rules. Fixes the specific failing test without changing the protocol.

**Cons:** Doesn't fix the underlying protocol for other tasks that might have the same issue in the future. Adds another special case to an already complex launcher.

---

### Solution 4C — Make the tiered explanation an optional format, not the default

Change the protocol's tier behavior to only activate when explicitly requested by the user, not as the default explanation style.

**Pros:** Eliminates the root cause of the tier-vs-contract conflict. Most users won't request tiered explanations — they'll get clean contract-compliant outputs. Simplifies the protocol.

**Cons:** The tiered explanation is a genuine product differentiator. Removing it as a default removes a significant capability. The pass-17 test specifically tests tiered explanation — this solution makes the test pass by removing the feature, not by fixing it.

---

### Solution 4D — Add tier-to-section mapping in the OUTPUT_CONTRACTS_BY_TASK

For tasks where tiered explanation is possible, add a mapping:

```
When using tier framing for frontend_implementation_review:
  - Functional tier covers: boundary explanation
  - Rendering and mutation strategy: required standalone (not inside any tier)
  - Risks and safer path: required standalone (not inside any tier)
```

**Pros:** Explicit and task-specific. Preserves tiered explanation while protecting required sections. Can be auto-generated from the task contract.

**Cons:** OUTPUT_CONTRACTS_BY_TASK is already being reduced (Problem 1). Adding to it goes in the wrong direction. Requires maintaining the mapping alongside contract changes.

---

### Solution 4E — Teach the section-anchor rule in SESSION_ZERO

Add rule 11 to SESSION_ZERO: *"If you use tiered framing, required Output expectations sections must still appear as standalone headings after or alongside the tier blocks."*

**Pros:** SESSION_ZERO applies to every task start. One rule covers all tiered explanation failures. Consistent with SESSION_ZERO's role as the universal task instruction.

**Cons:** SESSION_ZERO is supposed to be brief and universal. Adding task-specific structural guidance makes it longer. Models may not internalize the connection between the tier instruction in the protocol and this rule in SESSION_ZERO.

---

### Synthesis for Problem 4

Solutions 4A and 4E target different layers — the protocol and the session start. 4B targets the launcher. 4D is the wrong direction given Problem 1. 4C fixes by removal.

**Best synthesis:** Apply 4A (anchor rule in the protocol — fixes it at source) + 4E (session-zero rule — catches any protocol that the model didn't weight correctly) + 4B specifically for the `frontend_implementation_review` launcher where the failure is documented and tested. Three layers of the same fix increases the probability that any model, at any weight, gets it right.

---

## Problem 5 — SESSION_ZERO doesn't establish the evidence and tradeoff floor

The most common failure modes across all providers were `missing_tradeoff` (36 failures) and `missing_rationale` (32 failures). These are cross-model, cross-task, and cross-domain — they appear in brand reviews, backend specs, UI critiques, and case study rewrites alike. SESSION_ZERO is the one instruction that fires for every task. It currently handles section headings (rule 8) and substance depth (rule 9) but says nothing about what constitutes sufficient evidence, tradeoff language, or causal grounding.

---

### Solution 5A — Add three explicit rules to SESSION_ZERO

Add rules 10, 11, 12 covering: no preamble emission, tradeoff requirement, rationale requirement.

**Pros:** Universal coverage — every task, every model, every provider. Fixes the two most common failures at their conceptual root. SESSION_ZERO is the highest-reliability instruction surface.

**Cons:** SESSION_ZERO grows from 9 rules to 12. Each additional rule risks diluting the weight of earlier rules. If rules 8 and 9 already struggle to hold (models rename headings, produce thin sections), adding more rules may not improve compliance.

---

### Solution 5B — Add a "silent self-check" step to MASTER_CHAT_OPERATOR's silent critic pass

Expand the silent critic pass in `MASTER_CHAT_OPERATOR.md` with two checks:

```
- does the answer name what is preserved and what is sacrificed? (tradeoff check)
- does the answer name why each recommendation is necessary? (rationale check)
```

**Pros:** The silent critic pass already exists as a self-review step. Models that follow it will catch tradeoff and rationale gaps before outputting. Fixes the underlying quality gap rather than adding vocabulary hints.

**Cons:** The silent critic pass is a list of questions — models may scan it rather than actively apply each check. Adding two more items to an already long list reduces their individual weight.

---

### Solution 5C — Add tradeoff and rationale requirements to each skill card's core decision rules

Rather than fixing it globally, fix it in each skill's domain context:
- brand-strategy-expert: "every positioning recommendation must name what is sacrificed"
- frontend-architecture-expert: "every architecture decision must name the cost surface"
- etc.

**Pros:** Vocabulary and framing are contextual to each domain. A brand tradeoff sounds different from a frontend tradeoff — domain-specific instruction is more useful than a generic rule.

**Cons:** Requires updating every skill card. The same fix repeated 17 times. If a new skill is added, the fix must be added again.

---

### Solution 5D — Create a QUALITY_FLOOR.md file and add it to kernel_files

A single, short file that states the minimum evidence, tradeoff, and rationale requirements for any DesignPilot output, loaded alongside the master operator.

**Pros:** Single source of truth. Easy to update. Clear separation of concerns — the operator handles behavior, quality floor handles output standards.

**Cons:** Adds another kernel file to an already large deploy (conflicts with Problem 1 goals). Models already have RUNTIME_VALIDATION_LAYER for this purpose — a separate quality floor document may be ignored.

---

### Solution 5E — Strengthen the validation gate in MASTER_CHAT_OPERATOR

Add two explicit validation questions to the "Validation gate" section of `MASTER_CHAT_OPERATOR.md`:

```
- does the output name at least one tradeoff (what is preserved, what is sacrificed)?
- does the output include causal grounding (because, therefore, without which, this requires)?
```

**Pros:** The validation gate is already defined as a hard stop before output. Adding these two checks means models self-validate on the most common failures. No new files, no new instructions — just expands an existing gate.

**Cons:** Validation gate is a long checklist — adding to it may not increase compliance. Models that already skip tradeoff language are likely skipping the validation gate check too.

---

### Synthesis for Problem 5

Solutions 5A and 5E are the best pair — SESSION_ZERO sets the expectation at task start; the validation gate checks it before output. Solution 5B is a lighter version of 5E. Solution 5C does the right thing but is maintenance-heavy. Solution 5D adds size while Problem 1 is removing it.

**Best synthesis:** Apply 5A (rules 10–12 in SESSION_ZERO, covering preamble suppression, tradeoff requirement, and rationale requirement) + Apply 5E (two validation gate questions in MASTER_CHAT_OPERATOR) + Apply 5C selectively for only the three skill cards with the most failures (brand-strategy-expert, api-reliability-security-expert, front-end-architecture-expert).

---

## Synthesized Fix Plan — Three Sections

---

### Section 1 — Deploy restructure
**Files:** `config/deploy_manifest.yaml`, `src/operator/governance/RUNTIME_VALIDATION_LAYER.md`, `scripts/compile_designpilot.py`  
**Effort:** 2–3 hours  
**Effect:** Cuts deploy from 118KB to ~44KB. Fixes Gemini Flash truncation permanently. Speeds startup for all providers.

**Step 1.1 — Remove OUTPUT_CONTRACTS_BY_TASK from kernel_files**

In `config/deploy_manifest.yaml`, remove this line:
```yaml
- src/operator/governance/OUTPUT_CONTRACTS_BY_TASK.md
```

The contracts live in three places the model already reads: the launcher Output expectations, the task_contracts.json (compiled into launcher metadata), and the skill cards. The human-readable 56KB table adds nothing that isn't already present.

**Step 1.2 — Add a compact decision-token index to MASTER_CHAT_OPERATOR**

In `src/operator/core/MASTER_CHAT_OPERATOR.md`, after the "Validation gate" section, add a new section:

```markdown
## Contract decision index
When self-validating, check that your output satisfies the required decisions for the active task.
Named decisions per task type (use exact vocabulary):

ui_structure_critique: structural_failure · hierarchy_winner · intervention_order · tradeoff_resolution
component_spec: component_boundary · state_coverage · accessibility_behavior · implementation_boundary
dashboard_audit: dashboard_role · kpi_failure · chart_failure · density_or_navigation_decision
backend_feasibility_review: data_dependency · permissions_dependency · system_surface_dependency · blocking_constraint
pdf_remediation_plan: semantic_failure · reading_order_or_extraction · verification_method · destructive_shortcut_rejected
brand_positioning_pass: audience_frame · differentiation_frame · trust_logic · messaging_consequence
case_study_rewrite: claim_vs_proof_boundary · proxy_vs_measured · narrative_order · honesty_tradeoff
accessibility_feedback_audit: barrier_severity · wcag_rule · repair_priority · verification_method
color_system_spec: semantic_roles · state_mapping · contrast_boundary · migration_strategy
graphic_critique: communication_goal · hierarchy_failure · rebuild_move · distance_tradeoff
layout_reconstruction_plan: preserved_elements · inference_boundary · reconstruction_order · verification_method
type_system_recommendation: reading_context · scale_decision · pairing_rationale · adoption_sequence
ux_research_gap_map: known_evidence · gap_priority · method_mapping · research_sequence
frontend_implementation_review: rendering_model · state_ownership · boundary_placement · semantic_contract · cost_or_degraded_path
backend_architecture_spec: authority_model · consistency_stance · data_delivery · observability_tax
api_reliability_security_review: problem_details_contract · authorization_perimeter · idempotency_contract · async_job_model · resilience_strategy
text_humanization_revision: job_of_piece · pattern_scan · meaning_preservation · what_changed
```

This is ~80 tokens. It replaces 14,000 tokens of human-readable tables.

**Step 1.3 — Compress RUNTIME_VALIDATION_LAYER to a checklist**

Replace `src/operator/governance/RUNTIME_VALIDATION_LAYER.md` content with a compressed version:

```markdown
# Runtime Validation Layer
Run these checks before outputting. A draft is not acceptable until it clears hard rules.

## Hard rules (any failure = do not output)
- hr_accessibility_floor: do not recommend inaccessible color, missing keyboard, or destructive PDF repair
- hr_wrong_mode: audit answers diagnose; rebuild answers build; do not mix
- hr_unsupported_superlative: validated/proven/certified/production-ready requires evidence class receipt
- hr_missing_route_decision: required task decisions must be named in the output (see contract decision index)

## Semantic rules (soft failure = revise before outputting)
- sr_tradeoff_visibility: name what is preserved AND what is sacrificed in every recommendation
- sr_typed_evidence_coverage: claims of certainty need evidence class receipt
- sr_false_specificity: numbers without sources need inference labels
- sr_hollow_compliance: recommendations must map back to named failures, not float as generic advice
- sr_visual_boundary_honesty: separate observed from inferred when working from visual artifacts
- sr_prompt_restatement: output must transform the prompt, not restate it

## Integrity rules
- ir_contradiction: resolve conflicts with a named governing rule; do not carry both sides forward
- ir_route_traceability: route must be recoverable (internal trace is fine; visible header not required)
```

This is ~400 words vs 3,600 words. Same rules, no prose explanations the model doesn't need.

**Step 1.4 — Recompile**

Run `python3 scripts/compile_designpilot.py` to regenerate `dist/DESIGNPILOT_DEPLOY.md`. Verify the output is under 50KB. Run `validate_examples.py` to confirm golden outputs still pass.

---

### Section 2 — Operator and protocol fixes
**Files:** `dist/SESSION_ZERO.md`, `src/operator/protocols/RESPONSE_PROTOCOL.md`, `src/operator/protocols/ADAPTIVE_EXPLANATION_PROTOCOL.md`, `src/operator/core/MASTER_CHAT_OPERATOR.md`  
**Effort:** 2–3 hours  
**Effect:** Eliminates routing preamble emission. Establishes tradeoff/rationale floor for all tasks. Fixes tiered-explanation section compliance.

**Step 2.1 — Remove the preamble format template from RESPONSE_PROTOCOL**

In `src/operator/protocols/RESPONSE_PROTOCOL.md`, in the "Trace visibility policy" section, remove the "Recommended format" block:

```markdown
# REMOVE THIS BLOCK:
### 2. Compact visible trace - audit or trust-sensitive contexts
Recommended format:

```text
Mode: <MODE> | Phase: <PHASE> | Route: <ROUTE>
```
```

Replace with:

```markdown
### 2. Compact visible trace - only when explicitly requested
When the user asks for route debugging or audit output, include one line at the top:
`[route: <ROUTE> | mode: <MODE>]` — use square brackets to signal internal metadata.
In all other cases, route information belongs in the [SESSION_STATE] block only, not in visible output.
```

**Step 2.2 — Add rules 10–12 to SESSION_ZERO**

In `dist/SESSION_ZERO.md`, after rule 9, add:

```markdown
10. do not begin your response with Mode, Phase, Route, or Skills lines. Your first output
    token must be substantive content. Operator metadata belongs in the [SESSION_STATE]
    block at the end of your response, not in visible output.

11. every recommendation must name one explicit tradeoff — what is preserved and what is
    sacrificed. Acceptable phrases: "rather than", "instead of", "at the cost of",
    "this means accepting", "one downside is", "the risk is", "you sacrifice X to gain Y."
    A direction without a named tradeoff will fail tradeoff validation.

12. every claim of necessity, constraint, or cause must be expressed with causal grounding.
    Acceptable phrases: "because", "without which", "this requires", "the constraint is",
    "by doing so", "if you skip this", "the reason is", "this enables", "this prevents."
    A conclusion without explicit causal grounding will fail rationale validation.
```

**Step 2.3 — Add two validation gate checks to MASTER_CHAT_OPERATOR**

In `src/operator/core/MASTER_CHAT_OPERATOR.md`, in the "Silent critic pass" section, add two bullets:

```markdown
- the answer names at least one tradeoff (what is preserved vs what is sacrificed, not just a direction)
- the answer uses explicit causal language for every constraint or necessity (because/without which/this requires/the constraint is)
```

**Step 2.4 — Add contract anchor rule to ADAPTIVE_EXPLANATION_PROTOCOL**

In `src/operator/protocols/ADAPTIVE_EXPLANATION_PROTOCOL.md`, after the "Tier behavior rules" section, add:

```markdown
## Contract section anchor rule

Tier framing organizes explanation depth. It does not replace contract-required sections.

When a task launcher specifies required Output expectations sections, those sections must
appear as standalone headings in the final output even when Functional/Integrative/Strategic
tier framing is used.

Correct:
  ## Functional tier
  [tier content]
  ## Strategic tier
  [tier content]
  ## Rendering and mutation strategy   ← required section, standalone
  ## Risks and safer path              ← required section, standalone

Incorrect:
  ## Functional tier
  [rendering decisions embedded here — contract section missing]
  ## Strategic tier
  [risk analysis embedded here — contract section missing]

If the required section name appears in the launcher Output expectations, it must appear
as a named heading in the output. It may come after tier blocks or be surfaced within a
tier as a sub-heading, but it must be findable as a heading.
```

---

### Section 3 — Skill card vocabulary fixes
**Files:** `src/runtime/cards/skills/brand-strategy-expert.md`, `src/runtime/cards/skills/api-reliability-security-expert.md`, `src/runtime/cards/skills/front-end-architecture-expert.md`, `src/runtime/cards/skills/content-and-case-study-expert.md`, `src/runtime/cards/skills/back-end-aware-planner.md`  
**Effect:** Closes the vocabulary gap between skill intent and validator contracts. Directly addresses the top evidence class failures: implementation_constraint (10×), missing_tradeoff (36×), missing_rationale (32×).

**Step 3.1 — brand-strategy-expert.md**

In the "Core decision rules" section, expand the evidence rules with parenthetical vocabulary:

```markdown
## Core decision rules
- audience fit beats personal taste
- positioning requires a frame of reference, points of parity, points of difference, and a reason-to-believe
- every serious claim needs proof, scope, or an explicit downgrade to hypothesis
  (use: "trust requires...", "the audience will not accept without...",
  "this claim only holds if...", "category convention demands...",
  "without evidence of... this cannot be claimed")
- trust is domain- and risk-sensitive, not a vague vibe
- distinctiveness and differentiation are related but not identical; measure which one matters
- conventions may be bent only when the communication gain is real and the usability/trust cost is named
  (use: "rather than [convention], this brand...", "at the cost of [X], we gain [Y]",
  "this means accepting [constraint] in exchange for [differentiation]")
- brand systems and interface systems can overlap, but they are not automatically identical
```

**Step 3.2 — api-reliability-security-expert.md**

In "Core decision rules", add vocabulary anchors to the async and resilience rules:

```markdown
## Core decision rules
- structured failure before ad hoc error strings
  (use RFC 9457: type, title, status, detail fields — not generic error strings)
- authorization before identifier trust
  (use: "object-level authorization", "the caller must be the resource owner",
  "BOLA check required", "deny by default")
- idempotency before retry advice
  (use: "idempotency-key header", "store-and-replay", "409 on duplicate")
- async lifecycle before long-request optimism
  (use: "202 Accepted + status URL", "terminal states: queued → running → completed | failed",
  "job lifecycle", "polling interval", "long-running job")
- resilience before production-ready language
  (use: "circuit breaker", "exponential backoff with jitter", "graceful degradation",
  "rate limit + quota", "trace_id on all error responses")
- quotas and timeouts before cost-blind scale claims
- trace propagation before observability claims
```

**Step 3.3 — front-end-architecture-expert.md**

In "Core decision rules", add vocabulary anchors to cost and rendering rules:

```markdown
## Core decision rules
- architecture before code style
- explicit finite states before boolean piles
- static, server, or PPR before client-heavy rendering by default
  (name the rendering model explicitly: "server-rendered", "client-hydrated at X boundary",
  "PPR with streaming for Y", "CSR island for Z")
- semantic host elements before custom roles
- client boundaries down the tree
- mutation recovery before optimistic polish
- performance cost named, not implied
  (use: "the cost of this approach is...", "at scale this becomes...",
  "under load this degrades by...", "the architecture tax is...",
  "this requires [X] overhead", "the bundle grows by...")
```

**Step 3.4 — content-and-case-study-expert.md**

In "Core decision rules", add proof boundary vocabulary:

```markdown
## Core decision rules
- clarity beats inflated language
- mode fit beats stylistic flourish
- problem before solution in case-study and rationale writing
- evidence beats adjectives
  (use: "we measured X", "proxy evidence only: Y stands in for Z",
  "open gap: no data on...", "we cannot claim without...",
  "this result is inferred, not measured")
- UX copy, documentation, audits, rebuilds, and portfolio writing are different modes
- artifacts should never appear without narrative function
- user-facing guidance should sound helpful and direct
```

**Step 3.5 — back-end-aware-planner.md**

In "Core decision rules", add permission and sequencing vocabulary:

```markdown
## Core decision rules
- reveal hidden system implications before treating any request as UI-only
- data model before implementation plan
- permission rules before any storage or API decision
  (use: "only [role] may...", "session owner required",
  "gated by [permission check]", "deny by default",
  "object-level authorization on [resource]")
- sequencing constraints before phase assignments
  (use: "must come before", "cannot proceed until",
  "step N must precede step N+1 because...",
  "if you skip this, [consequence]")
- name blockers explicitly before suggesting paths around them
```

**Step 3.6 — Recompile and rerun golden output tests**

After all skill card updates: run `python3 scripts/compile_designpilot.py` to propagate changes to `dist/DESIGNPILOT_DEPLOY.md` and profile deploys. Run `python3 scripts/validate_examples.py` — all 18 currently-passing golden outputs must still pass. If any regress, review the vocabulary additions for false positives.

---

## Projected improvement matrix

| Problem | Root cause | Sections that fix it | Expected failure reduction |
|---------|-----------|---------------------|--------------------------|
| Gemini truncation | Deploy 118KB, max_tokens=2000 | Section 1 (deploy cut) + runner fix | 9 truncated tests → 0 |
| Routing preamble | Format template in RESPONSE_PROTOCOL | Section 2.1 + 2.2 (suppress at source + SESSION_ZERO) | 14/19 preamble → ~0 |
| missing_tradeoff (36×) | Skills and SESSION_ZERO say nothing specific | Section 2.2 rule 11 + Section 3 vocabulary | ~80% reduction |
| missing_rationale (32×) | Same gap | Section 2.2 rule 12 + Section 3 vocabulary | ~75% reduction |
| implementation_constraint (10×) | Skills use intent not vocab | Section 3.1–3.5 vocabulary anchors | ~80% reduction |
| pass-17 tiered structure | Protocol teaches tiers, not section anchoring | Section 2.4 anchor rule | 4-provider failure → ~1 |
| OpenAI superlatives | Model habit, no instruction against it | Section 2.3 validation gate + Section 1.3 compression | ~70% reduction |
| xAI evidence_use gap | No evidence vocabulary in skills | Section 3.2–3.5 | Score 3.26 → ~3.8+ |
| Gemini Flash capacity | Wrong model + deploy bloat | Section 1 + runner fix (gemini-2.5-pro) | 42% → 75%+ |

**Deploy size after Section 1:** ~44KB (from 118KB). Within Gemini Flash effective range.  
**Expected full-suite pass rate after all three sections:**

| Provider | Before | After |
|----------|--------|-------|
| Claude | 100% | 100% |
| Mistral | 100% | 100% |
| DeepSeek | 100% | 100% |
| OpenAI | 100%* | 100% |
| xAI | 97% | 100% |
| Gemini Flash | 42% | ~80% |
| Gemini Pro | ~75% | ~92% |

*Currently 11/19 via rubric only; pack fixes should shift most to clean validator passes.
