# UX laws reference

**Hick's law.** Decision time grows with number and complexity of choices. Apply: trim simultaneous options, chunk menus, progressive disclosure, recommended defaults. Limits: doesn't apply to scannable ordered lists (alphabetical pickers) or expert-memorized layouts; removing needed options trades decision time for task failure.

**Fitts's law.** Acquisition time depends on target distance and size. Apply: primary actions large and near the work; screen edges/corners are effectively infinite targets; group sequential controls; beware tiny adjacent icon buttons (misclick cost). Limits: keyboard-driven experts bypass it; giant buttons for rare actions waste space.

**Miller's law / chunking.** Working memory holds ~4-7 chunks. Apply: chunk IDs and numbers, group form fields, limit nav levels held in memory, summarize before detail. Limits: it's about memory, not display - a 40-row table users scan (not memorize) doesn't violate it.

**Jakob's law.** Users spend most time in other products; they import expectations. Apply: follow platform and category conventions (cart top-right, settings gear, drag to reorder); innovate only where you add clear value. In Optimizely: match sibling-surface conventions first. Limits: conventions can be outdated or wrong for expert workflows; copy the expectation, not necessarily the implementation.

**Tesler's law (conservation of complexity).** Every process has irreducible complexity; it moves between system and user but doesn't vanish. Apply: absorb complexity into defaults, automation, and smart mapping - don't export it as configuration. Ask "who should carry this: us once, or every user every time?" Limits: over-absorbing removes control experts need; provide escape hatches.

**Doherty threshold.** Sub-400ms system response keeps users in flow. Apply: optimistic UI, skeletons, instant local feedback even when the real work is async; performance budgets are UX specs. Limits: perceived speed can be honest theater but never lie about completion.

**Von Restorff (isolation) effect.** The one different thing gets remembered/noticed. Apply: exactly one visual outlier per view = the thing that matters (primary CTA, critical alert). Limits: many outliers cancel out; novelty draws attention but not necessarily comprehension.

**Aesthetic-usability effect.** Polished interfaces are perceived as more usable and get more error tolerance. Apply: craft buys patience and trust, worth investing in first impressions. Limits: it masks usability problems in testing - probe behavior, not just satisfaction; polish over broken flows is lipstick.

**Peak-end rule.** Experiences are judged by their peak moment and their end. Apply: invest in the emotional peaks (first success, publish moment) and endings (completion confirmations, offboarding); rescue bad peaks (error recovery quality defines the memory). Limits: doesn't excuse mediocre middles for long daily-use workflows where fatigue accumulates.

**Law of proximity.** Close things read as related. Apply: spacing is the primary grouping tool; intra-group gap clearly smaller than inter-group. Limits: proximity lies when unrelated items are cramped together by layout accident.

**Law of common region.** Shared boundaries/backgrounds group elements. Apply: containers when proximity can't do the job (dense dashboards, mixed content); one level of containment usually suffices. Limits: box-in-box nesting adds noise; if you need three nested borders, restructure.

**Serial position effect.** First and last items are recalled best. Apply: put critical nav items at ends of lists/menus; order steps and options so the vital ones anchor. Limits: applies to recall, not on-screen scanning.

**Zeigarnik effect.** Incomplete tasks occupy the mind. Apply: progress indicators, setup checklists, resume-where-you-left, draft badges - visible incompleteness motivates return. Limits: manufactured incompleteness (fake progress) erodes trust; too many open loops cause anxiety, not motivation.

**Postel's law (robustness).** Be liberal in what you accept, strict in what you send. Apply: accept messy input (paste with spaces, mixed date formats), normalize gracefully, output canonical formats; forgiving search and matching. Limits: silent normalization of consequential values (prices, IDs) must be confirmed, not assumed.

**Goal-gradient effect.** Motivation accelerates near a goal. Apply: show progress with the end visible, seed initial progress (step 1 pre-completed honestly), break long journeys into near-finish segments. Limits: fake progress bars and inflated steps are dark patterns - see design-critique ethics lens.
