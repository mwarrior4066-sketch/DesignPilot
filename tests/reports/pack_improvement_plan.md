# DesignPilot Pack Improvement Plan
**Source:** Cross-model batch test findings (6 providers, 170+ test results)  
**Scope:** Source-level improvements to the pack itself — not the validator or runner

---

## What the batch data reveals about the pack

The batch test data exposes four systemic issues that live in the pack source, not in the validator. The validator was detecting real gaps — it was right about the failures. The question is *why* those gaps appear in every non-Claude model's output, and the answer points back to the pack.

---

## Problem A — The deploy file is nearly twice as large as it needs to be

**Finding:** `DESIGNPILOT_DEPLOY.md` is 118KB. The single largest contributor is `OUTPUT_CONTRACTS_BY_TASK.md` at 56KB — 47% of the entire pack. This document is a human-readable mirror of the task contracts. The `MASTER_CHAT_OPERATOR.md` explicitly says: *"do not load human-readable mirrors at runtime unless debugging, maintaining, or explaining the pack itself."*

The human-readable contracts mirror is in the runtime deploy anyway. This is likely what causes Gemini-2.5-Flash to produce truncated 345–511 character responses: the model reads 60,000+ tokens of input, emits a routing preamble as instructed, and runs out of output budget before the actual answer.

**Pack source fix — `src/operator/governance/OUTPUT_CONTRACTS_BY_TASK.md`:**

Remove this file from the compiled `DESIGNPILOT_DEPLOY.md`. It is a maintenance and debugging reference — not a runtime instruction. The launchers already carry the required sections, the contracts.json carries the decision tokens, and the skill cards carry the domain logic. A model receiving `DESIGNPILOT_DEPLOY.md` does not need a 56KB human-readable repeat of all contracts.

**Also remove or compress from the deploy:**
- `RUNTIME_VALIDATION_LAYER.md` (15KB) — the model's job is to produce good output, not to study the validator's rulebook. The key rules belong in skill cards and SESSION_ZERO, not as a 200-row table.
- `CONTEXT_REMINDER_PROTOCOL.md` (2.6KB) — mid-conversation reminders are not relevant at session start.
- `SESSION_STATE_TRACKING_PROTOCOL.md` (2.4KB) — internal machinery description that doesn't improve output quality.

**Projected result:** Deploy shrinks from 118KB (~29,500 tokens) to approximately 42KB (~10,500 tokens) — within working range for Gemini Flash and significantly below the threshold that causes truncation.

---

## Problem B — The pack instructs models to emit routing metadata in responses

**Finding:** 14 of 19 Gemini outputs and several Claude outputs began with or contained lines like:

```
Mode: STANDARD | Phase: AUDIT | Route: ui_structure_critique
```

The `MASTER_CHAT_OPERATOR.md` trace visibility policy says: *"Use recoverable trace by default. Show compact visible trace only when route choice materially affects trust, debugging, or maintenance. A clean answer without a visible mode/route header is valid when the route remains recoverable."*

SESSION_ZERO rule 5 says: *"do not front-load internal architecture, startup modes, route IDs, or profile logic unless the user asks."*

Despite these instructions, something in the compiled pack is still generating this preamble in many responses. The likely source is the launcher kickoff prompt: *"I am starting a DesignPilot session for UI Structure Critique. Treat this launcher as the governing fit..."* — this triggers the model to acknowledge the route by emitting it visibly.

This preamble consumes ~150–200 tokens before the actual answer starts. For large-context models this is noise. For flash-class models it eats a meaningful chunk of the output budget.

**Pack source fix — `dist/runtime/task_launchers/*.md` (all launchers):**

Replace the current kickoff prompt across all launchers:

```markdown
# Current (triggers visible route emission):
- Suggested kickoff prompt: I am starting a DesignPilot session for UI Structure Critique.
  Treat this launcher as the governing fit, keep the startup light, and ask only for the
  missing context that would materially change the answer.
```

```markdown
# Replace with (suppresses visible routing preamble):
- Suggested kickoff prompt: Begin work on this task directly. Do not emit Mode, Phase,
  Route, or Skills metadata in your response. Keep all operator scaffolding internal.
  Start with the first required section.
```

**Also add to `dist/SESSION_ZERO.md` as rule 10:**

```
10. do not emit Mode, Phase, Route, or Skills header lines in the response. Keep all
    operator metadata internal. The first line of your response should be substantive
    content, not routing information.
```

---

## Problem C — Skill cards don't teach the vocabulary the validator checks

