---
layout: post
title: In-depth details of Particle Swarm Optimization
date: 2012-02-05T15:04:25-06:00
excerpt: I explain and show code to construct the Particle Swarm Optimization in Python. I conclude by optimizing on the Rastrigin function, a function that researchers use to test optimization algorithms on.
permalink: 2012/02/details-of-particle-swarm-optimization/
tags:
  - Optimization
  - Particle Swarm Optimization
  - Python
  - Rastrigin Function
---

In the [first part of this series](/2012/01/an-overview-of-particle-swarm-optimization/) on Particle Swarm Optimization (PSO), I posted an general overview of the algorithm and an example of how the algorithm searches for the minimum of a parabola. In this post, I explain an example of the algorithm constructed in Python. I will end with an example problem, called the [Rastrigin function](http://en.wikipedia.org/wiki/Rastrigin_function), a function that researchers use to test their optimization algorithms on.

The full Python code that I will be discussing is located [here](/assets/files/bare-bones-pso.py). It may be helpful to open this code since I will only be discussing specific portions of the code.

The file is set up in the following way:
* global variables and user-defined parameters
* function F(): the function being optimized, in the example file, I use the Rastrigin function
* function main(): the function that constructs the swarm and attempts to optimize F
* class Particle: the functions and local variables associated with each Particle

The function main, constructs the swarm and iterates for a user-defined number of trials (cmax). The best velocity, position, and error are saved and output at the end of the program. It is not necessary to use the number of trials to signal the end of optimization. One could also stop the optimization if the best error achieves a certain value or if all of the particles are below some error bound.

During optimization, particles' behavior are determined by the following set of equations:

![Velocity Equation](/assets/imgs/2012-02-05-details-of-particle-swarm-optimization/image-1.gif){:.centered}
![Position Equation](/assets/imgs/2012-02-05-details-of-particle-swarm-optimization/image-2.gif){:.centered}

The first equation _v<sub>ij</sub>(t)_ determines the velocity of particle _i_ in dimension _j_ for time step _t_. Particles adjust their trajectory in the search space according to their local neighborhood’s best position x**, their own best position _x*_, and their previous velocity. The first term of the velocity characterizes how much the previous velocity affects the new velocity with _w_ set to 1 in the code. In the code, a dampening parameter is included that can be used to slow particles as optimization progresses. The second term or "cognitive" term with _c<sub>1</sub>r<sub>1</sub>_ pull particles back to their best previous position. The third term or "social" term with _c<sub>2</sub>r<sub>2</sub>_ pushes particles together so they fly collaboratively through space. The second equation _x<sub>ij</sub>(t)_ determines the position of particle _i_ in dimension _j_ for time step _t_. New positions are determined by the previous position and the current velocity.

In the Python code, the particle class randomly initializes the positions and velocities (the InitPosition(self) and InitVelocity(self) functions) for each particle within some search space. After each time step in the optimization, the UpdateVelocity(self) and UpdatePosition(self) functions are called to construct new velocity and position vectors for each particle.

Within the main function, the particles' positions are evaluated after each update as the swarm moves towards the optimal position in the space.

The following graphs are from an example trial of the algorithm run on the 1-D [Rastrigin function](http://en.wikipedia.org/wiki/Rastrigin_function):

![Rastrigin Equation](/assets/imgs/2012-02-05-details-of-particle-swarm-optimization/image-3.png){:.centered}

PSO variations are often tested on the Rastrigin function because of how simple changes to the parameter <em>d</em> can extend the function to higher dimensions. Additionally, the number of deep local optima is quite large, as seen in the graph below. The global optimum is at <em>x=0</em>. For these results, the following parameters were used:

{% highlight python %}
# The dimension of the function
num_dimensions = 1
# The number of particles in the swarm
num_particles = 5

# Bounds on the positions and velocities
v_max = 5
v_min = -5
p_min = -10
p_max = 10
# The number of updates to do
cmax = 1000
# The amount to dampen the velocity after each update
dampener = 1
dampen_rate = 1
{% endhighlight %}

![Initial Swarm Positions (the green dots)](/assets/imgs/2012-02-05-details-of-particle-swarm-optimization/image-4.png)
Initial Swarm Positions (the green dots)
{:.centered.max-width-50-percent}

<br>

![After 250 steps](/assets/imgs/2012-02-05-details-of-particle-swarm-optimization/image-5.png)
After 250 steps
{:.centered.max-width-50-percent}

<br>

![After 500 steps](/assets/imgs/2012-02-05-details-of-particle-swarm-optimization/image-6.png)
After 500 steps
{:.centered.max-width-50-percent}

<br>

![After 750 steps](/assets/imgs/2012-02-05-details-of-particle-swarm-optimization/image-7.png)
After 750 steps, one particle ends up very far from the rest of the swarm, possibly because the particle ends up overshooting where the swarm is.
{:.centered.max-width-50-percent}

<br>

![After 1000 steps](/assets/imgs/2012-02-05-details-of-particle-swarm-optimization/image-7.png)
After 1000 steps
{:.centered.max-width-50-percent}

<br>

As you can see, the swarm does not necessarily converge to the global optimum (<em>x = 0</em>) but they are all somewhat close. If you measured the best position, at least one particle has encountered the optimal position during optimization but the particle did not end up settling down because of how the parameters, the dampening factor, <em>w</em>, <em>c<sub>1</sub></em>, and <em>c<sub>2</sub></em> were chosen. One of the simplest ways to improve the algorithm is to allowing the velocity to decay (<em>w < 1</em> or dampening factor) which should help all of the particles converge to an optimum.

Of course, this is just one example of how to set up the algorithm. Many researchers have experimented with portions of the algorithm trying to find the best way to optimize a function. As we will see later, changes to the particle's equations and the distributions used to select <em>r<sub>1</sub></em> and <em>r<sub>2</sub></em> are just a few open problems in PSO.

This post is part of a series:

1. [An overview of Particle Swarm Optimization Algorithm](/2012/01/an-overview-of-particle-swarm-optimization/ "An Overview of Particle Swarm Optimization")
2. In-depth details of the algorithm
3. [More applications of Particle Swarm Optimization](/2012/03/applications-of-particle-swarm-optimization/)