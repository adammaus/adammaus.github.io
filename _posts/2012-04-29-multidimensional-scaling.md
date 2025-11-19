---
layout: post
title: Multidimensional Scaling
date: 2012-04-29T09:38:20-05:00
excerpt: Multidimensional Scaling (MDS) is a linear embedding method used when we only know the pairwise distances between data points. For linear systems, MDS works well with as little as 10 points and the system is 2 dimensional.
permalink: 2012/04/multidimensional-scaling/
tags:
  - Embedding Mthod
  - Multidimension Scaling
  - Python
  - Time Series
---
Multidimensional Scaling (MDS) is a linear embedding method used when we only know the pairwise distances between data points. For linear systems, MDS works well with as little as 10 points and the system is 2 dimensional. For this program, you choose the window size or embedding for the system and MDS identifies what the true embedding should be. The following program uses Logistic map data when _r = 3.2_ but you can change _r_ to see how well MDS works as the map bifurcates and eventually becomes chaotic and nonlinear at 4. MDS breaks down at this point and the embedding defaults to just 1 over the embedding you choose.

{% highlight python %}
# Requires Numpy and Scipy libraries

from numpy import *
import scipy.linalg
import random

r = 3.2 # parameter on Logistic map
n = 10 # the number of timeseries points to use
d = 40 # your embedding choice

# Create a time series
def timeseries(number,throw, d):
  xList = []
  dataX0 = []

  t = 0
  while t < d:
    xList.append(.1)
    t += 1

  while t <= number+throw+d:
    x = r * xList[t-1] * (1 - xList[t-1]) # Logistic Map
    xList.append(x)

    if t > throw:
      y = xList[t-1]
      dataX0.append(x)

    t = t + 1

  return dataX0

# Construct an n x n centering matrix
# The form is P = I - (1/n) U where U is a matrix of all ones
def centering_matrix(n):
  P = eye(n) - 1/float(n) * ones((n,n))
  return P

def create_data(number, d):
  dataX0 = timeseries(number, 500, d)

  # Create a sliding window of size d
  data = []

  i = d
  while i < len(dataX0):
    data.append([])

    j = i - d
    while j < i:
      data[len(data)-1].append(dataX0[j])
      j = j + 1
    i = i + 1

  return data

def main():
  print "n =", n, ": number of timeseries points used"
  print "d =", d, ": embedding"

  P = centering_matrix(n)

  # Create the data with the number of dimensions
  data = create_data(n, d)
  X = pairwise_distances(data)
  A = -1/2.0 * P * X * P

  # Calculate the eigenvalues/vectors
  [vals, vectors] = scipy.linalg.eig(A)

  # Sort the values
  vals = sort(vals)
  embedding = 0
  for x in vals:
    if x > 10**(-10):
      embedding += 1

  print "mds embedding =", embedding

# Compute the pairwise distance between vector x and y
def metric(x1, y1):
  d = 2
  summ = []

  i = 0
  while i < len(x1):
    # in this case use euclidean distance
    summ.append((x1[i] - y1[i])**d)
    i = i + 1

  return sum(summ) ** (1 / float(d))

# Return a matrix of pairwise distances
def pairwise_distances(data):
  distances = []
  i = 0

  while i < len(data):
    distances.append([])
    x1 = data[i]

    j = 0
    while j < len(data):
      y1 = data[j]
      distances[i].append(metric(x1, y1)**2)
      j = j + 1
    i = i + 1

  return distances

main()
{% endhighlight %}