---
summary_version: 2.0.0
source_reference:
  - src/knowledge-base/source-docs/UI System Expert Research.md
  - src/knowledge-base/source-docs/Design Strategy and Communication Research.md
  - src/knowledge-base/source-docs/Comprehensive UI_UX Project Roadmap.md
last_updated: 2026-04-13
synchronized: true
domain: ui-system
---

# UI System Summary

## Navigation pattern selection

| Pattern | Item threshold | Viewport use | User context |
|---|---|---|---|
| Top navigation | ≤5 items | ~6.5% | General consumer, simple tasks |
| Left sidebar | 6–15 items | ~20% | Power users, complex task switching |
| Bottom tab bar | 3–5 items | Static (mobile) | High-frequency mobile actions |
| Navigation drawer | >15 items | Dynamic | Deep hierarchies, mobile utilities |

Default rule: top nav for ≤5 items; left sidebar for 6–15; drawer for >15.
Failure condition: >5 items in top nav collapses to hamburger, breaking discoverability.
Flat nav failure threshold: >30 items creates conceptual overlap and choice fatigue.

## Information architecture rules

- Breadth vs. depth: flat IA wins for discoverability; deep IA wins when relationships between content are complex
- Flat hierarchy limit: >30 items at one level triggers cognitive overload
- Deep hierarchy limit: >3 clicks to primary content is an IA failure signal
- IA failure signals in analytics: low traffic to important pages, high exit rates from navigation, frequent use of search as a fallback
- Chunking rule: group related items using proximity; max 7 items per group before sub-grouping is required

## Action hierarchy

| Level | Emphasis | Context | Limit |
|---|---|---|---|
| Primary | High (filled) | Move forward, submit, finish | 1 per region |
| Secondary | Medium (outline/gray) | Supporting, inline actions | Multiple allowed |
| Tertiary | Low (ghost/text) | Cancel, skip, dismiss | Multiple allowed |
| Destructive | Critical (red) | Permanent data loss | 1 per context |

CTA placement rules:
- Page-level: far right
- Multi-step flows: bottom right (reinforces forward direction)
- Form submission: bottom left (Western reading finish)
- Destructive: two-stage - secondary button triggers, primary button inside confirmation

Failure condition: >1 primary CTA per region creates decision fatigue and splits the critical path.

## Screen state system

Required states for every task-bearing screen: empty, loading, partial load, error, success, blocked, confirmation required.

- Empty state: must explain what is missing and provide one clear action
- Loading state: required when latency exceeds 1 second; skeleton preferred over spinner for content-heavy views
- Error state: must identify what failed, why, and what the user can do next
- Blocked state: must explain the blocker and who can resolve it
- Confirmation state: required for irreversible destructive actions only

Failure condition: missing empty or error states that leave users with no recovery path.

## Density thresholds

- Mobile: density-independent pixels (dp); touch targets ≥48×48dp
- List views: adequate whitespace to separate rows; max ~50 rows before pagination or filtering is required
- Detail views: max 2 columns on narrow viewports; progressive disclosure for secondary content
- Dense data tables: require filters, sorting, and column management before maximum density is reached
- Above-the-fold rule: critical action or status must be visible without scroll on target viewport

## Failure pattern catalogue

- **Polished components over broken flows**: solving visual detail before the primary task path is working
- **Missing screen states**: shipping without empty, error, or loading states
- **Primary CTA overload**: multiple filled buttons competing for the same region
- **Navigation abandonment triggers**: no wayfinding, no landmarks, no breadcrumb for depth >2
- **Premature component work**: designing component variants before the IA and task hierarchy are settled
- **Action placement drift**: CTA positions inconsistent across the same flow
- **Hidden destructive actions**: delete or reset placed without warning or confirmation
