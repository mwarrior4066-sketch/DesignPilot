# AI-to-Designer Response Filter Report

## Scope
Operational source document for the designer-readable transformation layer. This knowledge base governs how DesignPilot converts high-density specialist output into language a designer can act on without stripping the route’s real constraints, proof burden, or implementation logic.

## Why this layer exists
The pack now contains specialized domains that can easily produce answers that are technically correct but difficult to use in practice. A designer often does not need every implementation primitive in first-load form, but they **do** need the real constraint, the actual risk, and the next concrete move. The response filter exists to solve that explanation problem without degrading the underlying decision.

The filter is therefore not a style pass. It is a controlled transformation layer between expert reasoning and operator usability.

## Core thesis
Simplification removes detail. Translation remaps technical meaning into a domain the operator can act on. The response filter must preserve route integrity, constraints, and proof honesty while changing the explanation surface.

A compliant filter does all of the following at once:
- preserves the real verdict
- preserves hard constraints and feasibility boundaries
- changes jargon density and scaffolding depth to fit the active tier
- surfaces the most decision-useful information first
- gives the user an actionable next move

## Middleware position
The filter belongs **after** specialist draft generation and **before** final validation.

Canonical chain:
1. route chooses governing specialist
2. specialist produces the real answer
3. response filter reshapes explanation depth and framing
4. final validator checks whether the filtered answer still tells the truth of the specialist output

This placement matters. If filtering happens too early, the system may downgrade the reasoning itself. If it happens too late with no validation, the system may sound friendly while silently dropping constraints.

## What the filter is allowed to change
The filter may change:
- jargon density
- explanatory pacing
- sentence complexity
- framing order
- analogy use
- scaffold visibility
- example selection
- how next-step guidance is presented

The filter may compress or expand explanation depth depending on the active comprehension tier, but only if the decision logic remains intact.

## What the filter must not change
The filter must not change:
- the governing route
- the real verdict
- required task decisions
- evidence burden
- implementation constraints
- risk posture
- compliance or accessibility obligations
- code or strict spec artifacts when the request needs exactness

A filtered answer that becomes easier to read by becoming less true is a failure.

## Response architecture
Default response architecture for designer-readable transformation:
1. **Core verdict** - what the system thinks and why it matters now
2. **Impact framing** - what changes if the operator follows or ignores the advice
3. **Constraints and realism** - what still must be true technically or operationally
4. **Actionable next steps** - the smallest useful move the operator should make next

This architecture can compress or expand, but the order should stay stable in most cases because it mirrors how design operators decide.

## Tier behavior
### Functional tier
Use direct, task-led language. Minimize abstraction. Explain technical terms only when they block action.

### Integrative tier
Preserve more system logic. Show how the decision affects adjacent domains such as accessibility, front-end handoff, or component behavior.

### Strategic tier
Retain more tradeoffs, sequencing, and implementation implications. The user may want governance logic, proof boundaries, or architecture rationale made visible.

## Translation rules
### 1. Preserve the noun of record
If a specialist identifies a specific artifact or concern, keep the official noun. For example, do not replace “object-level authorization” with “better permissions” if the narrower term matters to implementation.

### 2. Bridge before replacing
When a term matters, bridge it with short explanation rather than swapping it for a vague equivalent.

### 3. Compress scaffolding first, not constraints first
The first thing to trim is decorative setup, not operational detail.

### 4. Make the implication explicit
If the answer implies a risk, name the risk directly instead of assuming the operator will infer it.

### 5. Keep the decision boundary visible
Do not let an easier tone obscure whether the system is passing, failing, warning, or redirecting.

## Failure patterns
Common failure patterns include:
- technically correct but unreadable for the current tier
- easy to read but stripped of the real constraint
- smooth tone with no decision edge
- no next-step direction
- bloated scaffolding that adds no decision value
- replacing implementation language with empty reassurance
- shifting from bounded recommendation to implied certainty

## Good filter behavior
A good filtered answer should feel like:
- the same decision
- told at the right density
- with the next action made obvious

It should not feel like a second opinion or a motivational rewrite.

## Validation logic
Every filtered answer should be checked for:
- **semantic preservation**: no meaning drift from the source answer
- **constraint preservation**: hard limits still visible
- **verdict preservation**: pass/fail/warn/escalate state unchanged
- **evidence preservation**: unsupported claims not introduced
- **actionability**: a next move exists when appropriate
- **tier fit**: explanation depth matches the chosen comprehension mode

## Use boundaries
Use the response filter on:
- critique
- planning
- design rationale
- implementation explanation
- case-study analysis
- audit writeups that need designer-readable presentation

Do not run it blindly on:
- code
- schemas
- task contracts
- raw validator output
- compliance artifacts where exact wording is part of the deliverable

## Relationship to adaptive explanation
The adaptive explanation system chooses **how much explanation** the user likely needs. The AI-to-designer response filter governs **how the chosen explanation should be expressed** while preserving truth and route integrity.

## Relationship to text humanization
Humanization restores authored texture and readability. The response filter preserves decision usability and technical truth. They may operate together, but they are not the same layer.

## Canonical operating stance
When in doubt:
- preserve the specialist’s actual decision
- remove decorative complexity
- surface the real constraint
- point the operator to the next useful move

The filter exists to improve actionability, not to make the answer merely sound nicer.


## Review checklist for DesignPilot
Use this source to ask:
- What is the real verdict the specialist produced?
- Which constraints are non-negotiable and must stay visible?
- What explanation density best fits the active tier?
- What is the smallest next move the operator should be able to take after reading the answer?
- Did the transformation improve usability without reducing truth?

## Success conditions
This layer succeeds when the operator can act more effectively while the routed answer remains equally correct, equally bounded, and equally honest about risk.
