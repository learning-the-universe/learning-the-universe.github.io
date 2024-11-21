---
layout: page
title: "Cosmic Graphs: the Language of Large-Scale Structure"
description: how much information is locked inside halo catalogues?
img:
importance: 1
category: Implicit Inference
related_publications: true
---

*With Tom Charnock, Pablo Lemos, Natalia Porqueres, Alan Heavens, & Ben Wandelt*

<figure class="align-center">
<p align="center">
  <img src="https://media4.giphy.com/media/b8ICuMdjg37vQNjwTA/giphy.gif?cid=790b7611da6738a8551bc2d92f2eb821b6d853092aa22ca9&rid=giphy.gif" alt="dark matter graph" style="width:70%" zoomable=true>
      </p>
  <figcaption align = "center"> </figcaption>
</figure>


<br/>
<div style="display: block; margin-left: auto; margin-right: auto; width:100%; text-align:center;">
  <a href="https://arxiv.org/abs/2207.05202" class="btn btn--primary">read the paper</a> 
  <a href="https://tlmakinen.github.io/blog/2022/cosmicgraphs/" class="btn btn--primary">blog post</a> 
  <a href="https://bit.ly/cosmicGraphsColab" class="btn btn--primary">
  <i class="fab fa-google fa-inverse"></i> run in browser  </a> 
</div> <br/>

The cosmic web, or Large-Scale Structure (LSS) is the massive spiderweb-like arrangement of galaxy clusters and the dark matter holding them together under gravity. The lumpy, spindly universe we see today evolved from a much smoother, infant universe. How this structure formed and the information embedded within is considered one of the "Holy Grails" of modern cosmology, and might hold the key to resolving existing "tensions" in cosmological theory.

But how do we go about linking this data to theory ? In this project, we proposed to look at LSS assembled as a *graph*, and use neural networks to optimally extract information about cosmological parameters (theory) from this representation.


Graphs provide a natural language with which to describe the cosmic web. Dark matter halos are attributed
to nodes (vertices), while filaments are traced by smaller
halos and edges. In this representation, clustering under gravitational interactions can
be translated into higher edge cardinality (number of
edges). Higher order n-point functions can be computed
efficiently for clusters, while avoiding the cost of computing extraneous connections across voids. Void catalogues
(where edges would correspond to the walls separating
the voids) can likewise be assembled into the dual of a
halo graph. Graph construction also allows extra information, such as the halo masses, to be added in the form
of node and edge labels, unlike correlation functions.

