---
concept: Maximum Matching
slug: maximum-matching
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 44
section: "2.1 Matching in bipartite graphs"
extraction_confidence: high
aliases:
  - "optimal matching"
  - "maximum cardinality matching"
prerequisites:
  - matching
  - m-augmenting-path
extends:
  - matching
related:
  - konigs-theorem
  - vertex-cover
  - one-factor
contrasts_with:
  - maximal-matching
answers_questions:
  - "What is a maximum matching?"
  - "How do I find a maximum matching?"
---

# Quick Definition
A maximum matching is a matching with the largest possible number of edges. A matching is maximum if and only if it admits no augmenting path.

# Core Definition
A matching with the largest possible number of edges is called an **optimal** or **maximum matching**. The algorithmic problem of finding such matchings reduces to that of finding augmenting paths: if we start with any matching and keep applying augmenting paths until no further such improvement is possible, the matching obtained will always be maximum (Diestel, p. 44).

# Prerequisites
- **Matching** — a maximum matching is a matching with a maximality property
- **M-augmenting path** — the characterization and algorithm depend on augmenting paths

# Key Properties
1. Contains the largest number of edges among all matchings in G
2. Characterized by the absence of augmenting paths (Exercise 1, p. 51)
3. In a bipartite graph, |maximum matching| = |minimum vertex cover| (Konig's theorem)
4. Can be found by the augmenting path algorithm
5. A graph may have multiple maximum matchings of the same size

# Construction / Recognition
## Augmenting Path Algorithm
1. Start with any matching M (e.g., the empty matching)
2. Search for an M-augmenting path P
3. If found, replace M with M symmetric-difference E(P); this increases |M| by 1
4. Repeat steps 2-3 until no augmenting path exists
5. The resulting matching is maximum

# Context & Application
Finding maximum matchings is one of the fundamental problems in combinatorial optimization. In bipartite graphs, efficient polynomial-time algorithms exist (e.g., Hopcroft-Karp). The characterization via augmenting paths (Berge's theorem, Exercise 1) is the theoretical foundation for these algorithms. Konig's theorem provides the min-max duality: max matching = min vertex cover in bipartite graphs.

# Examples
**Example** (p. 44-45): Starting from the matching M shown in Fig. 2.1.1, the augmenting path P allows us to increase |M| by 1. Repeating until no augmenting path exists yields a maximum matching.

# Relationships
## Builds Upon
- **Matching** — a maximum matching is a matching of largest size
- **M-augmenting path** — characterizes maximality

## Enables
- **Konig's theorem** — relates maximum matching to minimum vertex cover
- **Tutte-Berge formula** — gives the size of a maximum matching in general graphs

## Related
- **One-factor** — a maximum matching that covers all vertices
- **Vertex cover** — dual object by Konig's theorem

## Contrasts With
- **Maximal matching** — a matching that cannot be extended (by adding edges), but may not be maximum

# Common Errors
- **Error**: Confusing maximum with maximal
  **Correction**: A maximal matching cannot be extended by adding an edge; a maximum matching has the most edges possible. A maximal matching can be strictly smaller than a maximum matching.

# Common Confusions
- **Confusion**: Believing a greedy algorithm always finds a maximum matching
  **Clarification**: A greedy approach (adding edges one by one) finds a maximal matching but not necessarily a maximum one; augmenting paths are needed to reach the optimum

# Source Reference
Chapter 2, Section 2.1, p. 44 (pdf p. 44). See also Exercise 1 (p. 51).

# Verification Notes
- Concept from p. 44 discussion
- Augmenting path characterization from Exercise 1, p. 51
- Confidence: HIGH — standard concept, explicitly discussed
