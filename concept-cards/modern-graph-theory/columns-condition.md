---
concept: Columns Condition
slug: columns-condition
category: ramsey-theory
subcategory: null
tier: advanced
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 214
section: "VI.4 Ramsey Theory for Integers"
extraction_confidence: high
aliases: []
prerequisites:
  - partition-regularity
extends: []
related:
  - rados-theorem
contrasts_with: []
answers_questions:
  - "What is the columns condition for partition regularity?"
---

# Quick Definition
The columns condition on an integer matrix A: its column vectors a₁,...,aₙ can be reordered with partition indices 1 < n₁ < ... < nₗ = n such that b₁ = 0 and each subsequent bᵢ lies in the span of preceding columns. A is partition regular iff it satisfies this condition (Rado).

# Core Definition
Let a₁,...,aₙ ∈ ℤ^m be the column vectors of A. A satisfies the **columns condition** if the columns can be renumbered so there exist indices 1 < n₁ < ... < nₗ = n with: b₁ = Σ_{j=1}^{n₁} aⱼ = 0, and for i > 1, bᵢ = Σ_{j=n_{i-1}+1}^{nᵢ} aⱼ is a rational linear combination of a₁,...,a_{n_{i-1}} (Bollobás, p. 214).

# Prerequisites
- **Partition regularity** — the columns condition characterizes it

# Key Properties
1. Can be checked in finite time
2. (1 1 −1): columns sum to 0, so condition satisfied (Schur)
3. (1 −2): no partition of columns sums to 0, so NOT partition regular

# Relationships
## Related
- **Rado's theorem** — partition regular ⟺ columns condition

# Source Reference
Chapter VI: Ramsey Theory, Section VI.4, page 214.

# Verification Notes
- Definition source: Direct from p. 214
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
