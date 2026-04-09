---
concept: Vertex Cover
slug: vertex-cover
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
  - "cover"
  - "vertex cover of edges"
prerequisites:
  - graph
  - edge
  - vertex
extends: []
related:
  - matching
  - konigs-theorem
  - independent-set
  - edge-cover
contrasts_with:
  - matching
  - edge-cover
  - independent-set
answers_questions:
  - "What is a vertex cover?"
  - "What distinguishes a matching from a covering?"
---

# Quick Definition
A vertex cover of a graph G is a set U of vertices such that every edge of G has at least one endpoint in U.

# Core Definition
A set U of vertices in G = (V, E) is a **(vertex) cover** of E if every edge of G is incident with a vertex in U (Diestel, p. 44).

# Prerequisites
- **Graph** — vertex covers are defined within a graph
- **Edge** — the cover must meet every edge
- **Vertex** — the cover is a set of vertices

# Key Properties
1. Every edge of G has at least one endpoint in U
2. The complement V \ U is an independent set (no two vertices in V \ U are adjacent)
3. A minimum vertex cover has the smallest possible cardinality among all vertex covers
4. In bipartite graphs, min vertex cover = max matching (Konig's theorem)
5. V itself is always a (trivial) vertex cover

# Construction / Recognition
## To Verify a Vertex Cover
1. For each edge e = uv in G
2. Check that at least one of u, v lies in U
3. If all edges pass, U is a valid vertex cover

## To Find a Minimum Vertex Cover in Bipartite Graphs
1. Find a maximum matching M (using augmenting paths)
2. Construct the minimum vertex cover from M using the proof of Konig's theorem (p. 45)

# Context & Application
Vertex covers arise naturally as the dual of matchings. Any vertex cover must have at least as many vertices as any matching has edges (since each vertex in the cover can "cover" at most one matching edge). Konig's theorem states that in bipartite graphs, this obvious lower bound is tight: the minimum vertex cover has exactly as many vertices as the maximum matching has edges. In general graphs, finding a minimum vertex cover is NP-hard.

# Examples
**Example** (p. 45, Fig. 2.1.2): The vertex cover U is constructed from a maximum matching M by choosing one endpoint from each matching edge: the endpoint in B if some alternating path reaches it, and the endpoint in A otherwise.

# Relationships
## Builds Upon
- **Graph**, **vertex**, **edge** — fundamental structures

## Enables
- **Konig's theorem** — min vertex cover = max matching in bipartite graphs
- **Gallai's theorem** — relates vertex cover to independent set

## Related
- **Edge cover** — a set of edges (not vertices) meeting all vertices

## Contrasts With
- **Matching** — independent edges vs. covering vertices; dual concepts
- **Independent set** — complement of a vertex cover
- **Edge cover** — covers vertices with edges, not edges with vertices

# Common Errors
- **Error**: Confusing vertex cover with edge cover
  **Correction**: A vertex cover is a set of vertices meeting all edges; an edge cover is a set of edges meeting all vertices

# Common Confusions
- **Confusion**: Thinking a vertex cover must be minimal or minimum
  **Clarification**: Any set of vertices meeting all edges is a vertex cover, regardless of size; "minimum" is an optimization criterion

# Source Reference
Chapter 2, Section 2.1, p. 44 (pdf p. 44). Also Section 2.3.

# Verification Notes
- Definition from p. 44
- Confidence: HIGH — explicitly defined
