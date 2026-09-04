---
title: Program Schedule
layout: default
weight: 2
---

# Schedule

{% if site.conference.dates and site.conference.dates.first and site.conference.dates.first != "TBA" %}
{{ site.conference.short_name }} {{ site.conference.year }} main sessions run
{{ site.conference.dates.first | date: "%A, %B %-d" }} through
{{ site.conference.dates.last | date: "%A, %B %-d, %Y" }}
{% if site.conference.location %} in {{ site.conference.location }}{% endif %}.
{% else %}
Meeting days will appear here once conference dates are announced.
{% endif %}

<!-- Prefer linking out for session-level interactive calendars; keep a short
     archival summary on this page once the programme is fixed. -->

The detailed interactive schedule may be published on an external calendar when available. Do not dump a full live calendar into markdown.
