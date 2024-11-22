---
layout: page
title: Black Holes
description: Developing subgrid models for BH formation, motion, accretion, and feedback
img:
importance: 1
category: galaxies
related_publications: true
---

### People
**Leads**: Greg Bryan, Sophie Koudmani, Bryan Terrazas

{% capture members_list %}
**Members**: 
{% for row in site.data.members %}
{% if row.Working_Group contains "BH" %}
{{ row.First }} {{ row.Last }}, 
{% endif %}
{% endfor %}
{% endcapture %}
{{ members_list | strip_newlines }}


### Description

The Black Hole working group works to understand supermassive black holes and their role in galaxy evolution. We develop subgrid models related to black hole seeding, orbital tracking including effects of dynamical friction, as well as accretion and a variety of feedback modalities.

<div class="row">
    <div class="col-sm">
        {% include figure.liquid loading="eager" path="assets/img/BH_jet.jpg" title="BH jet" %}
    </div>
</div>


### Projects
<ul>
{% for project in site.projects %}
  {% if project.category contains "Black Holes" %}
    <li><a href="{{ project.url }}">{{ project.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
