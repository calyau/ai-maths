---
concept: Stationary Distribution
slug: stationary-distribution
category: random-walks
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 310
section: "IX.3 Hitting Times and Commute Times"
extraction_confidence: high
aliases:
  - "steady-state distribution"
  - "equilibrium distribution"
prerequisites:
  - transition-probability-matrix
  - simple-random-walk
extends: []
related:
  - detailed-balance-equations
  - mean-return-time
  - mixing-rate
contrasts_with: []
answers_questions:
  - "What must I know before understanding random walks on graphs?"
---

# Quick Definition
The stationary distribution $\pi$ of a random walk is a probability distribution satisfying $\pi P = \pi$. For the SRW on a connected graph, $\pi_x = d(x)/2m$.

# Core Definition
A probability distribution $\pi = (\pi_x)_{x \in V}$ is stationary for transition matrix $P$ if $\pi P = \pi$, meaning that if the walk starts from distribution $\pi$, it remains at $\pi$ after each step. For the SRW: $\pi_x = d(x)/2m$, and each edge transmits probability $1/2m$ in either direction under $\pi$ (Bollobás, p. 310).

# Prerequisites
- **Transition probability matrix** — $\pi$ is the left eigenvector of $P$ with eigenvalue 1
- **Simple random walk** — The default setting where $\pi_x = d(x)/2m$

# Key Properties
1. $\pi P = \pi$: invariant under one step of the walk
2. For SRW: $\pi_x = d(x)/2m$
3. Satisfies detailed balance: $\pi_x P_{xy} = \pi_y P_{yx} = 1/2m$ for edges $xy$
4. On non-bipartite connected graphs, $\mathbf{p}_t \to \pi$ for any initial distribution
5. On bipartite graphs, convergence may fail but Cesaro averages converge
6. $H(x,x) = 1/\pi_x$ (equation (21))

# Construction / Recognition
For SRW on a graph with $n$ vertices and $m$ edges: $\pi_x = d(x)/2m$ for each vertex $x$.

# Context & Application
The stationary distribution describes the long-run behaviour of a random walk: the fraction of time spent at vertex $x$ converges to $\pi_x$ (Theorem 15). For regular $d$-regular graphs, $\pi = (1/n, \ldots, 1/n)$ is uniform.

# Examples
**Example** (p. 310): For a regular graph of degree $d$: $\pi_x = d/2m = 1/n$, the uniform distribution.

# Relationships
## Builds Upon
- **transition-probability-matrix**

## Enables
- **mixing-rate** — Measures speed of convergence to $\pi$
- **mean-return-time** — $H(x,x) = 1/\pi_x$

## Related
- **detailed-balance-equations** — Imply stationarity

# Common Errors
- **Error**: Assuming the SRW always converges to the stationary distribution.
  **Correction**: On bipartite graphs, the distribution oscillates; convergence holds only for non-bipartite connected graphs.

# Source Reference
Chapter IX, Section IX.3, pages 310-311. Theorem 15.

# Verification Notes
- Definition source: Direct from p. 310
- Confidence rationale: Explicit definition with formula
- Uncertainties: None
- Cross-reference status: Verified
