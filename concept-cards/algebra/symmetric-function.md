---
concept: Symmetric Function
slug: symmetric-function
category: galois-theory
subcategory: symmetric-functions
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Galois Theory"
chapter_number: 16
pdf_page: 488
section: "16.1 Symmetric Functions"
extraction_confidence: high
aliases:
  - "symmetric polynomial"
prerequisites:
  - polynomial-ring
  - symmetric-group
extends: []
related:
  - elementary-symmetric-function
  - discriminant
contrasts_with: []
answers_questions:
  - "What is a symmetric function?"
---

# Quick Definition

A symmetric polynomial in variables u_1, ..., u_n is one that is unchanged by any permutation of the variables. The symmetric polynomials form a subring of the polynomial ring R[u_1, ..., u_n].

# Core Definition

A permutation sigma of the indices {1, ..., n} operates on polynomials by permuting the variables: f(u_1, ..., u_n) -> f(u_{sigma(1)}, ..., u_{sigma(n)}) (Artin, p. 488, equation 16.1.1). A symmetric polynomial is one that is fixed by every permutation. The symmetric polynomials form a subring of R[u].

# Prerequisites

- **Polynomial ring** -- Symmetric polynomials live in polynomial rings
- **Symmetric group** -- Acts by permuting variables

# Key Properties

1. Symmetric polynomials form a subring of R[u_1, ..., u_n]
2. The orbit sums form a basis for the space of symmetric polynomials
3. Every symmetric polynomial can be written uniquely as a polynomial in the elementary symmetric functions (Symmetric Functions Theorem, 16.1.6)
4. If f splits as (x - alpha_1)...(x - alpha_n) with coefficients in F, then g(alpha_1, ..., alpha_n) is in F for every symmetric polynomial g with coefficients in F (Corollary 16.1.12)

# Context & Application

Symmetric functions are the foundation of Galois theory. The Symmetric Functions Theorem connects the coefficients of a polynomial to its roots, and Corollary 16.1.12 is used to prove the Splitting Theorem.

# Examples

**Example 1** (p. 488): u_1^2 + u_2^2 + u_3^2 = s_1^2 - 2s_2 (equation 16.1.8).

**Example 2** (p. 489): u_1*u_2^2 + u_2*u_1^2 + u_1*u_3^2 + u_3*u_1^2 + u_2*u_3^2 + u_3*u_2^2 = s_1*s_2 - 3s_3 (16.1.10).

# Relationships

## Enables
- **Symmetric Functions Theorem** -- Expresses all symmetric polynomials in terms of elementary ones
- **Splitting Theorem** -- Uses symmetric functions to prove splitting fields have good properties

## Related
- **Elementary symmetric function** -- The generators of the ring of symmetric polynomials

# Source Reference

Chapter 16: Galois Theory, Section 16.1, pages 488-492.

# Verification Notes

- Definition source: Direct from Artin, p. 488
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
