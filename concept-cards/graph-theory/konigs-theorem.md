---
concept: "Konig's Theorem"
slug: konigs-theorem
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 45
section: "2.1 Matching in bipartite graphs"
extraction_confidence: high
aliases:
  - "Konig's duality theorem"
  - "Konig 1931"
  - "Konig's min-max theorem"
prerequisites:
  - matching
  - vertex-cover
  - bipartite-graph
  - m-augmenting-path
extends: []
related:
  - halls-marriage-theorem
  - mengers-theorem
  - gallais-theorem
  - maximum-matching
contrasts_with: []
answers_questions:
  - "How do matchings relate to vertex covers (Konig's theorem)?"
  - "What is the min-max relationship between matchings and covers?"
---

# Quick Definition
In a bipartite graph, the maximum number of edges in a matching equals the minimum number of vertices in a vertex cover.

# Core Definition
**Theorem 2.1.1 (Konig 1931).** The maximum cardinality of a matching in a bipartite graph G is equal to the minimum cardinality of a vertex cover of its edges (Diestel, p. 45).

# Prerequisites
- **Matching** — one side of the duality
- **Vertex cover** — the other side of the duality
- **Bipartite graph** — the theorem holds specifically for bipartite graphs
- **M-augmenting path** — used in the proof

# Key Properties
1. max |M| = min |U| where M ranges over matchings and U over vertex covers
2. This is a min-max theorem: the maximum of one quantity equals the minimum of its dual
3. The theorem fails for general (non-bipartite) graphs (Exercise 18, p. 52)
4. Konig's theorem is the bipartite special case of Menger's theorem (noted in the chapter notes)
5. The proof is constructive: given a maximum matching M, a minimum vertex cover U of size |M| can be explicitly constructed

# Construction / Recognition
## Constructing the Minimum Vertex Cover (from the proof)
1. Start with a maximum matching M in the bipartite graph G = (A, B; E)
2. From each edge in M, choose one endpoint for U:
   - Choose the endpoint in B if some alternating path ends at that vertex
   - Choose the endpoint in A otherwise
3. The resulting set U has |M| vertices and covers all edges

# Context & Application
Konig's theorem is one of the earliest and most fundamental results in combinatorial optimization. It establishes a min-max duality between matchings and covers in bipartite graphs, analogous to the duality between flows and cuts in network theory. The theorem connects to linear programming duality: the matching and covering problems are LP duals, and integrality holds because the constraint matrix is totally unimodular.

Konig's theorem is no more than the bipartite case of Menger's theorem (1929), as noted by Diestel in the chapter notes (p. 53).

# Examples
**Example** (p. 45, Fig. 2.1.2): A bipartite graph with a maximum matching M (bold edges) and the minimum vertex cover U (circled vertices) constructed from M. Each vertex in U covers at least one matching edge, and |U| = |M|.

# Relationships
## Builds Upon
- **Matching**, **vertex cover**, **bipartite graph** — the three ingredients

## Enables
- **Hall's marriage theorem** — can be derived from Konig's theorem (Exercise 4)
- **Konig duality** — the general principle of min-max duality for matchings/covers
- **Gallai's theorem** — relates vertex cover to independent set sizes

## Related
- **Menger's theorem** — Konig's theorem is the bipartite special case
- **LP duality** — Konig's theorem reflects LP duality for bipartite matching

## Contrasts With
- The theorem does not hold for non-bipartite graphs (Exercise 18)

# Common Errors
- **Error**: Applying Konig's theorem to non-bipartite graphs
  **Correction**: The theorem is specific to bipartite graphs; in general graphs, the minimum vertex cover can be strictly larger than the maximum matching

# Common Confusions
- **Confusion**: Confusing Konig's theorem with Hall's theorem
  **Clarification**: Konig gives a min-max equality (max matching = min cover); Hall gives a condition for the existence of a matching of A (the marriage condition)

# Source Reference
Chapter 2, Section 2.1, Theorem 2.1.1, p. 45 (pdf p. 45). Proof on pp. 45-46.

# Verification Notes
- Theorem statement directly from p. 45
- Proof strategy from pp. 45-46
- Connection to Menger from notes, p. 53
- Confidence: HIGH — major named theorem with full proof
