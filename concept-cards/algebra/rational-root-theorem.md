---
concept: Rational Root Theorem
slug: rational-root-theorem
category: factorization
subcategory: irreducibility-tests
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Factoring"
chapter_number: 12
pdf_page: 370
section: "Factoring Integer Polynomials"
extraction_confidence: high
aliases:
  - "rational root test"
prerequisites:
  - polynomial-ring
  - divisibility
extends: []
related:
  - eisenstein-criterion
  - reduction-modulo-p
contrasts_with: []
answers_questions:
  - "How do I find rational roots of a polynomial?"
---

# Quick Definition

If a primitive polynomial b_1 x + b_0 divides f(x) in Z[x], then b_1 divides the leading coefficient and b_0 divides the constant term. In particular, a rational root of a monic integer polynomial is an integer.

# Core Definition

(Lemma 12.4.2) (a) If a linear integer polynomial b_1 x + b_0 divides f in Z[x], then b_1 divides a_n and b_0 divides a_0. (b) A primitive polynomial b_1 x + b_0 divides f iff -b_0/b_1 is a root. (c) A rational root of a monic integer polynomial f is an integer (Artin, Lemma 12.4.2, p. 382).

# Prerequisites

- **Polynomial ring** -- Applied to Z[x]
- **Divisibility** -- Uses divisibility of leading/constant coefficients

# Key Properties

1. Only finitely many rational roots to check
2. Monic integer polynomials have integer roots (or none)
3. Useful as a first step before applying other methods

# Examples

**Example 1** (p. 382): For f(x) = x^3 + 3x^2 + 9x + 6, the possible rational roots are divisors of 6 (i.e., +/-1, +/-2, +/-3, +/-6). None works, so f has no linear factor.

# Relationships

## Related
- **Eisenstein criterion** -- Another tool for proving irreducibility
- **Reduction modulo p** -- Yet another irreducibility test

# Source Reference

Chapter 12: Factoring, Section 12.4, Lemma 12.4.2, pages 382-383.

# Verification Notes

- Definition source: Direct from Lemma 12.4.2
- Confidence rationale: Explicit lemma
- Uncertainties: None
- Cross-reference status: Verified
