---
concept: Polynomial Ring
slug: polynomial-ring
category: ring-theory
subcategory: polynomial-rings
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Rings"
chapter_number: 11
pdf_page: 339
section: "Polynomial Rings"
extraction_confidence: high
aliases:
  - "ring of polynomials"
prerequisites:
  - ring
extends:
  - ring
related:
  - degree-of-polynomial
  - division-with-remainder
  - polynomial-ring-several-variables
contrasts_with: []
answers_questions:
  - "What is a ring?"
  - "How are polynomial rings constructed?"
---

# Quick Definition

The polynomial ring R[x] over a ring R consists of all formal polynomials in x with coefficients in R, with addition and multiplication defined by the standard rules. It is the most important source of ring examples beyond the integers.

# Core Definition

A polynomial with coefficients in a ring R is an expression of the form f(x) = a_n x^n + ... + a_1 x + a_0, where the coefficients a_i are elements of R. The set of these polynomials forms a ring R[x] with addition defined componentwise and multiplication defined by the convolution formula p_k = sum_{i+j=k} a_i b_j (Artin, Section 11.2, pp. 340-341, Proposition 11.2.8).

# Prerequisites

- **Ring** -- Coefficients come from a ring R

# Key Properties

1. R is a subring of R[x] (constant polynomials)
2. Addition is componentwise (vector addition of coefficient sequences)
3. Multiplication uses the convolution formula
4. R[x] is commutative if R is commutative
5. If R is an integral domain, so is R[x]

# Construction / Recognition

## To Construct:
1. Start with a ring R
2. Introduce a formal variable x
3. Form all finite linear combinations of powers of x with coefficients in R
4. Define addition and multiplication by the standard polynomial rules

# Context & Application

Polynomial rings are fundamental to algebra. They provide a universal construction for adjoining elements to rings, and their ideals and quotients are central to algebraic geometry.

# Examples

**Example 1** (p. 340): Z[x] is the ring of integer polynomials.

**Example 2** (p. 341): R[x] over a field R has division with remainder whenever the divisor is monic (or has unit leading coefficient).

# Relationships

## Builds Upon
- **Ring** -- Polynomial ring extends a coefficient ring

## Enables
- **Division with remainder** -- Available when divisor is monic
- **Quotient ring** -- R[x]/(f) for adjoining roots
- **Substitution principle** -- Evaluating polynomials defines homomorphisms

## Related
- **Degree of polynomial** -- Measures size of polynomials
- **Polynomial ring in several variables** -- Extends to multiple variables

# Common Errors

- **Error**: Confusing formal polynomials with polynomial functions
  **Correction**: Over finite fields, distinct formal polynomials can define the same function; Artin uses "polynomial" to mean formal polynomial

# Source Reference

Chapter 11: Rings, Section 11.2 "Polynomial Rings," pages 340-343. See Proposition 11.2.8.

# Verification Notes

- Definition source: Direct from Section 11.2
- Confidence rationale: Explicit construction with formulas
- Uncertainties: None
- Cross-reference status: Verified
