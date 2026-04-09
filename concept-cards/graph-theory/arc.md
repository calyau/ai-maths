---
concept: Arc
slug: arc
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
  - "polygonal arc"
  - "simple arc"
  - "path in the plane"
prerequisites:
  - graph
extends: []
related:
  - polygon
  - plane-graph
  - region
contrasts_with:
  - polygon
answers_questions:
  - "What is an arc in planar graph theory?"
  - "What is a polygonal arc?"
---

# Quick Definition
An arc (polygonal arc) is a subset of R^2 that is the union of finitely many straight line segments and is homeomorphic to the closed unit interval [0,1].

# Core Definition
"A polygonal arc is a subset of R^2 which is the union of finitely many straight line segments and is homeomorphic to the closed unit interval [0,1]. The images of 0 and of 1 under such a homeomorphism are the endpoints of this polygonal arc, which links them and runs between them" (Diestel, p. 84). If P is an arc between x and y, the interior of P is denoted by P-ring = P \ {x, y}.

# Prerequisites
- **Graph** -- Arcs represent edges in plane graph drawings

# Key Properties
1. Composed of finitely many straight line segments
2. Homeomorphic to [0,1]
3. Has exactly two endpoints (images of 0 and 1)
4. The interior (denoted P-ring) excludes the endpoints
5. An arc does not separate the plane (Lemma 4.1.3)

# Construction / Recognition
## To Recognize an Arc
1. Verify the set is a union of finitely many straight line segments in R^2
2. Verify it is homeomorphic to [0,1] (i.e., it is a simple open curve with two endpoints)
3. Identify the two endpoints

# Context & Application
Arcs are the building blocks of plane graphs: each edge of a plane graph is an arc between its two endpoint vertices. Diestel simplifies the notion by restricting to piecewise linear arcs, noting that any drawing can be "straightened out in this way." The key topological fact about arcs is that they do not separate the plane (Lemma 4.1.3), in contrast to polygons which always do.

# Examples
**Example** (p. 84): A single straight line segment between two points p, q in R^2 is the simplest arc. Any piecewise-linear path from one point to another forms an arc.

**Example** (p. 85, Lemma 4.1.2): Three arcs P_1, P_2, P_3 between the same two endpoints, otherwise disjoint, divide R^2 \ (P_1 U P_2 U P_3) into exactly three regions.

# Relationships
## Builds Upon
- Basic topology of R^2

## Enables
- **Plane graph** -- Edges of plane graphs are arcs
- **Region** -- Arcs help define and relate regions of the plane
- **Jordan Curve Theorem** -- Unions of arcs form polygons

## Related
- **Polygon** -- A polygon is a closed curve (homeomorphic to S^1), formed by joining arcs

## Contrasts With
- **Polygon** -- A polygon is closed (no endpoints); an arc has two endpoints

# Common Errors
- **Error**: Assuming an arc can separate the plane
  **Correction**: Lemma 4.1.3 proves an arc does not separate the plane; only closed curves (polygons) do

# Common Confusions
- **Confusion**: Confusing "arc" with "path" in the graph-theoretic sense
  **Clarification**: An arc is a topological object in R^2; a path is a combinatorial object in a graph. In a plane graph, each edge is realized as an arc

# Source Reference
Chapter 4: Planar Graphs, Section 4.1 "Topological prerequisites," page 84. See also Lemmas 4.1.2 and 4.1.3 (p. 85).

# Verification Notes
- Definition directly adapted from p. 84
- Confidence: HIGH -- explicit definition in source
- Diestel notes: "Instead of 'polygonal arc' we shall simply say arc in this chapter"
