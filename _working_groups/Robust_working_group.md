---
layout: page
title: Robustness / Interpretability
description: Studying model misspecification robustness and model interpretability
img:
importance: 1
category: inference
related_publications: true
---

### People
**Leads**: Barnabás Póczos

{% capture members_list %}
**Members**: 
{% for row in site.data.members %}
{% if row.Working_Group contains "Robustness" %}
{{ row.First }} {{ row.Last }}, 
{% endif %}
{% endfor %}
{% endcapture %}
{{ members_list | strip_newlines }}


### Description
This working group coordinates with the other groups to help ensure that the inference is done in way that is robust to model misspecifications and can provide guidance on the data features that are driving the parameter selection.


### Projects
<ul>
{% for project in site.projects %}
  {% if project.category contains "Robustness" %}
    <li><a href="{{ project.url }}">{{ project.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
