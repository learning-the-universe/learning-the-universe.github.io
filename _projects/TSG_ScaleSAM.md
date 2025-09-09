---
layout: page
title: ScaleSAM
description: Cosmological Rescaling of Merger Trees for Semi-Analytic Galaxy Modelling
img:
importance: 1
category: Training Sets
related_publications: true
---

Cosmological Rescaling of Merger Trees for Semi-Analytic Galaxy Modelling (Stiskalek et al., in prep.) provides a fast, accurate route to explore cosmology for galaxy-formation studies without rerunning expensive numerical simulations. Building on [`CAMELS-SAM`](https://camels-sam.readthedocs.io/en/main/) {% cite 2023ApJ...954...11P %} we map existing merger trees to nearby target cosmologies and re-run the Santa Cruz semi-analytic model (SC-SAM) on the rescaled trees. We introduce novel halo profile corrections that minimize residual biases in scaled halo properties and enable near-instant rescaling of all merger trees from a single CAMELS-SAM realization.

We perform stringent object- and population-level checks to verify that halo and galaxy properties remain unbiased after rescaling. Building on this validation, we present a pipeline that generates a dense grid of rescaled merger trees across cosmological parameter space from a comparatively small set of baseline $N$-body simulations, and we use it to generate training data for downstream simulation-based inference.

Ongoing work aims to make the rescaling pipeline fully differentiable, allowing derivatives with respect to cosmology to propagate through both the merger trees and the semi-analytic galaxy formation model. In parallel, we are planning to integrate the framework with the Learning the Universe: Connections project to attach synthetic photometry to the rescaled galaxy populations, thereby enabling direct comparison with observations.
