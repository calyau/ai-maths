---
concept: Power of a Graph
slug: power-of-graph
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
  - "G^d"
  - "d-th power"
prerequisites:
  - graph
  - distance
extends:
  - square-of-a-graph
related:
  - fleischners-theorem
  - seymours-conjecture
contrasts_with: []
answers_questions:
  - "What is the d-th power of a graph?"
---

# Quick Definition
The d-th power G^d of a graph G is the graph on V(G) where two vertices are adjacent iff their distance in G is at most d. G = G^1 is a subgraph of G^2 is a subgraph of G^3, etc.

# Core Definition
Given a graph G and a positive integer d, **G^d** denotes the graph on V(G) in which two vertices are adjacent if and only if they have distance at most d in G. Clearly, G = G^1 is a subgraph of G^2 is a subgraph of G^3, etc. (Diestel, p. 291).

# Prerequisites
- **Graph** — G^d is defined for any graph G
- **Distance** — adjacency in G^d is determined by distance in G

# Key Properties
1. V(G^d) = V(G) for all d
2. G^d adds edges between vertices at distance <= d in G
3. G^1 = G; G^2 = square of G; G^3 = cube of G
4. G^3 of a connected graph is Hamiltonian (Exercise 12)
5. Seymour's conjecture relates powers to Hamilton cycles

# Context & Application
Graph powers increase connectivity by adding shortcut edges. Higher powers make it easier to find Hamilton cycles. Fleischner's theorem (d=2 for 2-connected G) and Exercise 12 (d=3 for connected G) illustrate this.

# Examples
**Example**: For a path P_n, P_n^2 adds edges between vertices at distance 2. P_n^3 connects vertices up to distance 3 apart, and is always Hamiltonian for n >= 3.

# Relationships
## Builds Upon
- **Square of a graph** — G^2 is the d=2 case

## Related
- **Fleischner's theorem** — G^2 Hamiltonian for 2-connected G
- **Seymour's conjecture** — relates powers of Hamilton cycles to minimum degree

# Source Reference
Chapter 10, Section 10.3, p. 291 (pdf p. 291).

# Verification Notes
- Definition from p. 291
- Confidence: HIGH — explicitly defined
