---
concept: Classification of Conics
slug: classification-of-conics
category: bilinear-forms
subcategory: conics-quadrics
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Bilinear Forms"
chapter_number: 8
pdf_page: 240
section: "8.7 Conics and Quadrics"
extraction_confidence: high
aliases: ["principal axis theorem for conics"]
prerequisites: [conic, spectral-theorem-symmetric]
extends: []
related: [quadric, signature]
contrasts_with: []
answers_questions: ["How are conics classified?"]
---
# Quick Definition
Every nondegenerate conic is congruent to an ellipse, hyperbola, or parabola. The classification uses the spectral theorem to diagonalize the quadratic form, then completing the square to eliminate linear terms.
# Core Definition
Theorem 8.7.5: Every nondegenerate conic is congruent to one of: Ellipse a_{11}x_1^2 + a_{22}x_2^2 - 1 = 0, Hyperbola a_{11}x_1^2 - a_{22}x_2^2 - 1 = 0, or Parabola a_{11}x_1^2 - a_{22}x_2 = 0 (Artin, p. 261). The type is determined by the signature of the matrix A of the quadratic part: A positive definite -> ellipse, A indefinite -> hyperbola, A singular -> parabola.
# Prerequisites
- **Conic** — The objects being classified
- **Spectral theorem for symmetric operators** — Used to diagonalize
# Key Properties
1. Three types: ellipse (A positive definite), hyperbola (A indefinite), parabola (A singular)
2. Coefficients a_{ii} are determined up to interchange (ellipse)
3. Algorithm: (1) orthogonal diag of A, (2) complete the square, (3) scale
4. Can determine type from A alone using signature, without full classification
# Examples
**Example 1** (p. 261): x_1^2 + 2x_1 x_2 - x_2^2 + 2x_1 + 2x_2 - 1 = 0 is a hyperbola (A is indefinite).
# Relationships
## Builds Upon
- **Conic** — Objects classified
- **Spectral theorem for symmetric operators** — Tool for diagonalization
## Related
- **Quadric** — Higher-dimensional analogue
- **Signature** — Determines the type
# Source Reference
Chapter 8: Bilinear Forms, Section 8.7, Theorem 8.7.5, pages 260-262.
# Verification Notes
- Definition source: Direct from Theorem 8.7.5
- Confidence rationale: Full classification theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
