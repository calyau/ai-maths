---
concept: Face of an Embedded Graph on a Surface
slug: face-on-surface
category: topological-graph-theory
subcategory: surfaces
tier: intermediate
source: "Graph Theory"
source_slug: graph-theory
authors: "Reinhard Diestel"
chapter: "Appendix B - Surfaces"
chapter_number: null
pdf_page: 374
section: null
extraction_confidence: high
aliases:
  - "face of embedded graph"
prerequisites:
  - graph-embedding-on-surface
extends:
  - face
related:
  - disc-on-surface
  - euler-characteristic
contrasts_with:
  - face
answers_questions:
  - "What are faces of graphs embedded on surfaces?"
  - "Are faces always discs on non-planar surfaces?"
---

# Quick Definition
A face of a graph G embedded in a surface S is a connected component of S \ sigma(G). Unlike on the sphere, faces on general surfaces need not be discs.

# Core Definition
"A face of G in S is a component of S \ sigma(G), and the subgraph of G that sigma maps to the frontier of this face is its boundary. Note that while faces in the sphere are always discs (if G is connected), in general they need not be" (Diestel, p. 363).

# Prerequisites
- **Graph embedding on a surface**

# Key Properties
1. Faces are connected components of S \ sigma(G)
2. On the sphere, faces are always discs (for connected G)
3. On general surfaces, faces need not be discs
4. Euler's formula applies only when all faces are discs
5. Every surface admits embeddings with all faces being discs

# Relationships
## Builds Upon
- **Graph embedding on a surface**

## Contrasts With
- **Face** (of plane graph) -- Plane graph faces are always discs

# Source Reference
Appendix B, page 363.

# Verification Notes
- From p. 363
- Confidence: HIGH
