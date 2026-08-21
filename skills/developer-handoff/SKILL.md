---
name: developer-handoff
description: >
  Package designs for engineering. This skill should be used when the user asks to "hand off", "write the
  spec for eng", "annotate for developers", "redlines", "acceptance criteria", "what does eng need",
  or finishes a design that engineering will build. Trigger at design-to-build transitions and when
  engineers ask "what should happen when...".
  Lead skill of the /handoff command.
metadata:
  version: "0.1.0"
  phase: spine
---

# Developer handoff

A handoff is complete when an engineer can build without guessing and QA can verify without asking. Static frames answer 40% of that; the spec answers the rest.

## Handoff package

1. **Intent paragraph.** What this does for whom and the one thing that must not be compromised - engineers make better micro-decisions when they know the why.
2. **Flow map.** Screens in sequence with triggers (from flows-and-states), including every state per screen: empty, loading, partial, error, permission-limited. The states table IS the handoff - happy-path-only specs generate the bug backlog.
3. **Component mapping.** Each element -> Axiom component with props/variant (verified via MCP `search_components`); intentional deviations flagged loudly with rationale; net-new components link to their spec (component-design).
4. **Behavior annotations.** Everything a frame can't show: validation rules and timing, sort/filter defaults, optimistic vs pessimistic saves, keyboard interactions, motion (values, not adjectives), responsive behavior per breakpoint, data limits (what happens at 0, 1, 1000, 100k rows).
5. **Content.** Final copy from ux-writing (no lorem in handoff), truncation rules, localization notes (+35% length survival), date/number formats.
6. **Accessibility requirements.** The a11y skill's design-time list as acceptance criteria, not suggestions.
7. **Acceptance criteria.** Given/when/then per flow, covering unhappy paths; each criterion testable by QA without a designer present.
8. **Open decisions.** Anything unresolved, with the default-if-unanswered and the owner - never hide unknowns in ambiguity.

## Handoff hygiene

- Annotate in the artifact engineers actually open (Figma dev mode notes, or the ticket) - a beautiful spec nobody opens is decoration. Link, don't duplicate; one source of truth per fact.
- Walk the spec live once (30 min) - the questions in that session are the spec's bugs; fix them in the spec.
- Stay available through build: triage eng questions within a day; log every "what should happen when" answer back into the spec.

## Output format

Inline spec structured per above, ready to paste into the ticket/Confluence (Atlassian MCP where connected). Route implementation review to `design-qa`.
