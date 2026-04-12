---
concept: Discriminant
slug: discriminant
category: galois-theory
subcategory: symmetric-functions
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Galois Theory"
chapter_number: 16
pdf_page: 488
section: "16.2 The Discriminant"
extraction_confidence: high
aliases: []
prerequisites:
  - elementary-symmetric-function
  - symmetric-function
extends: []
related:
  - galois-group
  - resolvent-cubic
contrasts_with: []
answers_questions:
  - "What is the discriminant of a polynomial?"
  - "How do I determine the Galois group of a polynomial?"
---

# Quick Definition

The discriminant of a polynomial with roots alpha_1, ..., alpha_n is D = product of (alpha_i - alpha_j)^2 for i < j. It is a symmetric function of the roots, hence an element of the coefficient field. D = 0 iff the polynomial has a repeated root.

# Core Definition

The discriminant of the polynomial P(x) = x^n - s_1*x^{n-1} + ... with variable roots u_1, ..., u_n is D(u) = product_{i<j} (u_i - u_j)^2 (Artin, p. 493, equation 16.2.1). It is a symmetric polynomial with integer coefficients. By the Symmetric Functions Theorem, D can be written as a polynomial Delta(z_1, ..., z_n) in the elementary symmetric functions. For a specific polynomial f with coefficients a_i, its discriminant is Delta(a_1, ..., a_n).

# Prerequisites

- **Elementary symmetric function** -- The discriminant is expressed in terms of them
- **Symmetric function** -- The discriminant is symmetric in the roots

# Key Properties

1. D = 0 iff two roots are equal
2. A permutation multiplies sqrt(D) by the sign of the permutation (p. 500)
3. For quadratic x^2 - s_1*x + s_2: D = s_1^2 - 4s_2 (16.2.3)
4. For cubic x^3 + px + q: D = -4p^3 - 27q^2 (16.2.8)
5. D is a square in F iff the Galois group is contained in the alternating group (16.9.6)

# Context & Application

The discriminant is the primary tool for determining whether a Galois group contains odd permutations. For cubics, it completely determines the Galois group. For quartics, combined with the resolvent cubic, it nearly determines the group.

# Examples

**Example 1** (p. 500): The discriminant of x^3 + 3x + 1 is -5*3^3 = -135 (not a square), so G = S_3.

**Example 2** (p. 500): The discriminant of x^3 - 3x + 1 is 3^4 = 81 (a square), so G = A_3.

# Relationships

## Builds Upon
- **Elementary symmetric function** -- D is a polynomial in the s_i

## Enables
- **Galois group determination** -- D square in F implies G in A_n

## Related
- **Resolvent cubic** -- Together with D, nearly determines the Galois group of a quartic

# Source Reference

Chapter 16: Galois Theory, Section 16.2, pages 493-496. Equations 16.2.1, 16.2.3, 16.2.8.

# Verification Notes

- Definition source: Direct from Artin, p. 493
- Confidence rationale: Explicit formulas and examples
- Uncertainties: None
- Cross-reference status: Verified
