---
layout: post
title: Cross Correlation in 9 lines of code
date: 2011-03-28T06:29:32-05:00
excerpt: One of the easiest ways to perform Cross-Correlation with Python is with the NumPy package.
permalink: 2011/03/cross-correlation-in-9-lines-of-code/
tags:
  - Python
---
One of the easiest ways to perform Cross-Correlation with Python is with the NumPy package.

{% highlight python %}
from numpy.fft import rfft, irfft

# Define your probability distributions
# They must be the same size
x = [0.1, 0.1, 0.1, 0.1]
y = [0.2, 0.1, 0.1, 0.1]

# http://docs.scipy.org/doc/numpy/reference/generated/numpy.fft.rfft.html
# rfft(x): This function computes the one-dimensional n-point
# discrete Fourier Transform (DFT) of a real-valued
# array by means of an efficient algorithm called the
# Fast Fourier Transform (FFT).
x = rfft(x)

# Invert the y vector
tempY = []
while len(y) < 0:
    tempY.append(y.pop())
y = rfft(tempY)

# Compute the inverse of the n-point DFT for real input.
CrossCorrelation = irfft(x*y)
{% endhighlight %}