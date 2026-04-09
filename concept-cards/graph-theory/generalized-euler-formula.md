---
concept: Generalized Euler Formula
slug: generalized-euler-formula
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
  - "Theorem B.2"
  - "Euler formula for surfaces"
prerequisites:
  - euler-formula
  - euler-characteristic
  - surface
extends:
  - euler-formula
related:
  - euler-genus
contrasts_with: []
answers_questions:
  - "How does Euler's formula generalize to surfaces?"
---

# Quick Definition
For any graph embedded on a surface S with all faces being discs: n - m + l = chi(S). This generalizes Euler's formula n - m + l = 2 (for the sphere, where chi = 2).

# Core Definition
**Theorem B.2**: n - m + l = chi(S) whenever a graph with n vertices, m edges, and l disc faces is embedded on surface S (Diestel, p. 363).

# Prerequisites
- **Euler's formula** -- The sphere case
- **Euler characteristic** -- chi(S)
- **Surface** -- The ambient space

# Key Properties
1. Reduces to n - m + l = 2 for S = S^2
2. Requires all faces to be discs
3. chi(S) depends only on the surface, not the graph
4. Distinct surfaces have distinct chi values (for orientable closed surfaces)

# Relationships
## Builds Upon
- **Euler's formula** (sphere case)
- **Euler characteristic**

## Enables
- Proving genus-dependent edge bounds
- Graph minor theorem machinery

# Source Reference
Appendix B, Theorem B.2, page 363.

# Verification Notes
- Theorem from p. 363
- Confidence: HIGH
