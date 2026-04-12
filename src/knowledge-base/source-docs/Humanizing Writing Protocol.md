# Humanizing Writing Protocol

## Purpose
Restore authored texture and readability to prose without changing meaning, adding claims, or flattening the writer’s voice.

This document governs the pack’s humanization layer for prose-heavy writing such as rationale, explanation, case-study narrative, design communication, and reflective analysis. It should not be treated as a generic “make it sound better” pass.

## Problem statement
AI-shaped writing often looks polished before it reads as believable. Common symptoms include:
- predictable sentence starts
- uniform sentence rhythm
- overuse of abstract nouns where concrete verbs should appear
- filler transitions that do not move the argument
- excessive smoothing that removes the writer’s actual stance

The humanization layer exists to correct these patterns while preserving meaning, structure, and voice identity.

## Core rule
Humanization is a revision discipline, not a style transplant. It must preserve the author’s intent, argument, and tone direction while reducing machine-shaped scaffolding.

## Hard rules
- preserve meaning
- preserve argument structure unless the task explicitly asks for reordering
- do not rewrite for difference only
- do not casualize by default
- do not add filler or mood padding
- do not replace the writer’s voice with generic polish
- do not invent sensory or emotional language the source did not support
- do not convert precise language into trendier but weaker language

## Revision sequence
1. identify the job of the piece
2. identify the writer’s current voice signals
3. scan for repeated sentence patterns and machine-shaped scaffolding
4. repair grammar, action logic, and sentence-to-sentence flow
5. rebalance rhythm, clause length, and transition load
6. trim inflated abstraction and needless qualifiers
7. run a final realism pass for tone and authored texture

## What counts as authored texture
Authored texture is not slang, looseness, or informality by default. It includes:
- specific phrasing choices that sound intentional
- variable rhythm
- concrete action verbs
- transitions that feel earned rather than inserted
- a consistent stance toward the subject
- selective emphasis instead of constant polish

## Anti-patterns
Common machine-shaped prose failures:
- predictable sentence openings repeated across the piece
- abstract nominalized phrases where concrete verbs should appear
- stacked qualifiers with no added precision
- flat rhythm and uniform clause length
- “helpful” transitions that say nothing
- overbalanced paragraph structures
- generic intensifiers such as “deeply,” “powerful,” or “nuanced” used without evidence
- replacement of exact terms with softer but less accurate phrasing

## Structural caution
Do not mistake organization for stiffness. Some writing, especially academic or technical rationale, needs formal structure. Humanization should remove mechanical repetition, not erase discipline.

## Voice preservation strategy
Before revising, identify the source voice on these axes:
- formal vs conversational
- analytical vs descriptive
- compressed vs expansive
- neutral vs opinionated
- technical vs plainspoken

Then revise toward the source, not away from it.

## Sentence-level priorities
At the sentence level, prioritize:
- concrete verbs over abstract nouns where possible
- shorter bridges between related claims
- fewer stacked prepositional phrases
- varied rhythm without forced fragmentation
- removal of duplicated qualifiers and self-explaining clauses

## Paragraph-level priorities
At the paragraph level, prioritize:
- a visible point for each paragraph
- transitions that genuinely move the thought forward
- reduced repetition of framing language
- better distribution of emphasis so every paragraph does not peak the same way

## Meaning-preservation rules
Never humanize by:
- adding new facts
- changing certainty level
- changing chronology
- softening a warning into a suggestion
- turning a bounded claim into a broad one
- reassigning agency or responsibility implicitly

## Special use cases
### Case studies and rationale
Preserve the project logic and proof chain. Humanization should make the narrative feel authored, not promotional.

### UX or design critique
Keep the decision edge. Do not smooth direct critique into neutral mush.

### Academic or research writing
Preserve precision and structure. Humanization may reduce stiffness, but it must not remove the argumentative spine.

### Portfolio writing
Preserve the author’s positioning and specificity. Avoid synthetic brand polish unless requested.

## Use boundaries
Run this on prose-heavy explanation, rationale, and narrative writing. Do not run it blindly on code, schemas, strict specs, validator reports, or policy language where exact wording matters.

## Validation logic
Humanization should be checked for:
- semantic drift
- transition pruning
- action-to-noun ratio improvement
- reduced structural predictability
- tone consistency with the source
- preserved argument order unless reordering was requested
- preserved certainty and claim boundaries

## Good output characteristics
A successful humanization pass should feel:
- more readable
- more intentional
- less repetitive
- more natural in rhythm
- still recognizably the same writer

## Failure patterns
Humanization fails when it:
- makes every sentence friendlier but less precise
- introduces generic “writerly” flourishes with no function
- strips out the original edge or tension
- turns direct analysis into decorative prose
- makes the text sound like the model instead of the writer

## Operating stance
The humanization layer should behave like an exacting editor, not a ghostwritten personality swap. The job is to preserve what is real in the prose and remove what reads like machine residue.


## Review checklist for DesignPilot
Use this protocol to ask:
- Is the text preserving the writer’s actual stance?
- Did revision improve readability without changing claim strength?
- Are transitions carrying argument weight rather than decorative tone?
- Is the voice still specific to the source rather than generalized into model polish?
- Would the revised piece still sound like the same author in a side-by-side read?

## Success conditions
A successful humanization pass should make the writing easier to trust because it reads more intentional and less machine-shaped, not because it becomes softer, trendier, or more uniformly polished.
