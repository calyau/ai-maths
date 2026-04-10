---
concept: Partition Regularity
slug: partition-regularity
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 213
section: "VI.4 Ramsey Theory for Integers"
extraction_confidence: high
aliases:
  - "partition regular matrix"
prerequisites:
  - schurs-theorem
extends: []
related:
  - rados-theorem
  - van-der-waerden-theorem
contrasts_with: []
answers_questions:
  - "What does it mean for a matrix to be partition regular?"
---

# Quick Definition
An integer matrix A is partition regular if Ax = 0 has a monochromatic solution in every finite colouring of ℕ. Rado's theorem characterizes partition regularity via the columns condition.

# Core Definition
Call an n×m integer matrix A **partition regular** if Ax = 0 has a monochromatic solution in every colouring of ℕ with finitely many colours: for every partition ℕ = ∪Nₗ, some Nₗ contains x₁,...,xₙ with Σⱼ aᵢⱼxⱼ = 0 for all i (Bollobás, p. 213).

# Prerequisites
- **Schur's theorem** — example: (1 1 −1) is partition regular

# Key Properties
1. (1 1 −1) is partition regular (Schur's theorem)
2. (1 −2) is NOT partition regular
3. Matrices with all positive entries and no negative entries are not partition regular
4. Rado's theorem: A is partition regular iff it satisfies the columns condition
5. By compactness, if A is partition regular then for each k, there exists R(A,k) such that Ax = 0 has a monochromatic solution in every k-colouring of [R(A,k)]

# Relationships
## Related
- **Rado's theorem** — complete characterization
- **Van der Waerden's theorem** — slightly weaker than a special case

# Source Reference
Chapter VI: Ramsey Theory, Section VI.4, pages 213–214.

# Verification Notes
- Definition source: Direct from p. 213
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
