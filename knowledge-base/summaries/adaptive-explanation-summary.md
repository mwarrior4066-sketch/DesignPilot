---
summary_version: 1.0.0
source_reference:
  - knowledge-base/source-docs/Adaptive Explanation Design Report.md
last_updated: 2026-04-11
synchronized: true
domain: designer-comprehension
---

# Adaptive Explanation Summary

## Purpose
Condensed operating rules for session-level explanation calibration.

## Use when
- the user’s preferred explanation depth is not yet known
- expert output risks being too dense or too tutorial-heavy
- the pack needs to decide how much scaffolding to provide before changing prose style

## Canonical tiers
- Functional
- Integrative
- Strategic

## Key state fields
- design_experience_tier
- jargon_threshold
- scaffolding_mode
- proactivity_index
- override_stack
- calibration_source
- calibration_complete

## Default rules
- explanation depth is a live session variable
- use a light startup calibration first
- allow temporary local overrides
- change scaffolding without weakening constraints
- preserve critical technical terms when they carry decision weight
