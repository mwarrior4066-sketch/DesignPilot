# DesignPilot — Batch Test Diagnostic & Fix Plan
**Source:** 6 batch runs, 170+ individual test results across 6 providers  
**Date:** April 14, 2026

---

## Diagnostic Summary

Ten distinct problems were identified from reading actual outputs and tracing exact failure paths. They fall into three categories: runner/infrastructure problems, validator logic problems, and contract coverage problems.

| # | Problem | Severity | Affects |
|---|---------|----------|---------|
| 1 | Gemini max_tokens=2000 truncates 9/19 outputs | Critical | Gemini |
| 2 | Routing preamble bleeds into outputs and confuses section parser | High | Gemini, Claude |
| 3 | `missing_tradeoff` and `missing_rationale` fire on good content | High | xAI, DeepSeek, OpenAI |
| 4 | `implementation_constraint` evidence class is underpowered | High | All non-Claude |
| 5 | `missing_required_decision` spread across 30 narrow token lists | Medium | All non-Claude |
| 6 | OpenAI unsupported superlatives and forbidden shortcuts | Medium | OpenAI |
| 7 | Gemini-2.5-flash wrong model — capacity too low | Medium | Gemini |
| 8 | pass-11 and pass-17 consistently fail every non-Claude provider | Medium | All non-Claude |
| 9 | xAI evidence_use quality gap (3.26/5.0 rubric) | Low | xAI |
| 10 | DeepSeek rationale expression gap (7x missing_rationale) | Low | DeepSeek |

---

## Problem 1 — Gemini max_tokens=2000 truncates 9/19 outputs

**Evidence:** Nine Gemini outputs were 345–511 characters long, all ending mid-sentence. All nine are exactly the size of the routing/session preamble the system prompt instructs the model to emit (~86–130 tokens) plus a few words of actual content. The remaining ten outputs ranged from 1,472 to 4,643 characters — these got enough tokens to complete their answer.

The cause is exact: `max_tokens=2000` is the universal default in `run_batch_parallel.py`. When the 118KB system prompt is prepended to the user message (as the Gemini fix requires), the combined input is ~30,000 tokens. Gemini then emits its routing preamble block (~150–200 tokens) and starts the actual analytical response — at which point it has already consumed most of its 2,000 output token budget. The nine truncated outputs hit this wall consistently.

**Fix — `scripts/run_batch_parallel.py`:**

Add per-provider max_tokens overrides instead of a global default:

```python
# Replace the single max_tokens=2000 default in call_gemini with:
PROVIDER_MAX_TOKENS = {
    'claude':   4096,   # Anthropic handles large outputs well
    'gemini':   8192,   # Must be high — system prompt prepend adds ~150 token preamble
    'openai':   4096,
    'xai':      4096,
    'mistral':  4096,
    'deepseek': 4096,
}

# In call_gemini, call_anthropic, and _openai_compat, use:
max_tokens = PROVIDER_MAX_TOKENS.get(provider_id, 4096)
```

Also update `call_gemini` to pass the correct max_tokens from `PROVIDER_MAX_TOKENS['gemini']` rather than the function parameter default.

**Expected impact:** Resolves truncation on all 9 affected Gemini tests. Combined with switching to gemini-2.5-pro (Problem 7), Gemini should move from 42% to 60–70%+ pass rate.

---

## Problem 2 — Routing preamble bleeds into outputs

**Evidence:** 14 of 19 Gemini outputs begin with or contain routing metadata blocks like:
```
Mode: STANDARD | Phase: AUDIT | Route: ui_structure_critique
```
Several Claude outputs end with `[SESSION_STATE] { ... }` JSON blocks. The session state stripping already handles the `[SESSION_STATE]` blocks. But the routing preamble (`Mode: ... | Phase: ... | Route: ...`) is NOT stripped — it appears as a section heading in the parser, creating phantom sections and consuming the early word budget.

**Fix — `scripts/runtime_validator.py`:**

Add routing preamble stripping to the existing `strip_reasoning_blocks` function:

