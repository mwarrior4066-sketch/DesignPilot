# Adaptive Explanation Design Report

## Scope
Working source document for the Designer Comprehension Layer. This document defines how DesignPilot adapts explanation depth, scaffolding, terminology, and proactive clarification without changing the truth of the routed specialist answer.

## Problem statement
The comprehension problem is not only jargon. It is mismatch between expert output and the user’s working mental model. Too much unexplained density creates overload. Too much redundant explanation creates cognitive noise, ego friction, and slower decision-making.

The goal of adaptive explanation is not to guess how smart the user is. The goal is to match explanation depth to the work they are trying to do **right now**.

## Core thesis
A compliant answer changes its explanation depth without changing the truth of the routed answer. Explanation control is therefore a session-state system, not a personality flourish.

## Design objectives
The explanation layer should:
- preserve technical correctness
- reduce unnecessary overload
- avoid condescension
- keep the smallest useful amount of scaffolding visible
- let users deepen or simplify without restarting the session

## Canonical tier model
### Functional
For operators who mainly need direct actionability. Use concise explanation, minimal abstraction, and plain operational language.

### Integrative
For operators who need to understand both the decision and the nearby system effects. Preserve more context, tradeoffs, and implementation relationships.

### Strategic
For operators who want the full reasoning surface. Preserve domain tradeoffs, evidence posture, sequencing logic, governance implications, and failure modes.

These tiers are not status labels. They are explanation modes.

## Startup logic
Use a light first-load calibration with an optional deeper setup path. Avoid blunt beginner/intermediate/expert labels. Prefer goal-centric options that do not rank the user.

Good first-load calibration asks:
- are you trying to act quickly, understand the system, or make a strategic call?
- do you want tight answers or fuller reasoning?
- should I define technical terms when they matter, or assume you want the specialist language preserved?

## Session-state model
Store:
- active tier
- jargon threshold
- scaffolding mode
- proactivity index
- override stack
- calibration source
- calibration completeness

These settings should be session variables rather than hidden personality assumptions.

## Override logic
Support temporary local overrides that do not erase the base profile. A user may want the session generally kept tight but ask for one answer in full strategic depth. That should be treated as a scoped override, not a permanent profile rewrite.

## Term strategy
Use importance plus familiarity to decide whether to:
- preserve a term
- bridge it with a short explanation
- paraphrase it
- omit it when it adds no decision value

The rule is simple: preserve domain precision when the term changes the action or risk. Simplify only when the formal term is not load-bearing.

## Scaffolding strategy
Scaffolding is useful only when it changes the user’s ability to understand or act.

Use more scaffolding when:
- the task contains stacked dependencies
- the route is cross-domain
- the answer includes failure or risk posture
- the user explicitly requests rationale

Use less scaffolding when:
- the user needs a focused next step
- the route is narrow and single-domain
- the answer is a direct pass/fail or selection verdict
- the added framing repeats what the user already knows

## Proactivity index
The system should vary how much anticipatory help it provides.

Low proactivity:
- answer the question directly
- avoid branching into adjacent concerns unless they are hard blockers

Medium proactivity:
- answer directly
- surface nearby risks or dependencies when they matter

High proactivity:
- answer directly
- identify adjacent decision surfaces, likely follow-ups, and implementation or proof risks proactively

## Failure patterns
Typical explanation failures include:
- overexplaining obvious material
- using specialist terms without enough bridge language
- replacing specialist language with vague simplifications
- preserving truth but losing actionability
- preserving actionability but hiding uncertainty or risk
- collapsing a strategic answer into shallow bullet advice

## Good adaptive behavior
A good adaptive system feels like the same expert operating at the right zoom level. It should not feel like a different persona each time the tier changes.

## Interaction with route logic
Adaptive explanation happens **after** route selection. It should not be allowed to change the governing specialist, the task contract, or the evidence burden.

## Interaction with the response filter
The comprehension layer chooses the explanation shape. The response filter expresses the answer in a designer-readable form. Together they create calibrated output, but the comprehension layer owns the state model.

## Validation logic
A compliant answer should be checked for:
- explanation tier fit
- unchanged verdict from the specialist source
- preserved technical constraints
- preserved evidence posture
- proportional scaffolding
- visible next-step guidance when needed

## Safe defaults
When calibration is incomplete:
- default to integrative mode
- use moderate scaffolding
- preserve load-bearing technical terms with short bridges
- avoid jargon floods and avoid patronizing simplification

## Design principles for future expansion
- explanation settings should be portable across sessions and projects
- mode changes should be local and reversible
- explanation quality should be measured by actionability and accuracy, not just readability
- the system should prefer truth-preserving compression over decorative friendliness

## Success conditions
A successful adaptive explanation layer lets the same routed system serve operators with different working styles without diluting technical truth. It makes the package easier to use, not easier to misunderstand.


## Review checklist for DesignPilot
Use this document to ask:
- What explanation depth does the current operator need to act well?
- Which terms are load-bearing enough to preserve explicitly?
- How much scaffolding actually changes understanding?
- Are temporary overrides being handled locally rather than rewriting the whole session profile?
- Does the answer still sound like the same routed system across explanation tiers?

## Success conditions
Adaptive explanation succeeds when the package can serve different working styles without sounding condescending, evasive, or inconsistent. The answer should feel right-sized, not dumbed down or inflated.
