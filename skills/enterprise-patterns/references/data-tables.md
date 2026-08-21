# Data tables

## Structure
- Columns: default set = what identifies + what users act on; everything else behind column config (show/hide, reorder, persisted per user per view). First column identifies the row and links to the detail.
- Density: comfortable default, compact toggle for power users; row height consistent, no wrapping in compact.
- Alignment: text left, numbers right with consistent decimals/units, dates in one format everywhere (relative + absolute on hover).
- Sticky header always; sticky first column when horizontal scroll exists; visible scroll affordance.

## Behavior
- Sorting: single-click header, visible direction, sensible default sort stated in spec. Multi-sort only if a real workflow needs it.
- Pagination vs infinite: pagination (with page size options) for reference/work tables where position matters; virtualized infinite scroll only for feed-like browsing. Show total count either way.
- Inline edit where the edit is atomic (one cell, immediate save with saving/saved/error states per cell); side panel or page for multi-field edits. Never a modal for editing you might need table context for.
- Row actions: 1-2 primary visible on hover AND focus, rest in an overflow menu; destructive actions separated at menu bottom.
- Empty, loading (skeleton rows), error, and no-permission states all specced (interaction-patterns reference).

## At scale
- 10k+ rows: server-side sort/filter/paginate mandatory - note it for engineering; instant client feel via optimistic UI.
- Export (CSV) is table stakes for merchandiser/admin tables; respects current filters, states row limit honestly.
- Summary row for numeric tables (totals/averages of the filtered set) when the job is monitoring.