```python
def strip_reasoning_blocks(text: str) -> str:
    # ... existing <think> and blockquote stripping ...

    # Strip routing metadata lines emitted by models following the system prompt
    # Pattern: "Mode: X | Phase: Y | Route: Z" (with or without surrounding **bold**)
    text = re.sub(
        r'\*?Mode:\s*\S+.*?Route:\s*\S+\*?\s*\n?',
        '',
        text,
        flags=re.IGNORECASE
    )
    # Strip "Governing Route:", "Task Weight:", "Active Skills:" preamble blocks
    # that appear before the first real heading
    first_heading = re.search(r'^#{1,3}\s', text, re.MULTILINE)
    if first_heading:
        preamble = text[:first_heading.start()]
        preamble_lines = preamble.splitlines()
        routing_indicators = [
            'governing route', 'task weight', 'active skills',
            'skills:', 'route:', 'phase:', 'mode:'
        ]
        routing_line_count = sum(
            1 for l in preamble_lines
            if any(ind in l.lower() for ind in routing_indicators)
        )
        if routing_line_count >= 2:
            text = text[first_heading.start():]

    return text.strip()
```

**Expected impact:** Removes phantom sections from validator parse tree. Prevents routing metadata from being counted as section content, improving density scores and section matching accuracy for Gemini and occasionally Claude.

---

## Problem 3 — `missing_tradeoff` and `missing_rationale` fire on good content

**Evidence:** 36 `missing_tradeoff` and 32 `missing_rationale` failures across all providers. xAI hits `missing_tradeoff` 7 times at validator scores of 86–92 — these are substantively good outputs. The rubric judge confirmed them as passing (rubric mean 3.74–4.63). The pattern matcher is not recognizing xAI's tradeoff and rationale vocabulary.

**Specific vocabulary gaps identified from xAI outputs:**
- "the cost of this approach is..." → not matched by TRADEOFF_TOKENS
- "this means accepting..." → not in current patterns  
- "the risk here is..." → "the risk is" is in TRADEOFF_TOKENS but "the risk here" is not
- "one downside of..." → "downside" is in TRADEOFF_TOKENS but "one downside of" needs word boundary check

DeepSeek rationale gaps (7x `missing_rationale`):
- "the reasoning here is..." → not matched
- "this is important because..." → "because" IS matched but appears to be missed in some contexts
- "the reason to prioritize X over Y is..." → not fully matched

**Fix — `scripts/runtime_validator.py`:**

Expand `_has_structural_tradeoff` comparison signals:

```python
comparison_signals = [
    r'\bvs\.?\\b', r'\bversus\b', r'\binstead of\b', r'\brather than\b',
    r'\b(option|path|approach|pattern|method)\s+(a|b|1|2)\b',
    r'\bchoose\b.{0,40}\b(over|instead|rather)\b',
    r'\b(a|b):\s',
    # Add these:
    r'\bthe cost of\b', r'\bthe cost is\b', r'\bat the cost\b',
    r'\bthe risk here\b', r'\bthe risk is\b', r'\bthe tradeoff here\b',
    r'\bone downside\b', r'\bthe downside of\b',
    r'\bthis means accepting\b', r'\bmeans giving up\b',
    r'\byou lose\b', r'\byou gain\b',
    r'\bwhat you give up\b', r'\bwhat you get\b',
    r'\bweigh(s|ing)?\b.{0,30}\b(against|vs)\b',
]
```

Expand `_has_structural_rationale` causal patterns:

```python
causal_patterns = [
    # ... existing patterns ...
    # Add these:
    r'\bthe reasoning\b', r'\bthe reason to\b', r'\bthe reason for\b',
    r'\bthis is important because\b', r'\bthis matters because\b',
    r'\bthis is necessary\b', r'\bthis is required\b',
    r'\bbehind this\b',  # "the logic behind this is..."
    r'\bby doing so\b', r'\bin doing so\b',
    r'\bthis allows\b', r'\bthis enables\b', r'\bthis forces\b',
    r'\bwithout which\b',
]
```

Also add these to the `TRADEOFF_TOKENS` list for the fallback:
```python
'the cost of', 'the risk here', 'means accepting', 'you lose',
'you gain', 'what you give up', 'weighing against'
```

