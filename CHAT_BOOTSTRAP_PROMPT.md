# Design Expert Pack Bootstrap

This file is the only root-level runtime entry point.

## Startup Order

1. Read `DesignExpert_Pack/MASTER_CHAT_OPERATOR.md`
2. Read `DesignExpert_Pack/TASK_ROUTER.md`
3. Read `DesignExpert_Pack/SESSION_CONTEXT.md`
4. Wait for user input
5. Use `DesignExpert_Pack/TASK_ROUTER.md` to identify intent
6. Hydrate only the needed files from `DesignExpert_Pack/skills/`, `DesignExpert_Pack/knowledge-base/summaries/`, `DesignExpert_Pack/libraries/`, and `DesignExpert_Pack/templates/`
7. Keep Tier 3–5 files minimal in active runtime context

## Runtime Constraints

- Do not load the full pack at startup
- Do not treat `DesignExpert_Pack/README.md` as runtime logic
- Do not load `DesignExpert_Pack/templates/` or `DesignExpert_Pack/skills/` unconditionally
- Use `DesignExpert_Pack/SYSTEM_PRECEDENCE.md` only when authority resolution is needed, not as part of cold-start loading

## Directory Rule

Everything except this bootstrap file lives inside `DesignExpert_Pack/`.
Run this prompt first, then enter `DesignExpert_Pack/` and follow the tiered hydration model.
