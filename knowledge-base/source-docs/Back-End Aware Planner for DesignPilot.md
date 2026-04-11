# Back-End Aware Planner for DesignPilot

## Research basis and design goals

A “Back-End Aware Planner” (BEAP) is best treated as a planning and feasibility control plane that sits between product/design intent and engineering execution: it translates UI or workflow requests into explicit requirements on identity, authorization, data models, APIs, storage, background processing, export pipelines, and reliability behaviors—then issues a feasibility decision with a defensible rationale. This positioning aligns with how architecture reviews are intended to function as a constructive discussion of architectural decisions rather than an audit, as framed by the Amazon Web Services[1] Well-Architected guidance. [2]

To make the planner “strict,” it should use normative requirement keywords (e.g., MUST/SHOULD/MAY) in the sense standardized for technical specifications. [3] This matters because BEAP outputs are effectively “design constraints” that downstream skills (front-end, dashboards, PDF/document, token/auth) must treat as contract, not suggestion.

The most directly relevant source base for this operator pack clusters into six practical pillars:

- API contracts and semantics: resource-oriented API design and canonical identifiers (e.g., Google[4] AIP guidance), explicit pagination and idempotency planning, and HTTP semantics/caching definitions. [5]
- Auth and access control planning: role-based and attribute-based access control definitions (National Institute of Standards and Technology[6]), plus “deny by default” and “least privilege” planning and enforcement guidance (OWASP[7]). [8]
- Security failure modes tied to API/design asks: object-level, property-level, and function-level authorization failures from OWASP’s API Security categories provide a ready-made threat-driven lens for detecting “simple UI, back-end heavy” requests. [9]
- Reliability engineering and degraded modes: graceful degradation, retry/backoff/jitter, circuit breakers, bulkheads, and queue-based load leveling are specifically useful as planning primitives BEAP can demand for exports, dashboards, and real-time features. [10]
- Document and file handling: file uploads as an attack surface (validation, scanning, safe storage), signed URL access patterns, and export safety issues like CSV injection. [11]
- Design-to-engineering handoff artifacts: Architecture Decision Records (ADRs) and lightweight architecture diagramming (C4) are well-suited to BEAP’s need to “freeze assumptions” and communicate backend implications to other skills. [12]
## Core operating model

A strict BEAP should behave less like a chatty advisor and more like a requirements compiler that produces a feasibility verdict plus a backend implication map and handoff payloads. To reliably do this across dashboards, workflows, document systems, and front-end requests, BEAP needs a consistent internal representation and decision procedure grounded in stable standards and best practices.

### Canonical output objects BEAP should always produce

BEAP outputs should be deterministic and comparable across requests so that teams can build muscle memory around “what gets blocked” and “why.” A practical minimum set:

- Feasibility Verdict: {feasible | feasible_with_constraints | not_feasible} with hard blockers explicitly enumerated. (Use MUST/SHOULD language per RFC normative keyword practice.) [13]
- Backend Implication Map (BIM): structured requirements across:
Identity & AuthN, Authorization & Policy, Data Model & SoT, API Surface, Sync/Realtime, Storage & Assets, Exports/Jobs, Observability, Reliability/Degradation, Compliance/Retention. This mirrors how access control decisions rely on subject/object/action context in ABAC framing and how authorization logic must be maintainable and validated per request. [14]
- Risk Scorecard: per-dimension risk (e.g., 0–5), with rationale anchored to known failure classes (e.g., BOLA/BOPLA/BFLA, unrestricted resource consumption, retry storms, cascading failures). [15]
- Assumptions & Unknowns Ledger: every assumption becomes either (a) a required clarification, (b) an enforced constraint, or (c) a fallback plan. This is essential because adding “missing primitives” late (pagination, long-running operations, access controls) frequently becomes backward-incompatible or architecturally expensive. [16]
- Skill Handoffs: explicit payloads for downstream skills (front-end/dashboard/PDF/token/document) containing required constraints and interface contracts (e.g., “this screen MUST show stale-data indicators because freshness is 15 minutes”). Dependency-driven SLO framing supports this style of interface contract. [17]
### The strict planning loop

BEAP can follow a fixed loop that mirrors established architecture/reliability patterns:

- Parse the ask into nouns/verbs/actors: turn the request into resources, operations, and relationships (resource-oriented thinking). [18]
- Infer access-control surfaces: any “dashboard,” “shared workspace,” “admin,” “export,” “approvals,” or “audit” language should automatically trigger a permissions model draft (deny by default; least privilege; validate on every request). [19]
- Derive the data model and source of truth: decide canonical identifiers and ownership of fields (server-modified defaults, normalization, and canonical names). [20]
- Derive the API contract: pagination at outset, idempotency/request IDs for mutations, explicit error model, caching semantics, and versioning plan. [21]
- Classify work as synchronous vs asynchronous: exports, heavy report generation, document processing, and bulk imports should be planned as long-running operations or asynchronous request-reply with status polling and queue buffering. [22]
- Plan failure behavior: timeouts, retries with jitter, circuit breakers, bulkheads, and graceful degradation rules (including a way to disable complex degradation mechanisms if they themselves become risky). [23]
- Score risk and gate: if critical unknowns remain, BEAP blocks or forces a constrained alternative. Security categories like BOLA/BOPLA/BFLA are particularly useful as “design ask → back-end implication” detectors. [9]
## Topic rulebooks

Each topic below is scoped to planning logic, feasibility detection, and correct handoff design—not production back-end coding.

