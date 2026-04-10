---
concept: Ramsey Numbers for Fans
slug: ramsey-for-fans
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 200
section: "VI.3 Ramsey Theory For Graphs"
extraction_confidence: high
aliases:
  - "Theorem VI.13"
  - "Li-Rousseau theorem"
prerequisites:
  - graphical-ramsey-number
  - ramsey-number-lower-bound
extends: []
related:
  - ramsey-number-for-trees
contrasts_with: []
answers_questions:
  - "What is the Ramsey number for fans vs. triangles?"
---

# Quick Definition
For ℓ ≥ 2, r(K₃, Fℓ) = 4ℓ + 1, where Fℓ = K₁ + ℓK₂ is the fan with ℓ blades. This gives equality in the general lower bound.

# Core Definition
**Theorem 13** (Bollobás, p. 200): For ℓ ≥ 2, r(F₁, Fℓ) = r(K₃, Fℓ) = 4ℓ + 1, where Fℓ = K₁ + ℓK₂ is the fan with ℓ blades (ℓ triangles sharing one vertex). The proof shows that a hypothetical counterexample would be a triangle-free 2ℓ-regular graph on 4ℓ + 1 vertices, which is impossible.

# Prerequisites
- **Graphical Ramsey number** — the quantity being determined
- **Ramsey number lower bound** — provides the lower bound 4ℓ + 1

# Key Properties
1. r(K₃, Fℓ) = 4ℓ + 1 for ℓ ≥ 2
2. Fℓ is K₃-good (equality in Theorem 11)
3. For fixed s ≥ 2 and large ℓ, Fℓ is Kₛ-good (Li-Rousseau)

# Relationships
## Related
- **Ramsey number for trees** — another family with exact formulas

# Source Reference
Chapter VI: Ramsey Theory, Section VI.3, Theorem 13, pages 200–201.

# Verification Notes
- Definition source: Direct theorem statement from p. 200
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
