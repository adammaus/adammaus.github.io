---
layout: post
title: Estimating Lyapunov Spectra of ODEs using Python
date: 2011-09-03T08:21:21-05:00
excerpt: Python code is shown that estimates the Lyapunov spectra for the Rossler and Lorenz systems. This code is written in a way that makes it adaptable for other continuous-time systems.
permalink: 2011/09/estimating-ode-lyapunov-spectra-u/
tags:
  - Lorenz Attractor
  - Lyapunov Spectrum
  - ODE
  - Python
  - Rossler Attractor
  - Time Series
---
Wolf _et al_. (1985) outlined an algorithm that estimates the Lyapunov spectra of systems whose equations are known using local Jacobian matrices and Gram-Schmidt orthonormalization. Python code is available for Wolf's algorithm and [discrete maps](/2011/07/lyapunov-spectra-of-inverted-discrete-dynamical-systems/) and their inverted counterparts. I have adapted [this code](2011/03/lyapunov-spectrum-for-invertible-maps/) to estimate Lyapunov spectra for continuous-time systems like the [Lorenz](http://en.wikipedia.org/wiki/Lorenz_attractor) attractor and [Rossler](http://en.wikipedia.org/wiki/R%C3%B6ssler_attractor) attractor. Additionally, [Python code](2011/05/generating-time-series-for-ordinary-differential-equations/) is available to generate time series for ordinary differential equations. Lyapunov spectrum code is also available on [Clint Sprott's website](http://sprott.physics.wisc.edu/chaos/lespec.htm).

![Lorenz Attractor](/assets/posts/2011-09-03-estimating-ode-lyapunov-spectra-u/image-1.png)
{:.centered.max-width-50-percent}

Lorenz Attractor
{:.centered}

Source Code:

{% highlight python %}
import math, operator, random
h = 0.01
cmax = 1000     #   number of iterations to perform
choice = input("Which system would you like?\n (1) Rossler \n (2) Lorenz\n")
while str(choice) != "1" and str(choice) != "2":
  print("Please select 1 or 2")
  choice = input("Which system would you like?\n (1) Rossler \n (2) Lorenz\n")

print "\n",
a = 0.2
b = 0.2
c = 5.7

def derivs(x, xnew, n):
  if choice == 1:
    return Rossler(x, xnew, n)
  else:
    return Lorenz(x, xnew, n)

def Rossler(x, xnew, n):
  # Nonlinear Rossler Equations
  xnew[1]  = -x[2]-x[3]
  xnew[2]  = x[1] + a * x[2]
  xnew[3]  = b + x[3] * (x[1] - c)

  # Linearized Rossler Equations
  xnew[4]  = -1*x[7]-x[10]
  xnew[5]  = -1*x[8]-x[11]
  xnew[6]  = -1*x[9]-x[12]
  xnew[7]  = x[4] + a*x[7]
  xnew[8]  = x[5] + a*x[8]
  xnew[9]  = x[6] + a*x[9]
  xnew[10] = x[3]*x[4] + x[1]*x[10] - c*x[10]
  xnew[11] = x[3]*x[5] + x[1]*x[11] - c*x[11]
  xnew[12] = x[3]*x[6] + x[1]*x[12] - c*x[12]
  return [x, xnew]

def Lorenz(x, xnew, n):
  # Nonlinear Lorenz Equations
  xnew[1]  = 10 * (x[2] - x[1])
  xnew[2]  = -1*x[1] * x[3] + 28 * x[1] - x[2]
  xnew[3]  = x[1] * x[2] - 8/3.0 * x[3]

  # Linearized Lorenz Equations
  xnew[4]  = -10 * x[4] + 10 * x[7]
  xnew[5]  = -10 * x[5] + 10 * x[8]
  xnew[6]  = -10 * x[6] + 10 * x[9]
  xnew[7]  = 28*x[4]-x[3]*x[4] - x[7] - x[1]*x[10]
  xnew[8]  = 28*x[5]-x[3]*x[5] - x[8] - x[1]*x[11]
  xnew[9]  = 28*x[6]-x[3]*x[6] - x[9] - x[1]*x[12]
  xnew[10] = x[2]*x[4] + x[1]*x[7] - 8/3.0 * x[10]
  xnew[11] = x[2]*x[5] + x[1]*x[8] - 8/3.0 * x[11]
  xnew[12] = x[2]*x[6] + x[1]*x[9] - 8/3.0 * x[12]
  return [x, xnew]

def timeseries(cmax):
  X0 = []
  Y0 = []
  Z0 = []
  xList = []
  yList = []
  zList = []
  changeInTime = h

  # Initial conditions
  if choice == 1:
    # Rossler
    X0.append(0.01)
    Y0.append(0.01)
    Z0.append(0.01)

  else:
    # Lorenz
    X0.append(0)
    Y0.append(1)
    Z0.append(0)

  t = 0
  while len(xList) <= cmax:
    [x, y, z] = Rk4o(X0, Y0, Z0, h, len(X0))
    X0.append(x)
    Y0.append(y)
    Z0.append(z)

    if 200 < t:
      xList.append(x)
      yList.append(y)
      zList.append(z)

    changeInTime += h
    t = t + 1
  return [xList, yList, zList]

def f(x,y,z):
  if choice == 1:
    dxdt = -y-z
  else:
    dxdt = 10 * (y - x)
  return dxdt

def g(x,y,z):
  if choice == 1:
    dydt = x + a * y
  else:
    dydt = 28 * x - y - x*z
  return dydt

def e(x,y,z):
  if choice == 1:
    dzdt = b + z * (x - c)
  else:
    dzdt = x * y - 8/3.0 * z
  return dzdt

def Rk4o(xList, yList, zList, h, t):
  k1x = h*f(xList[t-1],yList[t-1], zList[t-1])
  k1y = h*g(xList[t-1],yList[t-1], zList[t-1])
  k1z = h*e(xList[t-1],yList[t-1], zList[t-1])

  k2x = h*f(xList[t-1] + k1x/2,yList[t-1] + k1y/2, zList[t-1] + k1y/2)
  k2y = h*g(xList[t-1] + k1x/2,yList[t-1] + k1y/2, zList[t-1] + k1y/2)
  k2z = h*e(xList[t-1] + k1x/2,yList[t-1] + k1y/2, zList[t-1] + k1y/2)

  k3x = h*f(xList[t-1] + k2x/2,yList[t-1] + k2y/2, zList[t-1] + k2y/2)
  k3y = h*g(xList[t-1] + k2x/2,yList[t-1] + k2y/2, zList[t-1] + k2y/2)
  k3z = h*e(xList[t-1] + k2x/2,yList[t-1] + k2y/2, zList[t-1] + k2y/2)

  k4x = h*f(xList[t-1] + k3x/2,yList[t-1] + k3y/2, zList[t-1] + k3y/2)
  k4y = h*g(xList[t-1] + k3x/2,yList[t-1] + k3y/2, zList[t-1] + k3y/2)
  k4z = h*e(xList[t-1] + k3x/2,yList[t-1] + k3y/2, zList[t-1] + k3y/2)

  x = xList[t-1] + k1x/6 + k2x/3 + k3x/3 + k4x/6
  y = yList[t-1] + k1y/6 + k2y/3 + k3y/3 + k4y/6
  z = zList[t-1] + k1z/6 + k2z/3 + k3z/3 + k4z/6
  return [x,y,z]

n = 3           #   number of variables in nonlinear system
nn=n*(n+1)      #   total number of variables (nonlinear + linear)
m = 0
x = []
xnew = []
v = []
ltot = []
znorm = []
gsc = []
A = []
B = []
C = []
D = []
i = 0
while i <= nn:
  x.append(0)
  xnew.append(0)
  v.append(0)
  A.append(0)
  B.append(0)
  C.append(0)
  D.append(0)
  i = i + 1

i = 0
while i <= n:
  ltot.append(0)
  znorm.append(0)
  gsc.append(0)
  i = i + 1

irate=10      #   integration steps per reorthonormalization
io= 100       #   number of iterations between normalization

#   initial conditions for nonlinear maps
#   must be within the basin of attraction

# Generate a random transient before starting the initial conditions
i = 1
while i <= n:
  v[i] = 0.001
  i = i + 1

transient = random.randint(n,100000)
# Generate the initial conditions for the system
[tempx,tempy,tempz] = timeseries(transient)

v[1] = tempx[len(tempx)-1]
v[2] = tempy[len(tempy)-1]
v[3] = tempz[len(tempz)-1]

i = n+1
while i <= nn:  #   initial conditions for linearized maps
  v[i]=0        #   Don't mess with these; they are problem independent!
  i = i + 1

i = 1
while i <= n:
  v[(n+1)*i]=1
  ltot[i]=0
  i = i + 1
#print "v = ",v
t=0
w = 0
while (w < cmax):
  j = 1
  while j <= irate:
    i = 1
    while i <= nn:
      x[i]=v[i]
      i = i + 1
    [x, xnew] = derivs(x, xnew, n)

    i = 1
    while i <= nn:
      A[i] = xnew[i]
      x[i] = v[i] + (h*A[i]) / 2.0
      i = i + 1
    [x, xnew] = derivs(x, xnew, n)

    i = 1
    while i <= nn:
      B[i] = xnew[i]
      x[i] = v[i] + (h*B[i]) / 2.0
      i = i + 1
    [x, xnew] = derivs(x, xnew, n)

    i = 1
    while i <= nn:
      C[i] = xnew[i]
      x[i] = v[i] + h*C[i]
      i = i + 1
    [x, xnew] = derivs(x, xnew, n)

    i = 1
    while i <= nn:
      D[i] = xnew[i]
      v[i] = v[i] + h*(A[i] + D[i] + 2*(B[i] + C[i]))/6.0
      i = i + 1

    t = t + h
    j = j + 1

  # construct new orthonormal basis by gram-schmidt:
  znorm[1]=0  #normalize first vector

  j = 1
  while j <= n:
    znorm[1]=znorm[1]+v[n*j+1]**2
    j = j + 1

  znorm[1] = math.sqrt(znorm[1])

  j = 1
  while j <= n:
    v[n*j+1]=v[n*j+1]/znorm[1]
    j = j + 1

  #generate new orthonormal set:
  j = 2
  while j <= n:
    k = 1
    while k <= j-1:
      gsc[k]=0

      l = 1
      while l <= n:
        gsc[k]=gsc[k]+v[n*l+j]*v[n*l+k]
        l = l + 1
      k = k + 1

    k = 1
    while k <= n: # construct a new vector
      l = 1
      while l <= j-1:
        v[n*k+j]=v[n*k+j]-gsc[l]*v[n*k+l]
        l = l + 1
      k = k + 1

    znorm[j]=0     # calculate the vector's norm

    k = 1
    while k <= n: # construct a new vector
      znorm[j]=znorm[j]+v[n*k+j]**2
      k = k + 1

    znorm[j]=math.sqrt(znorm[j])

    k = 1
    while k <= n: # normalize the new vector
      v[n*k+j] = v[n*k+j] / znorm[j]
      k = k + 1

    j = j + 1

  k = 1
  while k <= n: #update running vector magnitudes
    if znorm[k] > 0:
      ltot[k] = ltot[k] + math.log(znorm[k])
    k = k + 1

  m = m + 1
  if m % io == 0 or w == cmax-1:  # normalize exponent and print every io iterations
    lsum=0
    kmax=0
    k = 1
    while k <= n:
      le = ltot[k] / t
      lsum = lsum + le

      if lsum > 0:
        lsum0 = lsum
        kmax = k
      k = k + 1

  w = w + 1
if choice == 1:
  print "Rossler:"
else:
  print "Lorenz:"

print n, "LEs = "

lsum=0
kmax=0

k = 1
while k <= n:
  le = ltot[k] / t
  lsum = lsum + le

  if lsum > 0:
    lsum0 = lsum
    kmax = k

  print le
  k = k + 1
{% endhighlight %}