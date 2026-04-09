# Validation Rubrics

Use weighted scoring only after hard gates pass.
Hard-gate violations override numeric scores.

## Global weighted rubric
- mode correctness: 15
- phase correctness: 10
- pathway correctness: 10
- output contract completeness: 15
- domain rule compliance: 20
- evidence / provenance quality: 15
- contradiction handling: 10
- clarity and directness: 5

Total: 100

## Decision bands
- 90–100: pass
- 80–89: pass only if no meaningful soft fails remain
- 70–79: auto-revise
- <70: fail

## Hard-gate overrides
Any of these force fail regardless of score:
- accessibility minimum violated
- wrong mode in a materially different way
- off-phase output presented as final without warning
- unsupported claim in high-stakes context
- PDF/document integrity break
- impossible request passed through as feasible

## Domain weighting adjustments
### Strategy / brand
Increase evidence and contradiction handling weights.

### UI / front-end / accessibility
Increase domain rule compliance weight.

### Dashboard / data-vis
Increase domain rule compliance and clarity weights.

### PDF / document
Increase domain rule compliance and output contract weights.

### Case study / content
Increase mode correctness and evidence quality weights.

## Rubric notes
- “sounds good” is not a criterion
- specificity without correctness is not a pass
- confidence without support is a penalty
