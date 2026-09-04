---
title: Call for Papers
layout: default
weight: 2
hide: false
---

# Call for Papers

<!-- TODO: Add the call for papers text, topics, and submission instructions.
     Keep venue/location/meeting days in Liquid from _config.yml (year site is
     primary). Mirror virtual only for body prose when that is the live draft. -->

{% if site.conference.location or site.conference.dates %}
Accepted papers will be presented at the conference
{% if site.conference.location %} in {{ site.conference.location }}{% endif %}
{% if site.conference.dates and site.conference.dates.first and site.conference.dates.first != "TBA" %}
  from {{ site.conference.dates.first | date: "%B %-d" }}–{{ site.conference.dates.last | date: "%B %-d, %Y" }}
{% elsif site.conference.year %}
  in {{ site.conference.year }}
{% endif %}.
{% endif %}

## Key dates

{% include listdates.html %}

{% if site.conference.submission.url %}
Submissions are handled at [{{ site.conference.submission.url }}]({{ site.conference.submission.url }}).
{% endif %}

See also the [Journal-to-Conference track]({{ "journal-track.html" | relative_url }}) and the [workshop call]({{ "workshops.html" | relative_url }}) when those tracks are open.
