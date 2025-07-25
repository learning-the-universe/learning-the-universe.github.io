---
layout: page
title: Synthesizer + CAMELS
description: CAMELS & CAMELS-SAM photometry
img: assets/img/CAMELS_LFs.png
importance: 1
category: Synthetic Observations
related_publications: true
---

[Synthesizer](https://synthesizer-project.github.io/synthesizer/) is a modular and efficient pipeline for generating synthetic galaxy spectral energy distributions (SEDs), photometry, and emission-line properties from simulated star formation histories. The tool supports a wide range of models and outputs, including stellar and AGN emission, photoionization, attenuation, and data cubes. It is publicly available at github.com/synthesizer-project/synthesizer.

Synthesizer has been applied to several thousand CAMELS simulations—including suites using TNG, SIMBA, Astrid, and Swift-EAGLE—using Bruzual \& Charlot (2003) and BPASS stellar population synthesis models, along with Charlot \& Fall (2000) dust attenuation. It produces observer-frame fluxes and luminosities for over 142 million galaxies across 34 snapshots (from $$z=0$$ to $$z=6$$), spanning filters from FUV to JWST/NIRCam.

In parallel, we have also developed tools to extract SDSS-like mock lightcones from standard simulation volumes and compiled a curated observational database to support calibration and validation of next-generation simulation suites.

Photometry for CAMELS-SAM galaxies is also being generated using Synthesizer, leveraging the stored star formation histories from the SC-SAM outputs. This enables efficient and scalable computation of broadband fluxes across the full CAMELS-SAM parameter space. The resulting synthetic photometry provides a key bridge between model predictions and upcoming survey data, and supports targeted analyses of parameter sensitivities in galaxy SEDs.

Data is available at: [https://camels.readthedocs.io/en/latest/photometry.html](https://camels.readthedocs.io/en/latest/photometry.html)