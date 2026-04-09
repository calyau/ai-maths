---
concept: Plane Dual
slug: plane-dual
category: planar-graphs
subcategory: plane-duality
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.6 Plane duality"
extraction_confidence: high
aliases:
  - "dual graph"
  - "geometric dual"
  - "G*"
prerequisites:
  - plane-multigraph
  - face
extends: []
related:
  - abstract-dual
  - whitney-planarity-theorem
  - plane-duality-cycle-bond
contrasts_with:
  - abstract-dual
answers_questions:
  - "What is the dual of a plane graph?"
  - "How is the dual graph constructed?"
---

# Quick Definition
The plane dual G* of a connected plane multigraph G is formed by placing a vertex inside each face of G and connecting two such vertices by an edge whenever their faces share an edge in G.

# Core Definition
A plane multigraph (V*, E*) is a plane dual of G, written G*, if there are bijections F -> V* (f -> v*(f)), E -> E* (e -> e*), V -> F* (v -> f*(v)) satisfying: (i) v*(f) lies in f; (ii) |e* intersection G| = 1 for each e, with this point interior to both e and e*; (iii) v lies in f*(v) (Diestel, pp. 103-104).

# Prerequisites
- **Plane multigraph** -- Duals are defined for plane multigraphs
- **Face** -- Vertices of the dual correspond to faces

# Key Properties
1. Vertices of G* correspond bijectively to faces of G
2. Edges of G* correspond bijectively to edges of G
3. Faces of G* correspond bijectively to vertices of G
4. G is a plane dual of G* (duality is symmetric)
5. Every connected plane multigraph has a plane dual
6. The dual is unique up to topological isomorphism
7. Cycles in G correspond to minimal cuts in G* (Proposition 4.6.1)

# Construction / Recognition
## To Construct the Plane Dual G*
1. Place one vertex v*(f) inside each face f of G
2. For each edge e of G (incident with faces f1, f2), draw an edge e* from v*(f1) to v*(f2) crossing e exactly once
3. If e is incident with only one face, draw a loop e* at the vertex in that face

# Context & Application
Plane duality is a fundamental concept linking the structure of a plane graph to its "complement" in the surface. The duality between cycles and bonds (Proposition 4.6.1) relates the cycle space and cut space, connecting planarity to algebraic structure. Whitney's theorem (4.6.3) shows that admitting an abstract dual characterizes planarity.

# Examples
**Example** (p. 103, Fig. 4.6.1): A plane graph G and its dual G* are shown, with dual vertices inside faces and dual edges crossing original edges.

**Example** (p. 108, Exercise 25): The plane dual of a plane tree is a graph with one vertex and loops.

# Relationships
## Builds Upon
- **Plane multigraph**, **Face**

## Enables
- **Whitney's planarity theorem** -- Planarity iff abstract dual exists
- **Cycle-bond duality** -- Cycles in G are cuts in G*

## Contrasts With
- **Abstract dual** -- Abstract dual is defined without reference to a plane embedding

# Common Errors
- **Error**: Expecting the dual of a simple graph to be simple
  **Correction**: The dual may have loops (from bridges) and multiple edges

# Common Confusions
- **Confusion**: Thinking the dual is defined for abstract graphs
  **Clarification**: The plane dual requires a specific embedding; different embeddings may yield non-isomorphic duals (for non-3-connected graphs)

# Source Reference
Chapter 4, Section 4.6, pages 103-104. Proposition 4.6.1.

# Verification Notes
- Definition adapted from pp. 103-104
- Confidence: HIGH -- explicit formal definition with bijections
