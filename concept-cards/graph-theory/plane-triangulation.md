---
concept: Plane Triangulation
slug: plane-triangulation
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
  - "triangulation"
  - "maximal plane graph"
prerequisites:
  - plane-graph
  - face
  - face-boundary
extends:
  - maximal-plane-graph
related:
  - maximal-planar-graph
  - euler-formula
contrasts_with: []
answers_questions:
  - "What is a plane triangulation?"
  - "When is every face of a plane graph a triangle?"
---

# Quick Definition
A plane triangulation is a plane graph in which every face (including the outer face) is bounded by a triangle (a cycle of length 3).

# Core Definition
"We call G a plane triangulation if every face of G (including the outer face) is bounded by a triangle" (Diestel, p. 90). A plane graph of order at least 3 is maximally plane if and only if it is a plane triangulation (Proposition 4.2.8).

# Prerequisites
- **Plane graph** -- A triangulation is a specific type of plane graph
- **Face** -- Every face must be triangular
- **Face boundary** -- Boundaries must be triangles (3-cycles)

# Key Properties
1. Every face (including outer) is bounded by a triangle
2. Equivalent to being maximally plane for n >= 3 (Proposition 4.2.8)
3. Has exactly 3n - 6 edges (Corollary 4.2.10)
4. Has exactly 2n - 4 faces (by Euler's formula)
5. Every edge lies on the boundary of exactly two faces

# Construction / Recognition
## To Check if a Plane Graph is a Triangulation
1. Verify n >= 3
2. Check that every face (including the outer face) is bounded by a triangle
3. Alternatively, check that the graph has exactly 3n - 6 edges and is connected

# Context & Application
Plane triangulations are maximal among plane graphs and play a central role in inductive proofs about planar graphs. Many planarity arguments reduce to the triangulation case, since any planar graph can be extended to a triangulation by adding edges. The five colour theorem proof, Thomassen's 5-choosability theorem, and many other results use triangulations as the base case.

# Examples
**Example** (p. 90): K^4 drawn in the plane is a plane triangulation with 4 vertices, 6 = 3(4) - 6 edges, and 4 = 2(4) - 4 faces.

**Example** (p. 122-123, Theorem 5.4.2): Thomassen's proof that planar graphs are 5-choosable proceeds by induction on plane triangulations.

# Relationships
## Builds Upon
- **Maximal plane graph** -- Equivalent for n >= 3

## Enables
- **Five colour theorem** -- Proof uses minimum-degree vertex in a triangulation
- **Thomassen's theorem** -- Proof by induction on triangulations
- **Maximal planar graph** -- Drawing of a maximal planar graph

## Related
- **Euler's formula** -- Gives exact edge and face counts for triangulations

# Common Errors
- **Error**: Forgetting that the outer face must also be a triangle
  **Correction**: All faces, including the outer face, must be bounded by triangles

# Source Reference
Chapter 4, Section 4.2, page 90. Proposition 4.2.8, Corollary 4.2.10.

# Verification Notes
- Definition from p. 90
- Confidence: HIGH -- explicit definition with equivalence proof
