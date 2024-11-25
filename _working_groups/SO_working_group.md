---
layout: page
title: Synthetic Observations
description: Creating realistic galaxy and CMB observables
img: assets/img/CAMELS_photometry.png
importance: 1
category: galaxies
related_publications: true
---

### People
**Leads**: Simone Ferraro, Shivam Pandey, Rachel Somerville

{% capture members_list %}
**Members**: 
{% for row in site.data.members %}
{% if row.Working_Group contains "SynthObs" %}
{{ row.First }} {{ row.Last }}, 
{% endif %}
{% endfor %}
{% endcapture %}
{{ members_list | strip_newlines }}


### Description
The Synthetic Observations working group develops techniques to take galaxies from hydrodynamical simulations and semi-analytic models and generate spectral and photometric observables. In addition, the group works to predict secondary CMB anisotropies (kinetic and thermal SZ effects).


### Projects
<ul>
{% for project in site.projects %}
  {% if project.category contains "Synthetic Observations" %}
    <li><a href="{{ project.url }}">{{ project.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
