---
protocol_version: 1.0.0
last_updated: 2026-04-13
domain: session-continuity
compiled_into: kernel
---

# Context Reminder Protocol

## Purpose
Define how the web integration layer reconstructs a [SESSION_CONTEXT] block
from stored session state and prepends it to each user message.
This documents the expected integration contract for any web layer consuming DesignPilot.

## Injection format
Prepend this block to the user message -- not to the system prompt:

[SESSION_CONTEXT]
Route: <route> (<escalation_level>)
Turn: <turn>
Decisions committed: <decisions_committed joined by ", " or "none">
Evidence cited: <evidence_classes_cited joined by ", " or "none">
Issues to fix: <validator_flags joined by ", " or "none">
Watch patterns: <weak_patterns_seen joined by ", " or "none">
Open questions: <open_questions joined by ", " or "none">
[/SESSION_CONTEXT]

## Reminder amplification rules
Apply these additions when state signals specific drift:

If validator_flags contains missing_tradeoff:
  Append: "REQUIRED THIS TURN: name what is preserved and what is sacrificed."

If validator_flags contains missing_required_decision:
  Append: "REQUIRED THIS TURN: the following decisions must be resolved: <list>"

If validator_flags contains missing_evidence_class:
  Append: "REQUIRED THIS TURN: include at least one measurable threshold,
  standard reference, or comparison artifact."

If validator_flags contains hollow_compliance:
  Append: "REQUIRED THIS TURN: recommendations must map back to named findings -- not generic advice."

If weak_patterns_seen contains prompt_restatement:
  Append: "REMINDER: restate the problem briefly, then move immediately to diagnosis."

If evidence_classes_cited is empty and turn > 1:
  Append: "REMINDER: no evidence classes have been cited in this session yet."

## Re-anchor trigger
If the same validator_flag appears in two consecutive turns, inject the
relevant rule section from the active launcher directly -- not just a reminder.
This is a re-anchor, not a nudge. The launcher section text takes precedence
over the reminder wording above.

## Compression trigger
If turn > 4, compress earlier conversation history to a synthetic summary turn
before injecting the context block.
Preserve: route, decisions committed, constraints named, evidence cited, unresolved issues.
Discard: prose, examples, formatting detail, repeated instructions.

## Do not inject
- do not inject a [SESSION_CONTEXT] block on turn 1 -- no prior state exists
- do not inject if session state is missing or unparseable --
  fall back to SESSION_CONTEXT_DEFAULTS.md behavior
- do not expose SESSION_STATE blocks to the user -- strip them from responses
  before display