Translating product and design requests into back-end requirements
1. Definition: A structured translation from UX/product asks into explicit requirements for resources, data ownership, access policies, API behaviors, storage/processing flows, and non-functional constraints; supported by resource-oriented API decomposition and architecture communication practices (C4/ADR). [24]
2. Why it matters for BEAP: Incomplete translations create “hidden architecture” where teams discover late that a visually small feature implies pagination, long-running operations, or strict access controls—changes that can be costly or backward-incompatible. [16]
3. Default rules:
- Every request MUST produce: (a) actors, (b) resources/nouns, (c) operations/verbs, (d) access policy sketch, (e) data lifecycle, (f) sync/async classification, (g) SLO/freshness expectations. [25]
- API resources SHOULD have canonical identifiers and predictable naming/hierarchy; aliases are allowed but responses should use canonical names. [26]
- Architecture decisions that materially affect dependencies, interfaces, or non-functional characteristics SHOULD be captured as ADR-like “decision + consequences.” [27]
4. Exception rules:
- If the request is a disposable prototype with no persistence, BEAP MAY allow relaxed modeling, but MUST label it “prototype-only” and prohibit assumptions like “we can add roles later.” (Access control and pagination are common “later becomes expensive” traps.) [28]
5. Fallback logic: If the ask is underspecified, BEAP falls back to the smallest contract that preserves safety: read-only views, single-tenant scope, or snapshot-based dashboards (explicitly stale) rather than implied real-time. [29]
6. Failure conditions: Block when any of these are missing: actor/tenant boundaries, ownership of data, required freshness, or an authorization story for non-public data. [30]
7. Measurable thresholds: Operator-pack defaults (tunable):
- Critical unknowns cap: ≥3 critical unknowns ⇒ “not_feasible” until clarified.
- Decision granularity: at least 1 canonical resource + 1 write path must be specified for any “editable” UI.
8. Implementation guidance for an AI operator pack:
- Implement a compulsory “Backend Requirements Card” output section per feature: {resources, operations, data-fields, authZ rules, API endpoints, async jobs, storage, observability, failure modes, acceptance thresholds}. This mirrors contract-first expectations (OpenAPI) and structured API guidance styles. [31]
9. Test cases:
- “Design a Kanban board with drag/drop and audit history” → BEAP must infer versioning, event/audit log, and permission checks.
- “Add infinite scroll to the activity feed” → BEAP must require pagination and stable ordering guarantees.

Auth, roles, permissions, and access-control planning
1. Definition: Planning authentication (who are you) and authorization (what can you do) via models like RBAC and ABAC, enforced through policy enforcement points and request-level validation. [32]
2. Why it matters for BEAP: Many “dashboard” or “workflow” asks implicitly require object-level authorization, property-level constraints, and function-level separation; these map directly to OWASP API authorization failure categories. [9]
3. Default rules:
- Authorization MUST be enforced server-side; deny by default; validate permissions on every request; enforce least privilege. [19]
- BEAP MUST explicitly model: tenant boundary, role/group hierarchy, object ownership, and whether field-level masking is required (to avoid property-level overexposure). [33]
- If IDs are user-supplied anywhere, BEAP MUST require object-level authorization checks to prevent BOLA-style attacks. [34]
4. Exception rules:
- Public, non-sensitive content MAY have “no auth required,” but BEAP must still define write/admin paths as authenticated and authorized. (Function-level separation is a recurring risk.) [35]
5. Fallback logic:
- If roles are unclear, BEAP falls back to: {owner, collaborator, viewer} with deny-by-default for any admin function, and requires a later ADR to expand the matrix. [36]
6. Failure conditions:
- “Share with anyone who has the link” without revocation/expiration semantics for documents or exports is a hard blocker unless scoped to time-limited signed URLs or equivalent. [37]
- “Admins can see everything” without audit/logging requirements is a blocker for enterprise contexts because authorization events and failures should be logged/monitored. [38]
7. Measurable thresholds: Operator-pack defaults (tunable):
- Any feature introducing cross-tenant access ⇒ risk +2 and requires explicit policy model.
- Any feature requiring field-level visibility rules ⇒ risk +2 and requires “property-level authorization” plan. [39]
8. Implementation guidance for an AI operator pack:
- Maintain a “Policy Table” object in outputs: subjects (users/service), objects, actions, conditions, effect (allow/deny), audit events. This aligns with ABAC’s subject/object/action/condition framing and PEP/PDP conceptual separation. [40]
9. Test cases:
- “Managers can export team performance PDFs, not individual contributors” → BEAP must infer role hierarchy and function-level authorization gates.
- “Users can update their profile but not their billing tier” → BEAP must infer property-level authorization.

Data models, relationships, and source-of-truth planning
1. Definition: Defining domain entities, identifiers, relationships, constraints, and ownership of fields (what system is authoritative), including handling server-modified defaults and normalization. [41]
2. Why it matters for BEAP: UI features often imply hidden invariants (“status transitions,” “audit history,” “approval chains”) which must exist in the data model; missing source-of-truth decisions create inconsistent dashboards/exports and correctness failures. [42]
3. Default rules:
- Each resource MUST have one canonical identifier (even if aliases exist); canonical identifiers MUST be returned consistently. [43]
- BEAP MUST declare “write authority” per field (user-set vs server-set/default/normalized). [44]
- If multiple teams/systems touch the same concept, BEAP SHOULD propose bounded contexts and explicit relationships/integration points. [45]
4. Exception rules:
- If the product requires immutable history (“audit,” “time travel,” “replay”), BEAP MAY recommend event-oriented storage approaches, but must flag operational complexity and the need for derived read models. [46]
5. Fallback logic:
- If “full fidelity model” is too heavy, fall back to a minimal operational model + append-only audit log capturing changes. (This preserves accountability while limiting schema complexity.) [47]
6. Failure conditions:
- “Real-time collaborative editing” without a conflict-resolution/versioning model is a blocker; BEAP must require explicit semantics for concurrent updates. (HTTP semantics define idempotency for methods but do not solve conflict resolution by themselves.) [48]
7. Measurable thresholds: Operator-pack defaults (tunable):
- Any editable entity SHOULD include {created_at, updated_at, created_by, updated_by, version/revision}.
- Any workflow entity SHOULD include {state, state_changed_at, state_changed_by, allowed_transitions}.
8. Implementation guidance for an AI operator pack:
- Output two structured artifacts:
- Entity Ledger: per entity: fields, types, invariants, indexes implied by queries/filters, and ownership.
- Source-of-Truth Map: for each field/domain: authoritative store, replication path, and “freshness contract” for consumers. The “server-modified defaults” guidance is a good anchor for explicitly documenting this. [49]
9. Test cases:
- “Add an approval workflow with ‘undo’ and audit log” → BEAP must infer state machine + immutable history requirements.
- “Merge two customer records and keep exports stable” → BEAP must infer identity resolution rules and canonical ID strategy.

