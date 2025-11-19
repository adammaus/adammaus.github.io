---
layout: post
title: Subgraph Centrality
date: 2011-03-28T21:31:20-05:00
excerpt: 'Subgraph Centrality: Accounts for the participation of a node in all subgraphs of the network'
permalink: 2011/03/subgraph-centrality/
tags:
  - Social Network Analysis
  - Subgraph Centrality
---
Subgraph Centrality

* Accounts for the participation of a node in all subgraphs of the network
* Smaller subgraphs are given more weight than larger ones, which makes this measure appropriate for characterizing network motifs (1)
* Measures density of eigenvalues within the network&#8217;s adjacency matrix **_A_**
* _SC(i) = SUM<sup>&infin;</sup><sub>t=0</sub>&mu;<sub>t</sub>(i) / t!_ where &mu;<sub>t</sub>(i) is the number of paths starting and ending with node _i_ of length _t_ and can be calculated by _&mu;<sub>t</sub>(i) = (**A**<sup>k</sup>)<sub>ii</sub>_
* This boils down to _SC(i) = (e<sup><strong>A</strong></sup>)<sub>ii</sub>_ where _e<sup><strong>A</strong></sup>_ is the [matrix exponential](http://en.wikipedia.org/wiki/Matrix_exponential) of **A**

For more information:

1. [Subgraph Centrality in Complex Networks](http://arxiv.org/ftp/cond-mat/papers/0504/0504730.pdf)
2. [Introduction to Graph Theory](http://www.scottishinsight.ac.uk/Portals/50/ComplexNetworks_Jan/Estrada_tutorial2.ppt)