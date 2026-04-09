---
concept: Straight-Line Drawing
slug: straight-line-drawing
category: planar-graphs
subcategory: drawings
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Planar Graphs"
chapter_number: 4
pdf_page: 94
section: "4.4 Planar graphs: Kuratowski's theorem"
extraction_confidence: high
aliases:
  - "Fary's theorem"
  - "rectilinear drawing"
prerequisites:
  - planar-graph
  - plane-graph
extends:
  - planar-embedding
related:
  - plane-triangulation
contrasts_with: []
answers_questions:
  - "Can every planar graph be drawn with straight edges?"
---

# Quick Definition
A straight-line drawing of a graph is a plane drawing where every edge is a single straight line segment (not a piecewise-linear arc). Every planar graph admits a straight-line drawing (Fary's theorem).

# Core Definition
Diestel notes that the proof of the 3-connected case of Kuratowski's theorem "can easily be adapted to produce a drawing in which every inner face is convex; in particular, every edge can be drawn straight" (p. 99). Exercise 12 asks to prove that every plane graph has a straight-line drawing.

# Prerequisites
- **Planar graph** and **Plane graph**

# Key Properties
1. Every planar graph has a straight-line drawing (Fary's theorem)
2. For 3-connected planar graphs, there is a drawing with all inner faces convex
3. Convex inner faces imply straight edges
4. Related to Steinitz's theorem: 3-connected planar graphs are polyhedral skeletons

# Context & Application
The existence of straight-line drawings shows that the piecewise-linear definition of plane graphs is not essential -- any plane graph can be redrawn with straight edges. This is both practically useful (for graph visualization) and theoretically important (for connecting planarity to convex geometry).

# Relationships
## Builds Upon
- **Planar graph**

## Related
- **Plane triangulation** -- The inductive construction is for triangulations

# Source Reference
Chapter 4, pages 99 and 107 (Exercise 12).

# Verification Notes
- Referenced on p. 99 and Exercise 12
- Confidence: HIGH -- well-known classical result
