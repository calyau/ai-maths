---
concept: Reduction Modulo p
slug: reduction-modulo-p
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
  - "mod p reduction"
  - "residue modulo p"
prerequisites:
  - ring-homomorphism
  - polynomial-ring
extends: []
related:
  - eisenstein-criterion
  - irreducible-polynomial
contrasts_with: []
answers_questions:
  - "How do I determine if a polynomial is irreducible?"
---

# Quick Definition

Reducing a polynomial modulo a prime p means applying the homomorphism Z[x] -> F_p[x] that sends each coefficient to its residue class. If the reduced polynomial is irreducible and has the same degree, the original is irreducible over Q.

# Core Definition

The homomorphism psi_p: Z[x] -> F_p[x] sends x to x and reduces coefficients modulo p (Artin, formula 11.3.6, p. 345). If f has leading coefficient not divisible by p and f-bar is irreducible in F_p[x], then f is irreducible in Q[x] (Proposition 12.4.3, p. 383).

# Prerequisites

- **Ring homomorphism** -- Reduction mod p is a ring homomorphism
- **Polynomial ring** -- Maps between polynomial rings

# Key Properties

1. The map preserves degree when p does not divide the leading coefficient
2. If f-bar is irreducible and has the same degree, f is irreducible
3. The method can fail: some irreducible polynomials are reducible mod every prime
4. x^4 - 10x^2 + 1 is an example of irreducible but reducible mod every prime

# Examples

**Example 1** (p. 384): x^5 - 64x^4 + 127x^3 - 200x + 99 is irreducible over Q because its reduction mod 2 is x^5 + x^3 + 1, which is irreducible in F_2[x].

# Relationships

## Builds Upon
- **Ring homomorphism** -- Reduction is a homomorphism

## Related
- **Eisenstein criterion** -- Another irreducibility test
- **Irreducible polynomial** -- What reduction tests for

# Source Reference

Chapter 12: Factoring, Section 12.4, Proposition 12.4.3, pages 383-384.

# Verification Notes

- Definition source: Direct from text and Proposition 12.4.3
- Confidence rationale: Explicit statement
- Uncertainties: None
- Cross-reference status: Verified
