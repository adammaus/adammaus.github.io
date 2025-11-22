---
layout: post
title: Modelling Sensitivity using Neural Networks
date: 2011-04-20T21:41:59-05:00
excerpt: Artificial neural networks can be applied to the delayed Henon map and shown to replicate the sensitivities of the map surprisingly well.
permalink: 2011/04/modeling-sensitivity-using-neural-networks/
tags:
  - Chaos
  - Delayed Henon Map
  - Henon Map
  - Invertible Maps
  - Neural Network
  - Sensitivities
  - Time Series
---

Artificial neural networks can be applied to the delayed Henon map[1] and shown to replicate the sensitivities[2] of the map surprisingly well. Models such as neural networks have a rich history with [numerous resources](http://wikipedia.org/wiki/Neural_network) available that describe there use in tasks that range from [automated driving](http://en.wikipedia.org/wiki/Driverless_car) to [medical diagnosis.](http://www.nd.com/apps/medical.html)

The network I will describe is much simpler and only estimates the sensitivities of the delayed Henon map. This network is a single-layer feedforward network that is optimized on next-step prediction. The network, shown below, involves a layer of inputs that connect to a single layer of hidden nodes with some weight **a**. The weighted inputs are then transformed by an activation function, in this case a hyperbolic tangent, within each node and the output ![b hat sub k](/assets/posts/2011-04-20-modeling-sensitivity-using-neural-networks/image-1.png) is the sum of these hidden node values weighted by **b**. The network shown schematically:

![Neural Network Schematic](/assets/posts/2011-04-20-modeling-sensitivity-using-neural-networks/image-2.png)
{:.max-width-50-percent}

The weights, **a** and **b** are an _n_ x _d_ matrix and _n_ x _1_ vector of real numbers, respectively. The 1 is a bias term that shifts neuron's value around without being tied to an input. The neural network can be represented by:

![Neural Network Equation](/assets/posts/2011-04-20-modeling-sensitivity-using-neural-networks/image-3.png)
{:.max-width-50-percent}

where _d_ is the embedding dimension or number of inputs in the network and _n_ is the number of neurons in the hidden layer. The network is trained on input data **x** by altering the weights to better fit the target data **x<sub>k</sub>**. For the delayed Henon map, we feed _d_ sequential points from the time series into the network and associate the target as the next point in the time series. The network is trained to fit that next point.

There are numerous network topologies, training methods, and error functions that one can use. One method we use is similar to simulated annealing and hill climbing. In this case, we search a neighborhood of potential solutions with the chance to randomly search a more distant one. If a good solution is found, we move to its neighborhood and start searching again. We slowly shrink the neighborhood size as training progresses to help home in on a good solution. A good solution is one that minimizes the average one-step mean-square distance between predictions from the neural network ![b hat sub k](/assets/posts/2011-04-20-modeling-sensitivity-using-neural-networks/image-1.png) and the actual data **x<sub>k</sub>**,

![e=\frac{\sum^{c}_{k=d%2b1}(\hat{x}_k-x_k)^2}{c-d}](/assets/posts/2011-04-20-modeling-sensitivity-using-neural-networks/image-4.png)
{:.max-width-50-percent}

Since the neural network model equations are known, we can easily analyze the sensitivity of a network trained on experimental data such as the delayed Henon map. Following the same procedure detailed in [Delayed Henon Map Sensitivities](/2011/04/delayed-henon-map-sensitivities/), we can take the partial derivative of the function with respect to each of the inputs _j_,

![\frac{\partial%20\hat{x}_k}{\partial%20x_{k-j}}=\sum^{n}_{i=1}a_{ij}b_i\hbox{sech}^2(a_{i0}%2b\sum^{d}_{m=1}a_{im}x_{k-m})](/assets/posts/2011-04-20-modeling-sensitivity-using-neural-networks/image-5.png)
{:.max-width-50-percent}

We could also use a numerical partial derivative instead by perturbing each input one by one and averaging the change in output through the time series.

After training one neural network, with 4 neurons and 5 dimensions, on 512 points from the delayed Henon map with a delay set to four, the following training error, _e_=8.4 x 10<sup>-6</sup>, and sensitivities were found,

```
S(1) = 1.8762
S(2) = 0.0020
S(3)= 0.0017
S(4)=0.1025
S(5)=0.0004
```

where S(_j_) represents the sensitivities for time lag _j_. The delayed Henon map with a delay of four has the following sensitivities,

```
S(1) = 1.8980
S(4) = 0.1
```

The neural network estimates the sensitivities fairly well and one could probably train longer to obtain more accurate sensitivities.

One question we asked in this blog series concerned the inverted delayed Henon map. There are two approaches that we could take to find the sensitivities of the inverted map, (1) invert the neural network trained on the righted map or (2) train a network on the inverted map data.

It is not easy to invert a neural network though there are many papers about training a network on data in a way similar to the original training method. Ref #3 highlights how one would do this by training the network on inputs using gradient descent. However, we can find the sensitivities of the inverted delayed Henon map by simply training on data taken from the righted map and reversing the entire time series. After training a network with the same number of neurons and dimensions as described above, we arrive at (_e_=0.001572),

```
S(1)=0.1525
S(2)=0.07741
S(3)=17.1847
S(4)=8.6787
S(5)=0.0237
```

The inverted delayed Henon map has the following sensitivities calculated [here](/2011/04/inverted-delayed-henon-map/),

```
S(3)=18.9795
S(4)=10
```

As we see from the difference in the righted and inverted trained networks, sensitivity accuracy varies. One idea is that the accuracy of the training error is correlated to the error in the sensitivities but I am unaware of any literature exploring this.

With this training method, we do not know when a network is optimized so there is a trade off in accuracy and time spent training the neural network. This particular example trained for several hours. If time is an issue, you could easily trade out the neural network with another model such as [Support Vector Regression](http://en.wikipedia.org/wiki/Support_vector_machine#Regression).

Once the model has been optimized on the data, you could take the partial derivatives of the finalized equation with respect to each of the inputs or perform a numerical partial derivative. In this case, it is also important to calculate the same perturbation in each of the time lags of the original system. For the delayed Henon map with 512 points, this changes the sensitivities to 1.90594 for the first delay and .10000 for the d-th delay.

If you try other models, I would like to hear about it.

A neural network model and simple mathematical systems such as the delayed Henon map help us approach complex systems such as the weather, politics, or economics. We can explore simple systems like the delayed Henon map and look at interesting properties that these systems possess such as the sensitivity of the output to each of the inputs. Aside from this property, we could analyze trained neural networks to see if they replicate the Kaplan-Yorke dimension, fractal dimension, or many others. Creating algorithms that estimate these properties fairly well on simple systems may help us to understand more complex phenomena in the future.

References:

1. Sprott JC. High-dimensional dynamics in the delayed Hénon map. Electron J Theory Phys 2006; 3:19–35.
2. Maus A. and Sprott JC. Neural network method for determining embedding dimension of a time series. Comm Nonlinear Science and Numerical Sim 2011; 16:3294-3302.
3. Dau A. Inversion of Neural Networks. 2000; <http://web.mit.edu/profit/PDFS/DuaA.pdf>

This post is part of a series:

1. [Delayed Henon Map Sensitivities](/2011/04/delayed-henon-map-sensitivities/)
2. [Inverted Delayed Henon Map](/2011/04/inverted-delayed-henon-map/)
3. Modeling Sensitivity using Neural Networks