# Roles and permissions UX

- Model to expose: roles as named bundles of capabilities; direct capability grants as the exception with an "overrides" indicator. Users think in job terms - lead role names with jobs (Editor, Approver, Admin), define each with a one-line "can... cannot...".
- Assignment UI: from the user side (this person has these roles, effective permissions expandable) AND the resource side (who can access this project). Both views, always.
- Effective-permission answerability: any admin must be able to answer "why can this person do X" - show the derivation (role Y via group Z). This single feature eliminates most permission support tickets.
- Denied-state design (the part everyone forgets): every permission-gated element is either hidden (when its existence is sensitive) or visible-but-locked with who-to-ask (default - hidden features generate "product is broken" tickets). Spec the choice per element.
- Changes: effective when, session handling on downgrade, and an audit entry (see audit reference). Warn when an admin action would lock themselves out.

# Settings and admin pages

- Scope architecture first: user settings vs project/account settings vs org settings - never mix scopes on one page; label the scope in the header ("These apply to everyone in Acme Corp").
- Organization: by user goal (Notifications, Security, Branding), 5-9 top groups, searchable when large. Each setting: plain-language label, one-line consequence ("Members can invite guests - guests see only shared projects"), current value visible without opening anything.
- Save model: pick one per page and be consistent - instant-apply with undo for low-risk toggles, explicit save with dirty-state indicator and leave-warning for grouped/high-risk. Never mix on one page.
- Dangerous zone: destructive account ops visually separated, extra confirmation, and clear about consequences and reversibility windows.
- Defaults are the product: every setting spec states the default and why; a setting most users must change is a design failure upstream.
