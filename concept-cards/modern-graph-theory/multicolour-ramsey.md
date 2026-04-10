---
concept: Multicolour Ramsey Numbers
slug: multicolour-ramsey
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
  - "R_k(s_1,...,s_k)"
  - "k-colour Ramsey numbers"
prerequisites:
  - ramsey-number
  - ramsey-theorem-finite
extends:
  - ramsey-theorem-finite
related:
  - hypergraph-ramsey-theorem
contrasts_with: []
answers_questions:
  - "Does Ramsey's theorem extend to more than two colours?"
---

# Quick Definition
R_k(s₁,...,sₖ) is the minimal n such that every k-colouring of Kₙ contains a monochromatic Kₛᵢ in colour i for some i. The reduction R_k(s₁,...,sₖ) ≤ R_{k−1}(R(s₁,s₂), s₃,...,sₖ) proves finiteness.

# Core Definition
Given k and s₁, s₂, ..., sₖ, if n is sufficiently large, then every colouring of Kₙ with k colours ensures that for some i, there is a Kₛᵢ coloured with the ith colour. The minimal such n is R_k(s₁,...,sₖ). This is proved by colour grouping: merge the first two colours into one, reducing to k−1 colours, then apply R(s₁,s₂) to separate them (Bollobás, p. 189).

# Prerequisites
- **Ramsey number** — the two-colour case
- **Ramsey theorem (finite)** — provides the base

# Key Properties
1. R_k(s₁,...,sₖ) ≤ R_{k−1}(R(s₁,s₂), s₃,...,sₖ)
2. R_k(3,3,...,3) ≤ ⌊ek!⌋ + 1
3. R₃(3,3,3) = 17
4. Extends to hypergraph version R_k⁽ʳ⁾(s₁,...,sₖ)

# Context & Application
Multicolour Ramsey numbers arise naturally in Ramsey-type problems with more than two classes. They grow much faster than two-colour numbers.

# Relationships
## Builds Upon
- **Ramsey theorem (finite)** — via colour grouping

# Source Reference
Chapter VI: Ramsey Theory, Section VI.1, pages 189–190.

# Verification Notes
- Definition source: Direct from pp. 189–190
- Confidence rationale: Explicitly defined with reduction
- Uncertainties: None
- Cross-reference status: Verified
