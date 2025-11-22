---
layout: post
title: Delayed Henon Map Sensitivities
date: 2011-04-02T21:57:27-05:00
excerpt: Partial derivatives can be used to explore how sensitive the output of a function is to perturbations in each of the time lags.
permalink: 2011/04/delayed-henon-map-sensitivities/
tags:
  - Delayed Henon Map
  - Invertible Maps
  - Sensitivities
  - Time Series
---
What previous days' weather affected today's weather? Historically, which states' votes affected the outcome of different presidential elections? How does a single trade affect the price of a stock?

Modelling the weather, politics, and economics would be a very difficult task but we can explore questions like this in less complex mathematical systems such  as the delayed Henon map [1]. The delayed Henon map is a time-delayed system represented by following equation:

![x_{t} =1-1.6x_{t-1}^2+.1x_{t-d}](/assets/posts/2011-04-02-delayed-henon-map-sensitivities/image-1.png)
{:.max-width-50-percent}

Since it has an adjustable _d_ parameter, which represents what dimension the function can be embedded in and provides us with a knob to turn to explore high dimensional dynamics. We can explore many different features about this map, the correlation dimension, fractal dimension, Lyapunov exponents, and much more but our primary focus will be looking at the sensitivities for this map. If you are interested in more information about this map, please consult Sprott 2005, a full reference is below. For the rest of this post, I will be using _d_=4. As we will see, this is more than adequate for the analysis I will show, but one could easily use _d_ = 1456 if they wanted to. Due to the linearity of **x<sub>t-d</sub>**, a different choice of _d_ will arrive at almost the same results.

So, how are the three questions posed above tied together? They all attempt to answer a common question. What is the sensitivity of each time lag in a function of the system [2]?

For the delayed Henon map, this would be akin to asking, how does **x<sub>t-1</sub>, x<sub>t-d</sub>** affect **x<sub>t</sub>**. We can infer this by taking the partial derivative of **x<sub>t</sub>** with respect to each time lag. Using a partial derivative is like asking, if I vary **x<sub>t-1</sub>, x<sub>t-d</sub>** just slightly, how will **x<sub>t</sub>** change. For the obviously non-zero time lags that would be:

![\frac{\partial x_t}{\partial x_{t-1}}=-3.2x_{t-1}](/assets/posts/2011-04-02-delayed-henon-map-sensitivities/image-2.png)
{:.max-width-50-percent}

![\frac{\partial x_t}{\partial x_{t-d}}=.1](/assets/posts/2011-04-02-delayed-henon-map-sensitivities/image-3.png)
{:.max-width-50-percent}

To accurately determine how much the output of the function varies when each time lag is perturbed, we need to find the mean of the absolute values of the partial derivatives around the attractor. Thus we have:

![\frac{\partial x_t}{\partial x_{t-1}}=S(1)=\frac{\sum_{k=d}^{n}\|-3.2x_{t-1}\|}{n-d}](/assets/posts/2011-04-02-delayed-henon-map-sensitivities/image-4.png)
{:.max-width-50-percent}

![\frac{\partial x_t}{\partial x_{t-d}}=S(d)=\frac{\sum_{k=d}^{n}\|.1\|}{n-d}](/assets/posts/2011-04-02-delayed-henon-map-sensitivities/image-5.png)
{:.max-width-50-percent}

Since the delayed Henon map has a chaotic attractor and the values of **x<sub>t</sub>** vary, you can estimate the value of the sensitivities for 10,000 iterations of the time series. Initializing the map with a vector such as [.1, .1, .1, .1], we get the following strange attractor (with the first 1,000 iterations removed):

![Strange Attractor of Delayed Henon Map](/assets/posts/2011-04-02-delayed-henon-map-sensitivities/image-6.png)
{:.centered.max-width-50-percent}

Delayed Henon Map with 9,000 points (<em>d</em>=4)
{:.centered}

<br>
We arrive at the following sensitivities for <em>d</em>=4:

**S(1)=1.8980**

**S(4)=.1**

By estimating a system's sensitivities, we can determine what is known as the lag space [3]. Dimensions with non-zero sensitivities make up this space and the largest dimension with a non-zero sensitivity also determines the embedding dimension. As we will see in another post, a neural network method can be devised to find the lag space of various time series.

References:

1. Sprott JC. High-dimensional dynamics in the delayed Hénon map. Electron J Theory Phys 2006; 3:19–35.
2. Maus A. and Sprott JC. Neural network method for determining embedding dimension of a time series. Comm Nonlinear Science and Numerical Sim 2011; 16:3294-3302.
3. Goutte C. Lag space estimation in time series modelling. In: Werner B, editor. IEEE International Conference on Acoustics, Speech, and SignalProcessing, Munich, 1997, p. 3313.

This post is part of a series:

1. Delayed Henon Map Sensitivities
2. [Inverted Delayed Henon Map](/2011/04/inverted-delayed-henon-map/)
3. [Modeling Sensitivity using Neural Networks](/2011/04/modeling-sensitivity-using-neural-networks/)