---
runtime_summary_version: 1.0.0
canonical_summary: src/knowledge-base/summaries/validation-and-stress-testing-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - src/knowledge-base/source-docs/AI Operator Pack Validation & Stress Testing.md
---
# Validation And Stress Testing Summary Runtime Summary

## Decision rules
- evaluate the whole execution path, not just the final wording
- keep smoke tests separate from deeper pathway, domain, contradiction, and regression tests
- validate mode, phase, pathway, output contract, domain compliance, evidence, and contradictions before accepting a draft
- use hard gates for accessibility, document integrity, unsupported claims, wrong-mode outputs, and impossible feasibility
- use weighted rubrics only after hard gates pass
- permit at most two self-revision loops before constraining, clarifying, or escalating

## Failure traps
- No extracted failure traps; fall back to the canonical summary.

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `src/knowledge-base/summaries/validation-and-stress-testing-summary.md`
- `src/knowledge-base/source-docs/AI Operator Pack Validation & Stress Testing.md`