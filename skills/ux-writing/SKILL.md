---
name: ux-writing
description: >
  UI copy in the Optimizely voice. This skill should be used when the user asks to "write the copy",
  "microcopy", "error message", "empty state text", "button label", "tooltip", "notification text",
  "onboarding copy", "rename this", or shares UI text to improve. Trigger for ANY words-in-the-interface
  task, however small - a single button label counts.
  Lead skill of the /ux-writing command; also loaded by /design-critique, /design-pattern, /ia and /handoff stacks.
metadata:
  version: "0.1.0"
  phase: ideate
---

# UX writing

Write copy that does work: orients, moves, or recovers the user. Every string earns its space.

## Voice

Clear, confident, helpful. Plain verbs, present tense, active voice, sentence case everywhere. Never cute at the user's expense; never blame ("Something went wrong on our end" when the system failed). Address the user as "you"; the product speaks as "we" only when the company acts. Consistent terminology: one noun per concept, matching the surface's existing vocabulary (check sibling screens before coining terms) - synonym drift (item/product/entry) is a defect.

## Patterns

- **Buttons and CTAs.** Verb + object naming the outcome: "Publish 12 products", "Save changes", "Connect Shopify". Never "OK/Yes/Submit" on consequential dialogs. Pairs must be parallel and unambiguous ("Discard changes / Keep editing", not "Cancel/Cancel").
- **Errors.** What happened + what to do now, in that order; cause only when it helps. Specific beats polite-vague: "This SKU already exists in Spring Catalog. Use a different SKU or edit the existing product." Include a reference ID on system errors. No "oops", no exclamation marks, no jargon codes as the headline.
- **Empty states.** Three jobs in two sentences + one action: what this area is for, what it looks like working, the first step. First-use vs no-results vs cleared vs error-empty each get their own copy (states from interaction-patterns).
- **Confirmations and destructive dialogs.** Title = the question with the object ("Delete 'Spring campaign'?"), body = consequence and reversibility ("This removes it for all 14 members. You can restore it from Trash for 30 days."), buttons per CTA rule.
- **Tooltips and helper text.** Helper text prevents errors before input (format, constraints, consequence); tooltips define or expand, never hide required information. Under ~12 words or it belongs in the UI or docs.
- **Notifications and toasts.** Lead with the outcome, name the object, past tense for done ("Price rule published to 240 products"), progressive for ongoing. Undo verb-labeled, not "Dismiss".
- **Labels and headings.** Front-load the keyword users scan for; parallel grammar within a group; no questions as section headings in enterprise surfaces.

## Numbers, dates, truncation

Localized formats, thousands separators, relative time with absolute on hover ("2h ago" / "Jul 29, 14:02"), pluralization handled ("1 product", "12 products" - flag string-concatenation plurals for engineering).

## Output format

Deliver copy in context: element, proposed string, character count where constrained, and one alternative when tone could go two ways. For revisions, show before/after with the reason in one line. Route voice-level strategy debates to design-context conventions, legal-sensitive claims to stakeholder review.
