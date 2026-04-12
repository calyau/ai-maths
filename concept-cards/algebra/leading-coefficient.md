---
concept: Leading Coefficient
slug: leading-coefficient
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
aliases: []
prerequisites:
  - polynomial-ring
  - degree-of-polynomial
extends: []
related:
  - monic-polynomial
contrasts_with: []
answers_questions:
  - "What is the leading coefficient of a polynomial?"
---

# Quick Definition

The leading coefficient of a nonzero polynomial is the nonzero coefficient of highest degree.

# Core Definition

The nonzero coefficient of highest degree of a polynomial is its leading coefficient (Artin, p. 341).

# Prerequisites

- **Polynomial ring** -- Leading coefficients are elements of the coefficient ring
- **Degree of polynomial** -- The leading coefficient corresponds to the degree

# Key Properties

1. The leading coefficient determines whether division with remainder is possible
2. Division is possible whenever the leading coefficient is a unit (Corollary 11.2.10)
3. A polynomial is monic if and only if its leading coefficient is 1

# Context & Application

The leading coefficient controls divisibility properties. Over a field, every nonzero polynomial has a unit leading coefficient, enabling unrestricted division.

# Examples

**Example 1** (p. 341): In 3x^2 + x + 5, the leading coefficient is 3.

# Relationships

## Builds Upon
- **Polynomial ring** -- Defined for elements of R[x]

## Related
- **Monic polynomial** -- Leading coefficient is 1

# Source Reference

Chapter 11: Rings, Section 11.2, page 341.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
