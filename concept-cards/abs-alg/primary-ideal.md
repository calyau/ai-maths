---
concept: Primary Ideal
slug: primary-ideal
category: commutative-algebra
subcategory: ideal-theory
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Commutative Rings and Algebraic Geometry"
chapter_number: 15
pdf_page: 706
section: "15.2 Radicals and Affine Varieties"
extraction_confidence: high
aliases:
  - "P-primary ideal"
prerequisites:
  - ideal
  - prime-ideal
  - radical-of-ideal
extends: []
related:
  - primary-decomposition
contrasts_with: []
answers_questions:
  - "What is a primary ideal?"
---

# Quick Definition
A proper ideal Q is primary if whenever ab ∈ Q and a ∉ Q, then b^n ∈ Q for some n ≥ 1. The radical of a primary ideal is always prime.

# Core Definition
A proper ideal Q in a commutative ring R is called **primary** if whenever ab ∈ Q and a ∉ Q, then b^n ∈ Q for some positive integer n (Definition, p. 706). Equivalently, every zero divisor in R/Q is nilpotent (Proposition 19(2)). If Q is primary, then rad Q is a prime ideal P, and Q is said to be **P-primary** or to belong to P.

# Prerequisites
- **ideal** — Primary ideals are special ideals
- **prime-ideal** — The associated prime rad Q
- **radical-of-ideal** — rad Q characterizes the primary ideal

# Key Properties
1. Prime ideals are primary (Proposition 19(1))
2. Q is primary iff every zero divisor in R/Q is nilpotent
3. rad Q is the unique smallest prime containing Q
4. If rad Q is maximal, then Q is primary (Proposition 19(4))
5. M^n ⊆ Q ⊆ M for maximal M implies Q is M-primary
6. Primary ideals need not be prime powers; prime powers need not be primary

# Examples
**Example** (p. 707): (x^2,y) in k[x,y] is primary (since (x,y)^2 ⊆ (x^2,y) ⊆ (x,y)), but not a power of any prime.

**Example** (p. 708): In R[x,y,z]/(xy-z^2), the square of the prime (x̄,z̄) is NOT primary.

# Relationships
## Builds Upon
- **prime-ideal** — Primes are special cases of primary ideals

## Enables
- **primary-decomposition** — Ideals decompose into intersections of primary ideals

# Source Reference
Chapter 15, Section 15.2, Definition and Proposition 19, pages 706-708.

# Verification Notes
- Confidence: HIGH — explicit definition with illuminating counterexamples
