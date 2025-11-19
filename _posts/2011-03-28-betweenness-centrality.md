---
layout: post
title: Betweenness Centrality
date: 2011-03-28T21:24:26-05:00
excerpt: "Betweenness Centrality: The higher a node's centrality is the more \"dependent\" other nodes are on it"
permalink: 2011/03/betweenness-centrality/
tags:
  - Betweeness
  - Centrality
  - Social Network Analysis
---
Betweenness Centrality

* The higher a node&#8217;s centrality is the more &#8220;dependent&#8221; other nodes are on it
* Based on shortest paths between nodes and the number of paths that pass through two points and the total number of paths
* _BC(i) = SUM<sub>s&ne;i&ne; t&isin;V</sub>&mu;<sub>st</sub>(i) / &mu;<sub>st</sub>_ where _&mu;<sub>st</sub>_ is the number of paths from _s_ and _t_ and _&mu;<sub>st</sub>(i)_ is the number of paths from _s_ and _t_ that pass through node _i_

Algorithm

Input: _V_, a vertex and _G_, a graph

1. For all pairs of vertices (_v<sub>1</sub>_ and _v<sub>2</sub>_) in graph G, compute every shortest path between them
2. Using _v<sub>1</sub>_ and _v<sub>2</sub>_, compute the fraction of paths between these vertices that pass through _V_
3. Sum over all pairs of vertices

More Information and other Algorithms:

1. [Approximating Betweenness Centrality](https://davidbader.net/publication/2007-bkmm/2007-bkmm.pdf)
2. [Better Approximation of Betweenness Centrality](https://dl.acm.org/doi/10.5555/2791204.2791213)

References to use of this measure in literature:

1. [Collaboration and Integration of Community-Based Health and Human Services in a Nonprofit Managed Care System](http://journals.lww.com/hcmrjournal/Abstract/2002/01000/Collaboration_and_Integration_of_Community_Based.3.aspx)
2. [The Peer Context of Adolescent Substance Use: Findings from Social Network Analysis](http://onlinelibrary.wiley.com/doi/10.1111/j.1532-7795.2006.00127.x/abstract)
3. [Peer Standing and Substance Use in Early-Adolescent Grade-Level Networks: A Short-Term Longitudinal Study](http://www.ncbi.nlm.nih.gov/pmc/articles/PMC2789699/)