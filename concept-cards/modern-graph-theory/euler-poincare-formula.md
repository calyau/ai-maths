---
concept: Euler-Poincaré Formula
slug: euler-poincare-formula
category: planar-graphs
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 163
section: "V.3 Graphs on Surfaces"
extraction_confidence: high
aliases:
  - "Euler-Poincaré relation"
prerequisites:
  - euler-formula-for-planar-graphs
  - euler-characteristic
extends:
  - euler-formula-for-planar-graphs
related:
  - heawood-bound
contrasts_with: []
answers_questions:
  - "How does Euler's formula generalize to surfaces?"
---

# Quick Definition
For a triangulation of a closed surface of Euler characteristic χ with α₀ vertices, α₁ edges, and α₂ faces: α₀ − α₁ + α₂ = χ. This implies e(G) ≤ 3n − 3χ for any graph drawn on the surface.

# Core Definition
The Euler-Poincaré formula states that if a triangulation of a closed surface of Euler characteristic χ has α₀ vertices, α₁ edges, and α₂ faces, then α₀ − α₁ + α₂ = χ. For a graph G of order n drawn on a surface of Euler characteristic χ, this gives e(G) ≤ 3n − 3χ, with equality iff G triangulates the surface (Bollobás, p. 163).

# Prerequisites
- **Euler's formula for planar graphs** — the special case χ = 2 (sphere)
- **Euler characteristic** — the surface invariant

# Key Properties
1. α₀ − α₁ + α₂ = χ for triangulations
2. e(G) ≤ 3(n − χ) for any graph on a surface of characteristic χ
3. Equality holds iff every face is a triangle
4. Specializes to e ≤ 3n − 6 for the sphere (χ = 2)

# Context & Application
This formula is the foundation for Heawood's bound on the chromatic number of graphs on surfaces.

# Examples
**Example** (p. 163): On the torus (χ = 0), a graph of order n has at most 3n edges.

# Relationships
## Builds Upon
- **Euler's formula for planar graphs** — special case for the sphere

## Enables
- **Heawood bound** — derived from the edge bound e ≤ 3n − 3χ

# Source Reference
Chapter V: Colouring, Section V.3, page 163.

# Verification Notes
- Definition source: Direct from p. 163
- Confidence rationale: Explicit formula and consequence
- Uncertainties: None
- Cross-reference status: Verified
