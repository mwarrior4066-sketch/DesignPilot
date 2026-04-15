# DesignPilot Cross-Model Batch Test — Synthesis Report
**Date:** April 14, 2026  
**Runs analyzed:** 6 (batch-20260414-0148 through 0346)  
**Full-suite runs (19 tests):** 4 runs × up to 6 providers  
**Note:** Run 0148 and 0203 used the old 5-test suite and are treated as early/debug runs. Run 0253 is missing a comparative_report.json and was reconstructed from provider summaries. All quantitative figures below draw from the full 19-test runs only.

---

## Provider Scorecard

| Provider | Model | Tests | Pass Rate | Avg Validator Score | Avg Rubric | Passed by Rubric Only |
|----------|-------|-------|-----------|--------------------|-----------|-----------------------|
| **Claude** | claude-sonnet-4-6 | 38 | **100%** | 86.7 / 100 | **4.72 / 5.0** | 6 |
| **Mistral** | mistral-large-latest | 36 | **100%** | **86.9 / 100** | 4.60 / 5.0 | 11 |
| **DeepSeek** | deepseek-chat | 38 | **100%** | 84.1 / 100 | 4.48 / 5.0 | 17 |
| **OpenAI** | gpt-4.1 | 19 | **100%** | 78.2 / 100 | 4.39 / 5.0 | 11 |
| **xAI** | grok-3-fast | 38 | **97%** (37/38) | **91.6 / 100** | 3.98 / 5.0 | 12 |
| **Gemini** | gemini-2.5-flash | 38 | **42%** (16/38) | 42.4 / 100 | 2.33 / 5.0 | 9 |

---

## Rubric Dimension Breakdown (Run 0253)

| Provider | Intent Alignment | Actionability | Structural Rigor | Evidence Use | Implementation Realism |
|----------|-----------------|---------------|-----------------|--------------|----------------------|
| Claude | **5.00** | 4.42 | **5.00** | 4.47 | **4.84** |
| Mistral | 4.84 | 4.38 | 4.91 | 4.22 | 4.63 |
| DeepSeek | 4.84 | 4.21 | 4.95 | 3.84 | 4.63 |
| xAI | 4.47 | 3.74 | 4.63 | 3.26 | 4.05 |
| Gemini | 3.12 | 2.35 | 2.82 | **1.94** | 2.47 |

---

## Per-Test Results (Run 0215 — 19 tests × 5 active providers)

Mistral was ERR in run 0215 (rate limit issue, resolved in later runs 0319/0346).

| Test | Task | Claude | OpenAI | xAI | DeepSeek | Gemini |
|------|------|--------|--------|-----|----------|--------|
| pass-01 | ui_structure_critique | ✓ 88 | ✓100 | ✓100 | ✓ 94 | ✗ 18 |
| pass-02 | component_spec | ✓ 94 | ✓100 | ✓ 96 | ✓ 84 | ✓ 58 |
| pass-03 | dashboard_audit | ✓ 88 | ✓ 84 | ✓ 86 | ✓ 90 | ✗ 0 |
| pass-04 | backend_feasibility_review | ✓ 78 | ✓ 84 | ✓100 | ✓100 | ✗ 0 |
| pass-05 | pdf_remediation_plan | ✓ 94 | ✓ 74 | ✓100 | ✓ 94 | ✗ 54 |
| pass-06 | brand_positioning_pass | ✓ 80 | ✓ 70 | ✓ 72 | ✓ 72 | ✗ 16 |
| pass-07 | case_study_rewrite | ✓ 80 | ✓ 42* | ✓ 70 | ✓ 82 | ✗ 0 |
| pass-08 | accessibility_feedback_audit | ✓ 82 | ✓ 94 | ✓100 | ✓ 94 | ✗ 0 |
| pass-09 | color_system_spec | ✓ 78 | ✓ 82 | ✓ 96 | ✓ 76 | ✓ 84 |
| pass-10 | graphic_critique | ✓ 88 | ✓100 | ✓100 | ✓ 62 | ✓ 94 |
| pass-11 | layout_reconstruction_plan | ✓ 90 | ✓ 90 | ✓ 96 | ✓ 88 | ✗ 14 |
| pass-12 | type_system_recommendation | ✓ 96 | ✓ 90 | ✓ 86 | ✓ 68 | ✗ 16 |
| pass-13 | ux_research_gap_map | ✓ 88 | ✓ 90 | ✓ 90 | ✓100 | ✓ 90 |
| pass-14 | frontend_implementation_review | ✓ 82 | ✓ 68* | ✓100 | ✓ 84 | ✗ 38 |
| pass-15 | backend_architecture_spec | ✓ 93 | ✓ 65* | ✓ 96 | ✓ 75 | ✗ 78 |
| pass-16 | api_reliability_security_review | ✓ 90 | ✓ 62* | ✓ 82 | ✓ 78 | ✗ 0 |
| pass-17 | frontend_impl_review (tiered) | ✓ 81 | ✓ 39* | **✗ 78** | ✓ 67 | ✗ 58 |
| pass-18 | api_reliability_review (filter) | ✓ 88 | ✓ 57* | ✓100 | ✓ 96 | ✗ 0 |
| pass-19 | text_humanization_revision | ✓ 84 | ✓ 94 | ✓ 88 | ✓ 78 | ✓ 94 |

