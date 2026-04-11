---
concept: Going-Down Theorem
slug: going-down-theorem
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
  - integral-closure
  - prime-ideal
extends: []
related:
  - going-up-theorem
contrasts_with:
  - going-up-theorem
answers_questions:
  - "When can descending chains of primes be extended in integral extensions?"
---

# Quick Definition
If S is an integral domain that is integral over an integrally closed subring R, then any descending chain of primes in R lying over primes in S can be extended downward in S.

# Core Definition
**Theorem 26(4) (Going-Down Theorem)**: Assume S is an integral domain and R is integrally closed in S. Let P_1 ⊇ ··· ⊇ P_n be primes in R and Q_1 ⊇ ··· ⊇ Q_m primes in S with P_i = Q_i ∩ R for i ≤ m < n. Then the descending chain can be completed (p. 720).

# Prerequisites
- **integral-extension** — S must be integral over R
- **integral-closure** — R must be integrally closed (stronger than Going-Up)

# Key Properties
1. Requires R to be integrally closed — this is the key additional hypothesis beyond Going-Up
2. S must be an integral domain

# Relationships
## Contrasts With
- **going-up-theorem** — Going-Up does not require R integrally closed

# Source Reference
Chapter 15, Section 15.3, Theorem 26(4), page 720. Proof outlined in Exercise 24, Section 4.

# Verification Notes
- Confidence: HIGH — stated explicitly; proof deferred to exercises
