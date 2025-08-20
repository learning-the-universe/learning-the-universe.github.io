---
layout: page
title: BORG enhanced
description: Improving data models for inference
img:
importance: 1
category: BORG
related_publications: true
---

We have engineered BORG to accommodate a wide array of physical models, a
necessity for scaling BORG inference to cosmological volume. These models are
enhanced by Machine Learning techniques, developed in conjunction with AFM WG.
Notably, we have broken new ground in non-linear N-body inference by
integrating a neural network emulator of the displacement field {% cite
Jamieson:2023 %}, {% cite Doeser:2023 %} with the BORG inference machine. We
have introduced a novel BORG-Velocity model {% cite Boruah:2022 %}, {% cite PrideauxGhee:2023 %},
potentially offering the most precise handling of
redshift space distortions in galaxy surveys to date.
We have developed new galaxy bias model capable of going beyond the simple
remappings that we were using so far, and be resistant to model
misspecifications {% cite Ding:2024 %}. We have also investigated innovative
methods for computing modified gravity evolution, enabling its incorporation
into our differentiable simulator. Our team has developed
new differentiable galaxy weak lensing software, rigorously validated against
analytical calculations. This validation process, utilized by ILI-WG, has
facilitated the creation of new weak lensing data compression for ILI.
We are also developing new metrics for to assess the quality of peculiar
velocity reconstruction with regard to distance data {% cite Stiskalek:2025 %}.
These metrics were used to assess the accuracy of the new Manticore-Main
inference {% cite McAlpine:2024 %} for which we found orders of magnitude of
improvements over all available distance tracers.
Exceeding our initial objectives, we have pioneered a new technology for
differentiable Zoom simulation in BORG {% cite Wempe:2024 %}. Furthermore we
provided key technology to the ILI WG for running fast simulation at scales
over the cosmological volume with BORG-PM in the GoBig pipeline.

