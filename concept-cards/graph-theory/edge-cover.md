---
concept: Edge Cover
slug: edge-cover
category: matching-and-covering
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Matching, Covering and Packing"
chapter_number: 2
pdf_page: 54
section: "2.3 Packing and covering"
extraction_confidence: medium
aliases:
  - "edge covering"
prerequisites:
  - graph
  - edge
  - vertex
extends: []
related:
  - vertex-cover
  - matching
  - gallais-theorem
contrasts_with:
  - vertex-cover
  - matching
answers_questions:
  - "What is an edge cover?"
  - "What distinguishes a matching from a covering?"
---

# Quick Definition
An edge cover of a graph G (with no isolated vertices) is a set of edges such that every vertex is incident with at least one edge in the set.

# Core Definition
An **edge cover** is a set F of edges such that every vertex of G is incident with at least one edge in F. This is dual to a vertex cover (which covers edges with vertices).

# Prerequisites
- **Graph**, **edge**, **vertex** — fundamental structures

# Key Properties
1. Every vertex must be incident with at least one edge in the cover
2. Edges in the cover may share endpoints (unlike a matching)
3. A graph must have no isolated vertices to have an edge cover
4. min edge cover + max matching = |V| (Gallai's identity for edge covers)
5. A matching extended by adding one edge per unmatched vertex gives an edge cover

# Construction / Recognition
## To Construct an Edge Cover from a Maximum Matching
1. Start with a maximum matching M
2. For each unmatched vertex v, add any edge incident with v
3. The result is an edge cover of size |M| + (|V| - 2|M|) = |V| - |M|

# Context & Application
Edge covers are the "edge dual" of vertex covers. Gallai's theorem for edge covers states that the minimum edge cover size plus the maximum matching size equals |V|.

# Examples
**Example**: In K3, any two edges form an edge cover (they cover all 3 vertices). The minimum edge cover has 2 edges, while the maximum matching has 1 edge, and 2 + 1 = 3 = |V|.

# Relationships
## Builds Upon
- **Graph**, **edge**, **vertex**

## Related
- **Matching** — dual relationship via Gallai's theorem
- **Gallai's theorem** — min edge cover + max matching = |V|

## Contrasts With
- **Vertex cover** — covers edges with vertices; edge cover covers vertices with edges
- **Matching** — edges in a matching must be independent; edges in an edge cover need not be

# Common Errors
- **Error**: Requiring edges in an edge cover to be independent
  **Correction**: Edge cover edges may share endpoints; only matchings require independence

# Common Confusions
- **Confusion**: Confusing edge cover with vertex cover
  **Clarification**: Edge cover uses edges to cover vertices; vertex cover uses vertices to cover edges

# Source Reference
Chapter 2, Section 2.3 context. Gallai's identity is standard.

# Verification Notes
- Concept implicit in Section 2.3's duality framework
- Confidence: MEDIUM — concept is standard but not explicitly defined in this section
