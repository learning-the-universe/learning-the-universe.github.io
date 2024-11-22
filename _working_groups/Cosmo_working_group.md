---
layout: page
title: Cosmology
description: Develops cosmological techniques with advanced subgrid techniques to carry out large cosmological simulations for training and analysis.
img:
importance: 1
category: forward models
related_publications: true
---

### People
**Leads**: Jan Burger, Volker Springel

{% capture members_list %}
**Members**: 
{% for row in site.data.members %}
{% if row.Working_Group contains "COSMO" %}
{{ row.First }} {{ row.Last }}, 
{% endif %}
{% endfor %}
{% endcapture %}
{{ members_list | strip_newlines }}


### Description

The Cosmology working group develops and implements new techniques for cosmological simulations, working with the star formation and black hole working groups to incorporate new subgrid models, as well as the training set generation and accelerated forward model working groups to develop fast emulators.


### Projects
<ul>
{% for project in site.projects %}
  {% if project.category contains "Cosmology" %}
    <li><a href="{{ project.url }}">{{ project.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
