---
concept: Face
slug: face
category: planar-graphs
subcategory: plane-graphs
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.2 Plane graphs"
extraction_confidence: high
aliases:
  - "face of a plane graph"
  - "region of a plane graph"
prerequisites:
  - plane-graph
  - region
extends:
  - region
related:
  - outer-face
  - face-boundary
  - euler-formula
contrasts_with:
  - region
answers_questions:
  - "What is a face of a plane graph?"
  - "How many faces does a plane graph have?"
---

# Quick Definition
A face of a plane graph G is a region (connected component) of R^2 \ G. Every plane graph has exactly one unbounded face (the outer face) and possibly several bounded inner faces.

# Core Definition
"For every plane graph G, the set R^2 \ G is open; its regions are the faces of G" (Diestel, p. 86). The set of faces of G is denoted F(G). Since G is bounded, exactly one face is unbounded: the outer face. The other faces are inner faces. A face is incident with the vertices and edges of its boundary.

# Prerequisites
- **Plane graph** -- Faces are defined for plane graphs specifically
- **Region** -- Faces are regions of R^2 \ G

# Key Properties
1. Faces are open connected subsets of R^2
2. Exactly one face is unbounded (the outer face)
3. A plane forest has exactly one face (Proposition 4.2.4)
4. In a 2-connected plane graph, every face is bounded by a cycle (Proposition 4.2.6)
5. Different faces of a plane graph have different boundaries, unless the graph is a cycle (Lemma 4.2.5)
6. If e lies on a cycle, e bounds exactly two faces; if e lies on no cycle, it bounds exactly one face (Lemma 4.2.2)

# Construction / Recognition
## To Identify Faces
1. Draw the plane graph G in R^2
2. Remove G from R^2 to get the open set R^2 \ G
3. Find the connected components of R^2 \ G
4. Each component is a face; the unbounded component is the outer face

# Context & Application
Faces are the third fundamental component (alongside vertices and edges) in the combinatorial structure of plane graphs. Euler's formula n - m + l = 2 relates the number of vertices (n), edges (m), and faces (l) in a connected plane graph. Face boundaries in 2-connected plane graphs are cycles, and they generate the entire cycle space.

# Examples
**Example** (p. 86): A plane triangle K^3 has two faces: one triangular inner face and one unbounded outer face.

**Example** (p. 88, Proposition 4.2.4): A plane forest (tree) has exactly one face -- the entire plane minus the tree.

**Example** (p. 89): A plane cycle C has exactly two faces (by the Jordan Curve Theorem): the interior and the exterior.

# Relationships
## Builds Upon
- **Plane graph** -- Faces exist only for plane graphs
- **Region** -- Faces are specific instances of regions

## Enables
- **Euler's formula** -- n - m + l = 2
- **Plane duality** -- Dual graph vertices correspond to faces
- **Face boundary** -- The subgraph bounding each face

## Related
- **Outer face** -- The unique unbounded face

## Contrasts With
- **Region** -- Regions are general topological; faces are specific to plane graphs

# Common Errors
- **Error**: Counting faces without including the outer (unbounded) face
  **Correction**: The outer face always counts; Euler's formula requires it

- **Error**: Assuming every face boundary is a cycle
  **Correction**: Face boundaries are cycles only in 2-connected plane graphs; in general, bridges appear on the boundary of just one face

# Common Confusions
- **Confusion**: Thinking faces are an intrinsic property of an abstract graph
  **Clarification**: Faces depend on the specific plane embedding; different embeddings of the same planar graph may yield different face structures

# Source Reference
Chapter 4: Planar Graphs, Section 4.2 "Plane graphs," pages 86-89.

# Verification Notes
- Definition directly quoted from p. 86
- Properties from Lemma 4.2.2, Proposition 4.2.4, Lemma 4.2.5, Proposition 4.2.6
- Confidence: HIGH -- explicit definitions and multiple propositions
