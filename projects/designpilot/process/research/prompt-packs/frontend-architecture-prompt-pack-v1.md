# Front-End Architecture Prompt Pack v1

## Research goal
Strengthen the front-end architecture route with deeper evidence on rendering strategy, boundary placement, state ownership, and mutation recovery.

## What is already known
- server/client boundaries, hydration cost, and Actions patterns are already loaded into the pack
- the route now exists and has example coverage

## What is missing
- more production-adjacent examples of when PPR, CSR islands, and rollback-safe mutations outperform simpler patterns
- additional evidence on hot-path profiling and hydration budgets

## Prompt 1
Collect production-oriented decision rules for choosing static rendering, dynamic rendering, PPR, streaming, and CSR islands in data-heavy enterprise dashboards.

## Prompt 2
Research the strongest implementation patterns for replacing boolean-explosion UI state with explicit finite-state or status-union models in React applications.

## Prompt 3
Find evidence-backed guidance on how to place Server Components, Client Components, and Server Actions so the UI stays resilient under permission-heavy interactions.

## Prompt 4
Compile production examples of rollback-safe optimistic updates, degraded mutation states, and instrumentation patterns for front-end architecture reviews.
