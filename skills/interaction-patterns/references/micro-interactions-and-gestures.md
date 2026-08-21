# Micro-interactions

Spec each as trigger -> rules -> feedback -> loops/modes:
- Trigger: user action or system event, exact target.
- Rules: what changes, constraints, edge conditions.
- Feedback: visual/motion (values from visual-design), within 100ms of trigger.
- Loops/modes: does it repeat, does it change state persistently, how does it end.

High-value micro-interactions in Optimizely surfaces: save state transitions (unsaved -> saving -> saved-at-time), copy-to-clipboard confirmation, inline edit commit/cancel, drag handle appearance on hover, row hover revealing actions (with a keyboard-visible equivalent), expand/collapse with content-preserving motion.

Restraint rules: one animated attention-getter per view; nothing loops indefinitely; nothing moves during reading; all honor prefers-reduced-motion.

# Gestures and direct manipulation

- Desktop-first enterprise reality: hover exists but must never be the only path - everything hover-revealed needs focus-visible and touch equivalents.
- Drag and drop: show pickup (elevation), valid targets (highlight), live preview of outcome, and cancel (esc / drop outside). Always pair with a non-drag method (move-to menu, cut/paste, keyboard) - required for accessibility and preferred by many for precision.
- Reordering lists: drop indicators between items, auto-scroll at edges, announce moves to screen readers.
- Selection: click selects, shift-click ranges, ctrl/cmd-click toggles, drag-select where spatial; visible selected count with clear-all (bulk actions continue in enterprise-patterns).
- Touch (mobile/tablet contexts): 44px targets, no hover-dependent info, swipe actions duplicated in visible menus.
