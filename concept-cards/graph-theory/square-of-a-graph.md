---
concept: Square of a Graph
slug: square-of-a-graph
category: hamiltonian-graph-theory
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Hamilton Cycles"
chapter_number: 10
pdf_page: 291
section: "10.3 Hamilton cycles in the square of a graph"
extraction_confidence: high
aliases:
  - "G^2"
  - "graph square"
  - "power of a graph"
prerequisites:
  - graph
  - distance
extends: []
related:
  - fleischners-theorem
contrasts_with: []
answers_questions:
  - "What is the square of a graph?"
---

# Quick Definition
The square G^2 of a graph G is the graph on V(G) where two vertices are adjacent if and only if their distance in G is at most 2.

# Core Definition
Given a graph G and a positive integer d, we denote by G^d the graph on V(G) in which two vertices are adjacent if and only if they have distance at most d in G. Clearly, G = G^1 is contained in G^2 is contained in G^3, etc. (Diestel, p. 291).

# Prerequisites
- **Graph** — the square is defined for graphs
- **Distance** — adjacency in G^2 is determined by distance in G

# Key Properties
1. V(G^2) = V(G)
2. Two vertices are adjacent in G^2 iff their distance in G is <= 2
3. G is a subgraph of G^2 (edges of G are edges of G^2)
4. G^2 adds edges between vertices at distance 2 (those sharing a common neighbor)
5. Fleischner's theorem: G^2 is Hamiltonian for every 2-connected G

# Construction / Recognition
## To Construct G^2
1. Start with V(G^2) = V(G)
2. For every pair u, v of vertices:
3. If d_G(u,v) <= 2, add edge uv to G^2
4. Equivalently: uv is an edge of G^2 iff u and v are adjacent in G or share a common neighbor

# Context & Application
The square of a graph adds "shortcut" edges between vertices at distance 2. This dramatically increases connectivity, so much so that Fleischner's theorem guarantees Hamiltonicity for squares of 2-connected graphs.

# Examples
**Example**: If G is a path v1-v2-v3-v4, then G^2 has edges v1v2, v2v3, v3v4, v1v3, v2v4. G^2 is Hamiltonian: v1-v3-v2-v4-... (actually v1-v2-v4-v3-v1 for a suitable cycle).

# Relationships
## Builds Upon
- **Graph**, **distance**

## Enables
- **Fleischner's theorem** — G^2 is Hamiltonian for 2-connected G
- **Seymour's conjecture** — generalizes to higher powers

# Common Errors
- **Error**: Including vertices at distance > 2
  **Correction**: G^2 connects only vertices at distance exactly 1 or 2 in G

# Common Confusions
- **Confusion**: Confusing G^2 with G x G (Cartesian product)
  **Clarification**: G^2 is the distance-2 power graph on the same vertex set; G x G is a product on V x V

# Source Reference
Chapter 10, Section 10.3, p. 291 (pdf p. 291).

# Verification Notes
- Definition from p. 291
- Confidence: HIGH — explicitly defined
