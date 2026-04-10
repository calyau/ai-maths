---
concept: Euler Characteristic
slug: euler-characteristic
category: planar-graphs
subcategory: null
tier: foundational
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 163
section: "V.3 Graphs on Surfaces"
extraction_confidence: high
aliases:
  - "χ (surface)"
prerequisites: []
extends: []
related:
  - euler-poincare-formula
  - heawood-bound
  - chromatic-number-of-surfaces
contrasts_with: []
answers_questions:
  - "What is the Euler characteristic of a surface?"
---

# Quick Definition
The Euler characteristic χ of a closed surface is a topological invariant: χ(Sₚ) = 2(1−p) for orientable surfaces of genus p, and χ(Nq) = 2−q for non-orientable surfaces of genus q.

# Core Definition
For p ≥ 0, the orientable surface Sₚ (obtained from a 4p-gon by identifying pairs of sides) has genus p and Euler characteristic χ(Sₚ) = 2(1−p). For q > 0, the non-orientable surface Nq has genus q and Euler characteristic χ(Nq) = 2−q. By the classification theorem, every closed surface is homeomorphic to exactly one Sₚ or Nq (Bollobás, p. 163).

# Prerequisites
This is a foundational concept with no prerequisites within this source.

# Key Properties
1. S₀ (sphere): χ = 2
2. S₁ (torus): χ = 0
3. N₁ (projective plane): χ = 1
4. N₂ (Klein bottle): χ = 0
5. Every closed surface is classified by its Euler characteristic and orientability

# Context & Application
The Euler characteristic connects topology to graph theory through the Euler-Poincaré formula and the Heawood bound on chromatic numbers of graphs on surfaces.

# Examples
**Example** (p. 163): The torus S₁ has χ = 0; the projective plane N₁ has χ = 1; the Klein bottle N₂ has χ = 0.

# Relationships
## Enables
- **Euler-Poincaré formula** — uses χ in the relation α₀ − α₁ + α₂ = χ
- **Heawood bound** — upper bound on chromatic number depends on χ

# Source Reference
Chapter V: Colouring, Section V.3, page 163.

# Verification Notes
- Definition source: Direct from p. 163
- Confidence rationale: Explicitly defined with examples
- Uncertainties: None
- Cross-reference status: Verified
