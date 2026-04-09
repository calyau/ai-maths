---
concept: Jordan Curve Theorem (for Polygons)
slug: jordan-curve-theorem
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
  - "JCT"
  - "Jordan Curve Theorem for Polygons"
  - "Theorem 4.1.1"
prerequisites:
  - polygon
  - region
  - frontier
extends: []
related:
  - face
  - plane-graph
  - separation
contrasts_with: []
answers_questions:
  - "What does the Jordan Curve Theorem say?"
  - "How many regions does a simple closed curve create in the plane?"
---

# Quick Definition
The Jordan Curve Theorem for Polygons states that for every polygon P in R^2, the set R^2 \ P has exactly two regions, and each region has the entire polygon P as its frontier.

# Core Definition
**Theorem 4.1.1** (Jordan Curve Theorem for Polygons): "For every polygon P in R^2, the set R^2 \ P has exactly two regions. Each of these has the entire polygon P as its frontier" (Diestel, p. 84).

# Prerequisites
- **Polygon** -- The theorem applies to polygons (subsets homeomorphic to S^1)
- **Region** -- The conclusion is stated in terms of regions
- **Frontier** -- The conclusion involves the frontier of each region

# Key Properties
1. Every polygon divides the plane into exactly two regions
2. One region is bounded (the interior), the other unbounded (the exterior)
3. Both regions have the entire polygon as their frontier
4. This is stated without proof as a foundational topological fact

# Construction / Recognition
Not applicable -- this is a theorem, not a constructive concept.

# Context & Application
The Jordan Curve Theorem is one of the most fundamental results underlying all of planar graph theory. In Diestel's approach, it is stated for polygons (piecewise linear curves) rather than arbitrary continuous simple closed curves, which simplifies the proof. The theorem is used repeatedly: in showing that cycle edges bound exactly two faces (Lemma 4.2.2), in proving Euler's formula, in the five colour theorem proof, and throughout the planarity criteria.

# Examples
**Example** (p. 84): A triangle in the plane divides R^2 into an interior triangular region and an exterior unbounded region.

**Example** (p. 85, Lemma 4.1.2): Three arcs between the same two endpoints form pairs of polygons, each dividing the plane into two regions; the three arcs together create three regions.

# Relationships
## Builds Upon
- **Polygon**, **Region**, **Frontier**

## Enables
- **Face** -- Faces of plane graphs are regions created by cycle boundaries
- **Euler's formula** -- The proof relies on the JCT
- **Five colour theorem** -- The proof uses the JCT to separate vertices
- **Plane duality** -- Cycle-cut duality relies on the JCT

## Related
- **Separation** -- The JCT is the fundamental separation result
- **Jordan-Schoenflies theorem** -- Extends the JCT to homeomorphisms between regions

# Common Errors
- **Error**: Applying the JCT to arcs (open curves)
  **Correction**: The JCT applies only to polygons (closed curves homeomorphic to S^1); arcs do not separate the plane

# Common Confusions
- **Confusion**: Thinking the JCT is trivially obvious and does not need stating
  **Clarification**: The result is intuitively clear but topologically deep; Diestel isolates it as a foundational fact to avoid repeating topological arguments

# Source Reference
Chapter 4: Planar Graphs, Section 4.1 "Topological prerequisites," Theorem 4.1.1, page 84.

# Verification Notes
- Theorem statement directly quoted from p. 84
- Confidence: HIGH -- explicitly stated theorem
- Diestel presents this without proof as a "basic topological fact needed later"
