---
name: design-review
description: "Audit and critique UX/UI designs for Optimizely product work. Use this skill whenever the user shares a screenshot, mockup, HTML prototype, or working URL and wants design feedback of any kind. Trigger on phrases like \"critique this\", \"audit my design\", \"design review\", \"UX review\", \"what do you think of this screen\", \"roast this\", \"any issues with this UI\", \"is this accessible\", \"does this follow Axiom\", or when an image/HTML file of a UI is uploaded with a request for feedback - even casual ones. Covers UX heuristics, Axiom design system compliance, accessibility (WCAG), and visual craft. Default output is a fast inline chat critique with severity ratings; a branded Word doc is an optional follow-up."
---

# Design UX Audit

Version: v31 (2026-08-20). When starting an audit, silently note this version internally; if the user asks which version is installed, tell them.

A critique skill for Optimizely designers. It evaluates a design against four lenses and returns an honest, severity-rated critique inline in chat. The goal is critique a senior designer would give: specific, actionable, tied to evidence, and never padded with flattery.

## When this triggers

- A screenshot or mockup image is shared with any request for feedback
- An HTML prototype file is uploaded ("review my prototype", "audit this build")
- A working URL is shared for review (Vercel deploys, sandbox links, staging)
- A Figma link is shared for critique (use Figma MCP `get_screenshot` / `get_design_context` to pull the frame)
- Requests for a heuristic evaluation, accessibility check, or Axiom compliance check

Do NOT use for: competitive research (use `design-competitor-research`), building new UI from scratch, or pure copy/content editing.

## Inputs and how to read them

**Screenshot(s)**: Analyze the image directly. If multiple screens are shared, treat them as a flow and also critique the transitions between them.

**HTML file**: Read the full source. Critique both what renders (infer layout from markup + CSS) and what the code reveals that a screenshot cannot: semantic HTML, ARIA usage, focus management, heading order, alt text, form labels, touch target sizes, and hardcoded colors vs tokens. Compute contrast ratios from CSS hex values where text/background pairs are identifiable. If visual judgment is impossible from code alone, say which findings are code-verified vs inferred, and ask for a screenshot only if it materially changes the audit.

**Working URL**: If Claude in Chrome tools are available, open the URL, take screenshots of key states, and interact where relevant (hover, focus, empty/error states, resize for responsiveness). Audit what you actually observed, and list which states you did or didn't reach. If browser tools are unavailable, use `web_fetch` on the URL and treat it like the HTML file case.

