---
concept: Edge Probability
slug: edge-probability
category: random-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Random Graphs"
chapter_number: 11
pdf_page: 304
section: "11.1 The notion of a random graph"
extraction_confidence: high
aliases:
  - "p"
  - "edge probability function"
prerequisites:
  - random-graph-gnp
extends: []
related:
  - threshold-function
contrasts_with: []
answers_questions:
  - "What is the edge probability in a random graph?"
---

# Quick Definition
The edge probability p is the probability that any given pair of vertices forms an edge in the random graph G(n,p). It may be a constant or a function p = p(n) of the number of vertices.

# Core Definition
In the random graph model G(n,p), for each potential edge e in [V]^2, the probability of e being an edge is p, and the probability of it not being an edge is q := 1-p. Often, p depends on n: p = p(n). Within each space G(n,p), the probability is the same for all potential edges (Diestel, pp. 304-305).

# Prerequisites
- **Random graph G(n,p)** — Edge probability parameterizes the model

# Key Properties
1. p may be constant (e.g., p = 1/2) or a function of n (e.g., p = n^{-1})
2. q = 1 - p is the probability an edge is absent
3. Fixed subgraph H with l edges occurs with probability p^l
4. The "interesting" behaviour depends on how p = p(n) scales with n

# Context & Application
The choice of edge probability determines the likely structure of random graphs. As p grows from 0 to 1, the random graph undergoes phase transitions: acquiring edges, then cycles, then connectivity, then Hamiltonicity.

# Relationships
## Related
- **Threshold function** — Critical p values at which properties appear

# Source Reference
Chapter 11, Section 11.1, pages 304-305.

# Verification Notes
- Definition from pp. 304-305
- Confidence: HIGH — explicit parameter definition
