---
concept: Excess Probability
slug: excess-probability
category: conductance-and-mixing
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 322
section: "IX.4 Conductance and Rapid Mixing"
extraction_confidence: high
aliases:
  - "e_{i,t}"
  - "d_2(t)"
prerequisites:
  - stationary-distribution
  - lazy-random-walk
extends: []
related:
  - conductance-bound-on-eigenvalue
  - total-variation-distance
contrasts_with: []
answers_questions:
  - "How does conductance relate to mixing time of random walks?"
---

# Quick Definition
The excess probability at vertex $i$ at time $t$ is $e_{i,t} = p_i^{(t)} - 1/n$, measuring deviation from the stationary distribution. The squared $\ell_2$-distance is $d_2(t) = \sum_i e_{i,t}^2$.

# Core Definition
For a $d$-regular graph with uniform stationary distribution $\pi = (1/n, \ldots, 1/n)$: $e_{i,t} = p_i^{(t)} - 1/n$ and $d_2(t) = \|\mathbf{p}_t - \pi\|_2^2 = \sum_{i=1}^n e_{i,t}^2$ (Bollobás, p. 322). For the LRW: $e_{i,t+1} = \frac{1}{2d}\sum_{j \in \Gamma(i)}(e_{i,t} + e_{j,t})$ (equation (31)).

# Prerequisites
- **Stationary distribution** — Excess is deviation from it
- **Lazy random walk** — The walk being analyzed

# Key Properties
1. $\sum_i e_{i,t} = 0$ always (probabilities sum to 1)
2. $d_2(0) \leq 2$ for any initial distribution
3. $d_2(t+1) \leq (1 - \Phi_G^2/4) d_2(t)$ (Theorem 27)
4. $d_1(t) \leq (n d_2(t))^{1/2}$ by Cauchy-Schwarz

# Relationships
## Builds Upon
- **stationary-distribution**, **lazy-random-walk**

## Enables
- **conductance-bound-on-eigenvalue** — Theorem 27 bounds $d_2$

## Related
- **total-variation-distance** — $d_1 \leq \sqrt{n \cdot d_2}$

# Source Reference
Chapter IX, Section IX.4, pages 322-323. Equation (31).

# Verification Notes
- Definition source: Direct from p. 322
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
