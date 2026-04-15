# Design Token Architecture

Use this file to keep design decisions translatable to code.

## Token layers
1. Primitive tokens - raw values
2. Semantic tokens - role-based aliases
3. Component tokens - component-specific applications

## Naming rule
Use:
`{category}-{role}-{variant}-{state}`

Examples:
- `color-text-primary`
- `color-border-negative`
- `space-layout-page-x`
- `radius-control-sm`
- `motion-feedback-fast`
- `button-bg-primary-hover`

## Non-negotiables
- primitives must not be used directly in component code unless no semantic alias exists yet
- names must not encode raw values like `16px` or `blue`
- stateful components must have state tokens or state rules
- dark mode must swap through semantic aliases, not one-off overrides
- token output should stay flat and human-readable

## Default stack
- color
- typography
- spacing
- radius
- border
- shadow
- motion
- z-index / layering
- component aliases

## Validation checks
- max 3 alias layers
- avoid more than 5 name segments
- reject raw-value naming
- prefer semantic and component aliases over ad hoc literals
