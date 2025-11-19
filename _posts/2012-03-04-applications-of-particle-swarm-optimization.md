---
layout: post
title: Applications of Particle Swarm Optimization
date: 2012-03-04T17:19:55-06:00
excerpt: Particle swarm optimization can be used in a variety of different applications. A few examples involving nonconvex, multi-objective, discontinuous search spaces and applications in neural networks and support vector machines are mentioned.
permalink: 2012/03/applications-of-particle-swarm-optimization/
tags:
  - Integer Programming
  - Multi-objective Optimization
  - Neural Network
  - Optimization
  - Particle Swarm Optimization
  - Rastrigin Function
  - Support Vector Machines
---
**Nonconvex Search Spaces**

The Rastrigin function from the post  [In-depth details of the algorithm](https://blog.adammaus.com/2012/02/details-of-particle-swarm-optimization/ "In-depth details of Particle Swarm Optimization") is a nonconvex function and therefore has a nonconvx search space. Convexity is extremely important in optimization algorithms because it has nice properties involving gradients that can make optimization guaranteed. In a space like the Rastrigin function, particle swarm optimization is able to deal with the local minima and in many cases finds the global optimum.

**Integer or Discontinuous Search Spaces**

In a similar vein, integer search spaces are difficult for traditional optimization algorithms. In problems that involve integer variables, the search space is discontinuous and gradient information is rarely effective. Particle swarm optimization does not require the space to be continuous but precautions need to be taken to position particles exactly on specific values. For more information see, ["An improved PSO algorithm for solving non-convex NLP/MINLP problems with equality constraints" by Yiqing _et al_](http://www.sciencedirect.com/science/article/pii/S0098135406001281).

**Neural Networks**

One could treat the neural network weight space as a high dimensional particle swarm optimization search space. In this application of PSO, particles could be a swarm of neural networks attempting to find the lowest error on some classification or regression task. See "[Particle Swarm Optimization of Neural Network Architectures and Weights](http://ieeexplore.ieee.org/Xplore/login.jsp?url=http%3A%2F%2Fieeexplore.ieee.org%2Fiel5
%2F4344004%2F4344005%2F04344074.pdf
%3Farnumber%3D4344074&authDecision=-203)" by Carvalho _et al_.

**Support Vector Machines (and Regression)**

For classification and regression tasks using Support Vector Machines, the user has the ability to choose a few hyperparameters that control the kernel function, the cost associated with failing to correctly classify a training item, the loss function parameters, etc. Traditionally, the grid search has been used since the search space is rarely the same between problems and unlikely to be convex. Since the search space is continuous there is a combinatorial explosion as the number of hyperparameters increases. Particle swarm optimization could be used to find the optimal set of hyperparameters by creating particles that search a space of various values for each of the hyperparameters while attempting to produce the best error on the data. To learn more, see "[Particle swarm optimization for parameter determination and feature selection of support vector machines](http://www.sciencedirect.com/science/article/pii/S0957417407003752)" by Lin _et al_.

**Multi-Objective Optimization**

In the spirit of optimization problems, multi-objective programs involve optimizing programs with multiple objective functions where objective functions are potentially in conflict with one another. In these problems, particle swarm optimization can be used to find a good trade-off between the different objective functions. See "[Multi-Objective Particle Swarm Optimizers: A Survey of the State-of-the-Art](http://www.softcomputing.net/ijcir/vol2-issu3-paper5.pdf)" by Reyes-Sierra _et al_.

This post is part of a series:

1. [An overview of Particle Swarm Optimization Algorithm](/2012/01/an-overview-of-particle-swarm-optimization/ "An Overview of Particle Swarm Optimization")
2. [In-depth details of the algorithm](/2012/02/details-of-particle-swarm-optimization/)
3. More applications of Particle Swarm Optimization