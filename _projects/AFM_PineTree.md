---
layout: page
title: Pinetree
description: Generative, fast, and differentiable halo model
img:
importance: 1
category: Accelerated Forward Models
related_publications: true
---

The PineTree galaxy emulator {% cite Ding:2024 %} builds on previous work (% cite Charnock:2020 %} to predict galaxy clustering and lensing observables, exploiting the cosmological scale hierarchy to accurately capture non-linear information while maintaining computational efficiency. PineTree is built to have an extremely low parameter count that can be inferred from the data themselves. By leveraging these and more accurate models currently under development, our pipeline can scale to the large data volumes anticipated from upcoming surveys like DESI and Rubin LSST.

PineTree is related to the [CHARM model](/projects/AFM_CHARM) by being much simpler and able to being fitted directly on observations. It comes at the cost of the flexibility, and thus the possibility to represent more complex matter-galaxy bias relations. The PineTree model relies on a very shallow neural network, with only on 18 to 34 trainable parameters compared to millions in CHARM, to produces halo catalogues from dark matter overdensity fields. The reduction of network weights is realised through incorporating symmetries motivated by first principles into our model architecture. The model shares some properties of Halo Occupation Distribution model: it maps abundances of objects through observable quantity, conditioned on the environment, and validate its two and three point correlation properties. 

By being so compact, and differentiable, this model is adequate to be incorporates into an [explicit BORG likelihood analysis](/working_groups/BORG_working_group).

An illustration, shown as well in the referenced article, of the way of PineTree works is given below:
{% include figure.liquid loading="eager" path="assets/img/pinetree.png" title="PineTree schematic" %}
