---
concept: Unique Factorization in F[x]
slug: unique-factorization-in-polynomial-rings
category: factorization
subcategory: domain-hierarchy
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Factoring"
chapter_number: 12
pdf_page: 370
section: "Unique Factorization Domains"
extraction_confidence: high
aliases: []
prerequisites:
  - polynomial-ring
  - principal-ideal-domain
  - unique-factorization-domain
extends: []
related:
  - irreducible-polynomial
contrasts_with: []
answers_questions:
  - "Do polynomials over a field have unique factorization?"
---

# Quick Definition

Every monic polynomial in F[x] factors uniquely (up to ordering) into monic irreducible polynomials. F[x] is a Euclidean domain, hence a PID, hence a UFD.

# Core Definition

Let F[x] be the polynomial ring in one variable over a field F. (a) Two polynomials have a unique monic gcd d, with d = rf + sg. (b) Coprime polynomials satisfy rf + sg = 1. (c) Every irreducible polynomial is prime. (d) Every monic polynomial factors uniquely into monic irreducibles (Artin, Theorem 12.2.17, p. 377).

# Prerequisites

- **Polynomial ring** -- F[x] is the ring
- **Principal ideal domain** -- F[x] is a PID
- **Unique factorization domain** -- F[x] is a UFD

# Key Properties

1. Over C, irreducibles are linear: f = (x-a_1)...(x-a_n)
2. Over R, irreducibles are linear or quadratic with negative discriminant
3. Over Q, irreducibles exist of every degree
4. The gcd can be computed by the Euclidean algorithm

# Examples

**Example 1** (p. 377): Over C, x^3 - 1 = (x-1)(x-omega)(x-omega^2).

**Example 2** (p. 378): Over R, x^4 + 1 is reducible (it factors into two quadratics).

# Relationships

## Builds Upon
- **Principal ideal domain** -- F[x] is a PID

## Related
- **Irreducible polynomial** -- The building blocks of factorization

# Source Reference

Chapter 12: Factoring, Section 12.2, Theorem 12.2.17, pages 377-378.

# Verification Notes

- Definition source: Direct from Theorem 12.2.17
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
