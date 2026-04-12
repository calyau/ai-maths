---
concept: Polynomial Ring in Several Variables
slug: polynomial-ring-several-variables
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
  - "multivariate polynomial ring"
prerequisites:
  - polynomial-ring
extends:
  - polynomial-ring
related:
  - monomial
  - homogeneous-polynomial
contrasts_with: []
answers_questions:
  - "How are polynomial rings in several variables defined?"
---

# Quick Definition

The polynomial ring R[x_1, ..., x_n] consists of finite linear combinations of monomials x_1^{i_1} ... x_n^{i_n} with coefficients in R. It is isomorphic to the iterated polynomial ring R[x_1]...[x_n].

# Core Definition

A polynomial in variables x_1, ..., x_n with coefficients in R is a linear combination f(x) = sum_i a_i x^i, where i runs through multi-indices, the coefficients a_i are in R, and only finitely many are nonzero. The ring R[x_1, ..., x_n] is isomorphic to R[x_1][x_2]...[x_n] (Artin, Section 11.2, formulas 11.2.12-11.2.14, Proposition 11.3.8, p. 343).

# Prerequisites

- **Polynomial ring** -- The single-variable case is the foundation

# Key Properties

1. Monomials x^i = x_1^{i_1} ... x_n^{i_n} form a basis
2. The total degree of a monomial is i_1 + ... + i_n
3. R[x, y] is isomorphic to R[x][y] (collecting terms in y)
4. Division with remainder in y is possible when f is monic in y

# Context & Application

Polynomial rings in several variables are essential for algebraic geometry, where varieties are zero loci of systems of polynomial equations.

# Examples

**Example 1** (p. 343): x^4 y + x^3 - 3x^2 y + y^2 + 2 = y^2 + (x^4 - 3x^2)y + (x^3 + 2), viewed in R[x][y].

# Relationships

## Builds Upon
- **Polynomial ring** -- Extends to multiple variables

## Enables
- **Algebraic variety** -- Defined as zero loci of polynomials in several variables

# Source Reference

Chapter 11: Rings, Section 11.2, pages 343-344, Proposition 11.3.8.

# Verification Notes

- Definition source: Direct from Section 11.2
- Confidence rationale: Explicit construction with multi-index notation
- Uncertainties: None
- Cross-reference status: Verified
