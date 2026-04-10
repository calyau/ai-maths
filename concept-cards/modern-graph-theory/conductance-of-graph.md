---
concept: Conductance of a Graph
slug: conductance-of-graph
category: conductance-and-mixing
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Random Walks on Graphs"
chapter_number: 9
pdf_page: 321
section: "IX.4 Conductance and Rapid Mixing"
extraction_confidence: high
aliases:
  - "isoperimetric constant"
  - "Cheeger constant"
  - "Phi_G"
prerequisites:
  - simple-random-walk
extends: []
related:
  - mixing-rate
  - rapid-mixing
  - spectral-gap-and-mixing
contrasts_with: []
answers_questions:
  - "How does conductance relate to mixing time of random walks?"
---

# Quick Definition
The conductance $\Phi_G$ of a $d$-regular graph $G$ measures the worst bottleneck: $\Phi_G = \min_{U \subset V} e(U, \bar{U}) / (d \min\{|U|, |\bar{U}|\})$, where $e(U, \bar{U})$ is the number of edges between $U$ and its complement.

# Core Definition
For a $d$-regular graph $G = (V, E)$, the conductance is $\Phi_G = \min_{U \subset V} \frac{e(U, \bar{U})}{d \min\{|U|, |\bar{U}|\}}$ (Bollobás, p. 321). More generally, for a multigraph: $\Phi_G = \min_{U \subset V} \frac{e(U, \bar{U})}{\min\{\text{vol } U, \text{vol } \bar{U}\}}$ where $\text{vol } U = \sum_{u \in U} d(u)$.

# Prerequisites
- **Simple random walk** — Conductance governs convergence of SRW

# Key Properties
1. $0 \leq \Phi_G \leq 1$
2. $\Phi_G = 0$ iff $G$ is disconnected
3. Small $\Phi_G$ means a bottleneck exists; the walk converges slowly
4. Large $\Phi_G$ means good expansion; the walk converges quickly
5. For large $n$, $\Phi_G$ can hardly exceed $1/2$
6. For $K_n$: $\Phi_{K_n} > 1/2$; for $Q^d$: $\Phi_{Q^d} = 1/d$

# Construction / Recognition
1. Enumerate (or bound) $e(U, \bar{U})/(d|U|)$ over all subsets $U$ with $|U| \leq n/2$
2. The minimum over all such $U$ gives $\Phi_G$

# Context & Application
Conductance was introduced by Jerrum and Sinclair. It quantifies the "bottleneck" in a graph: "when is $\Phi_G$ small? If for some set $U \subset V$ there are relatively few $U$-$\bar{U}$ edges; that is, if there is a 'bottleneck' in the graph. It is precisely the existence of such a bottleneck that slows down the convergence $\mathbf{p}_t \to \pi$" (p. 321).

# Examples
**Example** (p. 326): $\Phi_{K_n} > 1/2$ for $n \geq 2$.

**Example** (p. 326): $\Phi_{Q^d} = 1/d = 1/\log n$ where $n = 2^d$. The worst bottleneck is between $\{x : x_1 = 0\}$ and $\{x : x_1 = 1\}$.

# Relationships
## Builds Upon
- **simple-random-walk**

## Enables
- **rapid-mixing** — Large conductance implies rapid mixing
- **mixing-rate** — $\mu \leq 1 - \Phi_G^2/2$ (Corollary 30)
- **spectral-gap-and-mixing** — $\lambda_2 \leq 1 - \Phi_G^2$ (Corollary 31)

# Common Errors
- **Error**: Computing $\Phi_G$ by checking only a few subsets.
  **Correction**: The minimum is over all subsets; typically the worst case is not obvious.

# Common Confusions
- **Confusion**: Confusing graph conductance with edge conductance in electrical networks.
  **Clarification**: Graph conductance $\Phi_G$ is an expansion parameter; edge conductance $c_{xy}$ is the reciprocal of edge resistance. They are different concepts.

# Source Reference
Chapter IX, Section IX.4, pages 321-327.

# Verification Notes
- Definition source: Direct from p. 321
- Confidence rationale: Explicit definition with formula
- Uncertainties: None
- Cross-reference status: Verified
