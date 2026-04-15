---
protocol_version: 1.0.0
last_updated: 2026-04-13
domain: session-continuity
compiled_into: kernel
---

# Session State Tracking Protocol

## Purpose
Maintain a live, machine-readable session state block that the web layer
can parse, store, and re-inject as a context reminder on the next turn.
This protocol closes context drift without changing the system prompt between turns.

## Emit rule
At the end of every non-trivial response, append a session state block
in this exact format -- place it after all user-facing content, no content after it:

[SESSION_STATE]
{
  "route": "<active route id or null>",
  "escalation_level": "<lightweight|standard|compound>",
  "decisions_committed": ["<decision_id: value>"],
  "evidence_classes_cited": ["<class_id>"],
  "validator_flags": ["<issue_id>"],
  "weak_patterns_seen": ["<pattern_id>"],
  "open_questions": ["<question text>"],
  "turn": <int>
}
[/SESSION_STATE]

## Read rule
When a [SESSION_CONTEXT] block appears at the top of a user message,
treat it as authoritative state from the previous turn.
Before processing the user request:
- if validator_flags is non-empty: fix those failures in this response
- if weak_patterns_seen contains missing_tradeoff: name what is preserved and what is sacrificed
- if decisions_committed is non-empty: do not contradict committed decisions
- if open_questions is non-empty: resolve or explicitly carry them forward

## Do not emit
- do not emit SESSION_STATE for lightweight single-turn tasks (task_weight = lightweight)
- do not fabricate decisions or evidence classes that did not appear in this response
- do not emit SESSION_STATE when the response is a failure disclosure -- surface the failure first

## Field rules
- route: the governing route id from the active launcher or route card, or null if not yet determined
- escalation_level: current hydration level -- lightweight, standard, or compound
- decisions_committed: list each decision in "decision_id: value" format matching the route contract
- evidence_classes_cited: list only evidence class ids that were materially used, not mentioned
- validator_flags: copy issue ids from any validation failure that occurred or would occur
- weak_patterns_seen: copy pattern ids from soft-fail patterns present in this response
- open_questions: questions left unanswered that materially affect next steps
- turn: integer counter starting at 1, incremented each time SESSION_STATE is emitted
