---
concept: Outer Face
slug: outer-face
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
  - "unbounded face"
  - "infinite face"
  - "exterior face"
prerequisites:
  - face
  - plane-graph
extends:
  - face
related:
  - inner-face
  - euler-formula
contrasts_with:
  - inner-face
answers_questions:
  - "What is the outer face of a plane graph?"
---

# Quick Definition
The outer face of a plane graph G is the unique unbounded face -- the face containing R^2 \ D for any sufficiently large disc D enclosing G.

# Core Definition
"Since G is bounded -- i.e., lies inside some sufficiently large disc D -- exactly one of its faces is unbounded: the face that contains R^2 \ D. This face is the outer face of G; the other faces are its inner faces" (Diestel, p. 86).

# Prerequisites
- **Face** -- The outer face is a specific face
- **Plane graph** -- Defined for plane graphs only

# Key Properties
1. Unique: every plane graph has exactly one outer face
2. Unbounded
3. In a plane triangulation, the outer face is also bounded by a triangle
4. Via stereographic projection, the outer face is not topologically special

# Context & Application
The outer face plays a special role in many arguments about plane graphs. However, by working on S^2 via stereographic projection, any face can be made the outer face (by rotating the graph on the sphere so a different face maps to the unbounded region). This is used in the proof that 3-connected graphs have unique embeddings.

# Examples
**Example** (p. 89-90): In a plane triangulation with n >= 3, every face including the outer face is bounded by a triangle (Proposition 4.2.8).

# Relationships
## Builds Upon
- **Face** -- The outer face is a specific face

## Enables
- **Plane triangulation** -- Requires the outer face to also be a triangle

## Contrasts With
- **Inner face** -- Inner faces are bounded; the outer face is unbounded

# Source Reference
Chapter 4: Planar Graphs, Section 4.2 "Plane graphs," page 86.

# Verification Notes
- Definition directly quoted from p. 86
- Confidence: HIGH -- explicit definition
