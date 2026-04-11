# Project Brief Template

## 1. Project frame
- task:
- medium:
- current phase:
- requested deliverable:
- success metric:

## 2. User and behavior logic
- audience:
- psychographic notes:
- main pain point:
- primary action that should change:
- what would make the user trust this:

## 3. Decision tests
- decision test: what specific user action changes because of this?
- frequency test: how often will this be used?
- authority test: can the target user act on the information shown?
- failure test: what breaks if this is wrong?

## 4. System constraints
- framework or stack:
- target device or resolution:
- accessibility target:
- font licensing status:
- print or Pantone constraints:
- PDF or extraction requirements:
- data, auth, or API dependencies:

## 5. System decisions needed
- strategy decisions:
- layout or grid decisions:
- type decisions:
- color decisions:
- state or motion decisions:
- implementation decisions:

## 6. Output shape
- strategy:
- system:
- implementation:
- validation:

## Example output
### 1. Project frame
- task: redesign the compliance exceptions dashboard for weekly operational review
- medium: responsive web dashboard with exportable PDF summary
- current phase: structure-to-system transition
- requested deliverable: dashboard spec, grid plan, chart logic, and implementation notes
- success metric: reviewers can identify top exception drivers and assign action within 5 seconds on first view

### 2. User and behavior logic
- audience: compliance managers, operations leads, and regional team owners
- psychographic notes: risk-aware, time-constrained, low tolerance for decorative complexity, values auditability over novelty
- main pain point: current dashboard hides urgent exception clusters inside dense undifferentiated tables
- primary action that should change: users should move from passive monitoring to direct triage and export in one pass
- what would make the user trust this: clear data freshness, obvious severity logic, reliable filters, visible audit/export trail

### 3. Decision tests
- decision test: does the dashboard make it faster to identify where exceptions are increasing and who owns them?
- frequency test: used daily for triage, weekly for executive review, monthly for PDF reporting
- authority test: yes, the primary users can assign remediation and trigger exports
- failure test: if severity or ownership is unclear, urgent issues will miss the review window and audit prep will degrade

### 4. System constraints
- framework or stack: React dashboard in tokenized design system
- target device or resolution: desktop first, tablet review secondary, mobile glance only
- accessibility target: WCAG 2.2 AA minimum, APCA-informed color checks
- font licensing status: open-source preferred, no premium dependency allowed for runtime UI
- print or Pantone constraints: exported PDF must preserve readable hierarchy in grayscale and standard office printers
- PDF or extraction requirements: exported summary must remain selectable, tagged, and extraction-safe
- data, auth, or API dependencies: role-based access, export jobs, filter persistence, freshness timestamp, owner drill-down endpoints

### 5. System decisions needed
- strategy decisions: clarify whether this is an operational or executive surface first
- layout or grid decisions: 12-column dashboard with 4-card summary band and one-click drill-down panels
- type decisions: dense but readable UI scale with tabular figures for metrics
- color decisions: severity palette must work without color-only meaning and remain restrained in dense views
- state or motion decisions: loading, filtering, export, and drill-down transitions must be explicit and minimal
- implementation decisions: exports must run asynchronously and preserve filter state

### 6. Output shape
- strategy: task framing + KPI hierarchy
- system: dashboard spec + chart selection + grid logic
- implementation: auth/export/reliability notes
- validation: dashboard density, accessibility, and evidence checks