**Finding:** The validator's most common failures across non-Claude models were `missing_tradeoff` (36 failures), `missing_rationale` (32 failures), and `missing_evidence_class: implementation_constraint` (10 failures). These aren't just vocabulary mismatches — the batch data shows that xAI, DeepSeek, and OpenAI genuinely produce fewer causal connectors, explicit tradeoff statements, and constraint framings than Claude.

Reading the skill cards explains why. `brand-strategy-expert.md` says: *"every serious claim needs proof, scope, or an explicit downgrade to hypothesis."* This is correct in intent but doesn't teach the model what vocabulary satisfies the evidence requirement. A model reading this rule will produce well-intentioned brand analysis that still lacks `implementation_constraint` signal because it doesn't know it needs to use the words "trust requires", "category convention", or "only holds if."

Similarly, `api-reliability-security-expert.md` says: *"async lifecycle before long-request optimism"* — a good rule but not a vocabulary prescription. A non-Claude model following this rule produces good async discussion but still fails `async_job_model` because it doesn't know to name "202 accepted", "terminal state", "job lifecycle."

**Pack source fixes — skill cards:**

Add a `## Required vocabulary` block to each skill card, listing the specific phrases that satisfy evidence class and decision requirements. This doesn't constrain style — it teaches models what the contract considers sufficient evidence.

**`brand-strategy-expert.md`** — add:
```markdown
## Required vocabulary
- Express trust constraints as: "trust requires X", "the audience will not accept without Y",
  "category convention demands Z", "this only holds if..."
- Express differentiation logic as: "against [competitor/category]", "unlike X, this brand..."
- Express proof burden as: "proof requires", "the claim only works with", "without evidence of..."
- Name at least one explicit tradeoff: what is sacrificed for what gain.
  Use: "rather than", "instead of", "at the cost of", "this means accepting"
```

**`content-and-case-study-expert.md`** — add:
```markdown
## Required vocabulary
- Separate measured from inferred: "we measured X", "we inferred Y from Z",
  "open gap: no data on...", "proxy evidence only"
- Name proof constraints: "the case only demonstrates", "we cannot claim without",
  "what remains unverified"
- Express tradeoffs as: "narrative clarity vs proof precision", "rather than overstating..."
```

**`api-reliability-security-expert.md`** — add:
```markdown
## Required vocabulary
- Name the async job model explicitly: "202 Accepted + status URL", "terminal states:
  queued → running → completed | failed", "job lifecycle", "idempotency-key"
- Name resilience posture: "circuit breaker", "exponential backoff", "graceful degradation",
  "quota enforcement", "trace_id on all errors"
- Every reliability claim needs a mechanism: not "reliable" but "retry-safe because..."
```

**`front-end-architecture-expert.md`** — add:
```markdown
## Required vocabulary
- Name the cost surface explicitly: "the cost of this is...", "at scale this becomes...",
  "under load this degrades by...", "the architecture tax is..."
- Name the rendering decision: "server-rendered", "client-hydrated", "PPR boundary at..."
- Name the state ownership: "state lives in...", "mutations are owned by...",
  "the boundary between server and client is..."
```

**`back-end-aware-planner.md`** — add:
```markdown
## Required vocabulary
- Express permission rules as: "only [role] may", "session owner required",
  "gated by", "deny by default", "object-level check on..."
- Express sequencing constraints as: "must come before", "cannot proceed until",
  "step N before step N+1 because..."
```

---

## Problem D — The Adaptive Explanation Protocol doesn't protect required sections

**Finding:** pass-17 (the tiered explanation test) consistently failed on xAI, DeepSeek, and OpenAI. The problem is structural: when the `ADAPTIVE_EXPLANATION_PROTOCOL.md` instructs models to organize answers by Functional / Integrative / Strategic tiers, models embed all their content inside tier headings — and the required contract sections (`Rendering and mutation strategy`, `Risks and safer path`) never appear as standalone headings.

The protocol doesn't tell models that contract-required sections must survive the tier restructuring.

**Pack source fix — `src/operator/protocols/ADAPTIVE_EXPLANATION_PROTOCOL.md`:**

Add a contract section anchor rule to the tiered output behavior:

```markdown
## Contract section anchor rule

When a task launcher specifies required Output expectations sections, those sections
must appear as standalone headings in the final output even when tiered framing is used.

Tiered framing organizes explanation depth, not section coverage.

Correct pattern:
  ## Functional tier
  ## Integrative tier
  ## Rendering and mutation strategy   ← required section, appears standalone
  ## Risks and safer path              ← required section, appears standalone

Incorrect pattern:
  ## Functional tier
    (rendering decisions embedded here — contract section not surfaced)
  ## Strategic tier
    (risk analysis embedded here — contract section not surfaced)

Required sections are not optional even inside tiered explanations.
They may appear after the tier blocks or be called out within a tier,
but they must be surfaced as named headings the validator can find.
```

