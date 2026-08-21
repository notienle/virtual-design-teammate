# Forms

## Structure
- One column; group by topic with headings when over ~7 fields; multi-step (route to enterprise-patterns wizards) when over ~15 or when steps are conditional.
- Order: known-to-unknown, easy-to-hard, required before optional. Mark optional fields, not required ones, when most are required (enterprise default).
- Labels above inputs, always visible - no placeholder-as-label ever. Placeholder = format example only.
- Input types match data: constrained pickers over free text where the value set is known; but never a dropdown for 2 options (radio) or 50+ (search/combobox).

## Validation
- Validate on blur for format, on submit for cross-field; never on first keystroke. Reward early: turn errors into success states as the user fixes them.
- Error placement: inline at the field plus a summary at top for long forms, each summary item linking to its field.
- Messages say what's wrong and what right looks like ("Date must be after the start date, e.g. 2026-08-15"). Route wording to ux-writing.
- Preserve everything on error - wiping input is the cardinal sin.

## Enterprise specifics
- Long sessions: autosave drafts or warn on navigation with data loss; state which.
- Prefill from context (account, prior entries); show provenance of prefilled values.
- Disabled submit hides the why - prefer enabled submit that validates and explains, or a disabled state with a reason tooltip.
- Field-level permissions: read-only rendering with a "why" affordance, not hidden fields that break mental models.
