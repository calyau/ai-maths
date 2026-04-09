---
concept: Disc on a Surface
slug: disc-on-surface
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
  - "disc"
  - "topological disc"
prerequisites:
  - surface
extends: []
related:
  - face-on-surface
  - euler-characteristic
contrasts_with: []
answers_questions:
  - "What is a disc on a surface?"
  - "When are faces discs?"
---

# Quick Definition
A disc in a surface S is a subset homeomorphic to the unit disc {x in R^2 : ||x|| <= 1} or {x in R^2 : ||x|| < 1}. Faces that are discs are essential for the generalized Euler formula.

# Core Definition
A disc in S is a subset "homeomorphic to the unit disc {x in R^2 : ||x|| <= 1} or {x in R^2 : ||x|| < 1}" (Diestel, p. 361).

# Prerequisites
- **Surface**

# Key Properties
1. On the sphere, all faces of connected graphs are discs
2. On general surfaces, faces need not be discs
3. The generalized Euler formula requires all faces to be discs
4. Every surface admits graph embeddings where all faces are discs

# Relationships
## Enables
- **Euler characteristic** -- Requires disc faces

# Source Reference
Appendix B, page 361.

# Verification Notes
- Definition from p. 361
- Confidence: HIGH
