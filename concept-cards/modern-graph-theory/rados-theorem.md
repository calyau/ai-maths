---
concept: Rado's Partition Regularity Theorem
slug: rados-theorem
category: ramsey-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 213
section: "VI.4 Ramsey Theory for Integers"
extraction_confidence: high
aliases:
  - "Theorem VI.27"
  - "Rado's theorem"
  - "partition regularity"
  - "columns condition"
prerequisites:
  - schurs-theorem
  - van-der-waerden-theorem
extends:
  - schurs-theorem
related: []
contrasts_with: []
answers_questions:
  - "When does Ax = 0 have a monochromatic solution in every colouring of ℕ?"
---

# Quick Definition
An integer matrix A is partition regular (Ax = 0 has a monochromatic solution in every finite colouring of ℕ) if and only if it satisfies the columns condition: the column vectors can be partitioned so partial sums lie in the span of preceding columns.

# Core Definition
**Theorem 27** (Bollobás, p. 214): A matrix with integer entries is partition regular if and only if it satisfies the **columns condition**. The columns condition: columns a₁,...,aₙ can be reordered with indices 1 < n₁ < ... < nₗ = n such that b₁ = Σ_{j≤n₁} aⱼ = 0, and for i > 1, bᵢ = Σ_{j=nᵢ₋₁+1}^{nᵢ} aⱼ is a rational linear combination of a₁,...,a_{nᵢ₋₁} (Bollobás, pp. 213–214).

# Prerequisites
- **Schur's theorem** — special case: matrix (1 1 −1)
- **Van der Waerden's theorem** — essentially a special case

# Key Properties
1. Reduces partition regularity to a checkable finite condition
2. Schur's theorem: (1 1 −1) satisfies the columns condition
3. Van der Waerden strengthened: a specific matrix gives AP with common difference in same class
4. Neither implication is easy to prove
5. The finite version follows from the infinite by compactness

# Context & Application
Rado's theorem (1933) is one of the deepest results of Ramsey theory for integers. It gives a complete characterization of which systems of linear equations are partition regular.

# Examples
**Example** (p. 214): The matrix (1 1 −1) is partition regular (Schur's theorem).

**Example** (p. 214): The matrix with columns giving the AP-with-difference system satisfies the columns condition.

**Example** (p. 213): The matrix (1 −2) is NOT partition regular.

# Relationships
## Builds Upon
- **Schur's theorem** — special case

## Related
- **Van der Waerden's theorem** — weaker than a special case of Rado

# Source Reference
Chapter VI: Ramsey Theory, Section VI.4, Theorem 27, pages 213–215.

# Verification Notes
- Definition source: Direct theorem statement from p. 214
- Confidence rationale: Explicit theorem statement (proof not given)
- Uncertainties: Neither direction of proof is given
- Cross-reference status: Verified
