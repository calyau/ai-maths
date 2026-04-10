---
concept: Face
slug: face
category: planar-graphs
subcategory: planarity
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Fundamentals"
chapter_number: 1
pdf_page: 9
section: "I.4 Planar Graphs"
extraction_confidence: high
aliases:
  - country (in plane maps)
prerequisites:
  - plane-graph
extends: []
related:
  - eulers-formula
  - girth
contrasts_with: []
answers_questions:
  - "What is a face of a plane graph?"
---

# Quick Definition

A face of a plane graph is a connected component of the plane minus the graph's vertices and edges. Every plane graph has exactly one unbounded face.

# Core Definition

"If we omit the vertices and edges of a plane graph $G$ from the plane, the remainder falls into connected components, called faces. Clearly, each plane graph has exactly one unbounded face. The boundary of a face is the set of edges in its closure" (Bollobás, p. 30).

# Prerequisites

- **Plane graph** — Faces are defined for plane graphs

# Key Properties

1. Each plane graph has exactly one unbounded face
2. Each edge of a cycle is in the boundary of exactly two faces
3. $\sum_i f_i = f$ and $\sum_i i f_i = 2m$ (for bridgeless graphs), where $f_i$ = number of faces with $i$ boundary edges
4. Face count $f$ satisfies Euler's formula: $n - m + f = 2$

# Construction / Recognition

Faces are the regions of the plane determined by the embedding. They include both bounded (interior) and unbounded (exterior) regions.

# Context & Application

Faces are essential for Euler's formula, the edge-bound for planar graphs, and the dual graph construction. The four-colour theorem concerns colouring faces (countries) of a plane map.

# Examples

**Example** (p. 30): Drawing the graph of a convex polyhedron in the plane, the faces of the polyhedron correspond to the faces of the plane graph.

# Relationships

## Builds Upon
- **Plane graph** — Faces are defined by the embedding

## Enables
- **Euler's formula** — Counts faces: $n - m + f = 2$
- Edge bounds for planar graphs (Theorem 16)

# Common Errors

- **Error**: Forgetting to count the unbounded face
  **Correction**: The unbounded face must always be counted; Euler's formula includes it

# Common Confusions

- **Confusion**: Thinking every face is bounded
  **Clarification**: Every plane graph has exactly one unbounded (infinite) face

# Source Reference

Chapter I: Fundamentals, Section I.4, page 30.

# Verification Notes

- Definition source: Direct from p. 30
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
