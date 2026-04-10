---
concept: Transient Random Walk
slug: transient-random-walk
category: random-walks
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 306
section: "IX.2 Electrical Networks and Random Walks"
extraction_confidence: high
aliases:
  - "transience"
prerequisites:
  - random-walk-on-graph
  - effective-resistance
extends: []
related:
  - escape-probability
  - polyas-theorem-lattice-walks
  - monotonicity-principle
contrasts_with:
  - recurrent-random-walk
answers_questions:
  - "What distinguishes recurrent from transient random walks?"
---

# Quick Definition
A random walk on a connected, locally finite, infinite graph is transient if, starting from any vertex, there is a positive probability of never returning. Equivalently, the effective resistance to infinity is finite.

# Core Definition
"Our RW is said to be *transient* if $P_{\text{esc}}^{(\infty)} > 0$," where $P_{\text{esc}}^{(\infty)} = P_{\text{esc}}(s, \infty)$ is the probability that, starting at $s$, we never return to $s$ (Bollobás, p. 306). By Theorem 10: "The RW on a connected, locally finite, infinite electrical network is transient iff the effective resistance between a vertex $s$ and $\infty$ is finite."

# Prerequisites
- **Random walk on a graph** — Transience is a property of infinite random walks
- **Effective resistance** — Transience is characterized by finite $R_{\text{eff}}(s, \infty)$

# Key Properties
1. $P_{\text{esc}}^{(\infty)} > 0$ (positive probability of never returning)
2. $R_{\text{eff}}(s, \infty) < \infty$ (Theorem 10)
3. Independent of choice of starting vertex $s$
4. Characterized by existence of a finite-energy flow from $s$ to infinity (Theorem 13)
5. Monotonicity: cutting edges preserves transience

# Construction / Recognition
To prove transience (Theorem 13): construct a flow $(u_{xy})$ from a vertex to infinity with finite total energy $\sum u_{xy}^2 r_{xy} < \infty$.

# Context & Application
Transience means the walk "escapes to infinity" with positive probability. It is the typical behaviour in high dimensions: the SRW on $\mathbb{Z}^d$ is transient for $d \geq 3$.

# Examples
**Example** (p. 308): The SRW on $\mathbb{Z}^3$ is transient. A flow of size 1 from the origin with energy at most 1 is constructed in the positive octant.

# Relationships
## Builds Upon
- **random-walk-on-graph**, **effective-resistance**

## Enables
- **polyas-theorem-lattice-walks** — Classifies lattice walks as transient or recurrent

## Contrasts With
- **recurrent-random-walk** — Recurrent walks always return

# Common Errors
- **Error**: Thinking transience means the walk always escapes.
  **Correction**: Transience means the escape probability is positive, not that it is 1. The walk returns infinitely often with probability $1 - P_{\text{esc}}^{(\infty)}$.

# Common Confusions
- **Confusion**: Thinking transience depends on the starting vertex.
  **Clarification**: On a connected graph, transience is independent of the starting vertex.

# Source Reference
Chapter IX, Section IX.2, Theorems 10, 13, pages 306-308.

# Verification Notes
- Definition source: Direct from p. 306
- Confidence rationale: Explicit definition with characterization theorem
- Uncertainties: None
- Cross-reference status: Verified