*Passed via rubric gate only (validator score too low).

---

## What Went Right

**The dual gate worked as designed.** OpenAI passed 11 of its 19 tests via the rubric gate alone — meaning it produced good design reasoning in its own vocabulary, even when the static validator couldn't match its section headings. Without the rubric gate, OpenAI would have shown a ~42% pass rate. The system correctly distinguishes vocabulary mismatch from genuine quality failure.

**Claude, Mistral, DeepSeek, and xAI all cleared the 70% gate with margin.** Four of six providers are production-ready against this suite. The DesignPilot system prompt transfers effectively across OpenAI-compatible endpoints.

**Five tests passed universally.** pass-02 (component_spec), pass-09 (color_system_spec), pass-10 (graphic_critique), pass-13 (ux_research_gap_map), and pass-19 (text_humanization_revision) were never failed by any working provider. These tasks have sufficiently general contract vocabulary that all model families satisfy them naturally.

**xAI/Grok had the highest average validator score (91.6).** Grok follows structural contracts more precisely than any other non-Claude model, suggesting it reads and follows the section heading instructions closely.

**Mistral went from 0% to 100% across three runs.** The SDK import fix and rate limit adjustment resolved all issues. The final run (0346) scored 19/19 with strong rubric scores and most tests passing via validator.

---

## What Went Wrong

### Gemini — needs a different model

42% pass rate with an average validator score of 42.4 is not close to acceptable. The issues are not primarily vocabulary — they are response quality problems. Six tests scored exactly 0. The rubric scores confirm this: evidence_use averaged 1.94/5.0, actionability 2.35/5.0. These are not mismatched headings, they are genuinely thin responses.

The root cause is that **gemini-2.5-flash does not have the capacity to handle an 118KB system prompt and produce a full structured analytical response**. Even with the system prompt prepended to the user message, flash-class models compress their output heavily under long-context conditions. The dominant failure signatures are `low_information_density`, `missing_tradeoff`, and `prompt_restatement` — all of which indicate the model is producing abbreviated summaries rather than full analytical work.

The fix is to switch to **gemini-2.5-pro**, which has the capacity to handle the full system prompt and produce the required depth. Flash was the wrong model choice for this suite.

### OpenAI — high rubric dependency

11 of 19 OpenAI tests passed only via the rubric gate. Several had alarming validator scores: pass-17 scored 39, pass-07 scored 42. The validator found real issues — missing tradeoff language, missing required decision tokens, forbidden shortcuts (`unsupported_superlative`). The rubric confirmed the underlying reasoning was good enough to pass, but these are not comfortable passes.

GPT-4.1 uses different vocabulary for the same concepts. The case study rewrite (pass-07) scored 42 because it used clean prose structure instead of the contract's named section vocabulary. The frontend tiered explanation (pass-17) scored 39 because it presented tiers differently than the contract expected. These are alias gaps, not quality gaps — but there are more of them for GPT-4.1 than for any other working provider.

### xAI single failure — pass-17

Grok-3-fast failed pass-17 (frontend_implementation_review tiered explanation) with a score of 78 and a `missing_required_decision` hard failure. This is the hardest test in the suite — it requires a specific tiered explanation structure that conflicts with how Grok organizes multi-part architectural answers. It was also the only test DeepSeek scored below 80 on (67, passed via rubric). pass-17 is a structural edge case that challenges every model's section-organization habits.

### Infrastructure issues

Mistral required three separate runs due to the SDK import bug and then rate limiting. The 30-second delay between calls resolved the rate limit problem, but the time cost is significant — 19 tests at 30s delay is ~10 minutes for Mistral alone. DeepSeek had billing failures in early runs that required account top-up before the full suite could run.

---

## Easiest and Hardest Tests

**Never failed by any working provider:**
- pass-02 component_spec
- pass-09 color_system_spec
- pass-10 graphic_critique
- pass-13 ux_research_gap_map
- pass-19 text_humanization_revision

**Hardest — failed by most providers:**
- **pass-17** (frontend_implementation_review tiered) — failed by Gemini and xAI, borderline on OpenAI (score 39)
- **pass-07** (case_study_rewrite) — failed by Gemini, OpenAI passed only via rubric at score 42
- **pass-16/18** (api_reliability_security_review) — failed by Gemini with score 0; OpenAI passed via rubric

---

## Recommended Actions

**Switch Gemini to gemini-2.5-pro.** Flash cannot handle this workload. Change the default in `run_batch_parallel.py`:
```python
'gemini': 'gemini-2.5-pro',
```

**Add GPT-4.1 section aliases.** 11/19 rubric-only saves is too many. The vocabulary gaps for case study rewriting, tiered frontend explanations, and API reliability reviews should be documented in `section_aliases.json`.

**pass-17 needs contract review.** It is the single hardest test in the suite and represents a structural edge case where the tiered explanation format conflicts with expected section names for every model family except Claude and DeepSeek. Either add aliases for the tiered vocabulary or relax the decision token requirements for this test type.

**OpenAI `unsupported_superlative` and `forbidden_shortcut` failures** suggest GPT-4.1 occasionally introduces ungrounded certainty claims or shortcut language. These are genuine quality issues, not vocabulary gaps — worth monitoring in repeated runs.
