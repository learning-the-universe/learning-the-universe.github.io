---
layout: page
title: MilleniumTNG WL
description: A large scale cosmological simulation - ray tracing weak lensing
img:
importance: 1
category: Cosmology
related_publications: true
---

We produced very high resolution, all-sky weak gravitational lensing convergence maps for the MillenniumTNG simulations based on projections of the evolving mass distribution on the past backwards lightcone of a fiducial observer {% cite Ferlito:2023 %}. By comparing full physics hydrodynamical simulations with corresponding dark-matter-only runs, we could quantify the impact of baryonic physics on the most important weak lensing statistics. Likewise, we were able to predict the impact of massive neutrinos reliably far into the non-linear regime. We also demonstrated that the fixed & paired variance suppression technique increases the statistical robustness of the simulation predictions on large scales not only for time slices but also for continuously output lightcone data. We showed that both baryonic and neutrino effects substantially impact weak lensing shear measurements, with the latter dominating over the former on large angular scales. We have also developed a new full-sky ray-tracing scheme and applied it to the MillenniumTNG simulation suite {% cite Ferlito:2024 %}, allowing us to critically assess the accuracy of the much simpler Born approximation that is commonly employed in weak lensing studies. In this context we also introduced an interpolation technique based on non-uniform fast Fourier transforms on the unit sphere that avoids smoothing effects inherent in lower-order approaches such as bilinear interpolation. We could demontrate that the differences between the Born approximation and a full ray-tracing treatment are negligibly small at the power-spectrum level, but that some higher order statistics show more sizable effects that indicate that ray-tracing is necessary to achieve percent level precision.
