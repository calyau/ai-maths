---
concept: Convex Drawing
slug: convex-drawing
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
  - "Steinitz theorem"
prerequisites:
  - planar-graph
  - straight-line-drawing
extends:
  - straight-line-drawing
related:
  - three-connected-planarity
contrasts_with: []
answers_questions:
  - "Can 3-connected planar graphs be drawn with all inner faces convex?"
---

# Quick Definition
A convex drawing of a planar graph is one where every inner face is a convex polygon. Every 3-connected planar graph has a convex drawing (which implies a straight-line drawing).

# Core Definition
The proof of Lemma 4.4.3 "can easily be adapted to produce a drawing in which every inner face is convex; in particular, every edge can be drawn straight" (Diestel, p. 99). This is related to Steinitz's theorem (1922) that 3-connected planar graphs are precisely the 1-skeletons of 3-dimensional convex polyhedra.

# Prerequisites
- **Planar graph**, **Straight-line drawing**

# Key Properties
1. Every 3-connected planar graph has a convex drawing
2. Implies straight-line drawing (convex faces have straight edges)
3. 2-connected planar graphs may not have convex drawings (but always have straight-line drawings)
4. Equivalent to being the skeleton of a convex 3-polytope (Steinitz's theorem)

# Context & Application
Convex drawings connect planarity to convex geometry and polyhedral combinatorics. Tutte's "rubber band" method provides an algorithmic approach.

# Relationships
## Builds Upon
- **Straight-line drawing**

## Related
- **3-connected planarity** -- Convex drawings exist iff 3-connected

# Source Reference
Chapter 4, Section 4.4, page 99. Exercise 16.

# Verification Notes
- From p. 99 and Exercise 16
- Confidence: HIGH