---

## Improvement E — SESSION_ZERO should carry the minimum-evidence floor

**Finding:** Several non-Claude providers produced outputs that were structurally organized but thin on evidence — xAI's evidence_use rubric score was 3.26/5.0, the lowest of any working provider. The rubric judge confirmed these outputs were useful but not rigorously grounded. This is a quality gap the validator correctly penalizes but that the pack doesn't address at the session level.

SESSION_ZERO is the one instruction every task receives. It currently addresses section headings (rule 8) and substance depth (rule 9) but says nothing about evidence grounding or tradeoff language.

**Pack source fix — `dist/SESSION_ZERO.md`:**

Add three rules after rule 9:

```markdown
10. do not emit Mode, Phase, Route, or Skills header lines. Keep operator metadata internal.
    Start your response with substantive content.

11. every recommendation must name one explicit tradeoff — what is preserved and what is
    sacrificed. Use language like "rather than", "instead of", "at the cost of", or
    "this means accepting". A direction without a named tradeoff will fail validation.

12. every claim of necessity, constraint, or proof must be expressed as a causal statement.
    Use "because", "therefore", "without which", "this requires", or "the constraint is".
    A conclusion without explicit causal grounding will fail rationale validation.
```

Rules 11 and 12 directly address the two most common failure modes across the entire batch run.

---

## Summary — what changes, what it affects

| Change | File | Tokens saved | Failure modes addressed |
|--------|------|-------------|------------------------|
| Remove OUTPUT_CONTRACTS_BY_TASK from deploy | compiled deploy | ~14,000 | Gemini truncation, all flash-class models |
| Remove RUNTIME_VALIDATION_LAYER from deploy | compiled deploy | ~3,750 | Pack bloat |
| Remove 3 protocol files from deploy | compiled deploy | ~1,600 | Pack bloat |
| Suppress routing preamble in launchers | 17 launchers | ~150/response | Parser phantom sections, token waste |
| Add routing preamble suppression to SESSION_ZERO | SESSION_ZERO | ~150/response | Gemini, Claude routing bleed |
| Add required vocabulary to 5 skill cards | 5 skill cards | 0 | missing_tradeoff, missing_rationale, implementation_constraint, async_job_model, permission_rule |
| Add contract anchor rule to Adaptive Explanation Protocol | 1 protocol | 0 | pass-17 tiered structure failures |
| Add evidence floor rules to SESSION_ZERO | SESSION_ZERO | 0 | Evidence_use gap on xAI, DeepSeek |

**Pack size after deploy restructure:** ~42KB (from 118KB) — within Gemini Flash's effective operating range, significantly below the truncation threshold.

**Expected batch pass rate after pack improvements (combined with validator fixes):**

| Provider | Before any fixes | After validator fixes | After validator + pack fixes |
|----------|-----------------|----------------------|------------------------------|
| Claude | 100% | 100% | 100% |
| Mistral | 100% | 100% | 100% |
| DeepSeek | 100% | 100% | 100% |
| OpenAI | 100%* | 100% | 100% |
| xAI | 97% | ~99% | 100% |
| Gemini Flash | 42% | ~65% | ~80%+ |
| Gemini Pro | n/a | ~75% | ~90%+ |

*OpenAI currently passes via rubric gate on 11/19 tests; pack fixes should move most of those to clean validator passes.

---

## Implementation order

**Do first (no regression risk, immediate size benefit):**
1. Rebuild `DESIGNPILOT_DEPLOY.md` excluding `OUTPUT_CONTRACTS_BY_TASK.md`, `RUNTIME_VALIDATION_LAYER.md`, and the three non-essential protocol files
2. Add rules 10–12 to `SESSION_ZERO.md`
3. Update kickoff prompt in all 17 launchers to suppress preamble

**Do second (requires review before shipping):**
4. Add `## Required vocabulary` blocks to the 5 skill cards above
5. Add contract anchor rule to `ADAPTIVE_EXPLANATION_PROTOCOL.md`

**Verify with:**
- Run `validate_examples.py` on golden outputs after each change — pack changes affect Claude behavior too
- Run one full batch test after completing step 3 to confirm preamble suppression works
- Run a full batch after completing step 5 to measure the vocabulary improvement
