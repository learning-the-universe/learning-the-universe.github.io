---
layout: page
title: Pinetree
description: Generative, fast, and differentiable halo model
img:
importance: 1
category: Accelerated Forward Models
related_publications: true
---

The PineTree galaxy emulator {% cite Ding:2024 %} builds on previous work (% cite Charnock:2020 %} to predict galaxy clustering and lensing observables. It exploits the cosmological scale hierarchy to capture non-linear information accurately while maintaining computational efficiency. PineTree is designed to have an extremely low parameter count, allowing these parameters to be inferred directly from data. By leveraging this and more accurate models currently under development, our pipeline can scale to the large data volumes expected from upcoming surveys like DESI and Rubin LSST.

PineTree is a simplified alternative to the [CHARM model](/projects/AFM_CHARM), capable of being fitted directly to observations. This simplicity comes with a trade-off in flexibility, potentially limiting the representation of more complex matter-galaxy bias relations. The PineTree model employs a shallow neural network with only 18 to 34 trainable parameters (compared to millions in CHARM) to generate halo catalogues from dark matter overdensity fields. The reduction in network weights is achieved by incorporating symmetries motivated by first principles into the model architecture. Sharing properties with the Halo Occupation Distribution model, PineTree maps object abundances through observable quantities conditioned on the environment and validates two- and three-point correlation properties.

Due to its compactness and differentiability, PineTree is well-suited for integration into an [explicit BORG likelihood analysis](/working_groups/BORG_working_group).

An illustration, shown as well in the referenced article, of the way of PineTree works is given below:
{% include figure.liquid loading="eager" path="assets/img/pinetree.png" title="PineTree schematic" %}
