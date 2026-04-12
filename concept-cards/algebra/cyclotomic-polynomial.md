---
concept: Cyclotomic Polynomial
slug: cyclotomic-polynomial
category: factorization
subcategory: special-polynomials
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Factoring"
chapter_number: 12
pdf_page: 370
section: "Factoring Integer Polynomials"
extraction_confidence: high
aliases: []
prerequisites:
  - irreducible-polynomial
  - eisenstein-criterion
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What is a cyclotomic polynomial?"
---

# Quick Definition

The cyclotomic polynomial Phi(x) = x^{p-1} + x^{p-2} + ... + x + 1 (for prime p) has the pth roots of unity (other than 1) as its roots. It is irreducible over Q, proved via the Eisenstein criterion after substituting x = y + 1.

# Core Definition

For a prime p, the cyclotomic polynomial is Phi(x) = (x^p - 1)/(x - 1) = x^{p-1} + ... + x + 1, whose roots are the primitive pth roots of unity (Artin, formula 12.4.7, p. 385). Theorem 12.4.9 proves Phi(x) is irreducible over Q by substituting x = y+1 and applying the Eisenstein criterion with the prime p.

# Prerequisites

- **Irreducible polynomial** -- Phi(x) is irreducible
- **Eisenstein criterion** -- Used in the proof

# Key Properties

1. (x-1)*Phi(x) = x^p - 1
2. Roots are the pth roots of unity other than 1
3. Irreducible over Q (Theorem 12.4.9)

# Examples

**Example 1** (p. 385): For p = 5, Phi(x) = x^4 + x^3 + x^2 + x + 1 is irreducible over Q.

# Relationships

## Builds Upon
- **Eisenstein criterion** -- Applied after substitution x = y+1

# Source Reference

Chapter 12: Factoring, Section 12.4, Theorem 12.4.9, pages 385-386.

# Verification Notes

- Definition source: Direct from formula 12.4.7 and Theorem 12.4.9
- Confidence rationale: Explicit definition and proof
- Uncertainties: None
- Cross-reference status: Verified
