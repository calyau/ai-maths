---
concept: Planar Embedding
slug: planar-embedding
category: planar-graphs
subcategory: drawings
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.3 Drawings"
extraction_confidence: high
aliases:
  - "embedding in the plane"
  - "drawing of a graph"
prerequisites:
  - planar-graph
  - plane-graph
extends: []
related:
  - equivalent-embeddings
  - topological-isomorphism
  - combinatorial-isomorphism
contrasts_with: []
answers_questions:
  - "What is a planar embedding?"
  - "What is a drawing of a graph?"
---

# Quick Definition
A planar embedding of an abstract graph G is an isomorphism between G and a plane graph H. The plane graph H is called a drawing of G.

# Core Definition
"An embedding in the plane, or planar embedding, of an (abstract) graph G is an isomorphism between G and a plane graph H. The latter will be called a drawing of G" (Diestel, p. 92).

# Prerequisites
- **Planar graph** -- Only planar graphs admit embeddings
- **Plane graph** -- The target of the embedding

# Key Properties
1. An embedding maps abstract vertices and edges to points and arcs in R^2
2. Different embeddings of the same graph may yield different face structures
3. For 3-connected graphs, all embeddings are equivalent (Whitney's theorem 4.3.2)
4. Two embeddings are equivalent if the canonical isomorphism between their images preserves face structure

# Context & Application
Embeddings connect the abstract world of graph theory to the geometric world of plane graphs. The central question of Section 4.3 is how two embeddings of the same graph can differ. The answer (Theorem 4.3.2) is that for 3-connected graphs, they cannot differ in any essential way.

# Examples
**Example** (p. 93, Fig. 4.3.1): Two drawings of the same graph that are not topologically isomorphic, showing that embeddings can genuinely differ.

# Relationships
## Builds Upon
- **Planar graph** -- Must be planar to admit an embedding
- **Plane graph** -- The image of the embedding

## Enables
- **Equivalent embeddings** -- When two embeddings produce "the same" drawing
- **Whitney's theorem** -- Uniqueness of embeddings for 3-connected graphs

## Related
- **Topological isomorphism**, **Combinatorial isomorphism** -- Criteria for comparing embeddings

# Source Reference
Chapter 4, Section 4.3 "Drawings," page 92.

# Verification Notes
- Definition directly quoted from p. 92
- Confidence: HIGH -- explicit definition
