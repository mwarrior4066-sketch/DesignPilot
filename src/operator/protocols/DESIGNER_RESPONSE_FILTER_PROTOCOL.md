# Designer Response Filter Protocol

This protocol governs the AI-to-designer response filter.
It is a cross-cutting transformation layer, not a governing route.

## Purpose
Translate routed expert output into designer-readable explanation without weakening technical truth, implementation realism, or evidence burden.

## Placement in the runtime loop
Run the filter after route selection and draft generation, but before final validation.

1. route and draft normally
2. read the active explanation tier from `SESSION_CONTEXT.md`
3. transform the answer through the response filter
4. optionally run text humanization on prose-heavy sections
5. validate the filtered answer

## Core response architecture
Use this transformed response shape when the answer is explanatory or advisory:
1. executive summary or core verdict
2. impact analysis or contextual framing
3. constraints and implementation realism
4. actionable next steps

This structure may compress for Strategic tier, but the logic should remain visible.

## What the filter may change
- jargon density
- explanation depth
- contextual framing
- example use
- term translation behavior
- next-step direction
- hand-holding level

## What the filter may not change
- governing route
- required task decisions
- required evidence classes
- implementation constraints
- proof honesty
- code or spec artifacts that must stay literal

## Term-handling logic
Use a practical importance/familiarity filter per term:
- preserve directly
- preserve with a short inline bridge
- paraphrase into designer-facing functional language
- omit if the term does not change the user’s decision or action

## Faithfulness rule
Translation is not simplification by deletion.
If a hard boundary exists, the filtered answer must still state it.
If a system risk exists, the filtered answer must still expose it.
If proof is missing, the filtered answer must still say so.

## Tier shaping
### Functional
- shorter technical runs
- more explicit cause and effect
- more visible next steps
- stronger action framing

### Integrative
- moderate jargon with bridges
- rationale and cross-functional tradeoffs visible
- next steps shaped by dependencies

### Strategic
- compressed framing
- direct decisions and constraints
- minimal scaffolding and no tutorial filler

## Trigger conditions
Use the filter when:
- the answer is technically dense
- the user is a designer or adjacent operator who needs implementation truth translated into usable design reasoning
- the active explanation tier is Functional or Integrative
- the answer must end with a practical next move

## Anti-patterns
- replacing precision with vibe
- removing implementation realism
- converting hard constraints into soft suggestions
- bloating the answer with generic scaffolding
- flattening every answer into the same summary style
