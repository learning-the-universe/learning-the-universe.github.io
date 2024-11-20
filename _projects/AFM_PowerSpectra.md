---
layout: page
title: Power Spectrum Emulators
description: Power Spectrum Emulators
img:
importance: 1
category: Accelerated Forward Models
related_publications: true
---

This year saw the completion of a wide range of dark matter accelerated forward models, learning from numerical training sets and enabling the advanced inference techniques employed by the collaboration. This included an exceptionally precise learned symbolic emulator for the linear power spectrum {% cite 2024A&A...686A.209B %} and for the non-linear power spectrum {% cite 2024A&A...686A.150B %} (SYREN-HALOFIT). These emulators not only cover the <span>&Lambda;</span>CDM model, but include the effects of massive neutrinos and dynamical dark energy {% cite 2024arXiv241014623S %} (SYREN-NEW).

These tools provide symbolic regression-based emulators designed to provide rapid and precise calculations of the matter power spectrum <span>P(k)</span> for large-scale structure surveys. Such predictions are crucial for efficiently constraining the neutrino mass and the equation of state of dark energy, both of which are important for current and future cosmological analyses. 

By leveraging symbolic regression, the SYREN suite generates simple and interpretable analytic approximations for both the linear and nonlinear matter power spectra, as well as for the derived parameter <span>&sigma;<sub>8</sub></span>. These approximations match the accuracy of leading numerical emulators while being orders of magnitude faster, significantly improving the efficiency of cosmological simulations.

### Key features of SYREN-NEW include:
- **High Accuracy**: Achieves root mean squared errors of 0.1%, 0.3%, and 1.3% for <span>&sigma;<sub>8</sub></span>, the linear and nonlinear power spectra, respectively, across a wide range of cosmological parameters, redshifts, and wavenumbers.
- **Improved Efficiency**: At least 10 times faster than traditional numerical emulators on both CPUs and GPUs, making it ideal for large-scale data analyses.
- **Transparency and Interpretability**: Unlike black-box models, SYREN-NEW provides clear, symbolic expressions that are easily interpretable, enhancing the understanding of the underlying physical processes.

SYREN-NEW offers a powerful tool for modern cosmological research, enabling faster, more accurate simulations with full transparency. Publicly available [code](https://github.com/DeaglanBartlett/symbolic_pofk/) ensures that these advancements are accessible for researchers in the field.


<div class="row">
    <div class="col-sm">
        {% include figure.liquid loading="eager" path="assets/img/syren-new-performance.jpg" title="SYREN-NEW performance" %}
    </div>
</div>