---
concept: Edge Connectivity
slug: edge-connectivity
category: connectivity
subcategory: edge-connectivity
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
  - "λ(G)"
  - "lambda(G)"
prerequisites:
  - graph-connectivity
  - k-edge-connected-graph
extends: []
related:
  - vertex-connectivity
  - minimum-degree
contrasts_with:
  - vertex-connectivity
answers_questions:
  - "How does vertex connectivity relate to edge connectivity?"
  - "What distinguishes vertex connectivity from edge connectivity?"
---

# Quick Definition
The edge-connectivity $\lambda(G)$ of a graph is the maximum $k$ for which $G$ is $k$-edge-connected, i.e., the minimum number of edges whose removal disconnects $G$.

# Core Definition
The edge-connectivity $\lambda(G)$ is defined analogously to vertex connectivity: it is the maximal value of $k$ for which $G$ is $k$-edge-connected. For a nontrivial graph, $\kappa(G) \le \lambda(G) \le \delta(G)$, where $\delta(G)$ is the minimum degree (Bollobás, p. 80).

# Prerequisites
- **Graph connectivity** — Basic connectedness
- **k-edge-connected graph** — Defines $k$-edge-connectivity

# Key Properties
1. $\lambda(G) \le \delta(G)$ since deleting all edges at a minimum-degree vertex disconnects $G$
2. $\kappa(G) \le \lambda(G)$
3. $\lambda(G) - 1 \le \lambda(G - xy) \le \lambda(G)$ for any edge $xy$
4. $\lambda(K_n) = n-1$
5. $\lambda(K_{\ell,n}) = \ell$ for $\ell \le n$

# Construction / Recognition
1. Find the minimum number of edges whose removal disconnects $G$
2. This minimum is $\lambda(G)$

# Context & Application
Edge connectivity measures network resilience against link failures. It is always at least as large as vertex connectivity and at most as large as the minimum degree.

# Examples
**Example** (p. 80): $\lambda(P_\ell) = 1$, $\lambda(C_n) = 2$, $\lambda(K_n) = n-1$.

**Example** (p. 80): If $G$ is obtained from two $K_\ell$ joined at a new vertex $x$, then $\kappa(G) = 1$ but $\lambda(G) = \ell$.

# Relationships
## Builds Upon
- **k-edge-connected-graph** — $\lambda(G)$ is the maximum such $k$

## Enables
- **mengers-theorem** — Edge form characterizes edge connectivity

## Contrasts With
- **vertex-connectivity** — $\kappa(G) \le \lambda(G)$, can differ significantly

# Common Errors
- **Error**: Confusing edge-connectivity with minimum degree
  **Correction**: $\lambda(G) \le \delta(G)$ but they can differ

# Common Confusions
- **Confusion**: Assuming $\lambda(G-x)$ is at most $\lambda(G) - 1$ for all $x$
  **Clarification**: $\lambda(G-x)$ can drop to 0 even when $\lambda(G)$ is large (e.g., when $x$ is a cutvertex)

# Source Reference
Chapter III, Section III.2, page 80.

# Verification Notes
- Definition source: Direct from p. 80
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
