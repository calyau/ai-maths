---
concept: Hypergraph Ramsey Theorem
slug: hypergraph-ramsey-theorem
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 189
section: "VI.1 The Fundamental Ramsey Theorems"
extraction_confidence: high
aliases:
  - "Theorem VI.2"
  - "R^(r)(s,t)"
  - "Ramsey theorem for r-tuples"
prerequisites:
  - ramsey-theorem-finite
extends:
  - ramsey-theorem-finite
related:
  - hypergraph-ramsey-number
contrasts_with: []
answers_questions:
  - "Does Ramsey's theorem extend to hypergraphs?"
---

# Quick Definition
R⁽ʳ⁾(s,t), the hypergraph Ramsey number, is the minimal n such that every red-blue colouring of the r-tuples of an n-set yields a red s-set or blue t-set. It is always finite.

# Core Definition
**Theorem 2** (Bollobás, p. 189): Let 1 < r < min{s,t}. Then R⁽ʳ⁾(s,t) is finite and R⁽ʳ⁾(s,t) ≤ R⁽ʳ⁻¹⁾(R⁽ʳ⁾(s−1,t), R⁽ʳ⁾(s,t−1)) + 1.

The proof mirrors the graph case: pick x ∈ X, define a colouring c' on (r−1)-subsets of Y = X − {x} by c'(σ) = c(σ ∪ {x}), apply the induction hypothesis.

# Prerequisites
- **Ramsey theorem (finite)** — the case r = 2

# Key Properties
1. R⁽ʳ⁾(s,t) is finite for all r, s, t
2. R⁽²⁾(s,t) = R(s,t) (ordinary Ramsey number)
3. The bound grows extremely fast in r
4. Extends to k colours: R_k⁽ʳ⁾(s₁,...,sₖ)

# Context & Application
The hypergraph Ramsey theorem was part of Ramsey's original 1930 paper. The growth rate of R⁽ʳ⁾ for r ≥ 3 is much faster than for r = 2.

# Relationships
## Builds Upon
- **Ramsey theorem (finite)** — base case r = 2

## Related
- **Paris-Harrington theorem** — a strengthening that is unprovable in Peano arithmetic

# Source Reference
Chapter VI: Ramsey Theory, Section VI.1, Theorem 2, pages 189–190.

# Verification Notes
- Definition source: Direct theorem statement from p. 189
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
