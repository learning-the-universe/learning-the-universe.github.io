---
layout: page
title: Training Set Generation
description: Designing large suites of cosmological simulations
img:
importance: 1
category: forward models
related_publications: true
---

### People
**Leads**: Daniel Anglés-Alcázar, Francisco Antonio Villaescusa-Navarro, Shy Genel

{% capture members_list %}
**Members**: 
{% for row in site.data.members %}
{% if row.Working_Group contains "TSG" %}
{{ row.First }} {{ row.Last }}, 
{% endif %}
{% endfor %}
{% endcapture %}
{{ members_list | strip_newlines }}


### Description
The Training Set Generation working group designs suites of cosmological simulations (both N-body and hydrodynamical) to create rapid emulators and innovative inference techniques.


### Projects
<ul>
{% for project in site.projects %}
  {% if project.category contains "Training Sets" %}
    <li><a href="{{ project.url }}">{{ project.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
