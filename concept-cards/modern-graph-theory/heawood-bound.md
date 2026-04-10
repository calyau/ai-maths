---
concept: Heawood Bound
slug: heawood-bound
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
  - "Theorem V.9"
  - "Heawood number"
  - "h(χ)"
prerequisites:
  - euler-poincare-formula
  - euler-characteristic
extends: []
related:
  - chromatic-number-of-surfaces
  - four-colour-theorem
contrasts_with: []
answers_questions:
  - "What is the maximum chromatic number of a graph on a given surface?"
---

# Quick Definition
The chromatic number of a graph drawn on a closed surface of Euler characteristic χ ≤ 1 is at most h(χ) = ⌊(7 + √(49 − 24χ))/2⌋. For every surface except the sphere and Klein bottle, this bound is tight.

# Core Definition
**Theorem 9** (Bollobás, p. 163): The chromatic number of a graph G drawn on a closed surface of Euler characteristic χ ≤ 1 is at most h(χ) = ⌊(7 + √(49 − 24χ))/2⌋.

The proof uses the edge bound e(G) ≤ 3n − 3χ to show that a minimal k-chromatic graph has δ(G) ≤ h(χ) − 1, hence k ≤ h(χ).

# Prerequisites
- **Euler-Poincaré formula** — provides the edge bound
- **Euler characteristic** — the surface parameter

# Key Properties
1. h(χ) = ⌊(7 + √(49 − 24χ))/2⌋
2. h(0) = 7 (torus, Klein bottle), h(1) = 6 (projective plane)
3. For every surface except sphere and Klein bottle, s(M) = h(χ(M))
4. The Klein bottle has s(N₂) = 6, not h(0) = 7
5. Heawood's conjecture (proved by Ringel-Youngs): s(M) = h(χ) for χ ≤ 1, M ≠ Klein bottle

# Context & Application
Heawood proved this upper bound in 1890 while finding the error in Kempe's proof. The matching lower bound (Heawood's conjecture) was proved by Ringel and Youngs 75 years later — a major achievement requiring showing K_{h(χ)} can be drawn on each surface.

# Examples
**Example** (Theorem 11, p. 164): s(S₁) = 7 (torus), s(N₁) = 6 (projective plane), s(N₂) = 6 (Klein bottle). K₇ triangulates the torus, K₆ triangulates the projective plane.

# Relationships
## Builds Upon
- **Euler-Poincaré formula** — source of edge bounds

## Enables
- **Chromatic number of surfaces** — determines s(M) for most surfaces

## Related
- **Four colour theorem** — the sphere case (χ = 2) is fundamentally different

# Common Errors
- **Error**: Assuming h(χ) is always attained
  **Correction**: The Klein bottle is an exception: s(N₂) = 6 < h(0) = 7

# Common Confusions
- **Confusion**: Thinking the four-colour theorem and Heawood's conjecture are related problems
  **Clarification**: They are almost unrelated — the four-colour theorem requires showing ALL planar graphs are 4-colourable, while Heawood's conjecture requires drawing ONE specific graph on each surface

# Source Reference
Chapter V: Colouring, Section V.3, Theorems 9–11, pages 163–165.

# Verification Notes
- Definition source: Direct theorem statement from p. 163
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
