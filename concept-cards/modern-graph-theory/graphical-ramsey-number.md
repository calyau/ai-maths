---
concept: Graphical Ramsey Number
slug: graphical-ramsey-number
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 197
section: "VI.3 Ramsey Theory For Graphs"
extraction_confidence: high
aliases:
  - "r(H_1, H_2)"
  - "generalized Ramsey number"
prerequisites:
  - ramsey-number
extends:
  - ramsey-number
related:
  - chromatic-surplus
  - ramsey-number-for-trees
contrasts_with: []
answers_questions:
  - "What is a graphical Ramsey number?"
---

# Quick Definition
The graphical Ramsey number r(H₁, H₂) is the smallest n such that every red-blue colouring of Kₙ contains a red H₁ or a blue H₂. It generalizes R(s,t) = r(Kₛ, Kₜ).

# Core Definition
For graphs H₁, H₂, let r(H₁, H₂) be the smallest n such that every red-blue colouring of Kₙ contains a red H₁ or blue H₂. Since Hᵢ ⊂ K_{|Hᵢ|}, we have r(H₁, H₂) ≤ R(|H₁|, |H₂|). Equivalently, r(H₁, H₂) − 1 is the maximum n for which there exists G of order n with H₁ ⊄ G and H₂ ⊄ G̅ (Bollobás, p. 197).

# Prerequisites
- **Ramsey number** — r(Kₛ, Kₜ) = R(s,t)

# Key Properties
1. r(Kₛ, Kₜ) = R(s,t)
2. r(H₁, H₂) ≥ (χ(H₁) − 1)(c(H₂) − 1) + u(H₁) (Theorem 11)
3. r(Kₛ, T) = (s−1)(t−1) + 1 for every tree T of order t (Chvátal, Theorem 12)
4. r(H₁, H₂) ≤ C·(|H₁| + |H₂|) when max degrees are bounded (Theorem 18)

# Context & Application
Graphical Ramsey numbers have been extensively studied. They include classical Ramsey numbers as a special case and offer more tractable problems when one of the graphs is sparse.

# Examples
**Example** (Theorem 10, p. 198): r(ℓK₂, Kₚ) = 2ℓ + p − 2 (independent edges vs. complete graph).

# Relationships
## Builds Upon
- **Ramsey number** — generalization

## Related
- **Chromatic surplus** — appears in lower bound formula
- **Ramsey number for trees** — exact formula

# Source Reference
Chapter VI: Ramsey Theory, Section VI.3, pages 197–205.

# Verification Notes
- Definition source: Direct from p. 197
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
