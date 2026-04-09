---
concept: Inner Face
slug: inner-face
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
  - "bounded face"
  - "finite face"
prerequisites:
  - face
extends:
  - face
related:
  - outer-face
contrasts_with:
  - outer-face
answers_questions:
  - "What is an inner face of a plane graph?"
---

# Quick Definition
An inner face of a plane graph is any face that is not the outer face -- that is, a bounded region of R^2 \ G.

# Core Definition
The inner faces of a plane graph are the faces other than the outer (unbounded) face (Diestel, p. 86).

# Prerequisites
- **Face** -- Inner faces are a subset of the faces

# Key Properties
1. All inner faces are bounded (contained in a finite region)
2. A connected plane graph with n vertices and m edges has m - n + 1 inner faces (by Euler's formula)
3. In a plane triangulation, every inner face is bounded by a triangle

# Relationships
## Contrasts With
- **Outer face** -- The unique unbounded face

# Source Reference
Chapter 4, Section 4.2, page 86.

# Verification Notes
- Confidence: HIGH -- directly defined
