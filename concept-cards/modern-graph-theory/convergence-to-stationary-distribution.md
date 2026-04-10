---
concept: Convergence to the Stationary Distribution
slug: convergence-to-stationary-distribution
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
aliases: []
prerequisites:
  - stationary-distribution
  - simple-random-walk
extends: []
related:
  - mixing-rate
  - conductance-of-graph
contrasts_with: []
answers_questions:
  - "What must I know before understanding random walks on graphs?"
---

# Quick Definition
On a connected non-bipartite graph, the distribution $\mathbf{p}_t = \mathbf{p}_0 P^t$ of the SRW converges to the stationary distribution $\pi = (d(x)/2m)_x$ for any initial distribution $\mathbf{p}_0$.

# Core Definition
"If $G$ is not bipartite then it is easily seen that $\mathbf{p}^k = \mathbf{p}P^k$ does tend to $\pi$" (Bollobás, p. 310). In particular, $\mathbb{P}(X_j = x | X_i = y) \to \pi_x = d(x)/2m$ as $j \to \infty$ (equation (15)). On bipartite graphs, convergence fails but $S_k(x)/k \to \pi_x$ in probability (Theorem 15).

# Prerequisites
- **Stationary distribution** — The limit of convergence
- **Simple random walk** — The walk that converges

# Key Properties
1. Convergence holds for non-bipartite connected graphs
2. Rate of convergence governed by the second-largest eigenvalue (Theorem 26)
3. Even on bipartite graphs: time averages converge (Theorem 15)
4. The SRW visits each vertex $x$ a fraction $\pi_x$ of the time in the long run

# Context & Application
Convergence to stationarity is fundamental for algorithmic applications: after enough steps, the walk samples from (approximately) the stationary distribution, enabling approximate counting and random generation.

# Relationships
## Builds Upon
- **stationary-distribution**, **simple-random-walk**

## Enables
- **mixing-rate** — Quantifies the speed of convergence
- **conductance-of-graph** — Bounds the convergence speed

# Source Reference
Chapter IX, Section IX.3, Theorem 15, pages 310-311.

# Verification Notes
- Definition source: Synthesized from p. 310 and Theorem 15
- Confidence rationale: Explicit discussion with theorem
- Uncertainties: None
- Cross-reference status: Verified
