---
concept: Eisenstein Criterion
slug: eisenstein-criterion
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
  - "Eisenstein's criterion"
  - "Eisenstein's irreducibility criterion"
prerequisites:
  - irreducible-element
  - polynomial-ring
extends: []
related:
  - gauss-lemma
  - reduction-modulo-p
contrasts_with: []
answers_questions:
  - "How do I determine if a polynomial is irreducible?"
---

# Quick Definition

The Eisenstein Criterion is an irreducibility test: if an integer polynomial f(x) = a_n x^n + ... + a_0 has a prime p such that p does not divide a_n, p divides all other coefficients, and p^2 does not divide a_0, then f is irreducible over Q.

# Core Definition

Let f(x) = a_n x^n + ... + a_0 be an integer polynomial and let p be a prime. If: (1) p does not divide a_n, (2) p divides a_{n-1}, ..., a_0, and (3) p^2 does not divide a_0, then f is an irreducible element of Q[x] (Artin, Proposition 12.4.6, p. 384).

# Prerequisites

- **Irreducible element** -- The criterion tests for irreducibility
- **Polynomial ring** -- Applied to elements of Z[x]

# Key Properties

1. Sufficient but not necessary condition for irreducibility
2. Works by showing any factorization modulo p forces contradictory divisibility
3. Applies to prove irreducibility of cyclotomic polynomials (Theorem 12.4.9)

# Examples

**Example 1** (p. 384): x^4 + 25x^2 + 30x + 20 is irreducible (p = 5).

**Example 2** (p. 384): x^3 + 3x^2 + 9x + 6 is irreducible (p = 3).

**Example 3** (p. 384): The cyclotomic polynomial x^{p-1} + x^{p-2} + ... + x + 1 is irreducible for prime p (after substituting x = y+1, Eisenstein applies with the prime p).

# Relationships

## Builds Upon
- **Polynomial ring** -- Tests irreducibility of integer polynomials

## Related
- **Gauss's Lemma** -- Context for integer vs rational irreducibility
- **Reduction modulo p** -- Another irreducibility test

# Source Reference

Chapter 12: Factoring, Section 12.4, Proposition 12.4.6, pages 384-385.

# Verification Notes

- Definition source: Direct from Proposition 12.4.6
- Confidence rationale: Explicit statement with proof
- Uncertainties: None
- Cross-reference status: Verified
