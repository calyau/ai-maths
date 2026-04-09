---
concept: Graph Embedding on a Surface
slug: graph-embedding-on-surface
category: topological-graph-theory
subcategory: surfaces
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Appendix B - Surfaces"
chapter_number: null
pdf_page: 374
section: null
extraction_confidence: high
aliases:
  - "embedding in a surface"
  - "sigma: G -> S"
prerequisites:
  - surface
  - graph
extends:
  - planar-embedding
related:
  - face-on-surface
  - euler-characteristic
contrasts_with:
  - planar-embedding
answers_questions:
  - "What is a graph embedding on a surface?"
  - "How are faces defined for embedded graphs on surfaces?"
---

# Quick Definition
An embedding of a graph G in a surface S is a map that sends vertices to distinct points and edges to arcs between them, with no crossings. Faces are the connected components of S minus the image of G.

# Core Definition
"An embedding G -> S of a graph G in S is a map sigma that maps the vertices of G to distinct points in S and its edges xy to sigma(x)-sigma(y) arcs in S, so that no inner point of such an arc is the image of a vertex or lies on another arc. We then write sigma(G) for the union of all those points and arcs. A face of G in S is a component of S \ sigma(G), and the subgraph of G that sigma maps to the frontier of this face is its boundary" (Diestel, p. 363).

# Prerequisites
- **Surface** -- The target of the embedding
- **Graph** -- The object being embedded

# Key Properties
1. Vertices map to distinct points
2. Edges map to arcs (no crossings)
3. Faces are components of S \ sigma(G)
4. On the sphere, faces are always discs (for connected G)
5. On general surfaces, faces need not be discs
6. Every surface admits graph embeddings where all faces are discs

# Context & Application
Graph embeddings on surfaces generalize planar embeddings. The key difference from the plane is that faces need not be discs on general surfaces. The generalized Euler formula applies when all faces ARE discs, providing the main tool for studying surface embeddings.

# Relationships
## Builds Upon
- **Surface**, **Graph**

## Enables
- **Euler characteristic** -- n - m + l = chi(S) when all faces are discs
- **Graph minor theorem** -- Uses embeddings on surfaces

## Contrasts With
- **Planar embedding** -- Special case where S = S^2

# Source Reference
Appendix B, page 363.

# Verification Notes
- Definition from p. 363
- Confidence: HIGH -- explicit definition