API, sync, and real-time system implications
1. Definition: Planning API resources and behaviors (pagination, filtering, idempotency, error models, caching) and any sync/real-time mechanisms (polling, SSE, WebSockets). [50]
2. Why it matters for BEAP: “Visually simple” features (feeds, search filters, live updates) can impose strict backend requirements: stable ordering, pagination tokens, rate limiting, request deduplication, and delivery guarantees. [51]
3. Default rules:
- APIs returning collections MUST provide pagination from the outset because adding it later is backwards-incompatible. [52]
- Mutation requests SHOULD support idempotency via request IDs/keys to allow safe retries; HTTP defines idempotent methods but POST often needs explicit idempotency keys for fault tolerance. [53]
- If responses are cacheable or freshness-sensitive, BEAP MUST require explicit caching/freshness semantics (HTTP caching headers and revalidation strategies). [54]
- For long-running tasks, BEAP MUST require asynchronous patterns (LRO token/status or async request-reply with polling); do not hold synchronous requests open for minutes. [55]
- API contract documentation SHOULD be machine-readable (e.g., OpenAPI) for handoff and tooling. [56]
4. Exception rules:
- For internal-only tooling with bounded datasets, BEAP MAY allow simplified pagination or caching, but must still plan for growth if the UI pattern implies it (e.g., infinite scroll). [52]
5. Fallback logic:
- If real-time is requested without budgets/guarantees, fallback to polling with explicit refresh intervals and “last updated” UI, or SSE for one-way updates; WebSockets only if bidirectional real-time is justified. [57]
6. Failure conditions:
- “Live updates for everything” without rate limiting/resource consumption controls is a blocker because unrestricted consumption is a known API risk class. [58]
7. Measurable thresholds: Operator-pack defaults (tunable):
- Synchronous API budget: target <2s p95 for interactive calls; heavier operations must be async. (Treat as a planning heuristic; enforce via SLO definition.) [59]
- Realtime definition: require explicit update frequency, fanout size, ordering guarantees, and reconnect behavior before approving WebSockets/SSE. [60]
8. Implementation guidance for an AI operator pack:
- Emit an “API Surface Map” with: endpoints, auth scope, pagination/filtering rules, idempotency requirements, error model, caching rules, and whether the endpoint is synchronous vs async (plus status resource). AIP patterns for pagination, filtering, request IDs, and errors give a consistent checklist. [61]
9. Test cases:
- “A live incident dashboard that updates every second” → BEAP must demand explicit realtime architecture and resource consumption controls.
- “Bulk update 50k records from the UI” → BEAP must demand async job + idempotency + progress/status endpoint.

Uploads, storage, assets, and document handling
1. Definition: Planning ingestion, validation, storage, access control, lifecycle, and retrieval of user-supplied files (images, PDFs, attachments), including metadata and safe serving. [62]
2. Why it matters for BEAP: A single “Upload logo” UI implies file-type constraints, size limits, malware scanning, secure storage, and authorization to prevent unauthorized access or the storage system being abused. [63]
3. Default rules:
- Treat every upload as untrusted input; validate extension/type/size; avoid leaking internal paths; plan for scanning/sanitization where appropriate. [64]
- Use object storage access patterns that support time-limited access (signed URLs); BEAP must explicitly model who can generate them, how long they live, and what happens after expiry. [65]
- Persist file metadata separately from binary storage; attach authorization rules to both “file object” and “parent entity reference.” (This avoids orphaned, overexposed assets.) [66]
4. Exception rules:
- If attachments are purely optional, BEAP MAY propose “link-only attachments” (no upload pipeline) to avoid malware scanning/storage complexity, but must account for link rot and access control. [67]
5. Fallback logic:
- If scanning infrastructure is unavailable, fallback to restricting file types to low-risk formats (e.g., images only), strict size limits, and quarantined storage pending manual review—explicitly documented as constrained. [68]
6. Failure conditions:
- “Upload any file type” with public serving and no authentication/authorization story is a hard blocker given known unrestricted upload abuse cases. [69]
7. Measurable thresholds: Operator-pack defaults (tunable):
- Require explicit: allowed MIME types, max size, retention policy, virus scanning decision, access pattern (signed URL vs proxied), and audit logging for downloads of sensitive documents. [70]
8. Implementation guidance for an AI operator pack:
- Output an “Asset Handling Plan” containing: upload initiation (direct-to-storage vs via API), verification steps, metadata schema, access model, lifecycle/retention, and download/preview strategy. Signed URL semantics (anyone with URL can use while active) should be explicitly noted as a design constraint. [71]
9. Test cases:
- “Users can upload compliance evidence PDFs and only auditors can view them” → BEAP must infer sensitive storage + strict authZ + audit logs.
- “Drag-drop 500 photos into a project” → BEAP must infer bulk upload flow, quotas, and background processing for thumbnails.

