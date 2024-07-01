---
layout: about
title: about
permalink: /
subtitle: <a href='https://www.simonsfoundation.org/'>Simons Foundation</a>. 

profile:
  align: right
  image: icon.jpg
  image_circular: true # crops the image to make it circular
  address: >
    <p><center>Initial Conditions</center></p>
   

news: true  # includes a list of news items
latest_posts: false  # includes a list of the newest posts
selected_papers: true # includes a list of papers marked as "selected={true}"
social: true  # includes social icons at the bottom of the page
---

The evolution of our Universe is determined by its initial conditions and the physical laws that govern it. However, neither of these are open to direct determination, but must be inferred from observations. This collaboration plans to carry out this inference using a Bayesian forward modeling approach, where we repeatedly sample a set of initial conditions, predict the observational consequences of that choice, compare to the real observations of galaxies and gas, and compute the likelihood, either explicitly or implicitly, thereby constructing the posterior distribution of the initial conditions. In practice, this is an extremely challenging endeavor because galaxy formation simulations are costly and still only incompletely understood. Furthermore, the dimensionality of the initial parameter space is enormous so standard inference techniques fail.

To address these challenges, we will employ a three-pronged approach. First, we will develop improved galaxy formation simulations using novel sub-grid models for the influence of stars and black holes. The new models will be built on knowledge gained from detailed, high-resolution simulations of individual star forming regions or accreting black holes that resolve the relevant physical processes. These improved sub-grid models will be implemented in cosmological simulations and can be used to make direct observational predictions for a significant (but still limited) number of samples of initial conditions. Second, the collaboration will use the emerging power of machine learning, which can speed up the forward modeling by factors of millions or billions by training on the relatively small samples of full simulations produced in the first step. Third, we will develop and enhance fast, physically-motivated, neural-net likelihood, simulation-based or likelihood-free inference techniques that have the potential to fully exploit the enormous amount of information from upcoming observational surveys. By harnessing this pending explosion of data, we anticipate generating posterior distributions of not just the cosmological parameters, but the initial conditions and even the uncertain astrophysical parameters.
