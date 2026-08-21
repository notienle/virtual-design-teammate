# Search

- Scope visibly: what's being searched (this project, all products, docs) with a scope switcher when it matters.
- As-you-type: suggestions under 100ms perceived (debounce + optimistic), grouped by type (objects, actions, docs). Full results on enter.
- Results: best match first with why-it-matched highlighting; filters as facets after the query, not before (route facet design to enterprise-patterns filtering).
- Zero results is a design surface: check spelling suggestion, broaden-scope offer, and a create-new path when the noun is creatable. Never a bare "no results".
- Query understanding for enterprise nouns: IDs, SKUs, and exact-match syntax should just work; document operators only if power users exist (they do).
- Natural-language search UX routes to ai-agentic-ux; keep a keyword fallback visible.

# Onboarding and first-run

- Goal: first meaningful outcome fast, not feature tour completeness. Define the "aha" action per archetype and design the shortest legal path to it.
- Progressive setup: ask only what's needed for the next step; defer org-wide configuration with sensible defaults and a visible "finish setup" checklist (3-5 items, dismissible, progress-showing).
- Empty states do the onboarding work in perpetuity: each major surface's empty state teaches what it's for, shows an example, and offers the first action (copy via ux-writing).
- Templates and sample data beat blank canvases for complex objects (experiments, campaigns); mark samples clearly and make cleanup one action.
- Contextual education over upfront tours: tooltips/coach marks at the moment of first encounter, one at a time, dismiss-and-never-nag. Route measurement of activation to product-analytics.
