---
layout: page
title: Explicit Likelihood (BORG)
description: Infers cosmological initial conditions
img:
importance: 1
category: inference
related_publications: true
---

### People
**Leads**: Jens Jasche, Guilhem Lavaux

{% capture members_list %}
**Members**: 
{% for row in site.data.members %}
{% if row.Working_Group contains "ILI" %}
{{ row.First }} {{ row.Last }}, 
{% endif %}
{% endfor %}
{% endcapture %}
{{ members_list | strip_newlines }}

### Description

The BORG (Bayesian Origin Reconstruction from Galaxies) group uses Bayesian techniques coupled with fast dark matter forward models and flexible galaxy models to infer the cosmological initial conditions based on present day galaxy redshift catalogs and other data.

The core idea of what we are trying to achieve is summarized by the following figure:
{% include figure.liquid loading="eager" path="assets/img/BORG_in_a_shot.jpg" title="BORG schematic" %}

For more information, visit the [Aquila Consortium website](https://www.aquila-consortium.org/).
