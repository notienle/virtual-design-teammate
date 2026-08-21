---
name: flows-and-states
description: >
  User flows, screen states, and wireframe specs. This skill should be used when the user asks to "map the
  flow", "user flow for", "what screens do we need", "state machine", "happy path", "edge cases for this
  flow", "wireframe spec", or designs any multi-step experience. Trigger whenever sequence, branching, or
  state completeness is the question.
  Loaded by the /design-pattern and /handoff stacks.
metadata:
  version: "0.1.0"
  phase: ideate
---

# Flows and states

Make sequence and state explicit before pixels. Most flow bugs are missing states, not wrong screens.

## User flows

- Anchor on the user goal, entry points (all of them: nav, deep link, email, empty state CTA), and the success end state.
- Notate: screens, decisions (diamond = user choice or system branch), system actions, and exits including abandonment.
- Design the unhappy paths as first-class: validation failure, permission denied, timeout, conflict (someone else edited), offline/stale data, partial success in batch operations.
- Every decision point needs the information the user requires to decide, on that screen - if it's missing, the flow has a research or content gap.
- Output as a mermaid flowchart plus a numbered narrative; keep diagrams under ~12 nodes, split by stage beyond that.

## State completeness

For every screen in the flow, enumerate the canonical states: **empty** (first-use and cleared - route copy to ux-writing), **loading** (skeleton vs spinner; what's interactive meanwhile), **partial** (some data, degraded service), **ideal**, **error** (recoverable vs terminal, always with a next action), **permission-limited** (what a viewer-role sees). Enterprise additions: bulk-in-progress, sync-pending, and stale-data indicators. A flow spec is not done until each screen's states are listed.

## Wireframe specs

Per screen: purpose (one line), content priority order (what must be seen first - this drives layout more than aesthetics), components (verify against Axiom MCP), primary action (exactly one), and annotations for behavior that a static frame can't show (what changes on selection, what persists on navigation).

## Output format

Inline: flow diagram, state table per screen, and a risk list (states with unresolved design). Route micro-level behavior to `interaction-patterns`, visual layout to `visual-design`, formal FSM modeling for complex components (multi-step editors, sync engines) stays here: states, events, transitions, and illegal-transition guards in a table.