Exports, reporting, and PDF/document pipeline planning
1. Definition: Planning generation and delivery of exports (CSV, XLSX, PDF, doc packets) including templating, background jobs, access control, persistence, and safe rendering. [72]
2. Why it matters for BEAP: Exports are often compute-heavy, may require long-running operations, and introduce new data leakage surfaces (CSV formula injection, overbroad export permissions, link-sharing semantics). [73]
3. Default rules:
- Any export that can exceed interactive latency MUST be asynchronous (LRO token/status or async request-reply); include a status endpoint and durable job record. [74]
- Use queue buffering (queue-based load leveling) to absorb spikes and decouple UI/API from export workers. [75]
- Generated files MUST be access-controlled like primary data; signed URL delivery MUST have explicit expiry and re-generation policy. [76]
- CSV exports MUST mitigate CSV injection when including untrusted text. [77]
- PDF layout requirements MUST be explicit (page size, headers/footers, pagination rules, fonts); CSS paged media specs illustrate the breadth of “print layout” features that quickly become non-trivial. [78]
4. Exception rules:
- For tiny exports (bounded, small row counts) BEAP MAY allow synchronous generation, but must set a strict size/time ceiling and still require authorization + audit. [79]
5. Fallback logic:
- If “pixel-perfect PDF” is too heavy, fallback to: (a) printable HTML, (b) CSV only, or (c) a “summary PDF” with limited layouts; document exactly what fidelity is supported. [80]
6. Failure conditions:
- “Instant PDF for any dataset size” without background processing is blocked because it contradicts async patterns for long-running work. [81]
7. Measurable thresholds: Operator-pack defaults (tunable):
- Export job SLA target: define completion percentiles and queue backlog limits; if undefined, BEAP forces “best-effort” labeling and user-visible progress states. [82]
8. Implementation guidance for an AI operator pack:
- Emit an “Export Pipeline Plan” with: job model, queue, worker scaling assumptions, template layer, asset dependencies (fonts/images), storage/persistence, download authorization, and cleanup/retention. Treat export requests as idempotent-triggered jobs when users can spam clicks. [83]
9. Test cases:
- “Export quarterly board report PDF with charts and footnotes” → BEAP must infer template layer + chart rendering + asset storage + async jobs.
- “Let users export contacts to CSV” → BEAP must infer CSV injection mitigation + privacy/permissions scope.

Dashboard and data dependency planning
1. Definition: Planning dashboards as data products: metric definitions, data sources, refresh schedules, caching/freshness, filtering semantics, and permission propagation to every widget. [84]
2. Why it matters for BEAP: Dashboards are rarely “just UI”—they encode aggregation logic, freshness requirements, and authorization rules; ignoring these yields inconsistent numbers, stale data surprises, and access leaks. [85]
3. Default rules:
- Each dashboard tile MUST declare: metric definition, grain (per day/user/etc.), source-of-truth, refresh cadence, and permission rules (tenant/object/field). [86]
- If dashboards rely on batch processing, BEAP MUST surface batch intervals and communicate “freshness” explicitly; batch processing is common in analytics workloads. [87]
- Filters SHOULD follow a consistent spec; if filtering is exposed, BEAP should require a single filter expression field and define supported operators. [88]
4. Exception rules:
- For static, curated dashboards (no interactive filters), BEAP MAY accept a simple snapshot pipeline, but must still define refresh cadence and authorization boundaries. [86]
5. Fallback logic:
- If real-time freshness is too costly, fallback to “near-real-time” with explicit lag and a user-visible timestamp; if dependency outages occur, degrade to cached/snapshot data with banners. [89]
6. Failure conditions:
- “Show revenue in real time” without defining revenue recognition logic, data source, and update frequency is blocked as underspecified. (Metric definitions are part of the data product contract.) [90]
7. Measurable thresholds: Operator-pack defaults (tunable):
- Any dashboard advertised as “real time” must specify maximum staleness and dependency SLO alignment. [17]
8. Implementation guidance for an AI operator pack:
- Output a “Dashboard Dependency Ledger” with: {tile_id, metric, query shape, data sources, joins, freshness SLA, cache policy, permissions, failure fallback}. Use HTTP caching semantics language where appropriate for cached APIs. [91]
9. Test cases:
- “Sales dashboard with drill-down by region and role-based visibility” → BEAP must infer RBAC/ABAC + filter/index needs + freshness contract.
- “Executive dashboard emailed daily as PDF” → BEAP must infer batch pipeline + export job + access rules.

Error states, degraded modes, and failover behavior
1. Definition: Planning system behavior under faults: timeouts, retries, backoff/jitter, circuit breaking, bulkheads, load shedding, and graceful degradation paths that keep critical functions available. [92]
2. Why it matters for BEAP: UI/feature specs frequently omit failure behavior, yet reliability guidance emphasizes that unmanaged retries and dependency failures can cascade and amplify outages. [93]
3. Default rules:
- Every external/dependency call MUST have timeouts; retries MUST use exponential backoff with jitter; retries per request must be limited. [94]
- Use circuit breakers to prevent repeated calls to failing dependencies; combine with retries thoughtfully to avoid retry storms. [95]
- Plan graceful degradation and keep it simple; complex degradation itself can cause undesired feedback loops, so provide a way to disable/tune degradation mechanisms rapidly. [96]
- Use bulkheads to isolate failure domains (so one failing component doesn’t take down others). [97]
4. Exception rules:
- For early prototypes, BEAP MAY reduce reliability requirements, but must never waive basic timeouts and must label degraded behavior as undefined (not acceptable for production). [98]
5. Fallback logic:
- If a dependency fails: degrade to cached responses, partial responses, or read-only modes; surface clear UI error states (“data may be stale”) tied to dependency SLOs. [99]
6. Failure conditions:
- Any spec that implicitly assumes “no failures” (e.g., “export always completes instantly,” “real-time always connected”) without degraded-mode behavior is blocked. [100]
7. Measurable thresholds: Operator-pack defaults (tunable):
- Require explicit: timeout budgets, retry limits, circuit breaker trip conditions, and a degraded-mode UX rule per critical dependency. [101]
8. Implementation guidance for an AI operator pack:
- Emit a “Degraded Mode Matrix” mapping {dependency failure → user-visible state → backend behavior} and include observability hooks; context propagation helps correlate failures across services. [102]
9. Test cases:
- “Dashboard must work during partial outage of analytics DB” → BEAP must require cached/snapshot fallback and explicit stale labeling.
- “Webhook ingestion must never drop events” → BEAP must require retries/idempotency and durable queue/storage.

