---
concept: Minimum Degree
slug: minimum-degree
category: connectivity
subcategory: graph-parameters
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.2 Connectivity and Menger's Theorem"
extraction_confidence: high
aliases:
  - "δ(G)"
  - "delta(G)"
prerequisites: []
extends: []
related:
  - vertex-connectivity
  - edge-connectivity
  - connectivity-inequality
contrasts_with: []
answers_questions:
  - "What is the minimum degree of a graph?"
---

# Quick Definition
The minimum degree $\delta(G)$ is the smallest degree among all vertices of $G$.

# Core Definition
The minimum degree $\delta(G)$ appears in the fundamental inequality $\kappa(G) \le \lambda(G) \le \delta(G)$: deleting all edges at a minimum-degree vertex disconnects the graph, so $\lambda(G) \le \delta(G)$ (Bollobás, p. 80).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. $\delta(G) \ge \kappa(G)$ and $\delta(G) \ge \lambda(G)$
2. $\delta(G) \ge n/2$ implies Hamiltonian (Dirac's theorem)
3. $\delta(T_r(n)) = n - \lceil n/r \rceil$

# Context & Application
Minimum degree is the simplest measure of how "well-connected" a graph is. It provides an upper bound on both vertex and edge connectivity.

# Examples
**Example** (p. 80): For $K_n$: $\delta = n-1$. For $K_{\ell,n}$ ($\ell \le n$): $\delta = \ell$.

# Relationships
## Related
- **connectivity-inequality** — $\kappa \le \lambda \le \delta$
- **vertex-connectivity** — Bounded by $\delta$

# Source Reference
Chapter III, Section III.2, page 80.

# Verification Notes
- Definition source: Direct from p. 80
- Confidence rationale: Standard definition, explicitly used
- Uncertainties: None
- Cross-reference status: Verified