And to `RATIONALE_TOKENS`:
```python
'the reasoning', 'the reason to', 'this is important', 'this matters',
'by doing so', 'in doing so', 'this allows', 'this enables',
'this forces', 'without which'
```

**Expected impact:** Eliminates most false `missing_tradeoff` and `missing_rationale` failures for xAI and DeepSeek. Estimated +2 to +4 validator score improvement per affected test.

---

## Problem 4 — `implementation_constraint` evidence class underpowered

**Evidence:** `implementation_constraint` is the most commonly missing evidence class — 10 failures even after the previous context_overrides additions. It fires across all non-Claude providers on tests like brand_positioning_pass (pass-06), case_study_rewrite (pass-07), backend_feasibility_review (pass-04), and pdf_remediation_plan (pass-05).

The global regex patterns are still calibrated for UI/technical domains. Brand, content, and research task vocabulary is not covered.

**Fix — `scripts/runtime_validator.py`:**

Add to `EVIDENCE_CLASS_PATTERNS['implementation_constraint']`:

```python
# Content/brand/research constraint vocabulary
r'\bonly if\b',           # already present — confirm not double-added
r'\bonly works if\b',
r'\bthis only holds\b',
r'\bfails without\b',
r'\bbreaks if\b',
r'\bcannot claim\b',
r'\btrust requires\b',
r'\baudience requires\b',
r'\bproof requires\b',
r'\bthe constraint\b',
r'\bbound by\b',
r'\bconstrained by\b',
r'\bmust come first\b',
r'\bmust precede\b',
r'\bbefore you can\b',
r'\bstep \d+ must\b',
r'\bphase \d+ before\b',
r'\bsequence matters\b',
r'\bthe order matters\b',
r'\byou cannot skip\b',
r'\bif you skip\b',
```

**Expected impact:** Reduces `missing_evidence_class: implementation_constraint` failures by approximately 60–70%. Most impactful for brand positioning and PDF remediation tasks.

---

## Problem 5 — `missing_required_decision` spread across 30 narrow `any_of` lists

**Evidence:** 79 total `missing_required_decision` failures across all providers, distributed across 30 different decision IDs. No single decision fails more than 2 times, which means these aren't systematic gaps — each decision's `any_of` token list is just slightly too narrow for non-Claude vocabulary.

The highest-priority gaps based on which tests fail most:

**`async_job_model`** (api_reliability_security_review, 2 failures):
Current `any_of` includes: "async", "job", "queue", "status url", etc.
Add: `"lifecycle", "job lifecycle", "state machine", "polling interval", "202", "job state"`, `"in-progress"`, `"terminal"`.

**`cost_or_degraded_path`** (frontend_implementation_review, 2 failures):
Current `any_of` includes: "bundle", "hydration", "fallback", "degraded", "retry", "lazy", "performance cost", "rollback".
Add: `"the cost is"`, `"expensive"`, `"overhead"`, `"at scale"`, `"under load"`, `"degrades"`, `"breaks down"`, `"architecture cost"`, `"the tax"`.

**`structural_failure`** (ui_structure_critique, 1 failure):
Add: `"fails because"`, `"is failing"`, `"the failure is"`, `"breaks"`, `"the page fails"`.

**`inference_boundary`** (layout_reconstruction_plan, 1 failure):
Add: `"cannot be verified"`, `"assumed"`, `"inferred from"`, `"cannot confirm"`, `"uncertain"`, `"judgment call"`.

**Fix — `src/schemas/task_contracts.json`:**

For each of the above, add to the `any_of` array in the relevant task's `required_decisions` entry.

---

## Problem 6 — OpenAI unsupported superlatives and forbidden shortcuts

**Evidence:** OpenAI triggered `unsupported_superlative` 4 times (using words like "production-ready", "proven", "certified") and `forbidden_shortcut` once ("just convert it to React" pattern). These are genuine content quality issues — GPT-4.1 has a tendency to make overconfident claims in architectural reviews, and occasionally recommends shortcuts that the contract explicitly prohibits.

**Fix — Two parts:**

**Part A — `dist/runtime/task_launchers/frontend_implementation_review.md` and `api_reliability_security_review.md`:**

