---
layout: page
title: COmoving Computer Acceleration (COCA)
description: N-body simulations in an emulated frame of reference
img:
importance: 1
category: Accelerated Forward Models
related_publications: true
---

N-body simulations, widely used for studying complex systems such as gravitational structure formation, are computationally intensive. To address this, machine learning (ML)-based emulators have been developed to speed up the process. While they offer significant gains in efficiency, these emulators face issues with accuracy and trustworthiness, as they can introduce substantial errors that current methods are unable to correct.

One of the main challenges in using ML for N-body simulations is the inability to reliably detect or correct emulation errors in real-world scenarios, where no ground-truth data is available for comparison. Although perfect accuracy may not always be necessary – given that traditional simulations also make simplifying assumptions – the lack of interpretability in many ML models, especially deep neural networks, makes it difficult to assess the reliability of the results.

To address these concerns, we propose a framework {% cite Bartlett:2024 %} that enhances the trustworthiness of ML emulators by incorporating physical corrections for emulation errors. Rather than aiming for perfect ML predictions, our approach focuses on refining the approximate solutions provided by ML. This allows users to control the trade-off between speed and accuracy by adjusting the number and timing of force evaluations in the simulation. With more evaluations, the system asymptotically converges to the true physical solution, ensuring a balance between efficiency and reliability.

Tested on particle-mesh cosmological simulations, COCA reduces errors and requires fewer evaluations, providing accurate density and velocity fields. COCA outperforms direct emulation in accuracy and robustness, even beyond training data.

<div class="row">
    <div class="col-sm">
        {% include figure.liquid loading="eager" path="assets/img/COCA.jpeg" title="COCA" %}
    </div>
</div>
