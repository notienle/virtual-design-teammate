---
name: design-critique
description: >
  Critique and audit UX/UI designs - the default whenever a screenshot, mockup, Figma link, prototype, or
  URL arrives wanting feedback of ANY kind. Trigger on "critique this", "audit", "UX review", "what do you
  think of this screen", "roast this", "any issues", "is this good?", "does this follow Axiom", "feedback
  on my design", or an uploaded UI image with even a casual ask. Also use for focused single-lens critiques:
  hierarchy, typography, color, composition, affordance, information density, brand consistency, or ethics.
  Lead skill of the /design-critique command.
metadata:
  version: "0.1.0"
  phase: ideate
---

# Design critique

Run a four-lens audit by default; run a single lens when the user names one. Be candid and specific - a critique that only compliments is a failed critique, and so is one that buries the two things that matter under twenty nitpicks.

## Inputs

Accept screenshots, Figma links (pull via Figma MCP `get_design_context` / `get_screenshot`), HTML prototypes, and live URLs. If context is missing, ask ONE question max (who is the user and what's the primary task), then proceed with stated assumptions rather than stalling.

## Default four-lens audit

1. **UX heuristics** - Nielsen's ten plus flow logic: visibility of status, match to user language, control and freedom, consistency, error prevention, recognition over recall, efficiency, minimalism, error recovery, help. Load `ux-laws` when a finding needs its psychological why.
2. **Accessibility** - quick pass: contrast, target size, focus order, color-only meaning, labels. Load the `accessibility` skill for a full WCAG audit when stakes warrant.
3. **Axiom compliance** - verify against the live system via Axiom MCP (`search_components`, `get_tokens`, `get_patterns`): off-system components, off-scale type/spacing, wrong semantic token usage, pattern deviations from sibling Optimizely surfaces. Never assert a token violation from memory - check.
4. **Visual craft** - hierarchy, composition, density, type, color quality (criteria live in the lens references below).

## Focused lenses

When the user asks for one dimension, read the matching reference and go deep on it alone:
references/lens-visual-hierarchy.md, lens-typography.md, lens-color.md, lens-composition.md, lens-affordance.md, lens-information-density.md, lens-brand-consistency.md, lens-ethics.md

## Finding format

Each finding: **severity** (Blocker - prevents task or violates WCAG A/AA or trust; Major - significant friction or system violation; Minor - friction; Polish - craft), **location** (be exact: "primary button, table header row"), **issue**, **why it matters** (heuristic, law, token, or user-cost), **recommendation** (specific, Axiom-native where possible). No finding without a fix.

## Output format

Inline: one-paragraph overall read (what works, the core problem if any), then findings grouped by severity, then "if you fix only three things". End with counts by severity. Offer a branded Word report via the optimizely-brand skill only as a follow-up. Route copy rewrites to `ux-writing`, missing states to `flows-and-states`, verification after fixes to `design-qa`.
