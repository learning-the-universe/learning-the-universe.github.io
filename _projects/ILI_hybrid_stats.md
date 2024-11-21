---
layout: page
title: Hybrid Summary Statistics
description: New, Scalable Summaries
img:
importance: 1
category: Implicit Inference
related_publications: true
---




Neural networks can capture an impressive range of patterns in supervised and unsupervised settings. This makes them useful for capturing data features from simulations or training datasets that can be used for highly informative and in some cases optimal simulation-based inference. However, asymptotic optimality often requires both enormous networks and large vats of training data. 

We present a way to capture high-information posteriors from training sets that are sparsely sampled over the parameter space with smaller networks for robust simulation-based inference. In physical inference problems, we can often apply domain knowledge to define traditional summary statistics to capture some of the information in a dataset. We show that augmenting these statistics with neural network outputs to maximise the mutual information improves information extraction compared to neural summaries alone or their concatenation to existing summaries and makes inference robust in settings with low training data.
