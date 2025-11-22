---
layout: post
title: Lyapunov Spectrum for Invertible Maps
date: 2011-03-21T20:41:12-05:00
excerpt: Python code to calculate the Lyapunov Spectrum for maps using the method proposed by Wolf et al. involving Gram-Schmidt reorthonormalization.
permalink: 2011/03/lyapunov-spectrum-for-invertible-maps/
tags:
  - Invertible Maps
  - Lyapunov Spectrum
  - Python
---
Python code to calculate the Lyapunov Spectrum for maps using the method proposed by Wolf et al. involving Gram-Schmidt reorthonormalization.

This code was tested on several invertible maps: Henon Map, Delayed Logistic Map, Burger Map, and Tinkerbell Map. The code is adaptable for other maps, though more complex maps have not been tested. One problem that I had with producing and testing the code was linearizing the maps, this can be done by following the fairly straight-forward procedure in Wolf et al. on Page 291 and 292 for the Henon map. If you use this code, please let me know, I would be interested in learning about how you used it.

Adapted strongly from [WOLFMAP.BAS](http://sprott.physics.wisc.edu/chaos/wolfmap.bas) and based on research by Wolf et al. [Determining Lyapunov Exponents from a Time Series](https://venturi.soe.ucsc.edu/sites/default/files/Lyapunov_exponents.pdf)

See the Code: [le-spectrum-map.py](/assets/posts/2011-03-21-lyapunov-spectrum-for-invertible-maps/le-spectrum-map.py)