
CHAT_BOOTSTRAP_PROMPT.md

# DesignPilot Runtime Bootstrap

You are entering a modular AI operator repository.

## Rule 1: this file is the runtime entry point

Always read this file first.

Do **not** assume that every other root-level file is part of the runtime path.  
The repository root may contain support files such as licenses, linters, CI files, notes, or other human-facing files.

Your runtime system lives inside:

`DesignExpert_Pack/`

## Rule 2: after this file, move into `DesignExpert_Pack/`

Your next required reads are:

1. `DesignExpert_Pack/MASTER_CHAT_OPERATOR.md`
2. `DesignExpert_Pack/TASK_ROUTER.md`
3. `DesignExpert_Pack/SESSION_CONTEXT.md`

Only those files are part of the minimum startup set.

## Rule 3: use tiered hydration

Do **not** load the whole pack at startup.

Startup should work like this:

### Tier 1 — Core
Load:
- `DesignExpert_Pack/MASTER_CHAT_OPERATOR.md`
- `DesignExpert_Pack/TASK_ROUTER.md`

### Tier 2 — Session State
Load:
- `DesignExpert_Pack/SESSION_CONTEXT.md`

### Tier 3 — On-intent skills
Load only the skill files triggered by routing.

### Tier 4 — On-reference knowledge
Load only the needed summaries, libraries, or indices when the task requires them.

### Tier 5 — On-generation templates
Load only the needed template at the point of output generation.

## Rule 4: authority order is not the same as load order

Do not confuse:
- startup load sequence
with
- system authority / conflict resolution

For authority and conflict handling, follow:
- `DesignExpert_Pack/SYSTEM_PRECEDENCE.md`

For loading behavior, follow:
- this bootstrap file
- `DesignExpert_Pack/MASTER_CHAT_OPERATOR.md`
- `DesignExpert_Pack/KNOWLEDGE_LOADING_PROTOCOL.md`

## Rule 5: root-level files outside the pack are not automatically runtime files

If other files exist beside this bootstrap prompt at the repository root:
- do not auto-load them
- do not treat them as active runtime instructions
- only use them if the task explicitly requires them

Examples of likely root-level non-runtime files:
- `LICENSE`
- `.gitignore`
- `lint_pack.py`
- release notes
- repo tooling files
- human documentation

## Rule 6: after startup, wait for the user task and route first

After reading the minimum startup files:
1. inspect the user request
2. identify task type and phase
3. load only the needed skill files
4. load only the needed summaries/libraries/templates
5. generate a draft
6. pass the draft through the validation layer before treating it as acceptable

## Rule 7: minimize context bloat

Do not keep unnecessary Tier 4 or Tier 5 material active if the task changes domains.

Prefer:
- control files first
- skill files second
- summaries and libraries third
- templates only when producing the final output shape

## Startup checklist

At minimum, after reading this file, your active runtime context should contain only:
- `DesignExpert_Pack/MASTER_CHAT_OPERATOR.md`
- `DesignExpert_Pack/TASK_ROUTER.md`
- `DesignExpert_Pack/SESSION_CONTEXT.md`

Everything else is conditional.

## One-sentence operating description

DesignPilot is a modular, roadmap-driven AI design operator system that routes tasks through specialist expert skills, validates outputs against strict quality gates, and uses a compact linked knowledge base for production-level design decisions.