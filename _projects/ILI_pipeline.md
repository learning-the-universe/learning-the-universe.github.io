---
layout: page
title: LtU-ILI
description: An all-in-one framework  package for machine learning inference in astrophysics and cosmology
img: assets/img/ltu-ili-icon.png
importance: 1
category: Implicit Inference
related_publications: true
---


The Learning the Universe Implicit Likelihood Inference (LtU-ILI) pipeline is a versatile machine learning framework designed to tackle complex inference problems in astrophysics and cosmology {% cite 2024arXiv240205137H %}. Focused on flexibility and accessibility, LtU-ILI provides tools for implementing diverse neural architectures, training strategies, priors, and density estimators. Its modular design integrates easily into research workflows, supporting rapid experimentation with modeling choices and enabling scalable, parallelized computations.

{% include figure.liquid loading="eager" path="assets/img/ltu-ili.jpg" title="LtU-ILI diagram" %}

LtU-ILI unifies and extends several major simulation-based inference frameworks, including sbi, pydelfi, and lampe, under a single, cohesive interface. This integration not only facilitates direct comparisons between methods but also introduces additional features such as compatibility with image and graph-based datasets, novel neural density estimators, and advanced validation tools. Its dual Jupyter and command-line interfaces cater to both beginners and experienced users, making the pipeline highly accessible while retaining the flexibility for customization. The LtU-ILI framework also supports efficient hyperparameter tuning and rapid experimentation through its parallelized structure.

In the paper, we demonstrate the applicability and versatility of LtU-ILI via application to a wide range of astrophysical and cosmological problems. These include:
<ul>
  <li>Using CNN embedding networks for X-ray mass estimation of galaxy clusters</li>
  <li>Applying posterior coverage validation for cosmological inference from the matter power spectrum</li>
  <li>Embedding dark matter halo point clouds with graph neural networks </li>
  <li>Applying active learning for gravitational wave parameter estimation</li>
  <li>Quantifying information in photometric measurements for modeling galactic dust</li>
  <li>Aggregating information-optimal embeddings for inference of semi-analytic models of galaxy formation</li>
</ul>
Together, these examples highlight the pipeline's potential to streamline complex workflows and enable robust scientific discovery in a wide range of inference problems.
The LtU-ILI package, as well as all the above astronomy examples, are made publicly available at: [https://github.com/maho3/ltu-ili/tree/main/ili](https://github.com/maho3/ltu-ili/tree/main/ili)
