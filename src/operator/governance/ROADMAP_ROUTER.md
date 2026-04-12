# Roadmap Router

Use the roadmap before solving the task.
This file decides the project phase, the gate status, and whether an off-phase warning is needed.

## EPIS macro-cycle

### E — Exploration
Use when the task is about:
- problem definition
- market gap
- audience and psychographics
- behavioral logic
- ergonomic or cognitive constraints
- requirements and risk framing

### P — Preparation
Use when the task is about:
- information architecture
- writing logic
- brand direction
- grid, type, color, motion, accessibility, and token design
- system rules and style guides

### I — Implementation
Use when the task is about:
- front-end build decisions
- back-end-aware constraints
- component implementation
- design-to-code translation
- PDF production and remediation logic

### S — Sustainment
Use when the task is about:
- QA and audits
- validation
- reporting
- case-study framing
- post-launch iteration

## Detailed roadmap
1. problem and market gap
2. audience and psychographics
3. physical, cognitive, and ergonomic constraints
4. writing clarity and message logic
5. brand identity and logo system
6. interface logic, grid, type, and color system
7. accessibility, motion, feedback, and multisensory standards
8. token architecture and technical translation
9. implementation and deployment-aware planning
10. validation, reporting, and case-study framing

## Gate logic
Use these gate questions before letting work jump forward.

### Gate 1 — Problem validity
- is there a real problem, goal, or use case?
- is the target audience identifiable?
- is the task more than cosmetic drift?

### Gate 2 — Structural readiness
- is the information architecture clear enough?
- is the primary action clear?
- are the system constraints known enough to design responsibly?

### Gate 3 — System readiness
- are grid, type, color, motion, and accessibility directions defined enough?
- are the token and implementation boundaries clear enough?

### Gate 4 — Production readiness
- is the design implementable?
- are interaction states, contrast, and motion handled?
- for PDFs, are structure and extraction requirements clear?

### Gate 5 — Validation readiness
- is there enough evidence to audit, report, or package the work?

## Router behavior
Before answering, identify:
- current EPIS phase
- detailed roadmap step
- current gate
- whether the request is on-phase, off-phase-but-safe, or off-phase-and-risky

## Off-phase behavior
### Off-phase but safe
Solve the immediate task and note the upstream risk briefly.

### Off-phase and risky
Push back when the request would create a known failure state:
- high-fidelity UI before enough structure exists
- unreadable or inaccessible typography
- non-compliant contrast without fallback logic
- PDF edits that destroy reading order or extraction
- implementation detail before system logic exists

## Output rule
Always name:
- phase
- detailed step when useful
- the main upstream risk if one matters
