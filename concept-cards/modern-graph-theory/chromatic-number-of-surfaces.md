---
concept: Chromatic Number of Surfaces
slug: chromatic-number-of-surfaces
category: planar-graphs
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Colouring"
chapter_number: 5
pdf_page: 164
section: "V.3 Graphs on Surfaces"
extraction_confidence: high
aliases:
  - "s(M)"
  - "surface chromatic number"
prerequisites:
  - heawood-bound
  - euler-characteristic
extends:
  - heawood-bound
related:
  - four-colour-theorem
contrasts_with: []
answers_questions:
  - "What is the maximum chromatic number of a graph embeddable on a given surface?"
---

# Quick Definition
The chromatic number s(M) of a surface M is the maximum chromatic number over all graphs drawable on M. For all surfaces except the sphere and Klein bottle, s(M) equals the Heawood bound h(χ(M)).

# Core Definition
For a surface M, define s(M) = max{χ(G) : G can be drawn on M}. **Theorem 11** (Bollobás, p. 164): s(S₁) = 7, s(N₁) = 6, s(N₂) = 6. More generally, for every closed surface M with χ(M) ≤ 1 that is not the Klein bottle, s(M) = h(χ(M)) = ⌊(7 + √(49 − 24χ))/2⌋. This was Heawood's conjecture, proved by Ringel and Youngs.

**Theorem 10** (p. 164): For most values of χ ≤ 0, a minimal h-chromatic graph on the surface must be K_h, so the question reduces to embeddability of complete graphs.

# Prerequisites
- **Heawood bound** — provides the upper bound h(χ)
- **Euler characteristic** — parameterizes the surface

# Key Properties
1. s(S₀) = 4 (sphere — four-colour theorem)
2. s(S₁) = 7 (torus)
3. s(N₁) = 6 (projective plane)
4. s(N₂) = 6 (Klein bottle — exception to Heawood)
5. K₇ triangulates the torus uniquely (up to reflection)
6. K₇ cannot be drawn on the Klein bottle

# Examples
**Example** (p. 164, Figure V.6): K₆ triangulates the projective plane, K₇ triangulates the torus.

**Example** (p. 165, Figure V.7): The unique triangulation of the torus by K₇.

# Relationships
## Builds Upon
- **Heawood bound** — upper bound on s(M)

## Related
- **Four colour theorem** — the sphere case

# Source Reference
Chapter V: Colouring, Section V.3, Theorems 10–11, pages 164–166.

# Verification Notes
- Definition source: Direct from pp. 164–166
- Confidence rationale: Explicit theorems with proofs
- Uncertainties: None
- Cross-reference status: Verified
