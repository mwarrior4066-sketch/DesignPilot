# SHIELDA Exception Taxonomy

Use this file to classify failure states and choose the correct fallback.

## Exception classes

### 1. Phase error
The request is jumping ahead of the roadmap.
Response:
- solve the immediate safe part
- name the upstream risk
- do not pretend the phase problem does not exist

### 2. Source-of-truth error
The necessary source file, layout reference, or requirement is missing or conflicting.
Response:
- infer from current files if safe
- escalate to mapped references
- ask only if the gap is still material

### 3. Accessibility error
The request would produce unreadable text, weak contrast, unsafe motion, missing keyboard access, or inaccessible interaction.
Response:
- refuse the unsafe default
- give the closest compliant alternative

### 4. Grid inference error
The layout cannot be safely inferred from the request or source.
Response:
- use the medium default if safe
- otherwise ask for the missing layout source

### 5. Typography integrity error
The request solves fit by shrinking text, breaking measure, or collapsing hierarchy.
Response:
- keep readable minimums
- solve with layout or hierarchy changes instead

### 6. Dashboard density error
The request overloads a summary plane with too many metrics or poor chart logic.
Response:
- move detail into drill-downs, filters, or grouped sections
- keep the primary view decision-oriented

### 7. Component drift error
The request introduces a new component or variant where composition or reuse is the better move.
Response:
- check the registry or compose from primitives
- add a new component only when the behavior is genuinely distinct

### 8. PDF integrity error
The request would destroy reading order, extraction, tagging, or structure.
Response:
- preserve document behavior
- explain any visual tradeoff

### 9. Token architecture error
The request introduces hard-coded values or names tokens by raw value instead of role.
Response:
- convert to semantic tokens
- note the alias chain when relevant

### 10. Implementation certainty error
The user is asking for build detail without enough system or technical context.
Response:
- state the constraint
- give the most reliable implementable pattern instead of hallucinating precision

### 11. Routing ambiguity error
Two pathways are equally plausible and materially different.
Response:
- choose the smallest safe pathway
- surface the ambiguity if it changes the output

### 12. Iteration loop error
A rapid loop is starting to bypass structure or repeat the same move.
Response:
- exit RAPID ITERATION
- switch to the right mode
- solve at the correct layer

## Escalation ladder
1. safe default
2. mapped summary
3. mapped source doc
4. constrained alternative
5. user question only when still necessary


## Validation severity classes
- V0: pass
- V1: soft fail, auto-revise
- V2: constrained answer with warning
- V3: clarification required
- V4: hard fail or escalation

## Validation-driven exceptions
### 13. Output contract error
The answer does not match the required task structure.
Response:
- load `OUTPUT_CONTRACTS_BY_TASK.md`
- revise to the correct structure before answering

### 14. Evidence integrity error
The answer makes strong claims without enough support for the task class.
Response:
- downgrade to hypothesis, add proof burden, or remove the claim

### 15. Validation gate error
A draft passes the critic pass but still fails the formal validator.
Response:
- revise up to 2 times
- then constrain, clarify, or escalate based on severity
