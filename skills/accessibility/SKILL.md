---
name: accessibility
description: >
  Accessibility by design and by audit (WCAG 2.2 AA). This skill should be used when the user asks "is this
  accessible", "WCAG check", "contrast", "keyboard navigation", "screen reader", "a11y audit", "focus
  order", "alt text", or when designing any component/flow where inclusive access must be specified.
  Trigger proactively when a critique or spec touches color-only meaning, hover-only actions, custom
  controls, or media.
  Loaded by the /design-critique, /design-pattern, /ux-writing and /handoff stacks.
metadata:
  version: "0.1.0"
  phase: ideate
---

# Accessibility

Target WCAG 2.2 AA as the floor. Two modes: design-time guidance (build it right) and audit (find and grade violations).

## Design-time essentials

- **Perceivable.** Text contrast 4.5:1 (3:1 large), non-text UI 3:1; never meaning by color alone (pair icon/label/pattern); text resizable to 200% and layouts survive 400% zoom reflow; alt text for informative images, empty alt for decorative; captions for video.
- **Operable.** Everything keyboard-reachable and operable in a logical order; visible focus indicator (3:1, not removed, not obscured by sticky headers); no keyboard traps; targets 24x24 min (44 for touch); hover/focus-revealed content dismissible and hoverable; no time limits without extension; nothing flashes over 3/s.
- **Understandable.** Labels programmatically tied to inputs; errors identified in text with suggestions; consistent navigation and naming across screens; language of page set.
- **Robust.** Use native/Axiom components before custom (they ship the semantics); custom widgets need full ARIA pattern (role, states, keyboard model per APG); status changes announced via live regions (saves, async results, validation).

Enterprise specifics that get missed: data table headers programmatically associated, sort state announced; bulk-select and row actions keyboard paths; drag-and-drop with a non-pointer alternative (WCAG 2.5.7); toasts that also land somewhere persistent; charts with data table equivalents.

## Audit mode

Scope the screens/flows, then check systematically: automated-detectable (contrast, labels, structure - compute contrast from actual values), keyboard walkthrough (tab order narrated, operability, focus visibility), screen-reader reasoning (name/role/value per control, announcement of dynamic changes), and content (headings hierarchy, link purpose, error text). 

Finding format: WCAG criterion (number + name), level, location, issue, user impact (which assistive tech/ability affected), and remediation - specific to the Axiom component where possible. Severity: Blocker (A/AA failure preventing task), Major (AA failure with workaround), Minor (AAA or best practice). Report: counts by level, top risks, quick wins.

## Output format

Design-time: requirements woven into the spec, marked "a11y:". Audit: findings table + summary. Route implementation verification to `design-qa`, copy fixes to `ux-writing`. Note honestly what a static review cannot verify (actual SR behavior, reflow) and list it for engineering testing.
