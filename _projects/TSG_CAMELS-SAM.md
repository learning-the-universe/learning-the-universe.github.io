---
layout: page
title: CAMELS-SAM
description: Simulation suites with semi-analytic models
img:
importance: 1
category: Training Sets
related_publications: false
---

CAMELS-SAM combines larger $$ (100\,\mathrm{Mpc}/h)^3 $$ volume dark matter-only simulations with the Santa Cruz Semi-Analytic Model (SC-SAM) to investigate how both cosmology and galaxy formation physics shape galaxy properties. The simulations cover a wide range of cosmological parameters, varying the matter density ($$\Omega_\mathrm{M}$$) from 0.1 to 0.5 and the amplitude of matter fluctuations ($$\sigma_8$$) from 0.6 to 1.0. These are post-processed with SC-SAM, which models baryonic processes such as supernova and AGN feedback.

The current public version of CAMELS-SAM varies two modes of supernova feedback—one controlling the reheating of cold gas in galaxies, and the other driving large-scale galactic winds—as well as a parameter regulating AGN-driven gas ejection via radio jets. To efficiently sample the combined space of cosmological and astrophysical parameters, we generate 1000 simulations using Latin Hypercube sampling. This allows us to systematically study how different physical processes shape observable galaxy properties across a wide cosmological and astrophysical parameter space.

Ongoing expansions to CAMELS-SAM for the “Learning the Universe: Connections” project (link!) are adding several more astrophysical parameters, stored star formation histories, and post-processing with Synthesizer for photometry for all galaxies across the Latin Hypercube.
