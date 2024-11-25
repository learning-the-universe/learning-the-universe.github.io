---
layout: page
title: Resolved Star Formation and Galactic Winds
description: Developing subgrid models for the star-forming interstellar medium and galactic winds
img:
importance: 1
category: galaxies
related_publications: true
---

### People
**Leads**: Chang-Goo Kim, Eve Ostriker

{% capture members_list %}
**Members**: 
{% for row in site.data.members %}
{% if row.Working_Group contains "SFGW" %}
{{ row.First }} {{ row.Last }}, 
{% endif %}
{% endfor %}
{% endcapture %}
{{ members_list | strip_newlines }}


### Description
The Resolved Star Formation and Galactic Winds working group employs direct numerical simulations to develop and calibrate new subgrid models for predicting star formation rates, the effective equation of state, and multiphase wind loading from coarse grained information in cosmological simulations. Using state-of-the art methods to implement stellar feedback -- radiation, supernovae, and cosmic rays -- is crucial for high fidelity results. This working group also develops techniques for implementing subgrid models in cosmological simulations that is robust to variations in spatial and mass resolution while capturing key physical effects that cannot be directly resolved.


### Projects
<ul>
{% for project in site.projects %}
  {% if project.category contains "Star Formation" %}
    <li><a href="{{ project.url }}">{{ project.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
