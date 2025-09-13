---
layout: page
title: MIEST
description: Model-Insensitive ESTimator
img:
importance: 1
category: Robustness
related_publications: true
---

The rapid advancement of large-scale cosmological simulations has opened new avenues for cosmological and astrophysical research. 
However, the increasing diversity among cosmological simulation models presents a challenge to the _robustness_.
In this work, we develop the Model-Insensitive ESTimator (MIEST), a machine that can _robustly_ estimate the cosmological parameters, $\Omega_m$ and $\sigma_8$, from neural hydrogen maps of simulation models in the CAMELS project-IllustrisTNG, Simba, Astrid, and Eagle.
An estimator is considered _robust_ if it possesses a consistent predictive power across all simulations, including those used during the training phase.
We train our machine using multiple simulation models and ensure that it only extracts common features between the models while disregarding the model-specific features. 
This allows us to develop a novel model that is capable of accurately estimating parameters across a range of simulation models, without being biased towards any particular model.
Upon the investigation of the latent space-a set of summary statistics, we find that the implementation of _robustness_ leads to the blending of latent variables across different models, demonstrating the removal of model-specific features.
In comparison to a standard machine lacking _robustness_, the average performance of MIEST on the unseen simulations during the training phase has been improved by $\sim 17\%$ for $\Omega_m$ and $38\%$ for $\sigma_8$.
By using a machine learning approach that can extract _robust_, yet physical features, we hope to improve our understanding of galaxy formation and evolution in a (subgrid) model-insensitive manner, and ultimately, gain insight into the underlying physical processes responsible for _robustness_.
{% cite 2025arXiv250213239J %}.
