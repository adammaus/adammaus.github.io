---
layout: post
title: Lyapunov spectra of inverted discrete dynamical systems
date: 2011-07-10T11:21:09-05:00
excerpt: "One can estimate the lyapunov spectrum of dynamical systems and their inverted counterparts using local Jacobian matrices and Wolf's algorithm."

permalink: 2011/07/lyapunov-spectra-of-inverted-discrete-dynamical-systems/
tags:
  - Chaos
  - Invertible Maps
  - Lyapunov Spectrum
  - Python
  - Time Series
---
One can estimate the Lyapunov spectrum of dynamical systems and their inverted counterparts using local Jacobian matrices and [Wolf&#8217;s algorithm](http://www.google.com/search?q=wolf+alan+lyapunov). Basically, Jacobian matrices are calculated at each point in a trajectory and multiplied together to form a product matrix whose eigenvalues represent the Lyapunov exponents for the system studied. More specifically, these exponents measure the divergence of a ball of initial conditions as they move around an attractor, in this case, a strange attractor. As the Jacobians are multiplied together, Gram-Schmidt reorthonormalization is used to maintain the system of coordinates and unify the divergence because the ball of initial conditions quickly becomes an ellipisoid.

In 1985, Alan Wolf _et al_. published the paper that outlined a program that can be used to determine the spectrum of Lyapunov exponents for system&#8217;s whose equations are known. Wolf&#8217;s algorithm requires that the equations are linearized. After performing the necessary calculations, one can plug them into the program available [here (in Python)](/2011/03/lyapunov-spectrum-for-invertible-maps/) and estimate the Lyapunov spectrum.

Here is an example of how to linearize the Henon map and more complex Tinkerbell map:

The Henon map:

![Henon Map equation 1](/assets/imgs/2011-07-10-lyapunov-spectra-of-inverted-discrete-dynamical-systems/image-1.png)
{:.max-width-50-percent}

![Henon Map equation 2](/assets/imgs/2011-07-10-lyapunov-spectra-of-inverted-discrete-dynamical-systems/image-2.png)
{:.max-width-50-percent}

The Henon&#8217;s Jacobian matrix:

![Henon Map Jacobian Matrix](/assets/imgs/2011-07-10-lyapunov-spectra-of-inverted-discrete-dynamical-systems/image-3.png)
{:.max-width-50-percent}

Linearizing the Henon map:

![Linerizing the Henon map equation](/assets/imgs/2011-07-10-lyapunov-spectra-of-inverted-discrete-dynamical-systems/image-4.png)
{:.max-width-50-percent}

Partial Code for Wolf&#8217;s algorithm:

{% highlight python %}
def Henon(x, xnew, n):
	a=1.4
	b=0.3

	#   Nonlinear Henon map equations:
	xnew[1] = 1-a*x[1]*x[1]+b*x[2]

	xnew[2] = x[1]
	#   Linearized Henon map equations:
	xnew[3] = -2*a*x[1]*x[3]+b*x[5]
	xnew[4] = -2*a*x[1]*x[4]+b*x[6]
	xnew[5] = x[3]
	xnew[6] = x[4]
	return [x, xnew]
{% endhighlight %}

The Tinkerbell map:

![Tinkerbell Map equation 1](/assets/imgs/2011-07-10-lyapunov-spectra-of-inverted-discrete-dynamical-systems/image-5.png)
{:.max-width-50-percent}

![Tinkerbell Map equation 2](/assets/imgs/2011-07-10-lyapunov-spectra-of-inverted-discrete-dynamical-systems/image-6.png)
{:.max-width-50-percent}

The Tinkerbell&#8217;s Jacobian matrix:

![Tinkerbell Map Jacobian Matrix](/assets/imgs/2011-07-10-lyapunov-spectra-of-inverted-discrete-dynamical-systems/image-7.png)
{:.max-width-50-percent}

Linearizing the Tinkerbell map:

![Linerizing the Tinkerbell map equation](/assets/imgs/2011-07-10-lyapunov-spectra-of-inverted-discrete-dynamical-systems/image-8.png)
{:.max-width-50-percent}

Partial Code for Wolf&#8217;s algorithm:

{% highlight python %}
def tinkerbell(x, xnew, n):
	a =  0.9
	b = -0.6
	c =  2.0
	d =  0.5

	# Nonlinear
	xnew[1] = x[1]**2 - x[2]**2 + a*x[1] + b*x[2]   # x
	xnew[2] = 2*x[1]*x[2] + c * x[1] + d * x[2]	 # y

	# Linearized
	xnew[3] = 2 * x[1] * x[3] + a * x[3] - 2 * x[2] * x[5] + b * x[5] # delta x
	xnew[4] = 2 * x[1] * x[4] + a * x[4] - 2 * x[2] * x[6] + b * x[6] # delta x
	xnew[5] = 2 * x[2] * x[3] + c * x[3] + 2 * x[1] * x[5] + d * x[5] # delta y
	xnew[6] = 2 * x[2] * x[4] + c * x[4] + 2 * x[1] * x[6] + d * x[6] # delta y
	return [x, xnew]
{% endhighlight %}

To estimate the Lyapunov spectrum of the inverted system. One can simply reverse the signs on the exponent values of the forward system or take the more roundabout way and estimate them using Wolf&#8217;s algorithm.

To estimate the exponents, it is necessay to obtain to invert the system&#8217;s equations. In some cases, this is not possible such as the case of the Logistic map where each point could come from one of two previous points. To estimate the inverted system&#8217;s Jacobians (and the inverted system&#8217;s equations), one can simply invert the Jacobian matrix of the forward equations.

For the Henon map:

![Invert the Jacobian](/assets/imgs/2011-07-10-lyapunov-spectra-of-inverted-discrete-dynamical-systems/image-9.png)
{:.max-width-50-percent}

For the Tinkerbell map (and those with a magnifying glass):

![Invert the Jacobian](/assets/imgs/2011-07-10-lyapunov-spectra-of-inverted-discrete-dynamical-systems/image-10.png)
{:.max-width-50-percent}

The last issue that needs to be solved is generating data for the system. Since the system is inverted, the system has most likely turned from an attractor to a repellor and thus any trajectory will wander off to infinity. Therefore, we use the forward system&#8217;s equations and use the linearizations for the inverted system to estimate the Lyapunov spectrum. You can use the following [Python program](/2011/03/lyapunov-spectrum-for-invertible-maps/) and plug in the code above to see an example.