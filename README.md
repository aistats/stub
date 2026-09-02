# AISTATS Conference Stub Site

This repository is the GitHub template for yearly AISTATS conference websites (`aistats20XX`). Create a new public repository from this template, then replace the `20XX` placeholders.

The site is a [Jekyll](https://jekyllrb.com/) project hosted on GitHub Pages. Most content is driven by YAML in `_config.yml` and markdown pages; the visual chrome comes from the remote theme [`aistats/jekyll-theme`](https://github.com/aistats/jekyll-theme).

## First steps after creating `aistats20XX`

1. Set `baseurl` to `/aistats20XX/` and `repository` / `ghub.repository` in `_config.yml`.
2. Fill `conference.year`, `instance`, `location`, `venue`, `dates`, `banner`, and `banner_title`.
3. Add chair details under `conference.chairs` and a contact email under `author.email`.
4. Place banner (and optional venue) images in `assets/images/`.
5. Confirm the site builds at <https://aistats.org/aistats20XX/>.
6. Update the society landing page at [aistats.github.io](https://github.com/aistats/aistats.github.io) to link the new year.

Organiser workflow notes (venue, committees, submissions, and so on) live in [`_doc/`](./_doc/README.md). Those files are not published as site pages.

## Page layout

Standard public pages match recent conferences (2023–2025):

| File | Purpose |
|------|---------|
| `index.md` | Home |
| `dates.md` | Key dates (`{% include listdates.html %}`) |
| `call-for-papers.md` | Call for papers |
| `code-of-conduct.md` | Code of conduct |
| `registration.md` | Registration |
| `committee.html` | Organising committee from `_config.yml` |
| `faqs.md` / `reviewer_guidelines.md` / `ac_guidelines.md` | Author and review guidance |
| `invited.md` / `schedule.md` / `awards.md` | Programme |
| `camera.md` / `poster.md` | Camera-ready and posters |
| `other.md` | Past meetings (usually hidden) |

Optional venue starters are underscored (`_accommodation.html`, `_local.html`) so they stay out of the nav until you promote them.

## Technical notes

- Edit YAML and markdown rather than inventing new HTML layouts when possible.
- Local includes under `_includes/` override theme fragments for the banner and date lists.
- For local builds you may need `webrick` in the `Gemfile` on newer Ruby versions.
