---
layout: page
title: Synthetic Galaxies
description: Mock Galaxy observations
img:
importance: 1
category: Synthetic Observations
related_publications: true
---

We have constructed an efficient, flexible pipeline to compute synthetic galaxy spectral energy distributions (SED) and broad band photometry from simulated star formation histories (https://github.com/flaresimulations/synthesizer). This tool has been applied to several thousand of the CAMELS hydro simulations and the mock photometry is providing a valuable data product for project development. We developed and validated a technique to compress simulated star formation histories, which enables a factor of several hundred reduction in data volume while retaining acceptable precision in the target photometric quantities.  This proved essential in order to store star formation histories for our test suite of thousands of larger volume ((150/h)$$^3$$) CAMELS-SAM semi-analytic simulations. We have carried out radiative transfer post-processing on the IllustrisTNG50 simulation in order to study and characterize the impact of dust attenuation on galaxy SEDs. We have created a parameterized physics-based analytic model for dust attenuation informed by these results, which has been incorporated into the mock photometry pipeline and will form the basis of a publication to be submitted in the early Fall 2024. We are exploring how well we can constrain the parameters of the dust model using our general purpose LtU Implicit Likelihood Inference pipeline, as well as the impact of marginalizing over dust parameters when constraining cosmological parameters.  Additionally, we have built tools to extract SDSS-like mock lightcones from standard cubical simulation boxes, and compiled a curated database of observations that can be used to calibrate and validate our new simulation suites. 
