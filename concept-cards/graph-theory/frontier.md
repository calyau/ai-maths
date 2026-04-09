---
concept: Frontier
slug: frontier
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
  - "topological boundary"
  - "boundary of a set"
prerequisites:
  - region
extends: []
related:
  - arc
  - face-boundary
  - jordan-curve-theorem
contrasts_with: []
answers_questions:
  - "What is the frontier of a set in the plane?"
  - "How does the frontier relate to separation?"
---

# Quick Definition
The frontier of a set X in R^2 is the set of all points y such that every neighbourhood of y meets both X and R^2 \ X. It acts as the topological boundary between a set and its complement.

# Core Definition
"The frontier of a set X in R^2 is the set Y of all points y in R^2 such that every neighbourhood of y meets both X and R^2 \ X" (Diestel, p. 84). If X is open, its frontier lies in R^2 \ X.

# Prerequisites
- **Region** -- Frontiers are typically studied as frontiers of regions

# Key Properties
1. If X is open, the frontier of X lies in R^2 \ X
2. The frontier of a region O (of R^2 \ X, where X is a finite union of points and arcs) separates O from the rest of R^2
3. Accessibility: if x in X lies on the frontier of O, then x can be linked to some point in O by a straight line segment whose interior lies wholly inside O
4. Any two points on the frontier of O can be linked by an arc whose interior lies in O

# Construction / Recognition
## To Identify the Frontier of a Set X
1. For each point y in R^2, check if every neighbourhood of y intersects both X and R^2 \ X
2. Collect all such points y; this is the frontier of X

# Context & Application
The frontier is the topological analogue of the "boundary" concept used for faces of plane graphs. The frontier of a face of a plane graph turns out to be the point set of a subgraph (Corollary 4.2.3), which is the face boundary. The accessibility property of frontiers is used repeatedly in proofs about plane graphs.

# Examples
**Example** (p. 84): For a polygon P, the frontier of each of the two regions of R^2 \ P is the entire polygon P (by the Jordan Curve Theorem).

# Relationships
## Builds Upon
- **Region** -- Frontiers are frontiers of regions

## Enables
- **Face boundary** -- The boundary of a face is the subgraph forming its frontier
- **Plane graph** -- Frontier properties are essential to proving structural results about plane graphs

## Related
- **Jordan Curve Theorem** -- States that each region of R^2 \ P has P as its frontier

# Common Errors
- **Error**: Confusing "frontier" with the interior boundary of a face
  **Correction**: The frontier includes all limit points between a set and its complement

# Common Confusions
- **Confusion**: Thinking "frontier" and "boundary" are interchangeable
  **Clarification**: In Diestel, "frontier" is the topological term; "boundary" is reserved for the subgraph bounding a face of a plane graph

# Source Reference
Chapter 4: Planar Graphs, Section 4.1 "Topological prerequisites," page 84.

# Verification Notes
- Definition directly quoted from p. 84
- Confidence: HIGH -- explicit definition in source
