---
concept: Ramsey's Theorem (Finite Version)
slug: ramsey-theorem-finite
category: ramsey-theory
subcategory: null
tier: intermediate
source: "Modern Graph Theory"
source_slug: modern-graph-theory
authors: "Béla Bollobás"
chapter: "Ramsey Theory"
chapter_number: 6
pdf_page: 187
section: "VI.1 The Fundamental Ramsey Theorems"
extraction_confidence: high
aliases:
  - "Theorem VI.1"
  - "Erdős-Szekeres theorem (Ramsey)"
  - "Ramsey's theorem for graphs"
prerequisites:
  - ramsey-number
extends: []
related:
  - ramsey-theorem-infinite
  - hypergraph-ramsey-theorem
  - multicolour-ramsey
contrasts_with: []
answers_questions:
  - "What is Ramsey's theorem?"
  - "How do I determine upper bounds for Ramsey numbers?"
---

# Quick Definition
R(s,t) is finite for all s, t ≥ 2, and R(s,t) ≤ C(s+t−2, s−1). Every sufficiently large complete graph, with edges 2-coloured, contains a red Kₛ or blue Kₜ.

# Core Definition
**Theorem 1** (Bollobás, p. 188): The function R(s,t) is finite for all s, t ≥ 2. If s > 2 and t > 2 then R(s,t) ≤ R(s−1,t) + R(s,t−1) and R(s,t) ≤ C(s+t−2, s−1).

The proof of the recursive inequality: take n = R(s−1,t) + R(s,t−1) vertices, pick vertex x. Either x has ≥ R(s−1,t) red neighbours (giving red Kₛ by induction) or ≥ R(s,t−1) blue neighbours (giving blue Kₜ by induction). The binomial bound follows by induction on s+t.

# Prerequisites
- **Ramsey number** — the quantity being bounded

# Key Properties
1. R(s,t) ≤ R(s−1,t) + R(s,t−1) (recursive bound)
2. R(s,t) ≤ C(s+t−2, s−1) (binomial bound)
3. R(s) ≤ C(2s−2, s−1) ≤ 4ˢ/√s (diagonal case)
4. Extends to k colours: R_k(s₁,...,sₖ) ≤ R_{k−1}(R(s₁,s₂), s₃, ..., sₖ)
5. The bound was hardly improved for over 50 years; Thomason (1988): R(s) ≤ 2²ˢ/s

# Construction / Recognition
## Proof of Recursive Inequality
1. Let n = R(s−1,t) + R(s,t−1)
2. Pick vertex x; it has n−1 neighbours
3. Either ≥ R(s−1,t) neighbours connected by red edges, or ≥ R(s,t−1) by blue
4. In the red case: the R(s−1,t) vertices contain blue Kₜ (done) or red K_{s−1} → add x for red Kₛ
5. Blue case: symmetric

# Context & Application
This is the foundational theorem of Ramsey theory, published in 1930 by Ramsey and independently proved with the binomial bound by Erdős and Szekeres in 1935. The upper bound C(s+t−2,s−1) gives R(s) ≤ 4ˢ approximately. A matching exponential lower bound R(s) ≥ 2^{s/2} comes from the probabilistic method (Chapter VII).

# Examples
**Example** (p. 188): R(3,3) ≤ R(2,3) + R(3,2) = 3 + 3 = 6. Combined with a construction showing R(3,3) > 5, this gives R(3,3) = 6.

# Relationships
## Builds Upon
- **Ramsey number** — proves finiteness

## Enables
- **Multicolour Ramsey** — colour-grouping argument
- **Hypergraph Ramsey theorem** — generalization

## Related
- **Probabilistic method** — gives lower bounds

# Common Errors
- **Error**: Forgetting the −1 when counting neighbours of x
  **Correction**: x has n−1 = R(s−1,t) + R(s,t−1) − 1 neighbours, but pigeonhole still works

# Source Reference
Chapter VI: Ramsey Theory, Section VI.1, Theorem 1, pages 187–189.

# Verification Notes
- Definition source: Direct theorem statement from p. 188
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
