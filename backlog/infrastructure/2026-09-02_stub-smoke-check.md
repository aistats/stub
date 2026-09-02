---
id: "2026-09-02_stub-smoke-check"
title: "Smoke-check stub against 2025 page matrix"
status: "Ready"
priority: "Medium"
created: "2026-09-02"
last_updated: "2026-09-02"
category: "infrastructure"
related_cips: ["0001"]
owner: "Neil Lawrence"
dependencies:
- "2026-09-02_markdown-page-stubs"
- "2026-09-02_includes-and-doc-migrate"
- "2026-09-02_remove-obsolete-html"
tags:
- backlog
- testing
- cip0001
---

# Task: Smoke-check refreshed stub

> **Note**: Backlog tasks are DOING the work defined in CIPs (HOW).  
> Use `related_cips` to link to CIPs. Don't link directly to requirements (bottom-up pattern).

## Description

Verify the refreshed stub matches the 2023–2025 common page/include matrix, contains no forbidden leftovers, and optionally builds with Jekyll.

## Acceptance Criteria

- [ ] File-presence checklist vs 2025 common pages passes
- [ ] Grep finds no `lawrennd/proceedings`, and no real city/year copy outside intentional examples
- [ ] Optional: `bundle exec jekyll build` succeeds with placeholder `baseurl`
- [ ] Nav weights / `hide` flags reviewed for an early-conference surface

## Implementation Notes

Record any gaps as follow-up backlog items rather than silently skipping.

## Related

- CIP: 0001

## Progress Updates

### 2026-09-02

Task created at Ready status after CIP-0001 acceptance.
