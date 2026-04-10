---
concept: Graph Connectivity
slug: graph-connectivity
category: connectivity
subcategory: basic-definitions
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
  - "connected graph"
  - "connected"
  - "disconnected"
prerequisites: []
extends: []
related:
  - vertex-connectivity
  - edge-connectivity
  - component-of-graph
contrasts_with:
  - disconnected-graph
answers_questions:
  - "What is graph connectivity?"
---

# Quick Definition
A graph is connected if any two of its vertices can be joined by a path; otherwise it is disconnected.

# Core Definition
A graph is connected if any two of its vertices can be joined by a path, and otherwise it is disconnected. A maximal connected subgraph of a graph $G$ is a component of $G$. A connected graph is also said to be 1-connected and 1-edge-connected (Bollobás, p. 80).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. A connected graph has exactly one component
2. Every graph decomposes uniquely into its components
3. 1-connected = connected
4. Connectivity can be strengthened to $k$-connectivity for higher robustness

# Construction / Recognition
1. Starting from any vertex, perform a traversal (BFS or DFS)
2. If all vertices are reached, the graph is connected
3. Otherwise, the unreached vertices form separate components

# Context & Application
Connectivity is the most basic structural property of graphs. It is the starting point for the theory of $k$-connectivity and Menger's theorem, which is "the basic result in the theory of connectivity" (p. 80).

# Examples
**Example** (p. 80): $\kappa(P_\ell) = \lambda(P_\ell) = 1$ for paths of length $\ell \ge 1$, $\kappa(C_n) = \lambda(C_n) = 2$ for cycles, $\kappa(K_n) = \lambda(K_n) = n-1$ for complete graphs.

# Relationships
## Builds Upon
No prerequisites.

## Enables
- **vertex-connectivity** — Strengthened form of connectivity
- **edge-connectivity** — Edge version of connectivity
- **k-connected-graph** — Higher connectivity

## Related
- **component-of-graph** — Maximal connected subgraphs

## Contrasts With
- **disconnected-graph** — A graph that is not connected

# Common Errors
- **Error**: Confusing "connected" with "2-connected"
  **Correction**: A connected graph may have cutvertices; 2-connected requires no cutvertex (and at least 3 vertices)

# Common Confusions
- **Confusion**: Thinking connectivity is a binary property
  **Clarification**: Connectivity is quantified by $\kappa(G)$, which measures the degree of connectedness

# Source Reference
Chapter III, Section III.2, page 80.

# Verification Notes
- Definition source: Direct from p. 80
- Confidence rationale: Standard definition explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