Add to the `## Kickoff behavior` section:

```
- Avoid language like "production-ready", "proven", "certified", or "best-in-class" unless
  tied to a specific threshold, benchmark, or evidence artifact. These trigger validation failures.
- Do not recommend "just use X" or "simply convert to Y" framings — name the specific
  architectural decision instead.
```

**Part B — Expand `SUPERLATIVES` list in `runtime_validator.py`** to use word-boundary matches and add a few missing entries:

```python
SUPERLATIVES = [
    'validated', 'proven', 'certified', 'best-in-class', 'compliant',
    'externally validated', 'production-ready',
    # Add:
    'industry-standard',   # used by GPT without grounding
    'battle-tested',       # used by GPT occasionally
]
```

**Expected impact:** Eliminates recurring `unsupported_superlative` failures on OpenAI. The launcher change reduces frequency without affecting substantive output quality.

---

## Problem 7 — Gemini-2.5-flash is wrong model for this suite

**Evidence:** Even the Gemini outputs that were not truncated had low rubric scores — pass-01 scored 1.4, pass-06 scored 1.2, pass-07 scored 1.2, pass-15 scored 1.0. These are not truncation problems — these outputs, even when complete, failed because Flash lacks the capacity to produce the depth the DesignPilot suite requires under a 118KB system prompt.

Gemini-2.5-flash is designed for speed and efficiency. It compresses heavily under long-context conditions. The DesignPilot suite requires 800–2000+ word structured analytical outputs with multiple decision types and evidence classes. Flash cannot reliably produce this under the current system prompt weight.

**Fix — `scripts/run_batch_parallel.py`:**

```python
DEFAULT_MODELS = {
    'claude':   'claude-sonnet-4-6',
    'gemini':   'gemini-2.5-pro',    # Flash cannot handle 118KB system prompt at required depth
    'openai':   'gpt-4.1',
    'xai':      'grok-3-fast',
    'mistral':  'mistral-large-latest',
    'deepseek': 'deepseek-chat',
}
```

**Expected impact:** The most significant single change for Gemini. Pro has materially higher capacity and consistently handles long-context analytical tasks. Combined with Problem 1 fix (max_tokens=8192), estimated Gemini pass rate improvement from 42% to 65–75%.

---

## Problem 8 — pass-11 and pass-17 fail every non-Claude provider

**Evidence:** pass-11 (layout_reconstruction_plan) and pass-17 (frontend_implementation_review tiered) are the two hardest tests in the suite. pass-17 failed xAI (score 78), DeepSeek (score 53), Gemini (score 58), and OpenAI (score 39). pass-11 failed Gemini (score 14) and DeepSeek (score 64).

**pass-17 diagnosis:** The test asks for a tiered explanation (Functional / Integrative / Strategic). All non-Claude models use "tier" framing in their section headings ("Functional Tier Explanation", "Strategic Tier"). The contract requires `Rendering and mutation strategy` and `Risks and safer path` as standalone named sections. When the model uses tier framing, the required sections are embedded inside tier sections — the validator can't find them.

The section heading examples added to the launcher (in the v2.9 fix) use the Haiku/Sonnet vocabulary, not the tier vocabulary other models use. The negative examples need to be expanded.

**Fix for pass-17 — `dist/runtime/task_launchers/frontend_implementation_review.md`:**

```markdown
## Section heading examples (tiered explanation variant — pass-17 style)
When this task uses Functional / Integrative / Strategic tier framing:

  REQUIRED: Even inside tier framing, these sections must appear as standalone headings:
    ## Rendering and mutation strategy  (required — do not fold into any tier)
    ## Risks and safer path             (required — do not fold into any tier)

  Acceptable tier structure:
    ## Functional tier
    ## Integrative tier
    ## Rendering and mutation strategy  ← standalone, even after tiers
    ## Risks and safer path             ← standalone, even after tiers

  Not acceptable:
    ## Functional tier                  ← with rendering decisions embedded inside
    ## Strategic tier                   ← with risk analysis embedded inside
```

**Fix for pass-11 — `src/schemas/task_contracts.json` — `layout_reconstruction_plan`:**