Implementation feasibility gates and risk scoring
1. Definition: A repeatable gating process that blocks or constrains features until required backend primitives and constraints are specified, paired with a risk scoring rubric across architecture dimensions. [103]
2. Why it matters for BEAP: Without explicit gates, teams tend to accept underspecified work; later discovery that pagination, authorization, or async processing is required causes schedule slips and breaking changes. [104]
3. Default rules:
- BEAP MUST gate on: identity/tenant model, authorization model, canonical entities, write paths, async needs, error/degraded behavior, and export/storage implications. [105]
- Risk scoring SHOULD reflect known high-impact categories: authorization failures (object/property/function), unrestricted resource consumption, and dependency failure amplification. [106]
4. Exception rules:
- If explicitly labeled as “research spike,” BEAP MAY allow unresolved items, but must list them as blockers for any production commitment. [107]
5. Fallback logic:
- If risk is high, BEAP proposes narrower alternatives (e.g., remove real-time, reduce role complexity, use batch exports). Dependable degradation and async patterns are standard fallback pathways. [108]
6. Failure conditions:
- Any request with unclear data ownership + unclear permissions + implied high scale is blocked (risk compounding across axes). [109]
7. Measurable thresholds: Operator-pack defaults (tunable):
- Hard-block threshold: total risk ≥18 (out of 25 across 5 dimensions) ⇒ “not_feasible.”
- Soft-block threshold: any single dimension = 5 ⇒ “feasible_with_constraints” only if a fallback is accepted.
8. Implementation guidance for an AI operator pack:
- Encode the gates as a deterministic checklist + scoring function; produce the same field order every time so downstream skills can parse it reliably. Use ADR-style “decision + consequences” for any approved exception. [27]
9. Test cases:
- “Add SSO + per-department isolation + audit exports in 2 days” → BEAP should block as infeasible without existing IAM/roles, export jobs, and audit logging.
- “Add a read-only public status page” → BEAP should pass with constrained scope and clear caching rules.

Failure taxonomy for impossible or underspecified requests
1. Definition: A classification system of request failures that BEAP can detect and respond to consistently: missing identity model, missing authorization, undefined metrics, undefined freshness, impossible performance constraints, unsafe export/storage, and undefined degraded behavior. These categories are motivated by recurring security and reliability failure classes. [110]
2. Why it matters for BEAP: A taxonomy prevents “feature brainstorming” from becoming accidental commitments; it helps BEAP produce repeatable block messages like “visually simple but back-end heavy” with specific missing primitives. [111]
3. Default rules:
- Classify each blocker as: Undefined Policy, Undefined SoT, Undefined Freshness, Async Required, Unsafe Export, Unbounded Consumption, Undefined Failure UX, Inventory/Versioning Risk. [112]
- For every failure class, BEAP MUST offer either: a clarification question or a safe constrained alternative. (Strictness means the system does not “guess” silently.) [113]
4. Exception rules:
- If an operator explicitly approves a constraint (e.g., “no sharing; single tenant only”), BEAP can downgrade some failures from “block” to “constrained feasible,” recorded as a decision. [114]
5. Fallback logic:
- Prefer fallbacks that reduce attack surface and operational complexity: snapshots over live, polling over WebSockets, narrow exports over full dumps, minimal roles over complex hierarchies. [115]
6. Failure conditions:
- If the request implies BOLA/BOPLA/BFLA risk and refuses to define roles/policies, BEAP must block. [116]
7. Measurable thresholds: Operator-pack defaults (tunable):
- “Impossible” if any of these are demanded simultaneously without preexisting infrastructure: (a) global real-time, (b) unlimited exports, (c) complex multi-role sharing, (d) zero downtime, (e) no background processing. [117]
8. Implementation guidance for an AI operator pack:
- Maintain a library of standardized refusal templates keyed by failure class, each containing: (a) what’s missing, (b) why it’s required, (c) the minimal viable alternative, (d) the handoff skill that can proceed once constraints are accepted. [118]
9. Test cases:
- “Anyone can edit any record if they have the link; no logins” → BEAP blocks due to undefined auth and unsafe sharing.
- “Export everything instantly; no queues; must be perfect PDF” → BEAP blocks and offers async export + constrained templates.

## Operator pack file deliverables

Below are the requested deliverable files as operator-pack artifacts. Each file definition includes: purpose; what it contains; what it must not contain; dependencies; and skill handoffs. These files are intended to work together as a strict planning system (rules + scoring + test harness) rather than a set of generic essays.

back-end-aware-planner.md
Purpose: the top-level operating spec for BEAP (inputs, outputs, loop, gates, and refusal language).
Contains: the BEAP contract; BIM schema; gating checklist; structured output format; mandatory fields; refusal taxonomy; example outputs. (Use normative keywords per RFC 2119 style.) [13]
Must not contain: production code, framework-specific back-end tutorials, or “feature brainstorming” not tied to feasibility logic.
Depends on: feasibility-risk-matrix.md, auth-and-permissions-planning-rules.md, data-model-and-source-of-truth-rules.md, exports-and-document-pipeline-rules.md, degraded-mode-and-failover-rules.md.
Hands off to: front-end skill (UI states, loading/error), dashboard skill (metrics + freshness rendering), token/auth skill (session/token flows), document/PDF skill (templates/layout constraints), infra/reliability skill (timeouts, retries, circuit breakers, queues). [119]

