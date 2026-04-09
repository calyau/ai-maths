---
concept: "Infinite Menger's Theorem"
slug: infinite-mengers-theorem
category: infinite-graphs
tier: advanced
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Infinite Graphs"
chapter_number: 8
pdf_page: 227
section: "8.4 Connectivity and matching"
extraction_confidence: high
aliases:
  - "Erdős-Menger conjecture"
  - "Aharoni-Berger theorem"
prerequisites:
  - infinite-graph
  - separation
extends: []
related:
  - wave
contrasts_with: []
answers_questions:
  - "Does Menger's theorem extend to infinite graphs?"
---

# Quick Definition
The infinite Menger's theorem (Aharoni-Berger, 2005) states that for any graph G and vertex sets A, B, there exists a set P of disjoint A-B paths and an A-B separator consisting of exactly one vertex from each path in P.

# Core Definition
**Theorem 8.4.2** (Aharoni & Berger 2005): Let G be any graph, and let A, B be subsets of V(G). Then G contains a set P of disjoint A-B paths and an A-B separator on P (i.e., consisting of exactly one vertex from each path in P) (Diestel, p. 227).

# Prerequisites
- **Infinite graph** — The theorem addresses infinite graphs
- **Separation** — The theorem finds both paths and separators

# Key Properties
1. Originally conjectured by Erdős (the Erdős-Menger conjecture)
2. When k(G,A,B) is finite, follows easily from the finite Menger's theorem (Proposition 8.4.1)
3. When k is infinite, cardinal arithmetic makes the obvious approach trivial but wasteful
4. The proof for countable G uses "waves" — path systems that grow from A towards B

# Context & Application
This is one of the deepest results in infinite graph theory. The Erdős-Menger conjecture influenced much of the development of infinite connectivity and matching theory. The key innovation is the reformulation using separators "on" path systems rather than comparing cardinalities.

# Examples
**Example 1** (pp. 227-232): The proof for countable G constructs a maximal wave, then uses a linkability argument.

# Relationships
## Builds Upon
- **Menger's theorem** (finite) — The infinite version

## Enables
- **Infinite König's theorem** (Theorem 8.4.8)
- **Infinite matching theory**

# Source Reference
Chapter 8, Section 8.4, pages 227-232 (Theorem 8.4.2).

# Verification Notes
- Statement from p. 227
- Confidence: HIGH — named theorem with full proof for countable case
