# API Reliability and Security Prompt Pack v1

## Research goal
Strengthen the API reliability and security route with deeper evidence on structured failures, idempotency, async jobs, quotas, resilience, and telemetry.

## What is already known
- RFC 9457, BOLA/BFLA, Idempotency-Key, 202 Accepted, circuit breakers, and trace propagation are already in scope
- the route now exists and has example coverage

## What is missing
- more production-adjacent operational thresholds and postmortem-style examples
- more implementation receipts for expensive AI or document-generation workloads

## Prompt 1
Research the strongest production guidance for implementing RFC 9457 Problem Details, including extension fields, support IDs, and client recovery behavior.

## Prompt 2
Collect implementation-oriented guidance for idempotency-key storage, fingerprinting, TTL, and in-flight collision handling across distributed APIs.

## Prompt 3
Find evidence-backed patterns for 202 Accepted job lifecycles, status resources, webhook completion, and long-running export workflows.

## Prompt 4
Compile production guidance for circuit breakers, load shedding, graceful degradation, quota design, and trace propagation in expensive AI or API workflows.
