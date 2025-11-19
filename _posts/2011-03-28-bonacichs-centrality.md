---
layout: post
title: "Bonacich's Centrality"
date: 2011-03-28T21:26:26-05:00
excerpt: "Bonacich's Approach to Centrality (also known as Eigenvector Centrality): You are more central when there are more connections within your local network"
permalink: 2011/03/bonacichs-centrality/
tags:
  - Bonacich
  - Centrality
  - Social Network Analysis
---
Bonacich&#8217;s Approach to Centrality (also known as Eigenvector Centrality)

* You are more central when there are more connections within your local network
* Fewer connections within your local network means you are more powerful
    * Power comes from being connected to those that are powerless
* The Measure
    * The centrality nodes in a network are given by: _&lambda; e_ = _R e_ where R is matrix formulation of the network in question, e is an eigenvector of R, and &lambda; is its associated eigenvalue
    * Additional variations:
        * Introduction of user-defined Β and α to measure centrality c such that _c(&alpha;, Β)_ = _α(I-ΒR)<sup>-1</sup>R*1_ where c is a vector of node centralities, I is an identity matrix, and 1 is a column vector of 1&#8217;s.
        * Β reflects the degree to which a node&#8217;s power is related to the power of the nodes it is connected to
        * Intrepretation: A more positive Β means that other nodes centralities are taken more into account. A more negative Β means that a node&#8217;s power is reduced by the powerful nodes it is connected to.
        * α simply scales node centrality

More Information:

1. [R documentation](https://search.r-project.org/CRAN/refmans/igraph/html/power_centrality.html)
2. [Centrality and Centralization](http://www.analytictech.com/mb119/chapter5.htm)
3. [Degree centrality: Bonacich&#8217;s approach](http://www.faculty.ucr.edu/~hanneman/nettext/C10_Centrality.html#Bonacich)
4. [Power and Centrality: A Family of Measures](https://www.journals.uchicago.edu/doi/10.1086/228631)

References to use of this measure in literature:

1. [Peer Standing and Substance Use in Early-Adolescent Grade-Level Networks: A Short-Term Longitudinal Study](https://pubmed.ncbi.nlm.nih.gov/17013672/)
2. [Network Structure and Proxy Network Measures of HIV, Drug and Incarceration Risks for Active Drug Users](https://pmc.ncbi.nlm.nih.gov/articles/PMC3600060/)
3. [An Empirical Assessment of Rural Community Support Networks for Individuals with Severe Mental Disorders](https://pubmed.ncbi.nlm.nih.gov/9559239/)