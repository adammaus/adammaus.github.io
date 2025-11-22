---
layout: post
title: Inverted Delayed Henon Map
date: 2011-04-09T08:01:37-05:00
excerpt: Inverting the delayed Henon map yields a repellor whose sensitivities can be explored.
permalink: 2011/04/inverted-delayed-henon-map/
tags:
  - Chaos
  - Delayed Henon Map
  - Henon Map
  - Invertible Maps
  - Sensitivities
  - Time Series
---
The delayed Henon map:

![x_t = 1 - 1.6x_{t-1}^2 + 0.1y_{t-d}](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-1.png)
{:.max-width-50-percent}

offers insight into the high-dimensional dynamics through its adjustable _d_ parameter. In the previous post, [Delayed Henon Map Sensitivities](/2011/04/delayed-henon-map-sensitivities/), we looked at the sensitivity of the output to perturbations in each of the time lags of this map using partial derivatives. Since this function is known, it is simple to determine the lag space as well as the embedding dimension for the system. However, as we will see later, we can use this method to find the lag space and embedding dimension for unknown systems using artificial neural networks. Some interesting questions arise when you analyze neural networks trained on the delayed Henon map and its inverted counterpart so we will first look at the inverted delayed Henon map.

The delayed henon map can be inverted quite easily by separating the time delayed form into two equations such as the following:

![x_t = 1 - 1.6x_{t-1}^2 + 0.1y_{t-1}](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-2.png)
{:.max-width-50-percent}

![y_t = x_{t-d}](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-3.png)
{:.max-width-50-percent}

After a little algebra, you get:

![x_{t-d} = y_t](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-4.png)
{:.max-width-50-percent}

![y_t = 10x_t + 16x_{t-1}^2 - 10](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-5.png)
{:.max-width-50-percent}

Finally, we replace **x** with **y** to obtain the inverted map,

![y_t = 10y_{t+d} + 16y_{t+d-1}^2 - 10](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-6.png)
{:.max-width-50-percent}

After inversion, the map becomes a repellor and any initial condition on the original attractor will wander off to infinity. Since we cannot directly estimate the sensitivities from this function we can calculate a time series from the righted delayed Henon map and feed that data into the partial derivative equations of the inverted delayed Henon map. Using this process on 10,000 points from the righted delayed Henon map (the first 1,000 points removed) we obtain the following sensitivities,

![\frac\{\partial y_t\}\{\partial y_\{t+d-1\}\}=\|32y_\{t+d-1\}\|=18.9795](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-7.png)
{:.max-width-50-percent}

![\partial y_t/\partial y_{t+d} = \|10\|](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-8.png)
{:.max-width-50-percent}

Here are a few other maps, their sensitivities, their inverted equations, and those sensitivities:

**Original Henon map [1]**

![Graph of Henon map strange attractor](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-9.png)
{:.max-width-50-percent}

Equation

![x_t = 1 - 1.4x_{t-1}^2 + 0.3x_{t-2}](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-10.png)
{:.max-width-50-percent}

Sensitivities

![\partial x_t/\partial x_{t-1} = \|-2.8x_{t-1}\| = 1.8931](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-11.png)
{:.max-width-50-percent}

![\frac{\partial x_t}{\partial x_{t-2}}=\|.3\|](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-12.png)
{:.max-width-50-percent}

Inverted Equation

![y_t = -3 + 4.2y_{t+1}^2 + 3y_{t+2}](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-13.png)
{:.max-width-50-percent}

Inverted Sensitivities

![\frac{\partial y_t}{\partial y_{t+1}} = \|8.4y_{t+1}\| = 5.6795](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-14.png)
{:.max-width-50-percent}

![\frac{\partial y_t}{\partial y_{t+2}} = \|3\|](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-15.png)
{:.max-width-50-percent}

**Discrete map from preface of Ref. #2**

![Discrete map strange attractor](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-16.png)
{:.max-width-50-percent}

Equation

![x_t = x_{t-1}^2 - 0.2x_{t-1} - 0.9x_{t-2} + 0.6x_{t-2}](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-17.png)
{:.max-width-50-percent}

Sensitivities

![\frac{\partial x_t}{\partial x_{t-1}}=\|2x_{t-1}-.2\|=1.1598](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-18.png)
{:.max-width-50-percent}

![\frac{\partial x_t}{\partial x_{t-2}}=\|-.9\|](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-19.png)
{:.max-width-50-percent}

![\frac{\partial x_t}{\partial x_{t-3}}=\|.6\|](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-20.png)
{:.max-width-50-percent}

Inverted Equation

![y_t = 5.4y_{t+1} - 6y_{t+2}^2 + 1.2y_{t+2} + 6y_{t+3}](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-21.png)
{:.max-width-50-percent}

Inverted Sensitivities

![\frac{\partial y_t}{\partial y_{t+1}}=\|5.4\|](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-22.png)
{:.max-width-50-percent}

![\frac{\partial y_t}{\partial y_{t+2}}=\|-12y_{t+2}+1.2\|=6.9588](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-23.png)
{:.max-width-50-percent}

![\frac{\partial y_t}{\partial y_{t+3}}=\|6\|](/assets/posts/2011-04-09-inverted-delayed-henon-map/image-24.png)
{:.max-width-50-percent}

References:

1. Henon M. A two-dimensional mapping with a strange attractor. Commun Math Phys 1976;50:69–77.
2. Sprott JC. Chaos and time-series analysis. New York: Oxford; 2003.

This post is part of a series:

1. [Delayed Henon Map Sensitivities](/2011/04/delayed-henon-map-sensitivities/)
2. Inverted Delayed Henon Map
3. [Modeling Sensitivity using Neural Networks](/2011/04/modeling-sensitivity-using-neural-networks/)