# Degraded Mode Protocol

This protocol defines what happens when the pack cannot fully hydrate.
The goal is safe continuation when possible and explicit stop conditions when not.

## Degradation classes

### 1. Missing boot layer
Condition:
- one or both runtime boot helpers are missing
- canonical startup authority still exists

Behavior:
- continue from `MASTER_CHAT_OPERATOR.md`
- skip runtime boot aides
- disclose only if the missing boot layer changes token efficiency or debugging trace, not core answer quality

Allowed claims:
- normal routed answer with canonical fallback

Blocked claims:
- do not imply the runtime overlay was fully active

### 2. Missing runtime card with canonical fallback available
Condition:
- requested route or contract runtime card is missing
- canonical schema and canonical skill/summary sources exist

Behavior:
- continue using canonical schema and canonical files
- disclose when the missing runtime card changes speed, trace granularity, or confidence in thin defaults

Allowed claims:
- full capability may continue if canonical sources are intact

Blocked claims:
- do not say the runtime overlay fully covered the task

### 3. Missing session state
Condition:
- `SESSION_CONTEXT.md` is absent or unusable
- `SESSION_CONTEXT_DEFAULTS.md` is available

Behavior:
- continue with defaults
- assume no special explanation preference, no active project pin, and no elevated debug visibility
- disclose when user-specific calibration clearly matters

Allowed claims:
- normal task execution with default calibration

Blocked claims:
- do not imply preserved session-specific preferences that were not actually loaded

### 4. Below-minimum viable load
Condition:
- canonical startup authority is missing, or
- routing and contract authority cannot be recovered, or
- required canonical sources are too incomplete for honest execution

Behavior:
- stop and request reload or the missing files
- do not silently guess through the failure

Allowed claims:
- only describe what is missing and what cannot be done safely

Blocked claims:
- no routed answer
- no proof or release claims

## User-facing disclosure language
Use concise language.
Examples:
- "I can continue, but I’m running from canonical files because the runtime card is missing."
- "Session defaults are active, so I’m not assuming prior explanation preferences."
- "I can’t route this safely because the minimum startup files are missing."
