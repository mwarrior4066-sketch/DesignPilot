# Text Humanization Example
Fixture: tests/fixtures/text-humanization-pass.prompt.md
Validation result: tests/evals/text-humanization-pass.eval.json

## Input Prompt
Humanize this paragraph without changing the meaning:

"The interface facilitates user progression through the workflow by leveraging a systematic arrangement of controls and contextual indicators. This enables users to maintain awareness of status transitions while reducing the likelihood of interaction ambiguity during task completion."

## Selected Route and Loaded Skills
- Route: `rt_text_humanization`
- Task contract: `text_humanization_revision`
- Mode: REBUILD
- Phase: communication
- Skills: `text-humanization-expert.md`, `content-and-case-study-expert.md`

## Final Output
### Job of the piece
The text is trying to explain why the interface is easier to move through and understand. That purpose must still do the same job after revision, so the rewrite cannot drift into claims about delight, speed, or conversion.

### Pattern scan
The source relies on repeated abstract phrasing such as “user progression,” “systematic arrangement,” and “interaction ambiguity.” Those nominalization-heavy patterns flatten the rhythm, make the sentence feel formulaic, and hide the real action inside noun stacks instead of clearer verbs.

### Meaning-preservation guard
The meaning-preservation guard is explicit here. Three claims must stay unchanged: the layout helps users move through the workflow, it keeps status changes legible, and it lowers confusion during task completion. The main drift risk would be turning the paragraph into a claim about delight, acceleration, or ease beyond what the source actually states.

### Revised passage
The interface helps users move through the workflow because the controls and status cues are arranged in a way that stays clear as the task changes. Users can see where they are, what just changed, and what to do next without getting tripped up by unclear interactions. Compared with the source, the revision keeps the same claims but uses stronger verbs and a clearer before/after structure.

### Why this reads more human
The revision repairs the action logic, prunes formulaic scaffolding, and rebalances the rhythm so the paragraph sounds authored rather than generated. The voice is still restrained, but it is not replaced by generic polish or forced casualness, and the before/after comparison stays tied to the original meaning boundary.

### Drift check
No new performance, delight, or conversion claim was introduced. The revision stayed inside the original meaning boundary and used a before/after comparison artifact rather than vague polish language.

## Why This Passed
- It makes the meaning boundary explicit before rewriting.
- It names the machine-shaped patterns instead of vaguely calling the prose robotic.
- The revised paragraph uses clearer verbs and rhythm without changing the claims.

## What Would Have Failed
- Adding new claims about speed, delight, or conversion.
- Making it casual just to sound less formal.
- Changing the paragraph so much that the original purpose is lost.

## Revision Pass
The weak draft simply replaced words with looser synonyms. The corrected version preserved the original claims, changed the verb structure, used a before/after comparison, and removed the abstract noun pile that made the source sound mechanical.
