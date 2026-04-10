---
concept: Total Variation Distance
slug: total-variation-distance
category: conductance-and-mixing
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 325
section: "IX.4 Conductance and Rapid Mixing"
extraction_confidence: high
aliases:
  - "d_TV"
  - "d_1"
prerequisites:
  - stationary-distribution
extends: []
related:
  - mixing-rate
  - rapid-mixing
contrasts_with: []
answers_questions:
  - "How does conductance relate to mixing time of random walks?"
---

# Quick Definition
The total variation distance between the distribution $\mathbf{p}_t$ at time $t$ and the stationary distribution $\pi$ is $d_{TV}(\mathbf{p}_t, \pi) = \frac{1}{2}\|\mathbf{p}_t - \pi\|_1$, measuring how far the walk is from equilibrium.

# Core Definition
"The distance of the distribution $\mathbf{p}_t$ at time $t$ from the stationary distribution $\pi$ is usually measured by the $\ell_1$-norm of the difference, which is twice the so-called total variation distance: $d_1(t) = 2 d_{TV}(\mathbf{p}_t, \pi) = \|\mathbf{p}_t - \pi\|_1$" (Bollobás, p. 325). By Cauchy-Schwarz: $d_1(t) \leq (n d_2(t))^{1/2}$.

# Prerequisites
- **Stationary distribution** — The reference distribution for measuring distance

# Key Properties
1. $d_1(t) = \|\mathbf{p}_t - \pi\|_1 = 2 d_{TV}(\mathbf{p}_t, \pi)$
2. $d_1(t) \leq (n d_2(t))^{1/2}$ by Cauchy-Schwarz
3. $d_1(t) \leq (2n)^{1/2}(1 - \Phi_G^2/4)^{t/2}$ (Corollary 30)
4. Takes values in $[0, 2]$

# Construction / Recognition
$d_1(t) = \sum_{i=1}^n |p_i^{(t)} - 1/n|$ for a regular graph.

# Context & Application
Total variation distance is the standard measure for convergence of Markov chains. Rapid mixing requires $d_1(t) \leq \varepsilon$ after polynomially many steps in $\log n$.

# Examples
**Example**: For the LRW on a regular graph of order $n$ with conductance $\Phi_G$, after $t = 8\Phi_G^{-2}\log n \cdot \log(1/\varepsilon)$ steps, $d_1(t) < \varepsilon$.

# Relationships
## Builds Upon
- **stationary-distribution**

## Related
- **mixing-rate**, **rapid-mixing**

# Source Reference
Chapter IX, Section IX.4, page 325.

# Verification Notes
- Definition source: Direct from p. 325
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
