---
layout: page
title: Galaxy Inference from Photometry
description: Inference of cosmological and astrophysical parameters from galaxy photometry
img:
importance: 1
category: Synthetic Observations
related_publications: true
---

We perform the first direct inference of cosmological and astrophysical parameters using galaxy luminosity functions and colours via simulation-based (likelihood-free) inference. Leveraging synthetic photometry from thousands of CAMELS hydrodynamical simulations—including Swift-EAGLE, IllustrisTNG, SIMBA, and Astrid—we compile luminosity functions and colour distributions at $$z=0.1$$ and demonstrate their sensitivity to both cosmological parameters and feedback physics. {% cite lovell2024learninguniversecosmologicalastrophysical %}

We apply the LtU Implicit Likelihood Inference (ILI) framework {% cite 2024arXiv240205137H %}, using an ensemble of neural spline flow models to perform Neural Posterior Estimation (NPE). Our results show that both colour distributions and luminosity functions provide complementary constraints, and we notably recover tight constraints on $$\Omega_M$$ and $$\sigma_8$$ using only integrated galaxy photometry—without relying on spatial clustering information. Looking ahead, we are developing new inference runs that incorporate our physically motivated dust attenuation model, enabling a more realistic treatment of galaxy colours and their connection to cosmology.