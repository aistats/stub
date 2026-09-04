---
title: Registration
layout: default
weight: 3
---

# Registration

<!-- Checkout / booking stays on the registration provider or virtual portal.
     This year-site page holds policy notes and dates from _config.yml. -->

{% if site.conference.dates and site.conference.dates.first and site.conference.dates.first != "TBA" %}
## Meeting dates

{{ site.conference.short_name }} {{ site.conference.year }} meets
{{ site.conference.dates.first | date: "%B %-d" }}–{{ site.conference.dates.last | date: "%B %-d, %Y" }}
{% if site.conference.location %} in {{ site.conference.location }}{% endif %}
{% if site.conference.venue %} at {{ site.conference.venue }}{% endif %}.
{% endif %}

See [Key Dates]({{ "dates.html" | relative_url }}) for registration-related deadlines.

Registration details will be announced here. When registration opens, link the external portal rather than rebuilding checkout on this site.
