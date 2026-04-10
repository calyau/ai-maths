---
concept: Vertex Connectivity
slug: vertex-connectivity
category: connectivity
subcategory: vertex-connectivity
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
  - "connectivity"
  - "κ(G)"
  - "kappa(G)"
prerequisites:
  - graph-connectivity
  - k-connected-graph
extends: []
related:
  - edge-connectivity
  - minimum-degree
contrasts_with:
  - edge-connectivity
answers_questions:
  - "What is graph connectivity?"
  - "What distinguishes vertex connectivity from edge connectivity?"
  - "How does vertex connectivity relate to edge connectivity?"
---

# Quick Definition
The vertex connectivity $\kappa(G)$ of a connected graph $G$ is the maximum $k$ for which $G$ is $k$-connected. For disconnected $G$, $\kappa(G) = 0$.

# Core Definition
The maximal value of $k$ for which a connected graph $G$ is $k$-connected is the connectivity of $G$, denoted by $\kappa(G)$. If $G$ is disconnected, we put $\kappa(G) = 0$. For a nontrivial graph, $\kappa(G) \le \lambda(G) \le \delta(G)$ (Bollobás, p. 80).

# Prerequisites
- **Graph connectivity** — Basic notion of connectedness
- **k-connected graph** — Defines what $k$-connectivity means

# Key Properties
1. $\kappa(G) \le \lambda(G) \le \delta(G)$ for nontrivial $G$
2. $\kappa(K_n) = n-1$
3. $\kappa(G) - 1 \le \kappa(G-x)$ for any vertex $x$
4. $\kappa(G) = 0$ iff $G$ is disconnected
5. $\kappa(G) = \lambda(G) = |G|-1$ when $G$ is complete

# Construction / Recognition
1. Find the minimum size of a vertex set $W$ whose removal disconnects $G$
2. $\kappa(G) = |W|$ for this minimum separating set
3. For complete graphs, $\kappa(K_n) = n-1$ by convention

# Context & Application
Vertex connectivity measures how many vertices must be removed to disconnect a graph. The inequality $\kappa(G) \le \lambda(G) \le \delta(G)$ shows that vertex connectivity is the most restrictive measure.

# Examples
**Example** (p. 80): $\kappa(P_\ell) = 1$, $\kappa(C_n) = 2$, $\kappa(K_n) = n-1$, $\kappa(K_{\ell,n}) = \ell$.

**Example** (p. 80): If $G$ is the join of two $K_\ell$ copies via a single vertex $x$, then $\kappa(G) = 1$ but $\lambda(G) = \ell$, showing the gap can be arbitrarily large.

# Relationships
## Builds Upon
- **k-connected-graph** — $\kappa(G)$ is the maximum such $k$

## Enables
- **mengers-theorem** — Characterizes $\kappa(G)$ via independent paths

## Related
- **minimum-degree** — $\kappa(G) \le \delta(G)$

## Contrasts With
- **edge-connectivity** — $\kappa(G) \le \lambda(G)$, but they can differ

# Common Errors
- **Error**: Assuming $\kappa(G) = \lambda(G)$ for all graphs
  **Correction**: These can differ; $\kappa(G) \le \lambda(G)$ always holds but equality is not guaranteed

# Common Confusions
- **Confusion**: Thinking removing $\kappa(G)$ vertices always disconnects $G$
  **Clarification**: It depends on *which* vertices are removed; $\kappa(G)$ is the minimum over all separating sets

# Source Reference
Chapter III, Section III.2, page 80.

# Verification Notes
- Definition source: Direct from p. 80
- Confidence rationale: Explicitly defined with notation
- Uncertainties: None
- Cross-reference status: Verified
