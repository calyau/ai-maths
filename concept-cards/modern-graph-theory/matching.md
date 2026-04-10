---
concept: Matching
slug: matching
category: matchings
subcategory: basic-definitions
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Flows, Connectivity and Matching"
chapter_number: 3
pdf_page: 74
section: "III.3 Matching"
extraction_confidence: high
aliases:
  - "independent edges"
  - "set of independent edges"
prerequisites: []
extends: []
related:
  - complete-matching
  - perfect-matching
  - maximum-matching
contrasts_with: []
answers_questions:
  - "What is a matching in a graph?"
  - "What distinguishes a matching from a perfect matching?"
---

# Quick Definition
A matching in a graph is a set of independent (pairwise non-adjacent) edges — no two edges in the set share a vertex.

# Core Definition
A matching in a graph is a set of independent edges; that is, a set of edges no two of which share an endpoint. In the context of bipartite graphs, matchings arise naturally from the problem of finding systems of distinct representatives (Bollobás, pp. 84-85).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. Edges in a matching are pairwise vertex-disjoint
2. A matching covers (is incident with) some subset of vertices
3. Every edge by itself is a matching of size 1
4. The empty set is a matching of size 0

# Construction / Recognition
1. Select a set of edges $M$ from $G$
2. Verify that no vertex is incident with more than one edge in $M$
3. If so, $M$ is a matching

# Context & Application
Matchings model assignment problems: marrying boys to girls, assigning workers to jobs, or selecting distinct representatives from sets. The marriage theorem (Hall's theorem) gives conditions for the existence of certain matchings.

# Examples
**Example** (p. 84): Given sets $A_1, \ldots, A_m$ of a set $X$, a set of distinct representatives $\{x_1, \ldots, x_m\}$ with $x_i \in A_i$ corresponds to a matching of size $m$ in the associated bipartite graph.

# Relationships
## Builds Upon
No prerequisites.

## Enables
- **complete-matching** — A matching covering one vertex class
- **perfect-matching** — A matching covering all vertices
- **maximum-matching** — A matching of maximum size
- **halls-theorem** — Conditions for a complete matching

## Related
- **one-factor** — A matching that is also a spanning subgraph

# Common Errors
- **Error**: Allowing two edges in a matching to share a vertex
  **Correction**: Matching edges must be pairwise vertex-disjoint

# Common Confusions
- **Confusion**: Confusing "matching" with "complete matching" or "perfect matching"
  **Clarification**: A matching is any set of independent edges; it need not cover all vertices

# Source Reference
Chapter III, Section III.3, pages 84-85.

# Verification Notes
- Definition source: Direct from pp. 84-85
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
