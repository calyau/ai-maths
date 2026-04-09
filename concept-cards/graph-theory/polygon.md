---
concept: Polygon
slug: polygon
category: planar-graphs
subcategory: topological-prerequisites
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.1 Topological prerequisites"
extraction_confidence: high
aliases:
  - "closed polygon"
  - "simple closed curve"
prerequisites:
  - graph
extends: []
related:
  - arc
  - jordan-curve-theorem
  - plane-graph
contrasts_with:
  - polygonal-arc
answers_questions:
  - "What is a polygon in the context of planar graph theory?"
  - "How is a polygon defined topologically?"
---

# Quick Definition
A polygon is a subset of the Euclidean plane that is the union of finitely many straight line segments and is homeomorphic to the unit circle S^1.

# Core Definition
A polygon is defined as "a subset of R^2 which is the union of finitely many straight line segments and is homeomorphic to the unit circle S^1, the set of points in R^2 at distance 1 from the origin" (Diestel, p. 84). The subspace topology is assumed throughout.

# Prerequisites
- **Graph** -- The polygon is a fundamental topological object used to study plane graphs and planarity

# Key Properties
1. Composed of finitely many straight line segments
2. Homeomorphic to the unit circle S^1
3. Is a closed curve (no endpoints)
4. Divides the plane into exactly two regions (Jordan Curve Theorem)
5. Each region has the entire polygon as its frontier

# Construction / Recognition
## To Recognize a Polygon
1. Verify the set is a union of finitely many straight line segments in R^2
2. Verify it is homeomorphic to S^1 (i.e., it forms a simple closed curve)

# Context & Application
The polygon is the foundational topological object in Diestel's treatment of planar graphs. It serves as the basis for the Jordan Curve Theorem for Polygons (Theorem 4.1.1), which is central to proving properties of plane graphs. By working with piecewise linear curves rather than arbitrary continuous curves, Diestel avoids unnecessary topological complication while maintaining full generality.

# Examples
**Example** (p. 84): The unit circle S^1 itself is the canonical example of a polygon (being trivially homeomorphic to itself). Any triangle, square, or regular n-gon in the plane is a polygon.

# Relationships
## Builds Upon
- Basic topology of R^2

## Enables
- **Jordan Curve Theorem** -- The JCT applies to polygons
- **Plane graph** -- Edges of plane graphs are arcs, which combine to form polygons as cycle boundaries
- **Face** -- Face boundaries in 2-connected plane graphs are polygons (cycles)

## Related
- **Arc** -- A polygonal arc is homeomorphic to [0,1] rather than S^1

## Contrasts With
- **Polygonal arc** -- An arc is an open curve with two endpoints; a polygon is closed

# Common Errors
- **Error**: Confusing a polygon with a filled region
  **Correction**: A polygon is only the boundary curve itself, not the interior

# Common Confusions
- **Confusion**: Thinking "polygon" here means the same as in elementary geometry (a filled shape)
  **Clarification**: In Diestel's usage, a polygon is specifically the curve (boundary) that is homeomorphic to S^1, not the enclosed region

# Source Reference
Chapter 4: Planar Graphs, Section 4.1 "Topological prerequisites," page 84.

# Verification Notes
- Definition directly quoted from p. 84
- Confidence: HIGH -- explicit definition in source
- The source uses "polygon" in a purely topological sense
