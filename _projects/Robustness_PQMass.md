---
layout: page
title: PQMass
description: Assessing quality of generative models
img:
importance: 1
category: Robustness
related_publications: true
---

We have developed a likelihood-free, sample-based method for assessing the quality of generative models. The proposed approach, PQMass, enables the estimation of the probability that two sets of samples are drawn from the same distribution, providing a statistically rigorous method for assessing the performance of a single generative model or the comparison of multiple competing models trained on the same dataset. This comparison can be conducted by dividing the space into non-overlapping regions and comparing the number of data samples in each region. The method only requires samples from the generative model and the test data. Since it can be applied directly to high-dimensional data, it obviates the need for dimensionality reduction typically required in quality assessment metrics. Significantly, PQMass does not depend on assumptions regarding the density of the true distribution or rely on training or fitting any auxiliary models, but instead examines the integral of the density (probability mass) over sub-regions of the data space. More specifically, it is akin to a chi-squared test that captures the probability that two sets of samples are drawn from the same underlying distribution, after marginalizing over the unknown distribution itself. This paper was submitted to NeurIPS 2024 (2402.04355). This will be an indispensable tool to quantify the quality of generative models trained, as we have shown that given any generative model or any sampling distribution, if two sets are sampled from the same distribution, then the PQMass values will be chi2 distributed. This has been made available to the community through a pip-installable package available at https://github.com/Ciela-Institute/PQM
