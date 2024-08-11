---
layout: page
title: Multizoom ICs
description: Multizoom Cosmological Initial Conditions
img:
importance: 1
category: Cosmology
related_publications: false
---

Prompted by the need to efficiently study representative samples of galaxies at very high resolution in hydrodynamical cosmological simulations, we have developed a novel initial conditions pipeline that realizes an innovative solution to this problem. While the so-called zoom technique has long been established in the field as a basic approach to simulate the formation of individual galaxies within the correct cosmological embedding, the construction of suitable initial conditions for this has been a protracted and elaborate procedure. In addition, building up large samples of simulated galaxies or halos in this way required the tedious repetition of the needed steps and the systematic execution of a large number of individual simulations, making this process too cumbersome for widespread application. Our new approach has generalized our N-GenIC code, based on 2nd order Lagrangian perturbation theory, by inlining it directly into the simulation code AREPO and outfitting it with the ground breaking feature to produce combined high-quality zoom initial conditions for an arbitrary selection of target halos from a parent dark matter halo simulation, within a single simulation. This allows the computation of high-resolution predictions for the galaxy sample in a single simulation without any special preparation steps. This is not only more efficient computationally (as the low-resolution background has to be evolved only once instead of repeatedly) and allows much faster turn-around times, it also facilitates a subsampling of the full galaxy mass function for high-resolution simulation in such a way that the results can be subsequently upscaled to yield statistically reliable predictions for large cosmological volumes.
