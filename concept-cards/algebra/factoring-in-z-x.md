---
concept: Unique Factorization in Z[x]
slug: factoring-in-z-x
category: factorization
subcategory: integer-polynomials
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Factoring"
chapter_number: 12
pdf_page: 370
section: "Gauss's Lemma"
extraction_confidence: high
aliases:
  - "Z[x] is a UFD"
prerequisites:
  - gauss-lemma
  - unique-factorization-domain
extends: []
related:
  - principal-ideal-domain
contrasts_with: []
answers_questions:
  - "Is Z[x] a UFD?"
---

# Quick Definition

Z[x] is a unique factorization domain. Every nonzero polynomial factors uniquely as +/- p_1 ... p_m * q_1(x) ... q_n(x) where p_i are integer primes and q_j(x) are primitive irreducible polynomials. Z[x] is a UFD but NOT a PID.

# Core Definition

The polynomial ring Z[x] is a unique factorization domain. Every nonzero polynomial f(x) in Z[x] that is not +/-1 can be written as f(x) = +/- p_1 ... p_m q_1(x) ... q_n(x), where p_i are integer primes and q_j(x) are primitive irreducible polynomials. This expression is unique except for the order of the factors (Artin, Theorem 12.3.8, p. 379).

# Prerequisites

- **Gauss's Lemma** -- Key tool in the proof
- **Unique factorization domain** -- Z[x] is shown to be one

# Key Properties

1. Irreducible elements of Z[x] are: prime integers and primitive polynomials irreducible in Q[x]
2. Every irreducible element of Z[x] is prime (Proposition 12.3.7)
3. Z[x] is NOT a PID: the ideal (2, x) is not principal
4. Generalizes to R[x_1,...,x_n] for any UFD R (Theorem 12.3.10)

# Examples

**Example 1** (p. 379): 6x^3 + 9x^2 + 9x + 3 = 3(2x+1)(x^2+x+1).

# Relationships

## Builds Upon
- **Gauss's Lemma** -- Products of primitives are primitive

## Related
- **Principal ideal domain** -- Z[x] is a UFD that is NOT a PID

# Source Reference

Chapter 12: Factoring, Section 12.3, Theorem 12.3.8, page 379.

# Verification Notes

- Definition source: Direct from Theorem 12.3.8
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
