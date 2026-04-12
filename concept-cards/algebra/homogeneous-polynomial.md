---
concept: Homogeneous Polynomial
slug: homogeneous-polynomial
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
  - "form"
prerequisites:
  - polynomial-ring-several-variables
extends: []
related:
  - algebraic-variety
contrasts_with: []
answers_questions:
  - "What is a homogeneous polynomial?"
---

# Quick Definition

A homogeneous polynomial (or form) is a polynomial in several variables in which all monomials with nonzero coefficients have the same total degree.

# Core Definition

A polynomial in which all monomials with nonzero coefficients have (total) degree d is called a homogeneous polynomial (Artin, p. 343).

# Prerequisites

- **Polynomial ring in several variables** -- Homogeneous polynomials are elements of R[x_1,...,x_n]

# Key Properties

1. All terms have the same total degree
2. f(lambda*x) = lambda^d * f(x) for degree d
3. The zero locus of a homogeneous polynomial passes through the origin

# Examples

**Example 1** (p. 343): x^2 + xy + y^2 is homogeneous of degree 2.

# Relationships

## Builds Upon
- **Polynomial ring in several variables** -- Defined for multivariate polynomials

## Related
- **Algebraic variety** -- Zero loci of homogeneous polynomials define projective varieties

# Source Reference

Chapter 11: Rings, Section 11.2, page 343.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
