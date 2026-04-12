# Module Metadata Specification

DesignPilot is moving toward compiler-friendly source modules. Priority source files should add frontmatter matching `schemas/module_frontmatter.schema.json`.

## Required fields
- `id`
- `title`
- `kind`
- `audience`
- `profile_scope`
- `precedence_level`
- `runtime_mode`
- `summary_short`
- `status`

This release adds the schema and compiler support first. Full metadata coverage across every source file is still a follow-on maintenance sweep.
