---
name: interaction-patterns
description: >
  Universal interaction patterns. This skill should be used when the user designs forms, search, onboarding
  or first-run experiences, error handling, notifications and feedback, loading and empty states, or
  micro-interactions and gestures. Trigger on "form design", "validation", "search UX", "onboarding",
  "error message flow", "toast or banner", "empty state", "loading state", "hover behavior", "drag and
  drop". Do NOT use for enterprise-specific patterns like data tables, bulk actions, or permissions
  (route to enterprise-patterns).
  Co-lead of the /design-pattern command (universal pattern types).
metadata:
  version: "0.1.0"
  phase: ideate
---

# Interaction patterns

Universal patterns tuned for Optimizely's enterprise context. Read the matching reference before specifying, and check the Axiom MCP (`get_patterns`, `search_components`) for an existing implementation first - extend conventions, don't fork them.

| Designing... | Read |
|---|---|
| Forms, inputs, validation | references/forms.md |
| Search, onboarding, first-run | references/search-and-onboarding.md |
| Errors, feedback, notifications, loading, empty states | references/errors-feedback-loading.md |
| Micro-interactions, gestures, direct manipulation | references/micro-interactions-and-gestures.md |

## Universal rules

- Every interactive element needs visible affordance, all states (default, hover, focus, active, disabled-with-reason, loading), and keyboard operability (accessibility skill owns the details).
- Feedback within 100ms for direct manipulation, status within 1s for operations, progress for anything over 3s.
- Destructive and irreversible actions: confirm proportionally to blast radius; prefer undo over confirmation for reversible ops.
- Never trap: every state has an exit, every wizard has a save-and-leave.

## Output format

Inline spec: the pattern choice, behavior per state, and edge cases. Copy goes to `ux-writing`; motion values to `visual-design`; component props to `component-design`.
