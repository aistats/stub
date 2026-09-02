---
title: Home
layout: default
weight: 1
---

The {{ site.conference.instance }} {{ site.conference.styling }} {{ site.conference.full_name }} ({{ site.conference.short_name }}) will be held in {{ site.conference.year }}{% if site.conference.location %} in {{ site.conference.location }}{% endif %}{% if site.conference.venue %} at {{ site.conference.venue }}{% endif %}.

<!-- TODO: Replace this placeholder with dates, registration, proceedings, and other announcements as they become available. -->

{% if site.author.email %}
General inquiries should be sent to [{{ site.author.email }}](mailto:{{ site.author.email }}).
{% endif %}
