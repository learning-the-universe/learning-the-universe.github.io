---
layout: page
title: Manticore
description: Manticore Project -- 3D Inference of Primordial Density Fields
img:
importance: 1
category: BORG
related_publications: true
---

The LtU Manticore project aimed for a comprehensive reconstruction of the 3D primordial density field using all major spectroscopic galaxy surveys: 6dF, 2M++, SDSS, and BOSS. Obtaining initial conditions for a given set of galaxy count data allows for running precise counter factual tests with complementary data sets, such as CMB, galaxy SED emissions or X-ray observations. In return, these tests inform us on the physics required to run accurate cosmological inference at small scales. To perform the inference of initial conditions at scale and with high resolution, the BORG Manticore runs successfully implemented a novel staggered grid-splitting framework. This approach allows for tiling large cosmological volumes and performing massively parallel, out-of-core inferences distributed across multiple supercomputing centers in Europe and the US. This innovative design concept significantly enhanced the resolution and volume of field-level inferences, enabling us, for the first time, to infer the 3D cosmic initial conditions over an unprecedented volume of $$\sim(4 h^{-1}~\mathrm{Gpc})^3$$ at a resolution of 8$$h^{-1}$$~Mpc and 4$$h^{-1}$$~Mpc, resulting in a more than billion dimensional parameter inference.
Manticore provides a complete Bayesian posterior distribution over 3D initial density fields for two different cosmologies: Planck 2018 and DES. The project includes a thorough validation strategy with numerical posterior simulations to confirm the physical validity of initial conditions, halo masses, their mass functions, and cosmological summary statistics. We validated the accurate recovery of the spatial distribution and masses of clusters in the nearby universe, outperforming the state-of-the-art constrained simulations by the CLUES collaboration according to their metrics {% cite Pfeifer:2023 %}. These results extend to the full recovered volume, as tested through cross-correlation of inferred cosmic large-scale structures with the Planck Cosmic Microwave Background lensing signal.
We have achieved our first milestone with the publication of Manticore-Local initial conditions {% cite McAlpine:2024 %}. This has already been used in a new upcoming paper where we identify and produce a catalog of highly significant cosmic voids {% cite Malandrino:2025 %} (details available on https://voids.cosmictwin.org).
We are currently preparing inference results at even larger scales with the Manticore-Main, which will fold in data from SDSS (including BOSS), 2dFGRS, 2MRS, 6dFGRS and 2M++ {% cite Jasche:2025 %}.


