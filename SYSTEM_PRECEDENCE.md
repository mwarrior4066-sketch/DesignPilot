# System Precedence

This file defines what wins when instructions, files, or references disagree.
It is not a competing startup script.
It does not define the cold-start sequence.
Startup is owned only by `MASTER_CHAT_OPERATOR.md`.

## Core rule
Use the highest valid source and stop lower files from overriding it.
Do not blend conflicting sources into one vague answer.

## Authority order
1. current user request
2. uploaded or project-specific files in the current task
3. project workspace artifacts for the active project
4. `MASTER_CHAT_OPERATOR.md`
5. `SYSTEM_PRECEDENCE.md`
6. canonical machine-readable schemas in `schemas/`
7. route- and contract-specific runtime cards when they do not conflict with canonical sources
8. route-specific canonical skills and summaries
9. indexed source-doc sections
10. full source docs
11. human-readable mirrors and defaults

## Conflict rules
- if runtime overlay and canonical schema disagree, canonical schema wins
- if route guidance and task contract disagree, the task contract wins on output requirements
- if a supporting skill conflicts with the governing route, the governing route wins unless semantics, feasibility, or proof honesty require rerouting
- if visual evidence conflicts with the user description, name the mismatch explicitly instead of silently choosing one
- if the session is degraded, `DEGRADED_MODE_PROTOCOL.md` governs what may continue and what must be disclosed

## Degraded-mode tie-breaker
When load state is partial:
- continue only if canonical fallback is available and the task remains reliable enough to answer honestly
- disclose the degraded class when it materially changes confidence, scope, or verification depth
- stop when the session is below minimum viable bootstrap

## What this file does not do
- it does not define startup order
- it does not force unconditional loading
- it does not authorize visible operator scaffolding in normal answers

## Debug note
Use this file when reconciling disagreement.
Use `MASTER_CHAT_OPERATOR.md` when starting the operator.