Add to `required_decisions.inference_boundary.any_of`:
```json
"cannot be verified", "assumed from", "inferred from", "cannot confirm",
"uncertain", "judgment call", "not recoverable", "must be inferred",
"we cannot know", "not directly visible"
```

**Expected impact:** pass-17 improvements require structural content change (the tier framing), so launcher instructions are the lever. pass-11 is an alias/token issue, fixable via contract expansion. Together, should recover 1–2 tests per provider.

---

## Problem 9 — xAI evidence_use quality gap (3.26/5.0)

**Evidence:** xAI's evidence_use rubric score (3.26/5.0) is materially lower than other working providers (Claude 4.47, Mistral 4.22, DeepSeek 3.84). The validator catches `missing_tradeoff` 7 times and `missing_evidence_class` 5 times for xAI — these aren't just token-list misses, Grok genuinely grounds claims less rigorously than other models.

Grok's EQ-aware training produces more conversational outputs that explain clearly but don't always tie claims to explicit constraints, thresholds, or causal structures. It says "this is better" more often than "this is better because X constraint applies."

**Fix — `dist/runtime/task_launchers/brand_positioning_pass.md`, `api_reliability_security_review.md`:**

Add to `## Kickoff behavior`:
```
- Every recommendation must be grounded: name the constraint, threshold, or causal mechanism
  that makes it necessary. "X is better" without "because Y" will fail evidence class checks.
- Tradeoff language must be explicit: name what is sacrificed, not just what is gained.
```

This is primarily a guidance improvement. The token list fixes from Problem 3 will also help xAI's evidence_use score by correctly detecting more of its natural vocabulary.

---

## Problem 10 — DeepSeek rationale expression gap (7x missing_rationale)

**Evidence:** DeepSeek triggers `missing_rationale` 7 times. Its rubric evidence_use score (3.84) is also below Claude's (4.47). DeepSeek uses imperative/declarative phrasing ("Do this. Then do that.") more than causal phrasing ("Do this because it ensures..."). The `_has_structural_rationale` check requires causal connectors.

**Fix:** The token expansion in Problem 3 (`the reasoning`, `by doing so`, `this allows`, `this enables`) directly addresses DeepSeek's phrasing patterns. No additional fix needed beyond Problem 3.

---

## Implementation Order

### Immediate (1–2 hours, no regression risk)
1. **Problem 7** — Change Gemini default to `gemini-2.5-pro` in `run_batch_parallel.py`
2. **Problem 1** — Add `PROVIDER_MAX_TOKENS` dict and use per-provider max_tokens
3. **Problem 4** — Expand `implementation_constraint` patterns in `runtime_validator.py`
4. **Problem 3** — Expand `TRADEOFF_TOKENS`, `RATIONALE_TOKENS`, and structural pattern functions

### Short-term (2–4 hours, run validate_examples.py before merge)
5. **Problem 2** — Add routing preamble stripping to `strip_reasoning_blocks()`
6. **Problem 5** — Expand `any_of` token lists for top failing decisions in `task_contracts.json`
7. **Problem 6** — Add superlative/shortcut warnings to affected launchers

### Targeted (requires careful testing)
8. **Problem 8** — Expand pass-17 launcher instructions and pass-11 `inference_boundary` tokens
9. **Problems 9 & 10** — Add evidence-grounding instructions to xAI-weak launchers

---

## Projected Pass Rate Improvements

| Provider | Current | After immediate | After all fixes |
|----------|---------|-----------------|----------------|
| Claude | 100% | 100% | 100% |
| Mistral | 100% | 100% | 100% |
| DeepSeek | 100% | 100% | 100% |
| OpenAI | 100%* | 100% | 100% |
| xAI | 97% | 98% | 100% |
| Gemini | 42% | ~65% | ~80% |

*OpenAI passes via dual gate — validator score health improves from avg 78.2 to ~86+

Gemini's ceiling is gated by the model switch (Problem 7) and max_tokens fix (Problem 1). Even with all fixes applied, pass-17 (tiered frontend explanation) remains the hardest test across all providers and may need contract-level relaxation rather than purely alias-based fixes.