feasibility-risk-matrix.md
Purpose: a scoring system that converts backend implications into a repeatable feasibility decision.
Contains: risk dimensions; scoring rubric; hard-block thresholds; examples; mapping from OWASP API risk classes and reliability failure amplification patterns to planner risk points. [120]
Must not contain: vague “scale it later” advice; instead it must name concrete missing primitives (pagination, idempotency, async exports, deny-by-default authorization). [121]
Depends on: back-end-aware-planner.md for output schema and decision gates.
Hands off to: product/design review skill (scope cuts), infra/reliability skill (mitigation patterns), security review skill (authorization categories). [122]

auth-and-permissions-planning-rules.md
Purpose: the authorization planning rulebook BEAP uses to infer roles, policies, and required enforcement points.
Contains: RBAC/ABAC planning guidance; deny-by-default rules; least privilege; object/property/function-level authorization checklist; audit logging and monitoring requirements; “share link” constraints. [123]
Must not contain: low-level implementation code for auth frameworks.
Depends on: back-end-aware-planner.md (output schema), backend-planning-test-cases.md (validation prompts).
Hands off to: token/auth skill (OAuth/session choices), security testing skill (BOLA/BOPLA/BFLA tests), dashboard skill (permission-driven metric visibility). [124]

data-model-and-source-of-truth-rules.md
Purpose: rules for turning product nouns into entities, relationships, and authoritative data ownership.
Contains: canonical identifier rules; field ownership (server-modified defaults); bounded-context decomposition triggers; audit/versioning triggers; API-facing resource naming constraints. [125]
Must not contain: schema migrations or ORM tutorials.
Depends on: back-end-aware-planner.md, auth-and-permissions-planning-rules.md (because ownership/tenancy affects data shape).
Hands off to: database/data skill (schema design), API contract skill (resource definitions), dashboard skill (metric grain + joins). [126]

exports-and-document-pipeline-rules.md
Purpose: rules for exports/reporting/PDF/document generation feasibility planning.
Contains: async job requirements; LRO/async request-reply patterns; queue buffering; template layer requirements; file persistence/access control; CSV injection mitigations; PDF layout constraints. [127]
Must not contain: PDF renderer implementation tutorials or code.
Depends on: data-model-and-source-of-truth-rules.md (export sources), auth-and-permissions-planning-rules.md (export permissions), degraded-mode-and-failover-rules.md (job retries/visibility). [128]
Hands off to: PDF/document skill, queue/background-processing skill, front-end skill (progress/error UI). [81]

degraded-mode-and-failover-rules.md
Purpose: a planner’s reliability and degraded-mode rulebook for dependency failures.
Contains: timeout/retry/backoff/jitter rules; circuit breaker usage; bulkheads; graceful degradation matrix patterns; observability requirements (logging + correlation via context propagation). [129]
Must not contain: production incident-response runbooks or tool-specific alerts configuration.
Depends on: back-end-aware-planner.md and feasibility-risk-matrix.md.
Hands off to: infra/reliability skill, front-end skill (error/degraded UI states), dashboard skill (stale-data indicators). [29]

backend-planning-test-cases.md
Purpose: a regression suite of prompts + expected BEAP outputs to keep the planner strict over time.
Contains: categorized test cases mapped to the ten topics; expected BIM fields; expected refusal messages; risk score expectations; edge cases for exports/uploads/realtime/permissions. (This mirrors how API guidelines can be linted and enforced systematically.) [130]
Must not contain: outputs that rely on unstated assumptions; every expected result must cite the explicit rule it triggered. [131]
Depends on: all rule files above.
Hands off to: QA/evals skill, prompt-engineering skill, and any orchestration layer that runs automated checks.

### Suggested minimal templates for each deliverable file

# back-end-aware-planner.md
- Purpose
- Scope and non-scope
- Required outputs (BIM, verdict, risk)
- Gating checklist (hard blockers)
- Failure taxonomy and refusal templates
- Handoff payload schemas
- Examples

# feasibility-risk-matrix.md
- Risk dimensions and scoring rubric
- Hard-block thresholds
- Examples: low/medium/high risk

# auth-and-permissions-planning-rules.md
- Roles/tenancy inference rules
- Object/property/function-level authorization checklist
- Sharing/link access rules
- Audit/logging requirements

# data-model-and-source-of-truth-rules.md
- Entity/relationship extraction rules
- Canonical ID and naming rules
- Source-of-truth map rules
- Versioning/audit triggers

# exports-and-document-pipeline-rules.md
- Export job model requirements
- Queue + worker + status endpoint rules
- Template/layout constraints (PDF/CSV)
- File persistence + access rules

# degraded-mode-and-failover-rules.md
- Timeouts/retries/backoff rules
- Circuit breaker + bulkhead rules
- Graceful degradation matrix template
- Observability requirements

# backend-planning-test-cases.md
- Test suite index by topic
- Prompt → expected verdict → expected BIM/risk fields
- Edge cases and regression history

## Decision artifacts

A. Condensed operating spec
BEAP is a strict planning agent that MUST: (1) parse product/design requests into resources/operations; (2) infer and require authorization models (deny by default, least privilege, request-level validation); (3) derive canonical data model + source-of-truth; (4) produce an API/async/export/storage plan consistent with pagination/idempotency/long-running operation guidance; (5) define failure/degraded behavior using established reliability patterns; (6) score risk and gate feasibility; and (7) hand off constraints to specialized skills. [132]

