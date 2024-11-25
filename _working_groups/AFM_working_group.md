---
layout: page
title: Accelerated Forward Modeling
description: Using deep learning to create rapid emulators and inference tools
img:
importance: 1
category: forward models
related_publications: true
---

### People
**Leads**: Deaglan Bartlett, Laurence Perreault-Levasseur

{% capture members_list %}
**Members**: 
{% for row in site.data.members %}
{% if row.Working_Group contains "AFM" %}
{{ row.First }} {{ row.Last }}, 
{% endif %}
{% endfor %}
{% endcapture %}
{{ members_list | strip_newlines }}


### Description

The Accelerated Forward Model group employs machine learning techniques to develop fast emulators of cosmological simulations. This includes both summary statistics and field level information of hydrodynamical simulations, N-body simulations, and semi-analytic models.


### Projects
<ul>
{% for project in site.projects %}
  {% if project.category contains "Accelerated Forward Models" %}
    <li><a href="{{ project.url }}">{{ project.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
