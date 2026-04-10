---
concept: Connectivity Inequality
slug: connectivity-inequality
category: connectivity
subcategory: fundamental-results
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.2 Connectivity and Menger's Theorem"
extraction_confidence: high
aliases:
  - "κ ≤ λ ≤ δ"
  - "Whitney inequality"
prerequisites:
  - vertex-connectivity
  - edge-connectivity
extends: []
related:
  - minimum-degree
  - k-connected-graph
  - k-edge-connected-graph
contrasts_with: []
answers_questions:
  - "How does vertex connectivity relate to edge connectivity?"
---

# Quick Definition
For every nontrivial graph $G$, $\kappa(G) \le \lambda(G) \le \delta(G)$, where $\kappa$ is vertex connectivity, $\lambda$ is edge connectivity, and $\delta$ is minimum degree.

# Core Definition
If $G$ is nontrivial (has at least two vertices), then $\kappa(G) \le \lambda(G) \le \delta(G)$. The second inequality holds because deleting all edges at a minimum-degree vertex disconnects $G$. The first holds because if $\lambda(G) = k \ge 2$ and $\{x_1y_1, \ldots, x_ky_k\}$ disconnects $G$, then either $G - \{x_1, \ldots, x_k\}$ is disconnected (giving $\kappa \le k$) or each $x_i$ has degree exactly $k$, and deleting the neighbours of $x_1$ disconnects $G$ (Bollobás, p. 80).

# Prerequisites
- **Vertex connectivity** — $\kappa(G)$
- **Edge connectivity** — $\lambda(G)$

# Key Properties
1. Both inequalities can be strict simultaneously
2. $\kappa = \lambda = \delta$ when $G$ is complete
3. The gap between $\kappa$ and $\lambda$ can be arbitrarily large

# Construction / Recognition
The inequality is a theorem, not a construction. To verify:
1. Compute $\delta(G)$, $\lambda(G)$, and $\kappa(G)$
2. Check $\kappa \le \lambda \le \delta$

# Context & Application
This inequality provides the fundamental ordering of three key graph parameters. It shows vertex connectivity is the most restrictive measure of graph robustness.

# Examples
**Example** (p. 80): For the graph formed by joining two $K_\ell$ at a vertex $x$: $\kappa = 1$, $\lambda = \ell$, $\delta = \ell$.

**Example** (p. 80): For $K_n$: $\kappa = \lambda = \delta = n-1$ (all equal).

# Relationships
## Builds Upon
- **vertex-connectivity** — The smallest parameter
- **edge-connectivity** — The middle parameter

## Related
- **minimum-degree** — The largest parameter $\delta(G)$

# Common Errors
- **Error**: Assuming equality always holds
  **Correction**: All three parameters can be distinct

# Common Confusions
- **Confusion**: Thinking high minimum degree guarantees high vertex connectivity
  **Clarification**: $\kappa \le \delta$ but the gap can be large (consider the vertex joining two cliques)

# Source Reference
Chapter III, Section III.2, page 80.

# Verification Notes
- Definition source: Direct from p. 80 with proof sketch
- Confidence rationale: Explicit proof given
- Uncertainties: None
- Cross-reference status: Verified
