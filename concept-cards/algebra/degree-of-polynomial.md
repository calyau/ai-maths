---
concept: Degree of a Polynomial
slug: degree-of-polynomial
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
  - "deg f"
  - "degree"
prerequisites:
  - polynomial-ring
extends: []
related:
  - monic-polynomial
  - leading-coefficient
  - division-with-remainder
contrasts_with: []
answers_questions:
  - "What is the degree of a polynomial?"
---

# Quick Definition

The degree of a nonzero polynomial is the largest exponent with a nonzero coefficient. The zero polynomial has no defined degree.

# Core Definition

The degree of a nonzero polynomial, denoted deg f, is the largest integer n such that the coefficient a_n of x^n is not zero. A polynomial of degree zero is called a constant polynomial. The zero polynomial is also called a constant polynomial, but its degree is not defined (Artin, p. 341).

# Prerequisites

- **Polynomial ring** -- Degree is a property of polynomials

# Key Properties

1. deg(fg) = deg f + deg g when the coefficient ring is an integral domain
2. deg(f + g) <= max(deg f, deg g)
3. The zero polynomial has no defined degree
4. The leading coefficient is the coefficient of x^(deg f)
5. A monic polynomial has leading coefficient 1

# Context & Application

Degree serves as the size function for division with remainder in polynomial rings over fields, making F[x] into a Euclidean domain.

# Examples

**Example 1** (p. 341): The polynomial 3x^2 + x + 5 has degree 2.

# Relationships

## Builds Upon
- **Polynomial ring** -- Degree is defined for elements of R[x]

## Enables
- **Division with remainder** -- Degree decreases in the Euclidean algorithm

# Source Reference

Chapter 11: Rings, Section 11.2, page 341.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
