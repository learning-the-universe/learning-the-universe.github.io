---
layout: page
title: Massive Zooms CAMELS-GZ28
description: Zoom-in simulations of massive halos
img:
importance: 1
category: Training Sets
related_publications: true
---

Creating accelerated models of the systems that produce the observable signals the collaboration is targeting for cosmological information extraction, such as SDSS galaxies and tSZ surveys, requires large training sets of massive halos in the regime of galaxy groups. These training sets should ideally be based on the most accurate and sophisticated methods for cosmological modeling, namely hydrodynamical simulations, but obtaining such rare massive halos with standard cosmological simulations requires prohibitively large computations, therefore necessitating the use of focused zoom-in simulations. The simulations should also span large physical model parameter spaces, in order to facilitate robustness and applicability to real observations. We have made groundbreaking progress in this direction by generating CAMELS-GZ28, a suite of 768 zoom-in cosmological hydrodynamical simulations of group-scale halos that sample a 28-dimensional parameter space of the TNG galaxy formation model {% cite lee2024camelsgz28 %}. Using the novel CARPoolGP emulator, sample (cosmic) variance was suppressed by a factor of $$\sim10$$ compared to a naive sampling and emulation approach, increasing the accuracy of the emulator per given computational cost. The initial study produced an emulator for the integrated tSZ signal as a function of model parameters and halo mass, and upcoming follow-up studies (Hernandez in prep.~and Lau et al., in prep.) extend this to emulations of radial profiles of various thermodynamic properties, which can all be plugged in to accelerated modeling pipelines.
