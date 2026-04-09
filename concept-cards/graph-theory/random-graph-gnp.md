---
concept: Random Graph G(n,p)
slug: random-graph-gnp
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
  - "binomial random graph"
  - "Erdős-Rényi model"
  - "G(n,p)"
prerequisites:
  - graph
extends: []
related:
  - edge-probability
  - random-variable-on-gnp
  - expected-value
  - probabilistic-method
contrasts_with: []
answers_questions:
  - "What is a random graph?"
  - "What is the G(n,p) model?"
---

# Quick Definition
The random graph G(n,p) is a probability space on the set of all graphs on n vertices, where each potential edge is included independently with probability p. It is the standard model for studying random graphs.

# Core Definition
Let V = {0, ..., n-1} be a fixed set of n elements. For each potential edge e in [V]^2, define a probability space Omega_e = {0_e, 1_e} with P_e({1_e}) = p and P_e({0_e}) = q = 1-p. The probability space G(n,p) is the product space Omega = product of all Omega_e over e in [V]^2. An element omega of this space is identified with the graph G on V whose edge set is E(G) = {e | omega(e) = 1_e}. The graph G is called a *random graph* on V with edge probability p (Diestel, pp. 304-306).

# Prerequisites
- **Graph** — Random graphs are graphs with a probability structure

# Key Properties
1. The events A_e (edge e is present) are independent and occur with probability p (Proposition 11.1.1)
2. A fixed graph G_0 with m edges occurs with probability p^m * q^{n choose 2 - m}
3. P is determined uniquely by p and the independence of edge events
4. The value of p may depend on n: p = p(n) is common
5. For each n separately, all edge probabilities are equal

# Construction / Recognition
## To Generate a Random Graph in G(n,p)
1. Fix the vertex set V = {0, ..., n-1}
2. For each pair {u,v} of vertices, include the edge uv with probability p, independently
3. The resulting graph is a sample from G(n,p)

# Context & Application
The G(n,p) model is the standard model for random graph theory. It was introduced by Erdős and Rényi and has become one of the most fundamental objects in probabilistic combinatorics. The model allows the use of probabilistic methods to prove existence results about deterministic graphs.

# Examples
**Example 1** (pp. 306-307): The probability that G in G(n,p) contains a fixed k-cycle is computed using indicator random variables.

**Example 2** (pp. 307-308): Erdős's probabilistic lower bound for Ramsey numbers: R(k) > 2^{k/2} using G(n, 1/2).

# Relationships
## Enables
- **Probabilistic method** — G(n,p) is the probability space for the method
- **Threshold functions** — Properties appear/disappear at critical p values
- **Almost every graph** — Properties of random graphs as n -> infinity

## Related
- **Rado graph** — The infinite random graph G(aleph_0, p) is almost surely the Rado graph

# Source Reference
Chapter 11, Section 11.1, pages 304-308.

# Verification Notes
- Definition directly from pp. 304-306
- Confidence: HIGH — formal construction of probability space
