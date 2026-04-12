---
concept: Rational Function
slug: rational-function
category: ring-theory
subcategory: polynomial-rings
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Rings"
chapter_number: 11
pdf_page: 339
section: "Fractions"
extraction_confidence: high
aliases:
  - "field of rational functions"
  - "K(x)"
prerequisites:
  - field-of-fractions
  - polynomial-ring
extends: []
related: []
contrasts_with: []
answers_questions:
  - "What is a rational function?"
---

# Quick Definition

A rational function is a fraction f/g of polynomials, with g nonzero. The field of rational functions K(x) is the fraction field of the polynomial ring K[x].

# Core Definition

A fraction of polynomials p/q with q not the zero polynomial is called a rational function. The fraction field of K[x], where K is a field, is the field of rational functions in x with coefficients in K, denoted K(x) (Artin, formula 11.7.3, p. 362).

# Prerequisites

- **Field of fractions** -- K(x) is the fraction field of K[x]
- **Polynomial ring** -- The numerator and denominator are polynomials

# Key Properties

1. Elements are equivalence classes of fractions f/g
2. K(x) is a field containing K[x] as a subring
3. Formal rational functions should be distinguished from the functions they define

# Examples

**Example 1** (p. 362): (x^2 + 1)/(x - 1) is a rational function in R(x).

# Relationships

## Builds Upon
- **Field of fractions** -- K(x) is the fraction field of K[x]

# Source Reference

Chapter 11: Rings, Section 11.7, formula 11.7.3, page 362.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
