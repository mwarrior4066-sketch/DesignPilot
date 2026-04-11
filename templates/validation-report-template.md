# Validation Report Template

## Input
- task id:
- prompt class:
- expected mode:
- expected phase behavior:
- expected pathway:

## Draft check
- mode status:
- phase status:
- pathway status:
- output contract status:
- domain validator status:
- document/presentation architecture:
- evidence status:
- contradiction status:

## Hard-fail check
- triggered hard fail? yes/no
- if yes, why:

## Weighted score
- mode correctness:
- phase correctness:
- pathway correctness:
- contract completeness:
- domain compliance:
- evidence quality:
- document/presentation integrity:
- contradiction handling:
- clarity/directness:
- total:

## Decision
- pass / auto-revise / constrain / clarify / escalate / fail

## Revision notes
- 

## Example output
### Input
- task id: T-042
- prompt class: off-phase production request
- expected mode: structure or constrain, not rebuild
- expected phase behavior: block final UI production because research and IA are incomplete
- expected pathway: roadmap router -> task router -> UI + validation layer

### Draft check
- mode status: partial pass; the draft acted like a rebuild answer before acknowledging the phase problem
- phase status: fail on first pass, corrected on validation
- pathway status: pass; right skills were activated
- output contract status: pass after revision; final answer included constraint, rationale, and next step
- domain validator status: pass; no accessibility or layout rules violated in the abstract recommendation
- evidence status: medium; enough roadmap logic was cited but no explicit source reminders were included
- contradiction status: pass after validation; user wanted final UI, but the validator correctly forced an off-phase constraint

### Hard-fail check
- triggered hard fail? no
- if yes, why: not triggered because the draft was revisable rather than unsafe

### Weighted score
- mode correctness: 7/10
- phase correctness: 4/10 first pass, 10/10 after revision
- pathway correctness: 10/10
- contract completeness: 9/10
- domain compliance: 10/10
- evidence quality: 7/10
- contradiction handling: 9/10
- clarity/directness: 9/10
- total: 8.9/10 after revision

### Decision
- pass / auto-revise / constrain / clarify / escalate / fail: auto-revise, then pass

### Revision notes
- Front-load the phase gate earlier.
- Do not begin with solutioning language when the correct move is to block or constrain.
- Keep the answer direct: explain why the request is off-phase and what artifact should be completed first.