**Figma link**: do NOT resolve the node before the intake form - that's the main source of pre-form lag. Instead, the intake form carries a generic optional scope field ONLY when the user has not already specified what to audit (see the template conditions), and resolution happens after submission:
- **Single frame** → audit it; the scope field is ignored unless filled.
- **Section, page, or board with multiple frames/rows/flows** (e.g. a working board with labeled rows and dozens of screens) → never audit the whole thing shallowly and never silently pick one frame. If the user filled the scope field, match it against the detected rows/sections/frame layer names and audit that part. If the scope field was left blank, list the detected row/flow names in ONE short line with a recommendation ("This board has 4 rows: Admin view, Buyer flow, IA, Components - I'll audit 'Buyer flow' as the most complete; say the word if you want a different one or everything") and proceed with the recommendation without waiting - the user can redirect at any point, including at the confirmation gate.
- **Flow / range of screens**: when the chosen scope (or the user's request) is a flow or row of connected screens, audit it as a flow, not isolated frames - evaluate the step-by-step progression, pattern consistency across screens, what carries over between steps, and where a user would lose the thread. Locate issues by screen ("Screen 2 of 5: ...") and name the flow in the score card.
- **Whole section (broad pass)**: audit at the pattern level - recurring issues named once with instance counts - and say explicitly that per-screen depth is reduced at this breadth; offer to deep-dive any single row or frame afterward.

**HTML file and working URL - scope**: handled by the same generic optional scope field in the intake form; no pre-form fetching or route detection. After submission: a filled scope field is matched against the detected views/routes; an empty one on a multi-view prototype gets the same one-line list-and-recommend treatment as Figma boards (proceed with the recommendation, user can redirect anytime). If the user already named the screen or flow in their request ("audit the checkout flow in this prototype"), the scope field's answer is that - never ask for what's already stated. Whole-prototype audits follow the broad pass rules (pattern-level findings, reduced per-screen depth stated, deep-dive offered after).

## Context intake (always do this first)

**Fast intake path - the form must appear within the first few steps.** On invocation, do ONLY these before rendering: read `references/intake-form.md`, load the Visualizer elicitation guidance, render the form. Do NOT resolve Figma links, fetch URLs, read HTML files, read the product/heuristics references, or run any benchmark searches before the form is on screen - all of that happens AFTER the submission arrives. The user should see the form almost immediately.

Before running any audit, render ONE combined intake form (Visualizer elicitation pattern; template in `references/intake-form.md`) containing all three questions stacked in this order:

1. **"Which product is this design for?"** - single-select pills covering the Optimizely One portfolio: Commerce Connect (CoCo), Configured Commerce (CFG), CMS, CMP, Web Experimentation, Feature Experimentation, ODP, OCP, Opal, Analytics, Admin Center / Reporting, Other.
2. **"What is the context of this design?"** - free text field (what it's for, who uses it, what problem it solves). Never reduce this to preset options.
3. **"What do you want to audit for?"** - multi-select pills, numbered: 1. UX heuristics, 2. Accessibility, 3. Axiom compliance, 4. Visual craft - all four pre-selected; the user deselects what they don't need.

Rendering rules:
- One short chat line before the form, nothing after it - **the widget is the last thing in the turn**. End the turn immediately; the submission arrives as the next user message.
- If the Visualizer is unavailable, ask all three questions in one plain chat message instead (numbered options for lenses so the user can reply "1, 3").

Handling the submission (it arrives as one user message with the filled fields, e.g. "Product: Opal - Context: personality picker for VAUs - Lenses: 1. UX heuristics, 2. Accessibility"):
- Use whatever fields are present. For ANY missing, empty, or skipped field, apply its default silently: product = infer from the design; context = infer from the design; lenses = all four.
- A skip ("Skipped - proceeding with defaults") applies all defaults. **Never re-ask any intake question after the form has been submitted or skipped - not as a form, not in plain chat.** State inferred assumptions in one line at the top of the audit and proceed straight into it in the same turn.
- After the product is known (answered or inferred), read `references/optimizely-products.md` and judge findings against that product's job to be done and audit implications.
- Skip the form entirely only when the user's message already answers everything (e.g. "check the accessibility of this Opal personality screen for VAU setup" covers product, context, and lenses) - then confirm the reading in one line and audit immediately.
- Scope the audit to the selected lenses - but if you spot a Blocker outside the selected scope, mention it briefly anyway (never bury a Blocker for scope reasons). If the context answer is thin, work with it rather than interrogating. Don't ask about the design's stage, but if the user volunteers it, calibrate polish severity accordingly (lighter on early explorations, stricter on pre-ship builds).

## The four lenses

Run the lenses selected in the intake form (all four by default). In the output, show theme headers only for the selected lenses.

### 1. UX heuristics (NN/g + IA + mental models + scale)
Read `references/nng-heuristics.md` and walk through ALL of it: the 10 Nielsen Norman Group heuristics, the supporting UX-psychology laws (Fitts, Hick, proximity, chunking, peak-end), and the three deeper sections - Information architecture, Mental models, and Design at scale. The deeper sections matter as much as the heuristics: usability polish on a screen with broken hierarchy, a mismatched mental model, or a layout that collapses at real data volumes is polish on the wrong thing. Check everything against the design, but only report what's actually violated or notably well-handled - don't recite the checklist back. Name the framework in each finding (heuristic name, law, "IA: hierarchy", "mental model", "at scale") so it's teachable.

### 2. Axiom design system compliance
If the `axiom` MCP tools are available, verify rather than guess: `search_components` to check whether a pattern in the design has an existing Axiom component, `get_component` for correct props/variants, `get_tokens` for color/spacing/type tokens. Flag: custom-built elements where an Axiom component exists, off-token colors or spacing, wrong component variant for the context, and icon misuse (`search_icons`). If the tools aren't available, flag likely deviations as "verify against Axiom" instead of asserting.

**Compliance score**: this lens always reports a percentage. Method:
1. Inventory every distinct checkable element in the design - components (buttons, inputs, tables, chips, modals, nav...), colors, typography styles, iconography, and spacing patterns. Each distinct element type counts once.
2. Check each against Axiom and mark it compliant, mismatch, or unverifiable (can't be judged from this input, e.g. exact hex unknowable from a compressed screenshot).
3. Score = compliant / (compliant + mismatch). Unverifiable items are excluded from the math but disclosed.
4. Report as e.g. "Axiom compliance: 78% (14 of 18 checked elements match, 3 unverifiable)" followed by the mismatch list - every non-compliant element gets a line: the element, what it currently is, and the correct Axiom component/token/variant to use.

The percentage is an audit aid, not a precision instrument - keep the inventory honest and count each element type once so the number is comparable across audit rounds of the same design.

### 3. Accessibility (WCAG 2.2 AA)
Check what the input allows: text contrast (4.5:1 body, 3:1 large text and UI components), touch/click target size (24x24 minimum, 44x44 preferred), visible focus states, color as the only signal, form labels and error identification, heading hierarchy, and keyboard reachability (code/URL inputs only). Cite the specific WCAG criterion number for anything flagged so engineers can look it up.

### 4. Visual craft
Hierarchy (does the eye land where the job starts), spacing rhythm and alignment consistency, typography scale discipline, color usage restraint, density appropriate to an enterprise data product, and empty/loading/error state design if visible. This lens is subjective - frame findings as a designer's judgment call, not a rule violation.

## Screen type and pattern benchmark

Before auditing, AUTO-DETECT what kind of screen or flow this is - never ask the user. **The user's own words come first**: the context answer from the intake form (and anything stated in their request) outranks what's visually detectable on the screen. If they wrote "quote approval flow for CSR managers", classify and benchmark THAT - even if the screen superficially reads as a generic table or form. What's readable on screen refines the classification; it never overrides the stated context. Only when the context field is empty or too thin does on-screen detection carry the classification alone. Classify from the common taxonomy: dashboard/hub, list/table, detail view, form/settings, permissions & access management, wizard/multi-step flow, picker/selector, onboarding, empty state, auth/login, search/browse, checkout/order, builder/editor, notifications/activity, conversational/agent UI. Use the strongest signals each input offers:
- **Figma link**: layer and frame names from the resolved metadata (a frame named "Roles & permissions" answers the question), plus the rendered content when a screenshot is obtainable.
- **HTML file**: page title, headings, nav labels, route names, and dominant components in the markup (one big `<table>` with filters = list/table screen; grouped inputs with a save bar = settings).
- **Working URL**: the page as actually observed via browser tools - URL path, page title, visible structure.
- **Screenshot**: the visible UI itself.
If the screen genuinely spans types (a settings page containing a permissions table), classify as the primary job with the secondary noted. State the classification in the JTBD line (e.g. "This is a permissions management screen whose job is confident, mistake-proof access control").

**Benchmarking**: for the classified pattern, gather how current leading products design it - and build the search from the user's stated context first, not just the visual pattern. "Quote approval for B2B CSRs" should drive searches about quote/approval workflows in B2B commerce tools, not generic "table UI best practices"; the intake context tells you which competitors and which job to benchmark against. **Default source: general web search (Google-style)** - search the pattern plus the product's named competitors from the 'Benchmark competitors' list in `references/optimizely-products.md` (e.g. LaunchDarkly and Statsig for Feature Experimentation screens, Contentful and Sanity for CMS), plus pattern write-ups from NN/g and reputable design publications. Mobbin's public explore/flow pages may naturally appear in those results and are fine to fetch (they contain usable text: flow descriptions, implementing apps, UI elements - though not the screenshots themselves), but do not treat Mobbin as a required or primary source. Exception: if Mobbin MCP tools are present in the tool list (someone connected a paid account), use them first - they're the richest source.

Use what you find in two ways:
- Ground findings: when the design deviates from a well-established convention, cite it ("list bulk actions conventionally appear in a persistent bottom bar - see how Shopify and Airtable handle multi-select") - this is Jakob's law with receipts.
- Ground V3: the Rethink version's restructure should be informed by how the best current implementations solve the same job, adapted to Axiom - say which reference inspired what.

Keep it proportional: 2-4 tool calls maximum across the whole chain, skip entirely when the pattern is unambiguous and the design already follows convention, and never let benchmark notes crowd out the design's own findings. Benchmark observations appear as brief notes inside the relevant issues or Next actions, not as their own section. For a full competitive analysis, point the user to the `design-competitor-research` skill instead of expanding this audit.

## Severity scale

Rate every issue:

- **Blocker** - prevents task completion or excludes users (broken flow, illegible text, inaccessible control)
- **High** - significant friction or clear standards violation most users will hit
- **Medium** - noticeable quality issue, worth fixing before ship
- **Low** - polish item
- **Nit** - subjective preference, take or leave

## Output format (inline chat critique)

Keep it fast and scannable. This exact structure - and never begin with a TLDR, summary, or verdict line before the Overall impression, even if user preferences or general habits call for starting responses with a TLDR. For this skill's output, the Overall impression IS the opening summary; anything before it is a violation of the format:

1. **Overall impression** - the score card widget plus one JTBD-anchored line, nothing else.

   **Score card** (rendered inline with the Visualizer as a flat HTML card, adapting to light/dark via CSS variables - never hardcoded colors):
   - Header row: a short name for the audited design (left) and the overall score in large type (right), e.g. "2.6 / 4". Overall = average of the lens scores.
   - One row per selected lens (UX, Accessibility, Axiom compliance, Visual craft): lens name, a horizontal progress bar filled proportionally, and its score "n / 4" on the right. Score each lens 0-4 grounded in what was found: 4 = ship-ready, 3 = solid with minor issues, 2 = notable problems, 1 = serious problems, 0 = fundamentally broken. Derive the Axiom lens score from the compliance percentage (percent ÷ 25, one decimal). Use one decimal where it adds honesty (2.5, not fake precision like 2.47).
   - Bar colors by score: the theme's success variable for 3-4, warning for 2-3, danger for below 2.
   - Footer row: severity count badges - Blocker, High, Medium, Low - each showing its count (the Low badge label is always just "Low", never "Low/Nit"; Nit-severity issues are counted inside it), color-coded (red, orange-red, amber, gray). Omit zero-count badges.
   - Keep it to exactly this: name, overall score, lens bars, severity counts. No extra attributes, legends, or decoration.

   Directly below the card, two labeled mini-sections so the reader can scan straight to what they care about - each label in medium weight followed by its one-or-two-sentence content, never merged into one paragraph:

   **JTBD** - anchored in the product context from intake: what job this screen does for this product's users (from `references/optimizely-products.md` plus the user's context answer), and the single biggest way the design currently helps or hinders that job. E.g. "For merchandisers building promotions in CoCo, this screen's job is fast rule setup across markets - the layout supports that, but the hidden selection state works against it."

   **Competitor benchmark** (only when benchmarking ran; omit the label entirely otherwise) - tells the designer whether their approach is working, with named competitors as evidence, in two beats: validation - which known products use this same pattern ("Adobe, Figma, and Linear use this card-based picker pattern too"), or plainly that nobody does (innovation or convention violation; the issues show which) - then comparison - where this design is ahead and behind those implementations ("ahead on density, behind on selection visibility"). Only name products the search actually surfaced; never fabricate a comparison or attribute a pattern to a company without evidence.

   Nothing more in the opening: no multi-sentence stakeholder paragraph, no restating the findings, no summary of strengths and weaknesses - the score card and the issues carry those. Do not add a separate TLDR or summary section before or after this - the score card + the two labeled mini-sections IS the opening.

2. **Issues by theme** - rendered as a single interactive accordion widget (via the Visualizer), not as long markdown. One collapsible panel per selected theme, in this order: **UX**, **Accessibility**, **Axiom compliance**, **Visual craft**. All panels start collapsed so the audit stays compact and people expand only what they want.
   - **Panel header** (always visible): theme name in medium font weight (font-weight 500 - not bold), issue count, and compact severity chips (e.g. "UX · 4 issues · [Blocker 1] [Medium 2] [Low 1]") - CSS chips matching the score card's palette. The Axiom panel header also carries its compliance score ("Axiom compliance · 78% · 3 issues").
   - **Panel body** (on expand): the theme's annotated overview image at the top, then the issues - each one short line (roughly 15-25 words), numbered globally across all themes (1, 2, 3...), sorted by severity, in problem → fix format with the anchor in parentheses, severity chip at the start. Detail crops for Blocker/High/Medium issues sit directly under their issue line. The panel closes with a **Next actions** block: 1-3 imperative lines for THIS theme, ordered by impact, each referencing its issue numbers so the issue → solution connection is visible at a glance, and each carrying an effort tag rendered as a chip: `quick fix` (under an hour, no design decisions), `medium` (a working session or component swap), `high` (needs design exploration or restructuring). E.g. "Fix contrast on secondary buttons (issues 4, 7) - quick fix". Related issues sharing one fix are grouped into one action. There is no separate priority-actions section elsewhere in the audit - each theme carries its own next actions.
   - **Images inside the accordion**: embed the annotated overviews and detail crops as base64 data URIs in the widget (compress first: JPEG, overview max ~1200px wide, crops max ~600px, quality ~65 - keep total widget size modest). If embedding would make the widget too large or the environment can't produce images, fall back to the previous format: markdown theme sections with images presented as files, and severities as 🔴 `Blocker`-style dot+chip lines.
   - Empty and unverified themes keep their panels: "checked, no issues found" or "not verified" with the reason as the collapsed header's subtitle - never a silent skip.
   - **Tie findings to the product's job where it sharpens them**: when an issue directly blocks the JTBD from intake, say so in the issue line or the theme's Next actions. Don't force it onto every issue.
   - **Detail crop mechanics**: crop each Blocker/High/Medium issue's region from the ORIGINAL image (the element plus roughly 15-20% surrounding context so it's recognizable), draw a severity-colored rectangle around the exact element, upscale small crops so they're comfortably readable. Low/Nit issues get crops only when the finding is hard to picture from words. Neighboring issues on the same element may share one crop (draw both rectangles, label with both numbers).
   - **UX and Accessibility panels must have their annotated overview** whenever an image input exists - the reader should understand those themes' findings from the image alone; it's a UI audit, the feedback should live on the UI. Axiom compliance and Visual craft get overviews when their issues are locational; skip only when findings aren't pointable (e.g. "terminology inconsistent across the flow").
   - The **Axiom compliance** header always leads with the compliance score, e.g. "Axiom compliance - 78% (14 of 18 checked elements match, 3 unverifiable)", followed by one line per mismatch: the element, what it is now, and the correct Axiom component/token/variant. At 100%, show "Axiom compliance - 100%, all N checked elements match" so the user knows the check ran and how much was covered.
   - If a theme has no issues, still show the header with a one-line confirmation so the user knows the check ran, e.g. "Accessibility - checked, no issues found".
   - If a theme could not be checked (e.g. Axiom tools unavailable, contrast unverifiable from a low-res screenshot), say "not verified" and why - never a silent skip, and never "checked" when it wasn't.
3. **Couldn't assess** - OMIT this section entirely for static inputs (Figma links/frames, screenshots): staticness is inherent to the medium, so a limits section is noise there. Include it only for HTML files and working URLs where motion and interaction states ARE assessable in principle but genuinely couldn't be reached (browser tools unavailable, states not triggerable) - one short line naming what wasn't reached. Never list motion/hover/transitions for a static input anywhere in the audit.
4. **Output contract self-check** - before ending the audit turn, silently verify every required piece rendered: score card; labeled JTBD and Competitor benchmark mini-sections (benchmark only if it ran); one accordion panel per selected lens, each with its issues, next actions, and its annotated overview (or the structured-location fallback with its reason stated); detail crops for Blocker/High/Medium issues; couldn't-assess line (HTML/URL inputs only); confirmation gate. If anything is missing, produce it before closing the turn - the output structure must be identical across runs and across designs; partial audits are the failure mode testers noticed most.
5. **Confirmation gate** - the audit turn ENDS here. Do not generate improved versions yet. Close the audit with a short confirmation asking whether the findings look right and whether to proceed, rendered as tappable options when an interactive question tool is available (otherwise one plain chat line). Options: "Generate 3 improved versions", "Something's off - let me correct first", "Skip the redesigns". Mention in the same line that they can also reply with direction or constraints in their own words (e.g. "generate, but keep the table layout and don't touch the nav") and generation will honor it. Then wait.
   - "Generate 3 improved versions" → produce them in the next turn per "Proposing an improved version".
   - "Something's off" (or any message disputing findings) → revise honestly: drop or amend the disputed issues, recompute affected scores and counts, restate the corrected summary in a few lines (don't re-render the full audit), then offer generation again once.
   - "Skip" or no engagement → don't generate and don't re-offer.
6. **Improved versions** (only after explicit confirmation) - three variants of the fixed screen, from minimal to rethink (see "Proposing an improved version" below).

After delivering, offer once as part of the confirmation gate's closing line: a downloadable export of the full audit - PDF, Markdown, or branded Word doc (via the `optimizely-brand` skill) - since chat scrolls and inline visualizations reload when switching conversations, an exported file is the durable record. Also offer a fix-priority list mapped to their Jira ticket. Produce these only when asked. The export must contain the complete audit: score table, JTBD and benchmark lines, all issues with severities and effort tags, next actions, and the annotated images embedded.

## Annotating the design

Findings are easier to act on when they live on the design itself, so annotation is per theme, embedded in the critique (see output step 2): one annotated copy of the design per theme, showing only that theme's markers so images stay uncluttered. **For UX and Accessibility this is mandatory whenever there is an image input (or one can be captured) and code execution is available - do not deliver those theme sections as text-only.**

Annotation works ONLY on the real image - never a recreation:
- The base of every annotated image MUST be the literal pixels of the user's design: the actual uploaded file from `/mnt/user-data/uploads`, or an actual browser screenshot capture. Open that exact file and draw on a copy of it.
- NEVER redraw, recreate, rebuild, or approximate the design as SVG/HTML/mockup for annotation purposes - a recreated lookalike is not their design, loses detail, and destroys trust in the audit. If you cannot access or produce a real image of the design, use the text-location fallback below instead of fabricating a visual.
- Sanity check at the verify step: the annotated image must be pixel-identical to the original everywhere except the added gutter, labels, and arrows.

Annotation style - text callouts with arrows, not bare number dots:
- Extend the canvas with a white gutter on the right side (or bottom if the design is wide) roughly 35-40% of the original width, so callout text never covers the UI.
- Each issue gets a short text label in the gutter (issue number + a 3-6 word summary, e.g. "3. Cancel competes with primary CTA") in a legible font size relative to the image, color-coded by severity: red for Blocker/High, orange for Medium, gray for Low/Nit.
- Draw an arrow (line with arrowhead) from each label to the exact element in the design it concerns. Arrows must visibly touch or point into the target element, not float nearby.

Required workflow, in order:
1. Get the base image. Screenshot input: copy from `/mnt/user-data/uploads`. Working URL: capture screenshots of the audited states via the browser tools. HTML file: render to an image if the environment allows; if not, quote the exact code line/selector per issue instead.
2. `view` the base image and note the pixel positions of each issue's target element (use the image dimensions to compute coordinates - never guess blindly).
3. Draw the gutter, labels, and arrows with Python (PIL/Pillow).
4. **Verify before presenting**: `view` the annotated PNG. Check every arrow lands on the right element and every label is legible. If anything is off, adjust the coordinates and redraw. Do not present an unverified annotation.
5. **Deliver the images inside the accordion** (see output step 2): compress each verified overview and crop (JPEG, overview max ~1200px wide, crops max ~600px, quality ~65) and embed them as base64 data URIs in the accordion widget under their theme panel. Only in the fallback (widget too large or unavailable) save the PNGs to `/mnt/user-data/outputs` and present them with the file-presenting tool at the right points in the response. Either way, an image the user can't see is a failed step.
6. **Detail crops**: while the coordinates from step 2 are known, also cut the per-issue crops from the original image per the crop mechanics in output step 2, and embed each under its issue line in the accordion (same fallback rule).

- Marker numbers are the issue's global number from the critique text (not restarting per image) - the images and the text are one system.
- **Figma inputs - image availability is the exception, not the rule.** Figma image export URLs are typically unreachable from this execution environment, so for Figma links treat annotation as conditional, in this order:
1. Try to obtain a real image via the Figma MCP `get_screenshot` / `download_assets`; if a genuine image file lands on disk, annotate it per the workflow above.
2. If no real image can be obtained, do NOT treat it as a failure or fabricate a visual. Switch to the **structured location format as the first-class deliverable**: every issue's line starts with a precise locator - row/frame layer name, screen position in the flow, and element position ("Row 'Admin view', screen 3, top-right toolbar, third button"). Consistent locators replace arrows.
3. In the same breath, offer once: "paste a quick screenshot of this area and I'll produce the annotated versions" - a designer can screenshot in seconds, and that unlocks the full visual output.
Never present a recreation as the design in any of these paths.

If the environment genuinely can't produce images for other input types either, the same structured location format applies - never silently drop the visual step, and never fabricate one.

## Proposing an improved version

Generate these ONLY after the user confirms at the confirmation gate - never in the audit turn itself. Show, don't just tell - **three distinct versions**, not one. Each version is scoped to the audit findings; the three differ in how far they go:

- **V1 - Minimal fix**: the smallest change set that resolves the Blockers and Highs, inside the current layout. What ships this sprint.
- **V2 - Refined**: V1's fixes plus the Mediums and craft corrections - tightened hierarchy, spacing rhythm, correct Axiom components - still the same structure. What ships next sprint with a bit of room.
- **V3 - Rethink**: restructures the screen to solve the root causes behind the findings (e.g. if five issues trace back to a misplaced action bar, V3 moves it). The direction worth a design discussion.

Present each as an inline mockup with a one-line label of what it prioritizes and trades off, separated by brief prose - never three mockups stacked with no text between them. Every change in every version must trace to a numbered issue (V3 may additionally restructure, but its rationale still cites the issues that motivated it). No freelance redesigning of unflagged things - that undermines trust in the critique.

Generation logic - follow this process, borrowed from Anthropic's frontend-design skill (`/mnt/skills/public/frontend-design/SKILL.md`; read it before building if available):
1. **Plan before building**: for each version, write a short internal plan - which issues it resolves, what changes, what stays. Review the plan against the audit before writing any markup; only build from the reviewed plan.
2. **Fidelity first**: recreate the original screen faithfully - same layout, sections, and real content/data from the screenshot (product names, numbers, labels - never lorem ipsum or gray boxes). A viewer must recognize their screen instantly. This is the opposite of a from-scratch design brief: distinctiveness is NOT the goal here - Axiom consistency is. Pull real values via the `axiom` MCP tools (`get_tokens`, `get_component`) when available; no invented palettes or typefaces.
3. **Apply the frontend-design quality floor**: visible focus states, honest hover/disabled states, real hierarchy through spacing and type scale rather than decoration - executed quietly, no announcing.
4. **Apply its writing guidance to any copy the fixes touch**: name things by what users control, active verbs on controls ("Save changes", not "Submit"), errors that say what went wrong and how to fix it, empty states that invite action.
5. **Critique before presenting**: review each rendered version against its plan - are the fixes actually visible, does it still read as the user's screen, would a designer respect it? Revise once if not.
6. **Render inline** using Claude's default visual mockup capability (load the Visualizer's mockup guidance via its `read_me` before the first render) - do NOT produce HTML files. Only create a downloadable file if the user explicitly asks.

After the three versions, stop - no closing diff-to-issue mapping, no "which version to pick and when" comparison. Each version's one-line label plus the issue numbers cited in its intro prose carry everything needed.

Rules:
- **HTML file or URL input**: render the versions inline the same way; additionally offer (don't produce unprompted) a revised copy of their HTML file for whichever version they pick, since they have real code to update.
- **Screenshot input**: rebuild the full screen layout inline per the fidelity bar above - the complete view as the user shared it (nav, headers, content, footer areas all present), not a cropped region or isolated component. Only zoom into a region if the user explicitly asks for it.
- If the user says "critique only" or the fixes are purely conceptual (e.g. flow-level problems one screen can't show), replace the mockups with a short "recommended direction" note instead.

## Critique quality rules

- Be honest. If the design has real problems, the TLDR says so plainly. Softening a Blocker into a "consider maybe" wastes the user's time.
- Every issue needs a fix. "This is confusing" is not a finding; "the primary action competes with Cancel - make Cancel a text button per Axiom's button hierarchy" is.
- Anchor claims: heuristic name, WCAG criterion number, or Axiom component name. Unanchored opinion goes in Nits.
- Distinguish observed from inferred, especially for HTML/URL audits where some states weren't reached.
- Cap at roughly 10-12 issues. Past that, findings stop getting fixed. If there are more, name the pattern ("spacing is inconsistent throughout, 6 instances") instead of listing each instance.
- No em-dashes anywhere in the output. Use regular dashes.

## What to push back on

- A single low-res or cropped screenshot for a flow-level question: ask for the full screen or the surrounding steps.
- "Is this good?" with zero context: ask for the user job before auditing.
- A request to only validate ("just confirm this is fine"): audit honestly anyway - that is the job.
