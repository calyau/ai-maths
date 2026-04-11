---
concept: Going-Up Theorem
slug: going-up-theorem
category: commutative-algebra
subcategory: ring-extensions
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Commutative Rings and Algebraic Geometry"
chapter_number: 15
pdf_page: 720
section: "15.3 Integral Extensions and Hilbert's Nullstellensatz"
extraction_confidence: high
aliases: []
prerequisites:
  - integral-extension
  - prime-ideal
extends: []
related:
  - going-down-theorem
contrasts_with:
  - going-down-theorem
answers_questions:
  - "Can chains of prime ideals be lifted along integral extensions?"
---

# Quick Definition
In an integral extension S/R, any ascending chain of primes in R lying over some primes in S can be extended: primes in R lift to primes in S preserving containment.

# Core Definition
**Theorem 26(3) (Going-Up Theorem)**: Let S be integral over R. Let P_1 ⊆ ··· ⊆ P_n be primes in R and Q_1 ⊆ ··· ⊆ Q_m primes in S with P_i = Q_i ∩ R for i ≤ m < n. Then the chain can be completed: there exist primes Q_{m+1} ⊆ ··· ⊆ Q_n in S with P_i = Q_i ∩ R for all i (p. 720).

# Prerequisites
- **integral-extension** — The theorem requires S to be integral over R
- **prime-ideal** — Statement involves chains of prime ideals

# Key Properties
1. In integral extensions, ascending chains of primes in R can be lifted to S
2. P is maximal iff the corresponding Q is maximal (Theorem 26(2))

# Relationships
## Contrasts With
- **going-down-theorem** — Analogous for descending chains, but requires R integrally closed

# Source Reference
Chapter 15, Section 15.3, Theorem 26(3), page 720.

# Verification Notes
- Confidence: HIGH — explicitly stated and proved
