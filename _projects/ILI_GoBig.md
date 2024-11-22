---
layout: page
title: SDSS-CMASS Cosmological Analysis
description: Accelerated cosmological inference with the SDSS-CMASS galaxy sample
img: assets/img/cmass-icon.jpg
importance: 2
category: Implicit Inference
related_publications: false
---


We are currently developing the flagship LtU cosmological analysis using the CMASS spectroscopic galaxy sample from the Sloan Digital Sky Survey (SDSS). Spectroscopic galaxy observations are crucial for cosmological studies, as they probe the clustering of galaxies, which in turn helps us understand the nature of dark matter, dark energy, and the conditions of the early universe.



<div style="text-align: center;">
    {% include figure.liquid loading="eager" path="assets/img/cmass-pipeline.jpg" title="CMASS Pipeline" width="70%" %}
</div>



To analyze this data, we have developed a modular simulation pipeline that can rapidly generate mock galaxy catalogs for the CMASS sample. This pipeline, incorporating tools from the AFM, Robustness, and SynthObs groups, enables the application of Implicit Likelihood Inference (ILI) techniques to infer cosmological parameters from real data. This effort represents the largest use of ILI for a spectroscopic galaxy survey to date, and it is the first to use accelerated forward models to emulate full N-body simulations, making it a more efficient approach for handling the complexity of cosmological data.

By applying these ILI techniques, we aim to further refine statistical methods in cosmology and contribute to the development of analysis frameworks for future astronomical surveys. 