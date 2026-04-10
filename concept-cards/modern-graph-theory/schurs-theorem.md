---
concept: Schur's Theorem
slug: schurs-theorem
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 206
section: "VI.4 Ramsey Theory for Integers"
extraction_confidence: high
aliases:
  - "Theorem VI.21"
  - "Schur number"
  - "S(k)"
prerequisites:
  - ramsey-number
  - multicolour-ramsey
extends: []
related:
  - van-der-waerden-theorem
  - rados-theorem
contrasts_with: []
answers_questions:
  - "What is Schur's theorem?"
---

# Quick Definition
For every k ≥ 1, there exists m such that every k-colouring of [m] contains monochromatic x, y, z with x + y = z. The Schur number S(k) ≤ R_k(3) − 1 ≤ ek!.

# Core Definition
**Theorem 21** (Bollobás, p. 206): For every k ≥ 1 there is an integer m such that every k-colouring of [m] contains integers x, y, z of the same colour with x + y = z. The proof: set m = R_k(3) − 1, induce a k-colouring of K_n edges by c'(ij) = c(|i−j|), then a monochromatic triangle gives x + y = z.

# Prerequisites
- **Ramsey number** — R_k(3) is used
- **Multicolour Ramsey** — k-colour Ramsey numbers

# Key Properties
1. S(k) = minimal m that works
2. S(k) ≤ R_k(3) − 1 ≤ ek!
3. The matrix (1 1 −1) is partition regular (Rado's theorem framework)
4. Schur's theorem (1916) was one of the earliest Ramsey-type results for integers

# Context & Application
Schur proved this in 1916, predating Ramsey's theorem. It was the starting point for Ramsey theory on integers and for Rado's partition regularity theory.

# Relationships
## Related
- **Van der Waerden's theorem** — another Ramsey result for integers
- **Rado's theorem** — Schur's theorem is a special case (matrix (1 1 −1) is partition regular)

# Source Reference
Chapter VI: Ramsey Theory, Section VI.4, Theorem 21, pages 206–207.

# Verification Notes
- Definition source: Direct theorem statement from p. 206
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
