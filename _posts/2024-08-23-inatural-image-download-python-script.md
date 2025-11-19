---
layout: post
permalink: "2024/08/inatural-image-download-python-script/"
title: "iNatural Image Download Python Script"
date: 2024-08-23T10:12:32-05:00
tags:
  - Machine Learning
  - Python
---

I started working on a small project to replicate the results found in Justen et al. 2021 Identification of Public Submitted Tick Images: A Neural Network Approach. [https://doi.org/10.1371/journal.pone.0260622](https://doi.org/10.1371/journal.pone.0260622).

One of the sources of tick images used in the paper is from [iNaturalist.org](https://www.inaturalist.org/). iNaturalist has a publicly accessible data set with millions of observations of thousands of animal and plant species.

In that dataset, there are about 25,000 images of the Lone Star Tick, American Dog Tick, and the Black-legged Tick or Deer Tick that I plan to use in training the model.

Here is a Python script that allows you to download images for a given set of taxon_ids: [https://github.com/adammaus/inaturalist-image-download](https://github.com/adammaus/inaturalist-image-download)

\* Just a note, this script will not have ongoing support but hopefully it provides someone with a place to start.