---
runtime_summary_version: 1.0.0
canonical_summary: knowledge-base/summaries/component-systems-summary.md
last_generated: 2026-04-11
overlay: true
source_reference:
  - knowledge-base/source-docs/Component Systems Expert Research.md
---
# Component Systems Summary Runtime Summary

## Decision rules
- prefer reuse and composition before new components
- every component should document purpose, when to use, when not to use, variants, sizes, states, accessibility rules, and implementation status
- stable components beat local custom reinventions
- every interactive component needs state coverage, not just a rest state

## Failure traps
- phantom components with no real spec
- duplicate components solving the same task
- unstable variants used as if they were core system primitives
- visual variants added without new behavior or semantic need
- component docs missing “when not to use”

## Escalate when
- the runtime summary lacks exact thresholds, standards wording, or measurable criteria
- two summaries or skills conflict and the governing rule is unclear
- the validator flags missing evidence classes or insufficient evidence
- the task is high-stakes, standards-grade, or audit-sensitive
- the user explicitly asks for deep rationale or full-source synthesis

## Canonical fallback
- `knowledge-base/summaries/component-systems-summary.md`
- `knowledge-base/source-docs/Component Systems Expert Research.md`