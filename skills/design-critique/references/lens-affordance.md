# Lens: affordance and interaction clarity

Evaluate what looks actionable, state visibility, CTA clarity, discoverability.

- **Clickability signal.** Interactive elements share a consistent visual language (color, underline, iconography, elevation); flag interactive-looking non-interactive elements (false affordances) and flat interactive ones (hidden affordances). The screenshot test: circle everything clickable - would a new user circle the same things?
- **Primary action clarity.** Exactly one visually primary action per view/dialog; it names the outcome ("Publish 12 products", not "OK"/"Submit"). Competing primaries = Major.
- **State visibility.** Hover, focus-visible, active, selected, disabled all designed and distinguishable. Disabled elements carry a why (tooltip/inline). Selected vs hover must differ or multi-select breaks.
- **Hidden-on-hover audit.** Row actions or controls that only appear on hover: is there a focus-visible equivalent and a touch path? Hover-only = Major (accessibility + tablet reality).
- **Feedback loops.** Every action has an acknowledged result within expectations (see interaction-patterns timing); silent saves and mystery-state toggles are findings.
- **Destructive distinction.** Destructive actions visually distinct and separated from safe ones; adjacency of Delete to Save is a Blocker-adjacent Major.
- **Discoverability of the important.** Critical capabilities buried in overflow menus or behind unlabeled icons: check icon comprehension (unlabeled icons need to be system-conventional or get labels).
