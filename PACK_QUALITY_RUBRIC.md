# Pack Quality Rubric

> Generated from `tests/scorecards/task_quality_rubric.json`.

This readable mirror exists so a human maintainer can inspect the operational scoring logic without reading the raw JSON scorecard.

| Criterion | Weight | Pass threshold | Judge question |
|---|---:|---:|---|
| intent_alignment | 20 | 4 | Did the response resolve the actual ask without drifting? |
| actionability | 20 | 4 | Can a designer or maintainer act on this immediately? |
| structural_rigor | 20 | 4 | Does the answer show hierarchy, sequence, and route logic? |
| evidence_use | 20 | 4 | Are claims linked to thresholds, receipts, or explicit proof types? |
| implementation_realism | 20 | 4 | Is the proposal technically and operationally believable? |

## Bias controls
- penalize verbosity that does not improve actionability
- swap answer order in comparisons when judging baseline vs pack
- ignore references to outside authority unless supported by the artifact itself
