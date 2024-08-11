---
layout: page
title: Synthetic CMB
description: Mock CMB observations
img:
importance: 1
category: Synthetic Observations
related_publications: true
---

Having completed the necessary preparatory steps in 2023 and previous years, the CMB effort in 2024 focused on fast and differentiable baryon pasting techniques to turn the output of fast (dark-matter only) N-body simulations into a realistic gas and matter distributions trained on a variety of hydrodynamical simulations with a range of astrophysical and cosmological parameters. This is an essential step in the overarching goal of joint cosmological and astrophysical inference from galaxies and CMB observations. Building on previous LtU work highlighting the importance of the halo environment and projection effects in determining the gas properties in and around galaxies {% cite Hadzhiyska:2023cjj %},{% cite Baxter:2023lfb %}, {% cite Pandey:2023wqp %}, {% cite Pandey:2024pyt %}, we have developed two methods to process N-body simulations and predict the gas properties (density, temperature, pressure, etc.) as well as CMB observables (primarily the thermal and kinematic Sunyaev-Zel'dovich effects and CMB lensing) in a way that preserves the environmental dependence of the signal. The first method is halo-based (Pandey et al, in prep.), while the second one is field-based (Liu, Hadzhiyska, Ferraro et al, in prep). We are in the process of benchmarking and comparing them, together with a careful comparison with other recent suggestions in the literature.
