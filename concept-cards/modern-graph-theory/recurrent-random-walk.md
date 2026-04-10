---
concept: Recurrent Random Walk
slug: recurrent-random-walk
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
  - "recurrence"
prerequisites:
  - random-walk-on-graph
  - effective-resistance
extends: []
related:
  - polyas-theorem-lattice-walks
  - monotonicity-principle
contrasts_with:
  - transient-random-walk
answers_questions:
  - "What distinguishes recurrent from transient random walks?"
---

# Quick Definition
A random walk on a connected infinite graph is recurrent if, starting from any vertex, the walk returns to that vertex with probability 1. Equivalently, the effective resistance to infinity is infinite.

# Core Definition
The RW is *recurrent* if $P_{\text{esc}}^{(\infty)} = 0$ (Bollobás, p. 306), meaning that with probability 1 the walk returns to the starting vertex. By Theorem 10, recurrence holds iff $R_{\text{eff}}(s, \infty) = \infty$. By Theorem 13, recurrence holds iff for every $\varepsilon > 0$ there exists a finitely-supported potential function with $V_s \geq 1$ and energy less than $\varepsilon$.

# Prerequisites
- **Random walk on a graph** — Recurrence is a property of infinite random walks
- **Effective resistance** — Recurrence characterized by infinite $R_{\text{eff}}(s, \infty)$

# Key Properties
1. $P_{\text{esc}}^{(\infty)} = 0$ (the walk always returns)
2. $R_{\text{eff}}(s, \infty) = \infty$ (Theorem 10)
3. The walk visits every vertex infinitely often (on a connected graph)
4. Monotonicity: shorting vertices preserves recurrence

# Construction / Recognition
To prove recurrence (Theorem 13): for every $\varepsilon > 0$, construct a finitely-supported function $(V_x)$ with $V_s \geq 1$ and $\sum (V_x - V_y)^2 c_{xy} < \varepsilon$.

# Context & Application
Recurrence means the walk "always comes home." It is the typical behaviour in low dimensions: the SRW on $\mathbb{Z}^d$ is recurrent for $d = 1, 2$.

# Examples
**Example** (p. 307-308): The SRW on $\mathbb{Z}^2$ is recurrent. Proof: short vertices at $\ell^\infty$-distance $n$ to get a one-way path with resistance $1/(8n+4)$ at step $n$; the sum $\sum 1/(8n+4)$ diverges.

# Relationships
## Builds Upon
- **random-walk-on-graph**, **effective-resistance**

## Enables
- **polyas-theorem-lattice-walks** — $\mathbb{Z}^1$ and $\mathbb{Z}^2$ are recurrent

## Contrasts With
- **transient-random-walk** — Transient walks have positive escape probability

# Common Errors
- **Error**: Thinking recurrence implies the walk stays near the starting vertex.
  **Correction**: A recurrent walk visits every vertex infinitely often; it wanders arbitrarily far but always returns.

# Source Reference
Chapter IX, Section IX.2, Theorems 10, 13, pages 306-308.

# Verification Notes
- Definition source: Direct from p. 306
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
