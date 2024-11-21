---
layout: page
title: PRFM
description: A subgrid model for star formation and effective equation of state
img:
importance: 1
category: Star Formation
related_publications: true
---

This year saw completion of an extensive simulation study calibrating the parameters in our pressure-regulated, feedback-modulated (PRFM) star formation rate (SFR) theory covering a wide range of galactic environments {% cite Kimetal2024 %} and {% cite 2023ApJS..264...10K %}.
The survey employed the TIGRESS numerical framework and provides fits for feedback yield (used in the SFR prediction) and effective velocity dispersion (equivalent to an equation of state, EOS) ; these are chosen as calibration variables because they can be robustly measured in cosmological simulations even at coarse resolution.
We submitted a paper {% cite Jeffreson2024 %} presenting results from global galaxy simulations of both disk- and bulge-dominated systems using the GalactISM framework; these global simulations were used to validate the PRFM theory hypotheses (thermal and vertical dynamical equilibrium) and extend subgrid model calibrations.
We also submitted a paper {% cite Hassan2024 %} in which we post-processed outputs from the IllustrisTNG cosmological simulations to compare the native-TNG SFRs with PRFM predictions, also assessing what cosmological resolution is required for employing the PRFM-resolved vs. the PRFM-unresolved subgrid model formulation for setting the SFR.
We explored the impact of this model on cosmological simulations in a post-processing approximation {% cite Hassan2024 %}.
Because the PRFM model has higher star formation efficiency (SFE) at higher density and pressure while the native-TNG model has nearly constant SFE, we expect implementation of the PRFM SFR model in next-generation LtU cosmological simulations will lead to significant enhancements of star formation at high redshift, consistent with recent JWST observations.
We have also worked with the Cosmological Modeling Working Group to implement the PRFM-resolved subgrid model, and we have been testing an implementation of PRFM-unresolved in isolated galaxies.

{% include figure.liquid loading="eager" path="assets/img/LtU-TIGRESS_NCR_LGR4.png" title="tigress ncr" %}
