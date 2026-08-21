---
name: design-communication
description: >
  Communicate design work: rationale, decks, case studies, impact reporting, and critique facilitation.
  This skill should be used when the user asks to "explain this decision", "write the rationale", "build a
  deck", "present this to", "design review deck", "case study", "show design's impact", "prep for the
  exec review", or needs to run a structured critique session. Trigger for any design-work-meets-audience
  moment.
  Loaded by the /strategize stack.
metadata:
  version: "0.1.0"
  phase: spine
---

# Design communication

Audience first, always: what do they care about, what do they already believe, what decision do we need from them. Ask if unknown - one question, then build.

## Design rationale

Structure: the decision, the user need and evidence behind it, options considered with why-rejected (2-3, honestly represented), tradeoffs accepted, and what would change our mind. Connect to principles (design-strategy) and data (product-analytics) where they exist; label judgment as judgment - laundering taste as data destroys credibility exactly once.

## Decks and reviews

- Narrative spine before slides: situation -> complication -> resolution -> ask. Every deck ends with an explicit ask (decision, resources, alignment) on its own slide.
- One idea per slide; the headline states the point ("Merchandisers abandon setup at step 3", not "Research findings"). Show the design big; annotate sparingly; demo flows as sequences, not single screens.
- Exec variant: lead with the outcome and the ask, evidence as backup slides, 10 minutes of content for a 30-minute slot - the rest is their questions. For exec-level reviews: business framing first (revenue, retention, cost), design craft second.
- Anticipate the three hardest questions and put the answers in appendix slides.
- File output: PowerPoint via the optimizely-brand skill, always.

## Case studies

Arc: context and constraints -> problem with evidence -> process honestly (including the wrong turns - they build trust) -> solution with the reasoning visible -> outcomes with numbers where possible -> what you'd do differently. For portfolio vs internal: portfolio emphasizes judgment and range; internal emphasizes reusable learning.

## Impact reporting

Translate design work into outcome language: metric moved (with baseline and attribution honesty), cost avoided (support tickets, eng rework), velocity gained (system adoption, reuse), risk reduced (a11y compliance, churn signals addressed). Report the chain: design change -> behavior change -> business number; where attribution is shared, say "contributed to", never claim solo credit for team outcomes. Pull numbers via product-analytics; never invent.

## Critique facilitation

Session structure: presenter states the question they want feedback on + fidelity stage; silent look; feedback rounds - clarifying questions, then what's working, then concerns phrased against the stated goal ("does X serve the goal of Y") not taste ("I don't like X"); presenter listens, doesn't defend; close with decisions and owners. Facilitator's job: protect the question, park scope creep, draw out quiet voices, timebox.

## Output format

Inline drafts and outlines by default; formatted documents/decks only on request via optimizely-brand. Route the persuasion strategy for a specific difficult stakeholder to `stakeholder-navigation`.
