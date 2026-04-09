---
concept: Matching
slug: matching
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 43
section: "2.1 Matching in bipartite graphs"
extraction_confidence: high
aliases:
  - "independent edge set"
prerequisites:
  - graph
  - edge
  - vertex
extends: []
related:
  - matched-vertex
  - maximum-matching
  - one-factor
  - vertex-cover
contrasts_with:
  - vertex-cover
  - edge-cover
answers_questions:
  - "What is a matching?"
  - "What distinguishes a matching from a covering?"
---

# Quick Definition
A matching in a graph G = (V, E) is a set M of independent (i.e., pairwise non-adjacent) edges. Equivalently, no two edges in M share an endpoint.

# Core Definition
A set M of independent edges in a graph G = (V, E) is called a **matching**. M is a matching of U (where U is a subset of V) if every vertex in U is incident with an edge in M (Diestel, p. 43).

# Prerequisites
- **Graph** — A matching is defined within a graph
- **Edge** — A matching is a set of edges with a specific independence property
- **Vertex** — Vertices are matched or unmatched relative to M

# Key Properties
1. No two edges in a matching share a vertex
2. A matching M of a set U covers every vertex in U
3. A matching can be empty (the trivial matching)
4. The size of a matching is the number of edges it contains
5. In a bipartite graph G = (A, B; E), a matching of A pairs every vertex of A with a distinct vertex of B

# Construction / Recognition
## To Verify a Matching
1. Examine each pair of edges in M
2. Check that no two edges share an endpoint
3. If all pairs pass, M is a valid matching

## To Find a Maximum Matching (Augmenting Path Method)
1. Start with any matching M (possibly empty)
2. Search for an M-augmenting path
3. If found, augment M along this path to increase |M| by 1
4. Repeat until no augmenting path exists
5. The resulting matching is maximum (Exercise 1, p. 51)

# Context & Application
Matchings are the central objects of Chapter 2. The matching problem asks: given a graph, find as many independent edges as possible, ideally pairing up all vertices. This has applications in assignment problems (e.g., matching workers to jobs). The marriage theorem (Hall's theorem) characterizes when a complete matching of one side of a bipartite graph exists.

# Examples
**Example** (p. 43-44): In a bipartite graph G with bipartition {A, B}, a matching M is depicted in Fig. 2.1.1, where bold edges form the matching and an augmenting path P is shown that can increase the matching size.

# Relationships
## Builds Upon
- **Graph**, **edge**, **vertex** — fundamental structures

## Enables
- **Maximum matching** — a matching of largest possible size
- **One-factor** — a matching that covers all vertices
- **Konig's theorem** — relates maximum matching to minimum vertex cover
- **Hall's marriage theorem** — characterizes existence of complete bipartite matchings

## Related
- **Matched vertex** — a vertex incident with an edge of M
- **M-alternating path** — path alternating between M and non-M edges
- **M-augmenting path** — alternating path that can enlarge M

## Contrasts With
- **Vertex cover** — a set of vertices (not edges) covering all edges
- **Edge cover** — a set of edges covering all vertices (edges may share endpoints)

# Common Errors
- **Error**: Including two edges that share an endpoint in a matching
  **Correction**: Every vertex can be incident with at most one edge of M

- **Error**: Confusing a matching of A with a matching of V
  **Correction**: A matching of A covers all of A but may leave vertices of B unmatched; a matching of V (a 1-factor) covers all vertices

# Common Confusions
- **Confusion**: Believing a matching must cover all vertices
  **Clarification**: A matching may leave vertices unmatched; only a perfect matching (1-factor) covers all vertices

- **Confusion**: Confusing matching (independent edges) with covering (meeting all edges)
  **Clarification**: A matching maximizes independent edges; a cover minimizes vertices meeting all edges. They are dual concepts related by Konig's theorem

# Source Reference
Chapter 2: Matching, Covering and Packing, p. 43 (pdf p. 43). Opening definition of the chapter.

# Verification Notes
- Definition directly from p. 43, paragraph 1
- Confidence: HIGH — explicitly defined as the opening concept of Chapter 2
