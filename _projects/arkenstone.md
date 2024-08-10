---
layout: page
title: Arkenstone
description: A subgrid model for hot and cool galactic winds
img:
importance: 1
category: Star Formation
related_publications: true
---

Arkenstone is a new model for multiphase, stellar feedback driven galactic winds designed for inclusion in coarse resolution cosmological simulations. The method has two parts: one that can properly treat high specific energy wind components and a second that follows small, dense, cool clumps as they exchange mass, momentum, and energy with the hot medium. The method is implemented in the Arepo code. 
Hot, fast gas phases with low mass loadings are predicted to dominate the energy content of multiphase outflows. In order to treat the huge dynamic range of spatial scales involved in cosmological galaxy formation at feasible computational expense, cosmological volume simulations typically employ a Lagrangian code or else use adaptive mesh refinement with a quasi-Lagrangian refinement strategy. However, it is difficult to inject a high specific energy wind in a Lagrangian scheme without incurring artificial burstiness. Additionally, the low densities inherent to this type of flow result in poor spatial resolution. Arkenstone addresses these issues with a novel scheme for coupling energy into the transition region between the interstellar medium (ISM) and the CGM, while also providing the necessary level of refinement at the base of the wind.

The theoretical framework for this project was described in
\cite{fb2022}; the implementation of the high-specific energy winds
was described in Paper I \cite{ArkenstoneI} with a description of the
cool clouds in Paper II (Smith et al, in prep).

<div class="row">
    <div class="col-sm">
        {% include figure.liquid loading="eager" path="assets/img/arkenstone_schematic.jpg" title="BH jet" %}
    </div>
</div>