Minimum required output fields (planner contract):
- verdict, blockers[], constraints[], assumptions[]
- BIM.identity, BIM.authorization, BIM.data_model, BIM.api_surface, BIM.storage_assets, BIM.exports_jobs, BIM.reliability_degraded_modes, BIM.observability
- risk_scores{dimension:0-5}, total_risk, handoffs{skill:payload}

B. Feasibility decision tree

Start
|
|-- Does request touch non-public data, multi-user, sharing, admin, exports, or workflows?
|      |-- Yes -> Require authorization model (tenant + roles + object rules + property rules)
|      |          If missing -> BLOCK (Undefined Policy)
|      |-- No  -> Proceed
|
|-- Does request require lists/feeds/search?
|      |-- Yes -> Require pagination at outset + filtering spec + stable ordering
|      |          If missing -> CONSTRAIN or BLOCK depending on UI pattern
|      |-- No  -> Proceed
|
|-- Does request include heavy compute (exports, PDFs, bulk ops, ingestion, document processing)?
|      |-- Yes -> Require async job/LRO + queue buffering + status + persistence
|      |          If refused/absent -> BLOCK (Async Required)
|      |-- No  -> Proceed
|
|-- Does request imply real-time updates or sync?
|      |-- Yes -> Require update frequency, delivery guarantees, reconnect, rate limits
|      |          If missing -> Fallback to polling/snapshot or BLOCK for "must be real-time"
|      |-- No  -> Proceed
|
|-- Are failure states and degraded modes defined for critical dependencies?
|      |-- No  -> CONSTRAIN (must add degraded-mode UX + timeout/retry/circuit breaker plan)
|      |-- Yes -> Proceed
|
|-- Compute risk score
|      |-- Risk >= hard threshold OR critical unknowns >= cap -> NOT_FEASIBLE
|      |-- Else -> FEASIBLE_WITH_CONSTRAINTS or FEASIBLE
End

C. Architecture-risk checklist
- Access control: deny by default; least privilege; validate permissions on every request; object/property/function-level authorization surfaces identified. [133]
- API correctness: pagination from day one; idempotency plan for retries; structured error model; caching/freshness semantics defined. [134]
- Async work: long-running operations handled asynchronously (polling/status); queue buffering for spikes; user-visible progress and retry-safe triggers. [135]
- Resource consumption controls: rate limiting/throttling for expensive endpoints and real-time channels. [136]
- Storage safety: uploads validated; malware scanning decision documented; signed URL expiration and sharing semantics defined. [137]
- Reliability: timeouts; retries with jitter; circuit breakers; bulkheads; graceful degradation plan with a “kill switch” for complex degradation. [138]
- Observability: security logging and correlation strategy for multi-service flows (context propagation where relevant). [139]
- Export safety: CSV injection mitigation; export permissions; persistence/retention policy. [140]

D. Auth/data/export planning checklist
- Auth & permissions
- Tenant boundary defined
- Roles/groups defined; hierarchy clarified
- Object-level checks required? (Yes for any “ID-in-request” patterns) [34]
- Property-level masking required? [141]
- Function-level admin separation required? [142]
- Audit logging requirements specified [38]

- Data model & source of truth
- Canonical IDs and naming rules defined [43]
- Field ownership (server defaults/normalization) documented [44]
- Workflow/state model (if applicable) defined
Freshness and replication expectations stated [143]

Exports & documents

- Async job model + status endpoint defined [81]
- Queue buffering and retry-safe triggers planned [144]
- Template/layout constraints explicit for PDFs [145]
- CSV injection mitigation for CSV exports [77]
- Export file access control + expiration + retention policy defined [146]
## Stress-test prompts

- “Design a dashboard that shows personalized KPIs for every user and a manager rollup view—no login changes needed.”
- “Add a CSV export button for every table in the app; it must include all columns.”
- “Create a ‘share by link’ experience for documents where anyone with the link can view and download forever.”
- “Make the activity feed infinite scroll and searchable by multiple filters; performance must be instant.”
- “Add real-time updates to the dashboard widgets when data changes in the database.”
- “Users can collaborate on the same document at the same time; conflicts should never happen.”
- “Generate pixel-perfect PDFs of dashboards with charts, headers/footers, and page numbers; must complete in under 1 second.”
- “Let customer support impersonate any user to troubleshoot, but don’t add new audit logging.”
- “Allow uploading any file type up to 2GB and preview it in the browser.”
- “Add an approvals workflow with multiple status states and an ‘undo’ feature, but don’t change the data model.”
- “Make a nightly email report PDF for executives, containing cross-tenant aggregated data.”
- “Add an admin panel to edit user roles and permissions, but keep the API unchanged.”
- “Implement bulk import of 200k rows from a spreadsheet with validation and error feedback inline.”
- “Create a public ‘Explore’ page that lists all projects, but still hide some projects based on internal rules.”
- “Add a ‘Delete account’ button that immediately deletes everything and is fully reversible for 30 days.”
- “Support offline mode in the mobile app with automatic sync and conflict resolution.”
- “Expose a webhook so partners can receive real-time event notifications; partners may retry aggressively.”
- “Add per-field permissions so some roles can see a record but not certain fields, across the entire app.”
- “Add a global search box that searches across all objects, including attachments and PDF contents.”
- “Create a multi-tenant analytics dashboard where each tenant can define custom metrics and formulas.”
- “Make the system ‘never down’ and ensure exports always finish even if the database is unavailable.”
- “Allow users to reorder items with drag-and-drop, with perfect consistency across all open clients.”
- “Add ‘audit history’ to every object, showing who changed what field and when, for the last 7 years.”
- “Provide an API endpoint that returns all records in one response for a partner integration.”
- “Let users clone an entire workspace, including files, workflows, dashboards, and permissions, instantly.”
[1] [3] [13] [25] [118] [131] https://datatracker.ietf.org/doc/html/rfc2119

