# Filtering and faceted search

- Filter bar above the table: high-frequency filters as visible controls (status, date range, owner), the long tail in an "add filter" builder. Applied filters render as removable chips with plain-language labels ("Status: Active").
- Facets show counts when computable; zero-count options disabled-not-hidden (users need to know the option exists).
- Combination logic: AND across facets, OR within a facet - the near-universal mental model; anything else needs explicit UI ("match any/all").
- Results update on apply for expensive queries, live for cheap ones - pick per surface and state it. Filter state lives in the URL: shareable, back-button-safe.
- Saved views = named filter+column+sort bundles: personal by default, shareable to team with a badge, one default view per user, rename/duplicate/delete managed inline. Saved views are the power feature that retains merchandisers - do not cut them for v1 without a fight.
- Clear-all always visible when any filter is applied; show "N results of M total".

# Bulk actions

- Selection: checkbox column, header checkbox = page, explicit "select all N matching" link for cross-page selection (never silently select unseen rows). Persistent action bar appears on selection showing count + actions.
- Only show actions valid for the whole selection; for mixed validity, show with count ("Publish (12 of 15 eligible)") and explain exclusions.
- Confirmation by preview for consequential bulk ops: what will change, on how many, with a sample. Type-to-confirm only for irreversible + large.
- Execution: progress with per-item outcome, cancel-remaining, and a partial-failure report (succeeded / failed with reason / retry failed only). Result persists in notification center for long jobs - users navigate away.
- Undo window for reversible bulk ops beats any confirmation dialog.
