---
concept: Plane Graph
slug: plane-graph
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
  - "embedded graph"
  - "graph drawn in the plane"
prerequisites:
  - graph
  - arc
extends:
  - graph
related:
  - planar-graph
  - face
  - euler-formula
  - planar-embedding
contrasts_with:
  - planar-graph
answers_questions:
  - "What is a plane graph?"
  - "What distinguishes a plane graph from a planar graph?"
---

# Quick Definition
A plane graph is a pair (V, E) where V is a finite set of points in R^2 and E is a set of arcs between vertices, such that different edges have different endpoint sets and the interior of each edge contains no vertex or point of another edge.

# Core Definition
"A plane graph is a pair (V, E) of finite sets with the following properties: (i) V is a subset of R^2; (ii) every edge is an arc between two vertices; (iii) different edges have different sets of endpoints; (iv) the interior of an edge contains no vertex and no point of any other edge" (Diestel, p. 86).

# Prerequisites
- **Graph** -- A plane graph defines an abstract graph on V
- **Arc** -- Edges are arcs (piecewise linear curves) in R^2

# Key Properties
1. Vertices are points in R^2
2. Edges are arcs (piecewise linear curves) between vertices
3. No two distinct edges share the same pair of endpoints
4. Edge interiors are pairwise disjoint and contain no vertices
5. The complement R^2 \ G is open; its regions are the faces of G
6. Exactly one face is unbounded (the outer face)

# Construction / Recognition
## To Construct a Plane Graph
1. Place vertices at distinct points in R^2
2. For each edge, draw an arc between its endpoints
3. Ensure no two arcs cross (except at shared endpoints)
4. Ensure no arc passes through a vertex other than its own endpoints

# Context & Application
The plane graph is the concrete geometric realization of the abstract planarity concept. While a "planar graph" is an abstract graph that admits such a drawing, a "plane graph" IS such a drawing. This distinction is crucial: a planar graph may have many different plane embeddings, but each specific drawing is a single plane graph. All structural properties of plane graphs (faces, Euler's formula, face boundaries) depend on the specific drawing.

# Examples
**Example** (p. 86): Any drawing of K^4 in the plane with no edge crossings is a plane graph with 4 vertices, 6 edges, and 4 faces (including the outer face).

**Example** (p. 92): K^5 cannot be drawn as a plane graph because it has 10 > 3(5) - 6 = 9 edges, violating Corollary 4.2.10.

# Relationships
## Builds Upon
- **Graph** -- Every plane graph defines an underlying abstract graph
- **Arc** -- Edges are arcs in R^2

## Enables
- **Face** -- Faces are defined as regions of R^2 \ G
- **Euler's formula** -- Relates vertices, edges, and faces of a plane graph
- **Plane duality** -- Dual graphs are defined for plane graphs

## Related
- **Planar embedding** -- An isomorphism between an abstract graph and a plane graph

## Contrasts With
- **Planar graph** -- A planar graph CAN be drawn in the plane; a plane graph IS drawn in the plane

# Common Errors
- **Error**: Using "planar" and "plane" interchangeably
  **Correction**: "Plane" means already embedded; "planar" means embeddable. A planar graph has many possible plane representations.

# Common Confusions
- **Confusion**: Thinking every plane graph with the same abstract structure is "the same"
  **Clarification**: Two plane graphs can realize the same abstract graph but have different face structures (different embeddings)

# Source Reference
Chapter 4: Planar Graphs, Section 4.2 "Plane graphs," page 86.

# Verification Notes
- Definition directly quoted from p. 86
- Confidence: HIGH -- explicit, precise definition
- The plane/planar distinction is emphasized throughout Ch. 4
