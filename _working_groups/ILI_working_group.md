---
layout: page
title: Implicit Likelihood Inference Working Group
description: Develops techniques and tools to infer cosmological information from observations
img:
importance: 1
category: inference
related_publications: true
---

### People
**Leads**: Matthew Ho, Benjamin Wandelt


**Members**: {% capture members_list %}
{% for row in site.data.members %}
{% if row.Working_Group contains "ILI" %}
{{ row.First }} {{ row.Last }}, 
{% endif %}
{% endfor %}
{% endcapture %}
{{ members_list | strip_newlines }}

### Description
The Implicit Likelihood working group develops techniques to carry out inference (including high dimensional inference) in cases where the full likelihood or posterior cannot easily be written down and is instead described with machine-learning tools.

### Projects
<ul>
{% for project in site.projects %}
  {% if project.category contains "Implicit Inference" %}
    <li><a href="{{ project.url }}">{{ project.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>