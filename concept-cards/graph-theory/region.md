---
concept: Region
slug: region
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
  - "connected component of open set"
prerequisites:
  - arc
extends: []
related:
  - face
  - frontier
  - jordan-curve-theorem
contrasts_with:
  - face
answers_questions:
  - "What is a region in the context of planar graph theory?"
---

# Quick Definition
A region of an open set O in R^2 is an equivalence class under the relation of being linked by an arc in O. Regions are the connected components of open sets.

# Core Definition
"Let O be an open subset of R^2. Being linked by an arc in O defines an equivalence relation on O. The corresponding equivalence classes are again open; they are the regions of O" (Diestel, p. 84).

# Prerequisites
- **Arc** -- Regions are defined via the equivalence relation of being linked by arcs

# Key Properties
1. Regions are equivalence classes under arc-connectivity in an open set
2. Regions are themselves open sets
3. A polygon divides R^2 into exactly two regions (Jordan Curve Theorem)
4. An arc does not create new regions (Lemma 4.1.3)

# Construction / Recognition
## To Identify Regions
1. Start with an open set O in R^2
2. Two points in O are equivalent if they can be linked by an arc lying entirely in O
3. Each equivalence class is a region of O

# Context & Application
The notion of region is the topological precursor to the graph-theoretic concept of a face. When a plane graph G is drawn in R^2, the complement R^2 \ G is open, and its regions are the faces of G. The Jordan Curve Theorem (Theorem 4.1.1) states that R^2 \ P has exactly two regions for any polygon P.

# Examples
**Example** (p. 84-85): For a polygon P in R^2, the set R^2 \ P has exactly two regions: a bounded (inner) region and an unbounded (outer) region.

**Example** (p. 85, Lemma 4.1.2): Three arcs between the same two endpoints, otherwise disjoint, create exactly three regions.

# Relationships
## Builds Upon
- **Arc** -- Used to define the equivalence relation

## Enables
- **Face** -- Faces of plane graphs are regions of R^2 \ G

## Related
- **Frontier** -- The frontier of a region separates it from the rest of the plane
- **Jordan Curve Theorem** -- Characterizes regions created by polygons

## Contrasts With
- **Face** -- A face is a region specifically of R^2 \ G for a plane graph G

# Common Errors
- **Error**: Assuming regions must be bounded
  **Correction**: Regions can be unbounded; the outer region of a polygon is unbounded

# Common Confusions
- **Confusion**: Treating "region" and "face" as identical concepts
  **Clarification**: A region is a general topological concept for open sets; a face is the specific case when the open set is the complement of a plane graph

# Source Reference
Chapter 4: Planar Graphs, Section 4.1 "Topological prerequisites," page 84.

# Verification Notes
- Definition directly quoted from p. 84
- Confidence: HIGH -- explicit definition in source
