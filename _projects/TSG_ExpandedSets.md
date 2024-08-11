---
layout: page
title: Expanded Training Sets
description: Training sets with expanded sub-grid parameter spaces
img:
importance: 1
category: Training Sets
related_publications: false
---

In order to achieve robustness and avoid the risk of model mis-specification during Implicit Likelihood Inference, it is crucial for training sets to cover large model parameter spaces. We made two significant advances in this direction over the past year. First, we generated a new large training set based on 25$$h^{-1}$$ Mpc volumes that uses the EAGLE galaxy formation model, thereby substantially increasing the range of community flagship subgrid frameworks based on which emulators and inference machines can be trained (Lovell et al., in prep.). Second, we are near completion of a new implementation of the SIMBA subgrid framework in the Arepo code that will allow a smooth, tunable transition between the SIMBA and TNG frameworks in the model parameter space itself, rather than in the results space (Garcia et al., in prep.). This novel approach, and the upcoming large training set we will generate based on it, will allow testing and pushing the limits of our inference machines and robustness tools.