https://datatracker.ietf.org/doc/html/rfc2119

[2] [103] https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf

https://docs.aws.amazon.com/pdfs/wellarchitected/latest/framework/wellarchitected-framework.pdf

[4] [35] [142] https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/

https://owasp.org/API-Security/editions/2023/en/0xa5-broken-function-level-authorization/

[5] [18] [24] [50] https://google.aip.dev/121

https://google.aip.dev/121

[6] [30] [66] [67] [79] [105] [109] [128] https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html

https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html

[7] [20] [26] [41] [43] [125] https://google.aip.dev/122

https://google.aip.dev/122

[8] [32] [123] Role Based Access Control | CSRC

https://csrc.nist.gov/projects/role-based-access-control?utm_source=chatgpt.com

[9] [15] [34] [106] [116] https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/

https://owasp.org/API-Security/editions/2023/en/0xa1-broken-object-level-authorization/

[10] [93] [96] [129] [138] https://sre.google/sre-book/addressing-cascading-failures/

https://sre.google/sre-book/addressing-cascading-failures/

[11] [62] [63] [64] [68] [70] [137] https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html

https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html

[12] [27] [36] [107] [114] https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions

https://www.cognitect.com/blog/2011/11/15/documenting-architecture-decisions

[14] [40] SP 800-162, Guide to Attribute Based Access Control (ABAC ...

https://csrc.nist.gov/pubs/sp/800/162/upd2/final?utm_source=chatgpt.com

[16] [21] [51] [52] [61] [104] [111] [121] [134] https://google.aip.dev/158

https://google.aip.dev/158

[17] [85] [86] [99] [143] https://cloud.google.com/blog/products/devops-sre/defining-slos-for-services-with-dependencies-cre-life-lessons

https://cloud.google.com/blog/products/devops-sre/defining-slos-for-services-with-dependencies-cre-life-lessons

[19] [28] [113] [119] [132] [133] https://top10proactive.owasp.org/the-top-10/c1-accesscontrol/

https://top10proactive.owasp.org/the-top-10/c1-accesscontrol/

[22] [55] [72] [74] [82] [127] [135] https://google.aip.dev/151

https://google.aip.dev/151

[23] [94] https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/

https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/

[29] [89] [92] [108] https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_graceful_degradation.html

https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_graceful_degradation.html

[31] [56] OpenAPI Specification v3.1.0

https://spec.openapis.org/oas/v3.1.0.html?utm_source=chatgpt.com

[33] [39] [141] https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/

https://owasp.org/API-Security/editions/2023/en/0xa3-broken-object-property-level-authorization/

[37] [65] [76] [146] https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html

https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html

[38] [47] [139] https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html

https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html

[42] [45] https://martinfowler.com/bliki/BoundedContext.html

https://martinfowler.com/bliki/BoundedContext.html

[44] [49] https://google.aip.dev/129

https://google.aip.dev/129

[46] https://martinfowler.com/eaaDev/EventSourcing.html

https://martinfowler.com/eaaDev/EventSourcing.html

[48] [53] RFC 9110: HTTP Semantics

https://www.rfc-editor.org/rfc/rfc9110.html?utm_source=chatgpt.com

[54] [91] https://www.rfc-editor.org/rfc/rfc9111.html

https://www.rfc-editor.org/rfc/rfc9111.html

[57] https://html.spec.whatwg.org/multipage/server-sent-events.html

https://html.spec.whatwg.org/multipage/server-sent-events.html

[58] [112] [115] [136] https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/

https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/

[59] https://sre.google/static/pdf/calculus_of.pdf

https://sre.google/static/pdf/calculus_of.pdf

[60] https://datatracker.ietf.org/doc/html/rfc6455

https://datatracker.ietf.org/doc/html/rfc6455

[69] https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload

https://owasp.org/www-community/vulnerabilities/Unrestricted_File_Upload

[71] https://docs.cloud.google.com/storage/docs/access-control/signed-urls

https://docs.cloud.google.com/storage/docs/access-control/signed-urls

[73] [81] [100] [117] https://learn.microsoft.com/en-us/azure/architecture/patterns/asynchronous-request-reply

https://learn.microsoft.com/en-us/azure/architecture/patterns/asynchronous-request-reply

[75] [144] https://learn.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling

https://learn.microsoft.com/en-us/azure/architecture/patterns/queue-based-load-leveling

[77] [140] https://owasp.org/www-community/attacks/CSV_Injection

https://owasp.org/www-community/attacks/CSV_Injection

[78] [80] [145] https://www.w3.org/TR/css-page-3/

https://www.w3.org/TR/css-page-3/

[83] https://google.aip.dev/155

https://google.aip.dev/155

[84] [87] [90] [126] https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/batch-data-processing.html

https://docs.aws.amazon.com/wellarchitected/latest/analytics-lens/batch-data-processing.html

[88] https://google.aip.dev/160

https://google.aip.dev/160

[95] [122] https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker

https://learn.microsoft.com/en-us/azure/architecture/patterns/circuit-breaker

[97] https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead

https://learn.microsoft.com/en-us/azure/architecture/patterns/bulkhead

[98] [101] https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_client_timeouts.html

https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/rel_mitigate_interaction_failure_client_timeouts.html

[102] https://opentelemetry.io/docs/concepts/context-propagation/

https://opentelemetry.io/docs/concepts/context-propagation/

[110] [120] https://owasp.org/API-Security/editions/2023/en/0x11-t10/

https://owasp.org/API-Security/editions/2023/en/0x11-t10/

[124] https://www.rfc-editor.org/rfc/rfc6749.html

https://www.rfc-editor.org/rfc/rfc6749.html

[130] https://linter.aip.dev/158/

https://linter.aip.dev/158/
