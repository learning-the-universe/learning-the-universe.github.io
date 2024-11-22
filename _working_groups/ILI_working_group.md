---
layout: page
title: Implicit Likelihood Inference
description: Developing techniques to infer information from astronomical observations
img: assets/img/ltu-ili-icon.png
importance: 1
category: inference
related_publications: true
---

### People
**Leads**: Matthew Ho, Benjamin Wandelt

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
The Implicit Likelihood Inference (ILI) working group develops state-of-the-art techniques to perform observational inference for problems where the full, analytic likelihood cannot be easily described. This is achieved through the use of machine learning models, which learn the likelihood of observational data directly from simulations.

The ILI group also creates and maintains generalized software solutions to tackle the diverse physical challenges studied by the Learning the Universe (LtU) collaboration. This includes the development of the LtU-ILI framework {% cite 2024arXiv240205137H %}, a highly configurable and user-friendly software package that provides access to multiple simulation-based inference techniques. The framework facilitates the comparison of different ILI methods on standardized test problems, making these cutting-edge tools more accessible to the broader scientific community. Additionally, the group explores high-dimensional inference challenges, including those complementary to the BORG group’s efforts to infer three-dimensional cosmological initial conditions {% cite 2024MNRAS.527L.173L %}.

ILI innovates on these techniques, developing new state-of-the-art tools for performing automated inference on astrophysical datasets. These include: optimal information extraction and compression, amortized estimation of Bayesian evidence {% cite 2024MLS&T...5a5008J %}, information aggregation from set-based data {% cite 2023arXiv231003812M %}, field-level inference {% cite 2023arXiv231015234D %}, sensitivity tests {% cite 2023arXiv230915071M %}, and machine learning interpretability tools {% cite ho2023information %}. These works are developed out of necessity for the problems studied in the LtU collaboration, but are practically applicable to a wide range of scientific inference problems.

ILI also leads the flagship LtU cosmological survey analysis of the CMASS galaxy sample from the Sloan Digital Sky Survey (SDSS). Incorporating tools from the AFM, Robustness, and SynthObs groups, we have developed a modular simulation pipeline to rapidly generate mock galaxy catalogs for the CMASS sample. We then apply ILI techniques to infer cosmological parameters from real data. To date, this is the largest application of Implicit Likelihood Inference to a spectroscopic galaxy survey and the first to use accelerated forward models to emulate full N-body simulations.

### Projects
<!-- markdown-link-check-disable -->
<ul>
{% for project in site.projects %}
  {% if project.category contains "Implicit Inference" %}
    <li><a href="{{ project.url }}">{{ project.title }}</a></li>
  {% endif %}
{% endfor %}
</ul>
<!-- markdown-link-check-enable -->
