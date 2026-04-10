---
concept: k-Edge-Connected Graph
slug: k-edge-connected-graph
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
  - "k-edge-connected"
prerequisites:
  - graph-connectivity
extends:
  - graph-connectivity
related:
  - edge-connectivity
  - k-connected-graph
contrasts_with:
  - k-connected-graph
answers_questions:
  - "What distinguishes vertex connectivity from edge connectivity?"
---

# Quick Definition
For $k \ge 2$, a graph $G$ is $k$-edge-connected if it has at least two vertices and no set of at most $k-1$ edges separates it.

# Core Definition
For $k \ge 2$, a graph $G$ is $k$-edge-connected if it has at least two vertices and no set of at most $k-1$ edges separates it. A connected graph is 1-edge-connected (Bollobás, p. 80).

# Prerequisites
- **Graph connectivity** — $k$-edge-connectivity strengthens basic connectivity

# Key Properties
1. A 2-edge-connected graph is connected, has at least 2 vertices, and has no bridge
2. $\lambda(G) - 1 \le \lambda(G - xy) \le \lambda(G)$ for any edge $xy$
3. If $\lambda(G) = k \ge 2$, deleting $k$ edges from $G$ results in at most 2 components

# Construction / Recognition
1. Check that $G$ has at least 2 vertices
2. Verify that no set of $k-1$ or fewer edges disconnects $G$

# Context & Application
$k$-edge-connectivity measures resilience to edge failures. By Menger's theorem (edge form), a graph is $k$-edge-connected iff any two vertices can be joined by $k$ edge-disjoint paths.

# Examples
**Example** (p. 80): $C_n$ is 2-edge-connected, $K_n$ is $(n-1)$-edge-connected.

# Relationships
## Builds Upon
- **graph-connectivity** — Extends to edge-specific connectivity

## Enables
- **edge-connectivity** — $\lambda(G)$ is the maximum $k$ for $k$-edge-connectivity

## Contrasts With
- **k-connected-graph** — Vertex vs. edge removal

# Common Errors
- **Error**: Thinking $k$-edge-connected implies $k$-connected
  **Correction**: $k$-edge-connected only implies $\kappa(G) \le \lambda(G)$; vertex connectivity can be strictly smaller

# Common Confusions
- **Confusion**: Conflating bridges with cutvertices
  **Clarification**: A bridge is an edge whose removal disconnects; a cutvertex is a vertex whose removal disconnects

# Source Reference
Chapter III, Section III.2, page 80.

# Verification Notes
- Definition source: Direct from p. 80
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
