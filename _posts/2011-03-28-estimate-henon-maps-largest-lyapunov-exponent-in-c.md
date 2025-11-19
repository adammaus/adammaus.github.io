---
title: "Estimate Henon Map's Largest Lyapunov Exponent in C"
date: 2011-03-28T06:33:25-05:00
author: Adam
excerpt: I have been experimenting with C since I have not had as much exposure to the language since college and I recently built a computer with a CUDA-enabled graphics card that I hope to use for my research.
layout: post
permalink: 2011/03/estimate-henon-maps-largest-lyapunov-exponent-in-c/
tags:
  - C
  - CUDA
---
I have been experimenting with C since I have not had as much exposure to the language since college and I recently built a computer with a CUDA-enabled graphics card that I hope to use for my research.

I hope to translate more of the programs we use to C and eventually to a version that works with CUDA. This program estimates (or calculates) the Largest Lyapunov Exponent of the Henon Map. The Largest Lyapunov Exponent for this Dissipative Map is about 0.419227 with log base e. To change the map, would require altering the TimeSeries function, initial conditions, and parts of the code that perform the actual calculation.

{% highlight c %}
// Includes
#include <stdio.h>
#include <cuda.h>
#include <math.h>

// Global Variables
bool noprompt = false;
int NumPts = 1000000;
float Perturb = pow(10, -8);

// Functions
void Cleanup(void);
void ParseArguments(int, char**);
void TimeSeries(double*);

// C - program to get Largest LE of Henon map (pre CUDA)
int main(int argc, char** argv) {
  printf("Largest Lyapunov Exponent (Henon)\n");
  ParseArguments(argc, argv);

  // Define the vector sliding window
  double* xList;
  xList = (double*)malloc(2*sizeof(double));
  double* closeXList;
  closeXList = (double*)malloc(2*sizeof(double));

  // Initialize the data for the map
  double x1 = .1;
  double x2 = .1;
  xList[0] = x1;
  xList[1] = x2;

  // Initialize the data for the LLE calculation
  double closeX1 = .1 + Perturb;
  double closeX2 = .1 + Perturb;
  closeXList[0] = closeX1;
  closeXList[1] = closeX2;

  double delR = pow((pow(x1,2) + pow(x2,2)),.5);
  double DELdelR = pow((pow(closeX1,2) + pow(closeX2,2)), .5);
  double delR0 = delR - DELdelR;
  double delR1, delX1, delX2, lambda, lambdaSum;
  lambdaSum = 0;

  int t = 0;
  while (t < NumPts+1000) {
   // Get a new set of points
   TimeSeries(xList);
   TimeSeries(closeXList);

   if (t > 1000) {
    delR1 = pow(pow(xList[0],2)+pow(xList[1],2),.5);
    delR1 = delR1 - pow(pow(closeXList[0],2)+pow(closeXList[1],2),.5);
    delX1 = xList[0] - closeXList[0];
    delX2 = xList[1] - closeXList[1];

    // Recalculate the perturbed trajectory
    closeXList[0] = xList[0] + (delR0/delR1) * delX1;
    closeXList[1] = xList[1] + (delR0/delR1) * delX2;
    lambda = log(abs(delR1) / abs(delR0));

    // Keep running total of lambda
    lambdaSum += lambda;
   }

   t = t + 1;
  }

  // Estimate the LLE
  double LLE = lambdaSum / (double)NumPts;
  printf("%d: %f\n", NumPts, LLE);

  // Free arrays
  free(closeXList);
  free(xList);
}

void TimeSeries(double* x) {
  double NewVal = 1 - 1.4 * pow(x[0], 2) + .3 * x[1];

  // Move new data into list
  x[1] = x[0];
  x[0] = NewVal;
}

void Cleanup(void){
    if (!noprompt) {
        printf("\nPress ENTER to exit...\n");
        fflush( stdout);
        fflush( stderr);
        getchar();
    }

    exit(0);
}

// Parse program arguments
void ParseArguments(int argc, char** argv){
    for (int i = 0; i < argc; ++i){
        if (strcmp(argv[i], "--noprompt") == 0 || strcmp(argv[i], "-noprompt") == 0)  {
            noprompt = true;
            break;
        }
    }
}
{% endhighlight %}