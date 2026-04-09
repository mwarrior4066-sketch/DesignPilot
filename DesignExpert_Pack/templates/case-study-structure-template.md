# Case Study Structure Template

## Writing Mode
- Case study / audit / rebuild / expand / UX copy / documentation:
- Audience:

## Hero / Title
- Project name:
- One-line summary:
- Outcome headline:

## Overview
- Product / company:
- Role:
- Team:
- Duration:
- Tools / methods:
- Core challenge:

## Problem
- What was wrong or missing:
- Why it mattered:
- Constraints:

## Discovery / Research
- Methods used:
- What each method showed:
- How findings changed decisions:

## Process
- Key problem → decision pairs:
- Tradeoffs:
- What was rejected and why:

## Solution
- What changed:
- Why this version won:

## Outcome
- Metrics / validation:
- Qualitative outcomes if metrics are unavailable:
- Before / after framing:
- Evidence strength:

## Learnings / Next Steps
- What you would improve next:
- What remains uncertain:

## Example output
### Writing Mode
- Case study / audit / rebuild / expand / UX copy / documentation: case study
- Audience: hiring managers, senior designers, and product collaborators

### Hero / Title
- Project name: Compliance Exceptions Dashboard Redesign
- One-line summary: Reframed a noisy audit dashboard into a triage-first operational surface for compliance teams
- Outcome headline: Reduced exception-identification time and made ownership visible at first glance

### Overview
- Product / company: enterprise cloud governance platform
- Role: lead product designer
- Team: product manager, analytics lead, one front-end engineer
- Duration: 6 weeks
- Tools / methods: audit review, stakeholder interviews, dashboard inventory, low-fi wireframes, prototype testing
- Core challenge: the existing dashboard showed a lot of data but did not help teams act on it quickly

### Problem
- What was wrong or missing: urgent exception drivers were buried inside dense tables and inconsistent severity cues
- Why it mattered: compliance leads were spending too long locating root causes before review meetings and PDF reporting
- Constraints: existing data model, existing token system, no major backend rewrite in phase one

### Discovery / Research
- Methods used: stakeholder interviews, dashboard audit, analytics review, prototype walk-throughs
- What each method showed: interviews exposed trust issues around stale data, the audit showed visual flatness, analytics showed drill-down underuse, testing showed users wanted ownership cues first
- How findings changed decisions: the redesign shifted from “more charts” to a triage-first hierarchy with ownership and severity visible immediately

### Process
- Key problem → decision pairs: flat KPI band -> risk-tiered summary row; overloaded table -> grouped drill-down logic; unclear severity -> explicit semantic color and label system
- Tradeoffs: retained some existing data structures to avoid backend delay, but simplified the front-end grouping aggressively
- What was rejected and why: a card-heavy visual redesign was rejected because it looked cleaner but weakened scan speed in dense review contexts

### Solution
- What changed: summary KPIs were reduced to four primary metrics, ownership and severity became top-level fields, chart choices were narrowed to trend and comparison views, and exports inherited the same hierarchy
- Why this version won: it made action paths visible quickly without pretending the dashboard was a lightweight executive surface

### Outcome
- Metrics / validation: first-pass identification of critical exception clusters improved in moderated testing; stakeholders reported clearer meeting prep and export handoff
- Qualitative outcomes if metrics are unavailable: reviewers described the dashboard as “finally readable” and “less like hunting through logs”
- Before / after framing: before = dense monitoring surface; after = triage-oriented operational dashboard
- Evidence strength: medium; tested with internal stakeholders and prototype sessions, but production analytics are still pending

### Learnings / Next Steps
- What you would improve next: unify export and in-app filters more tightly and test regional ownership views at scale
- What remains uncertain: how much drill-down depth users will tolerate before wanting a separate analysis surface
