---
concept: Topological End Space
slug: topological-end-space
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 237
section: "8.5 The topological end space"
extraction_confidence: high
aliases:
  - "|G|"
  - "Freudenthal compactification"
prerequisites:
  - end-of-a-graph
  - locally-finite-graph
extends:
  - end-of-a-graph
related:
  - topological-spanning-tree
  - topological-circle
  - topological-cycle-space
contrasts_with: []
answers_questions:
  - "What is the topological end space of a graph?"
  - "What is the Freudenthal compactification?"
---

# Quick Definition
The topological space |G| associated with a graph G and its ends is formed by adding "inner points" to each edge (making it a copy of [0,1]) and adding ends as limit points. For connected locally finite graphs, |G| is a compact Hausdorff space (the Freudenthal compactification).

# Core Definition
Given G = (V, E, Omega), the space |G| is built as follows: start with V union Omega; for every edge e = uv, add a set of continuum many inner points forming a topological edge [u,v] homeomorphic to [0,1]; define open sets via open stars around vertices and basic open neighbourhoods of ends of the form C_epsilon(S, omega) (Diestel, pp. 237-238). When G is connected and locally finite, |G| is a compact Hausdorff space (Proposition 8.5.1), called the *Freudenthal compactification* of G.

# Prerequisites
- **End of a graph** — Ends are the additional points in |G|
- **Locally finite graph** — Compactness requires local finiteness

# Key Properties
1. |G| is always Hausdorff
2. For connected locally finite G, |G| is compact (Proposition 8.5.1)
3. The closure of V is V union Omega (every end is a limit of vertices)
4. The closure of a ray is obtained by adding its end
5. |G| is metrizable iff G has a normal spanning tree (Theorem 8.5.2)
6. Every locally finite closed connected subspace is arc-connected (Lemma 8.5.4)

# Context & Application
The topological space |G| makes precise the intuition that ends are "points at infinity." By considering topological versions of paths, cycles, and spanning trees in this space, one can extend to infinite graphs parts of finite graph theory that otherwise have no infinite counterpart.

# Examples
**Example 1** (p. 238): For a connected locally finite graph, the closure of a subgraph C(S, omega) in G - S is C(S, omega) union Omega(S, omega).

**Example 2** (p. 241): A circle in |G| can contain uncountably many ends.

# Relationships
## Builds Upon
- **End of a graph** — Ends are the added points

## Enables
- **Topological spanning tree** — Arc-connected standard subspace containing all vertices and ends
- **Topological cycle space** — Based on circuits in |G|
- **Topological circle** — Homeomorphic image of S^1 in |G|

# Source Reference
Chapter 8, Section 8.5, pages 237-240 (Proposition 8.5.1, Theorem 8.5.2).

# Verification Notes
- Definition from pp. 237-238
- Confidence: HIGH — detailed formal construction
