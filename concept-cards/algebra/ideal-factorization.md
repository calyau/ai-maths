---
concept: Ideal Factorization
slug: ideal-factorization
category: number-theory
subcategory: ideal-theory
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Quadratic Number Fields"
chapter_number: 13
pdf_page: 394
section: "Factoring Ideals"
extraction_confidence: high
aliases:
  - "unique factorization of ideals"
prerequisites:
  - prime-ideal
  - ideal-multiplication
  - main-lemma
extends: []
related:
  - unique-factorization-domain
  - class-group
contrasts_with: []
answers_questions:
  - "Do ideals factor uniquely?"
---

# Quick Definition

Every proper ideal of the ring of integers in an imaginary quadratic field factors uniquely as a product of prime ideals (up to ordering). This holds even when unique factorization of elements fails.

# Core Definition

Every proper ideal of R (the ring of integers in an imaginary quadratic field) is a product of prime ideals. The factorization into prime ideals is unique except for the ordering of the factors (Artin, Theorem 13.5.5, p. 406).

# Prerequisites

- **Prime ideal** -- Factorization is into prime ideals
- **Ideal multiplication** -- Products of ideals
- **Main Lemma** -- A*A-bar = (n) is the key tool

# Key Properties

1. Ideals always factor uniquely into primes, even when elements don't
2. R is a UFD iff R is a PID iff the class group is trivial (Theorem 13.5.6)
3. The proof uses: if P is prime and P divides AB, then P divides A or B (Corollary 13.5.3)

# Context & Application

Unique factorization of ideals is Dedekind's great insight: when unique factorization of elements fails, one can restore it by working with ideals instead. This is the foundation of algebraic number theory.

# Examples

**Example 1** (p. 402): In Z[sqrt(-5)], (6) = (2,1+d)(2,1-d)(3,1+d)(3,1-d), giving the common refinement of the two element factorizations 2*3 = (1+sqrt(-5))(1-sqrt(-5)).

# Relationships

## Builds Upon
- **Prime ideal** -- Factorization is into primes
- **Ideal multiplication** -- Uses ideal products

## Related
- **Unique factorization domain** -- UFD iff ideal factorization is trivially into principal ideals
- **Class group** -- Measures failure of element factorization

# Source Reference

Chapter 13: Quadratic Number Fields, Section 13.5, Theorem 13.5.5, page 406.

# Verification Notes

- Definition source: Direct from Theorem 13.5.5
- Confidence rationale: Explicit theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
