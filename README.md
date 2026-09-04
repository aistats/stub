# AISTATS Conference Stub Site

This repository is the GitHub template for yearly AISTATS conference websites (`aistats20XX`). Create a new public repository from this template, then replace the `20XX` placeholders.

The site is a [Jekyll](https://jekyllrb.com/) project hosted on GitHub Pages. Most content is driven by YAML in `_config.yml` and markdown pages; the visual chrome comes from the remote theme [`aistats/jekyll-theme`](https://github.com/aistats/jekyll-theme).

## Create the yearly repo (org admin)

These steps need admin access on the `aistats` GitHub organisation:

1. Create a new public repository named `aistatsXXXX` from this template ([new repository](https://github.com/organizations/aistats/repositories/new)).
2. Set a short description (dates and venue), then create the repo.
3. Create an `aistatsXXXX` admin team and grant it admin on that repository.
4. After the site is live, update the society landing page at [aistats.github.io](https://github.com/aistats/aistats.github.io) if this year should be listed as current.

## First steps after creating `aistats20XX`

1. Set `baseurl` to `/aistats20XX/` and `repository` / `ghub.repository` in `_config.yml`.
2. Fill `conference.year`, `instance`, `location`, `venue`, `dates`, `banner`, and `banner_title`.
3. Add chair details under `conference.chairs` and a contact email under `author.email`.
4. Place banner (and optional venue) images in `assets/images/`.
5. Confirm the site builds at <https://aistats.org/aistats20XX/>.

Organiser workflow notes (venue, committees, submissions, and so on) live in [`_doc/`](./_doc/README.md). Those files are not published as site pages.

Programme management (CIPs, backlog, VibeSafe) for AISTATS sites and themes lives in the sibling **site-management** repository (`aistats/site-management`), not in this template.

## Jekyll site vs virtual.aistats.org

Yearly repos on GitHub Pages (`aistats.org/aistats20XX/`) archive stable conference information. The live operations site is [virtual.aistats.org](https://virtual.aistats.org/).

| Keep on the Jekyll year site | Prefer virtual (link out) |
|------|---------|
| Key dates in `_config.yml` / `dates.md` | Registration checkout and attendee portal |
| Call for papers, CoC, FAQs, review guidelines | Paper browser / OpenReview listings |
| Invited speakers, awards, camera-ready and poster policy | Interactive schedule and session abstracts |
| Journal-to-conference and workshop *calls* (summary) | Workshop/session detail pages once published |
| Committee from `_config.yml` | Hotel booking blocks and live travel updates |
| Proceedings link when PMLR is up | Sponsor application portal |

Do not copy large virtual-only catalogues (full paper lists, calendar feeds, booking engines) into the stub. Seed a short page here, then point to virtual when that system is the source of truth.

## Page layout

Standard public pages match recent conferences (2023–2026):

| File | Purpose |
|------|---------|
| `index.md` | Home |
| `dates.md` | Key dates (`{% include listdates.html %}`; `timezone: AOE` by default) |
| `call-for-papers.md` | Call for papers (key dates via include; location/dates from config) |
| `journal-track.md` | Journal-to-Conference track call / acceptances |
| `workshops.md` | Workshop call and links to the workshop programme |
| `code-of-conduct.md` | Code of conduct |
| `registration.md` | Registration (meeting days from config; checkout link when ready) |
| `committee.html` | Organising committee from `_config.yml` |
| `faqs.md` / `reviewer_guidelines.md` / `ac_guidelines.md` | Author and review guidance (guidelines are seeded from recent years; edit in place, then fold improvements back into this stub) |
| `invited.md` / `schedule.md` / `awards.md` | Programme (schedule summarises `conference.dates`) |
| `camera.md` / `poster.md` | Camera-ready and posters |
| `other.md` | Past meetings (usually hidden) |

Optional venue starters are underscored (`_accommodation.html`, `_local.html`) so they stay out of the nav until you promote them (e.g. rename to `accommodation.md`). Set `conference.venue_url` to the hotel or booking page when you have one — the year site is primary.

## Technical notes

- Edit YAML and markdown rather than inventing new HTML layouts when possible.
- Local includes under `_includes/` override theme fragments (including `listdates.html`).
- Deadline timezone: top-level `timezone: AOE` (Anywhere on Earth). Override a single deadline with `tz: UTC` (or another zone). Keep date values parseable; do not put “Anywhere on Earth” inside YAML date strings.
- For local builds you may need `webrick` in the `Gemfile` on newer Ruby versions.
