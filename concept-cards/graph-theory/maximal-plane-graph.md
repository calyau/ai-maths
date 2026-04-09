---
concept: Maximal Plane Graph
slug: maximal-plane-graph
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
  - "maximally plane graph"
prerequisites:
  - plane-graph
  - face
extends:
  - plane-graph
related:
  - plane-triangulation
  - maximal-planar-graph
contrasts_with:
  - maximal-planar-graph
answers_questions:
  - "What is a maximal plane graph?"
  - "When can no more edges be added to a plane graph?"
---

# Quick Definition
A plane graph G is maximally plane if no new edge can be added (between existing vertices) to form a larger plane graph.

# Core Definition
"A plane graph G is called maximally plane, or just maximal, if we cannot add a new edge to form a plane graph G' with V(G') = V(G) that properly contains G" (Diestel, p. 90).

# Prerequisites
- **Plane graph** -- This is a property of a specific drawing
- **Face** -- Maximality is equivalent to every face being a triangle

# Key Properties
1. A plane graph of order >= 3 is maximally plane iff it is a plane triangulation (Proposition 4.2.8)
2. Every maximal plane graph is maximally planar (Proposition 4.4.1)
3. Has exactly 3n - 6 edges for n >= 3 (Corollary 4.2.10)

# Context & Application
The maximality concept for plane graphs is about a specific drawing: no edge can be added without creating a crossing. This is a property of the drawing, not just the abstract graph. Importantly, Proposition 4.4.1 shows that this drawing-dependent property coincides with the abstract graph property of being maximally planar.

# Examples
**Example** (p. 90): Any plane triangulation is maximally plane. K^4 drawn as a plane graph with all faces triangles is maximally plane.

# Relationships
## Builds Upon
- **Plane graph**

## Enables
- **Plane triangulation** -- Equivalent to maximal plane for n >= 3

## Contrasts With
- **Maximal planar graph** -- A maximal planar graph is an abstract graph property; a maximal plane graph is a drawing property. They coincide (Prop 4.4.1).

# Source Reference
Chapter 4, Section 4.2, page 90. Proposition 4.2.8.

# Verification Notes
- Definition from p. 90
- Confidence: HIGH -- explicit definition
