---
concept: k-Connected Graph
slug: k-connected-graph
category: connectivity
subcategory: vertex-connectivity
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
  - "k-vertex-connected"
  - "k-connected"
prerequisites:
  - graph-connectivity
extends:
  - graph-connectivity
related:
  - vertex-connectivity
  - k-edge-connected-graph
  - mengers-theorem
contrasts_with:
  - k-edge-connected-graph
answers_questions:
  - "What is graph connectivity?"
  - "What distinguishes vertex connectivity from edge connectivity?"
---

# Quick Definition
For $k \ge 2$, a graph $G$ is $k$-connected if it is either $K_{k+1}$ or has at least $k+2$ vertices and no set of $k-1$ vertices separates it.

# Core Definition
For $k \ge 2$, a graph $G$ is $k$-connected if either $G$ is a complete graph $K_{k+1}$ or else it has at least $k+2$ vertices and no set of $k-1$ vertices separates it. A connected graph is also said to be 1-connected (Bollobás, p. 80).

# Prerequisites
- **Graph connectivity** — $k$-connectivity strengthens basic connectivity

# Key Properties
1. A 2-connected graph is connected, has at least 3 vertices, and has no cutvertex
2. $\kappa(K_n) = n-1$
3. If $G_1$ and $G_2$ are $k$-connected subgraphs sharing at least $k$ vertices, then $G_1 \cup G_2$ is $k$-connected
4. $\kappa(G) - 1 \le \kappa(G-x)$ for every vertex $x$
5. $\kappa(G) \le \lambda(G) \le \delta(G)$ for nontrivial graphs

# Construction / Recognition
1. Check if $G$ is $K_{k+1}$ (if so, it is $k$-connected)
2. Verify $|G| \ge k+2$
3. Verify that no set of $k-1$ vertices separates $G$
4. Equivalently (by Corollary 6): any two vertices can be joined by $k$ independent paths

# Context & Application
$k$-connectivity measures the robustness of a network: a $k$-connected graph remains connected after removing any $k-1$ vertices. This is fundamental in network reliability and the theory of Menger's theorem.

# Examples
**Example** (p. 80): $\kappa(P_\ell) = 1$, $\kappa(C_n) = 2$, $\kappa(K_n) = n-1$, $\kappa(K_{\ell,n}) = \ell$ (for $\ell \le n$).

**Counterexample** (p. 80): The graph obtained by joining a new vertex $x$ to all vertices of two disjoint copies of $K_\ell$ has $\kappa(G) = 1$ (since $x$ is a cutvertex) but $\lambda(G) = \ell$.

# Relationships
## Builds Upon
- **graph-connectivity** — $k$-connectivity strengthens it

## Enables
- **vertex-connectivity** — $\kappa(G)$ is the maximal $k$ for which $G$ is $k$-connected
- **mengers-theorem** — Characterizes $k$-connectivity via independent paths
- **block-of-graph** — Maximal 2-connected subgraphs

## Contrasts With
- **k-edge-connected-graph** — Edge removal vs. vertex removal

# Common Errors
- **Error**: Forgetting the special case $K_{k+1}$ in the definition
  **Correction**: $K_{k+1}$ is $k$-connected even though removing $k$ vertices leaves an empty graph

# Common Confusions
- **Confusion**: Thinking $k$-connected implies $k$-edge-connected with equality
  **Clarification**: $\kappa(G) \le \lambda(G)$ always, but they can differ significantly

# Source Reference
Chapter III, Section III.2, page 80.

# Verification Notes
- Definition source: Direct from p. 80
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
