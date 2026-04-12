# Design System Component Spec

## Required fields
- Component name
- Purpose and boundary
- Anatomy
- Variants
- State matrix
- Content rules
- Accessibility rules
- Implementation notes
- Rejected alternative

## Field standards
### Purpose and boundary
- Good looks like: explains when the component appears and what it does not own
- Minimum detail: one paragraph plus one explicit out-of-scope note
- Failure mode: naming the component but not its boundary

### State matrix
- include default, disabled, loading, error, success, and any conflict state that matters
- every state should name trigger, visible change, and interaction consequence

### Accessibility rules
- include keyboard, focus, label/announcement, and motion requirements when relevant
- never defer this to “engineering later”

## Anti-patterns
- anatomy-only specs
- states listed without triggers
- implementation note that says “TBD”
