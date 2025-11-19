---
layout: post
title: "Freeman's Approach to Degree Centrality"
date: 2011-03-28T21:29:52-05:00
excerpt: "Freeman's Approach to Degree Centrality: Centrality is based on connections between nodes in the network"
permalink: 2011/03/freemans-approach-to-degree-centrality/
tags:
  - "Freeman's Degree Centrality"
  - Social Network Analysis
---
Freeman's Approach to Degree Centrality:

* Centrality is based on connections between nodes in the network
* Measure in-degree and the out-degree and degree percentage of entire network for each node
* Can measure network statistics such as mean, standard deviation, etc.
* Network Centralization calculation compares a network to the perfect star network of the same size
    1. A star network of size N (nodes)
        * Has one node whose in-degree is N-1 and whose out-degree is 0
        * Other N-1 nodes have out-degree 1 and in-degree 0
    2. Network Centralization = (N * D – m) / ((N-1)(N-2)) where N is the number of nodes, D is the max degree whether that is in or out, and m is the number of edges

For more information:

1. <https://faculty.ucr.edu/~hanneman/nettext/C10_Centrality.html#Freeman>

References to use of this measure in literature:

1. [Collaboration and Integration of Community-Based Health and Human Services in a Nonprofit Managed Care System](http://journals.lww.com/hcmrjournal/Abstract/2002/01000/Collaboration_and_Integration_of_Community_Based.3.aspx)
2. [Interorganization Relationships Among HIV/AIDS Service Organizations in Baltimore: A Network Analysis](https://pubmed.ncbi.nlm.nih.gov/11564850/)
3. [Peers, schools, and adolescent cigarette smoking](https://pubmed.ncbi.nlm.nih.gov/11429302/)