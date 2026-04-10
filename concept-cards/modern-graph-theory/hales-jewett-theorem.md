---
concept: Hales-Jewett Theorem
slug: hales-jewett-theorem
category: ramsey-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 208
section: "VI.4 Ramsey Theory for Integers"
extraction_confidence: high
aliases:
  - "Theorem VI.23"
  - "HJ(p,k)"
  - "Hales-Jewett function"
prerequisites:
  - van-der-waerden-theorem
  - combinatorial-line
extends: []
related:
  - shelahs-theorem
  - combinatorial-cube
contrasts_with: []
answers_questions:
  - "What is the Hales-Jewett theorem?"
---

# Quick Definition
For every p and k, there exists n such that every k-colouring of the cube [p]ⁿ contains a monochromatic combinatorial line. This abstract combinatorial result implies van der Waerden's theorem.

# Core Definition
**Theorem 23** (Bollobás, p. 208): For every p and k, there is an integer n such that if A is an alphabet with p letters then every k-colouring c: Aⁿ → [k] contains a monochromatic line. The Hales-Jewett function HJ(p,k) is the minimal such n.

A combinatorial line in Aⁿ is determined by a non-empty set I ⊂ [n] of "variable" coordinates (which all take the same value, varying over A) and fixed values for coordinates outside I.

# Prerequisites
- **Van der Waerden's theorem** — implied by Hales-Jewett via the map θ(a₁,...,aₙ) = a₁ + ... + aₙ
- **Combinatorial line** — the monochromatic structure being found

# Key Properties
1. HJ(p,k) is always finite
2. Implies W(p,k) ≤ p^{HJ(p,k)}
3. Original proof gave Ackermann-function bounds
4. Shelah (1988): HJ(p,k) has primitive recursive bounds
5. Every line has exactly |A| = p elements

# Context & Application
The Hales-Jewett theorem (1963) is a purely combinatorial abstraction of van der Waerden's theorem. It removes all algebraic structure (no addition needed) and works in the abstract setting of cubes and lines.

# Relationships
## Enables
- **Van der Waerden's theorem** — via the natural map from cubes to integers

## Related
- **Shelah's theorem** — gives the best known bounds on HJ(p,k)

# Source Reference
Chapter VI: Ramsey Theory, Section VI.4, Theorem 23, pages 208–209.

# Verification Notes
- Definition source: Direct theorem statement from p. 208
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
