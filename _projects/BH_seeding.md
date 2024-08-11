---
layout: page
title: BH seeding
description: A subgrid model for BH seeding
img:
importance: 1
category: Black Holes
related_publications: true
---

The origin of supermassive black holes (SMBHs) remains a mystery.  Theories predict a wide range of initial masses for SMBHs, ranging from $$\sim 100 M_{\odot}$$ (the remnants of early, massive stars), to $$\sim 10^3 - 10^4 M_{\odot}$$ (dynamical evolution in dense star clusters), to $$\sim 10^5 M_{\odot}$$ (the direct collapse of massive gas clouds).  
Large-scale cosmological simulations are unable to resolve these mass scales and simplifying approximations are made about seeding SMBHs, typically by placing $$\approx 10^6 M_{\odot}$$ collisionless particles to represent SMBHs, once a galaxy halo exceeds a mass scale that is resolved.  
This limits the ability of cosmological simulations to study scaling relationships between galaxy properties and SMBH masses at the low mass end of the mass function, and also makes it impossible to test various models for the origin of SMBHs.  
Together with Aklant Bhowmick and Laura Blecha (Univ. of Florida), We have recently developed and implemented a new sub-grid model to seed SMBHs in cosmological simulations {% cite Bhowmick2024 %}.  In this approach, extremely high resolution simulations are employed, which can resolve the sites of SMBH formation, and that are then evolved to lower redshifts allowing these black holes to grow by accretion and mergers.  
The resulting population predicts a probability distribution for SMBHs that can be sampled and used to populate lower resolution cosmological simulations with SMBH seeds.  
This will enable direct testing of the various models proposed for the origin of SMBHs.
