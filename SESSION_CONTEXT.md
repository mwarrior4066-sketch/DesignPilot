# Session Context

Track only active session state here.

## Required fields
- active_mode
- active_phase
- active_pathway
- loaded_tiers
- loaded_skills
- loaded_summaries
- loaded_templates
- active_constraints
- unresolved_questions
- validation_status
- design_experience_tier
- jargon_threshold
- scaffolding_mode
- proactivity_index
- override_stack
- calibration_source
- calibration_complete

## Runtime rule
This file is the live session scratch state.
Do not treat it as a source of truth for domain logic.
Do not preload deep knowledge into it.
Keep it short.

## Comprehension-layer rule
Store only the currently active explanation behavior here.
Do not use this file to restate the whole protocol.
The protocol lives in `ADAPTIVE_EXPLANATION_PROTOCOL.md`.
