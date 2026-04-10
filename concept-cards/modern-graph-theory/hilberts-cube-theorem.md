---
concept: Hilbert's Cube Theorem
slug: hilberts-cube-theorem
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 205
section: "VI.4 Ramsey Theory for Integers"
extraction_confidence: high
aliases:
  - "Theorem VI.20"
prerequisites:
  - ramsey-number
extends: []
related:
  - schurs-theorem
  - van-der-waerden-theorem
contrasts_with: []
answers_questions:
  - "What is Hilbert's cube theorem?"
---

# Quick Definition
If ℕ is coloured with finitely many colours, then for every ℓ ≥ 1, one colour class contains infinitely many translates of the same ℓ-cube.

# Core Definition
**Theorem 20** (Bollobás, p. 205): If ℕ is coloured with finitely many colours then, for every ℓ ≥ 1, one of the colour classes contains infinitely many translates of the same ℓ-cube. An ℓ-cube C(s₀; s₁,...,sₗ) = {s₀ + Σεᵢsᵢ : εᵢ ∈ {0,1}} is the affine image of {0,1}ℓ with 2ℓ vertices. The proof constructs H(k,ℓ) by double induction.

# Prerequisites
- **Ramsey number** — Hilbert's theorem is a Ramsey-type result

# Key Properties
1. H(k,1) = k + 1 (a 1-cube is just a pair)
2. H(k, ℓ+1) ≤ kn^{ℓ+1} where n = H(k,ℓ)
3. Proved by Hilbert in 1892, predating most other Ramsey results
4. The finite version: there exists H(k,ℓ) such that every k-colouring of [H(k,ℓ)] contains a monochromatic ℓ-cube

# Context & Application
Hilbert's theorem (1892) was one of the earliest results in Ramsey theory, though it had essentially no influence on the field's development. It demonstrates that the pigeon-hole principle, while simple, leads to non-trivial results.

# Relationships
## Related
- **Schur's theorem** — later Ramsey result for integers
- **Van der Waerden's theorem** — more influential Ramsey result for integers

# Source Reference
Chapter VI: Ramsey Theory, Section VI.4, Theorem 20, pages 205–206.

# Verification Notes
- Definition source: Direct theorem statement from p. 205
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
