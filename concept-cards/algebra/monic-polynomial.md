---
concept: Monic Polynomial
slug: monic-polynomial
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
  - leading-coefficient
  - division-with-remainder
contrasts_with: []
answers_questions:
  - "What is a monic polynomial?"
---

# Quick Definition

A monic polynomial is one whose leading coefficient (the coefficient of the highest-degree term) is 1.

# Core Definition

A monic polynomial is one whose leading coefficient is 1 (Artin, p. 341). The leading coefficient of a nonzero polynomial is the nonzero coefficient of highest degree.

# Prerequisites

- **Polynomial ring** -- Monic polynomials are elements of R[x]
- **Degree of polynomial** -- The leading coefficient is the coefficient of x^(deg f)

# Key Properties

1. Division with remainder is always possible when the divisor is monic
2. In a field, any nonzero polynomial can be made monic by dividing by its leading coefficient
3. The product of monic polynomials is monic

# Context & Application

Working with monic polynomials eliminates ambiguity from associate factorizations in polynomial rings over fields. The unique monic irreducible factorization is the standard form.

# Examples

**Example 1** (p. 341): x^3 - 2 is monic; 3x^2 + 1 is not monic.

# Relationships

## Builds Upon
- **Polynomial ring** -- Monic polynomials live in R[x]

## Enables
- **Division with remainder** -- Always possible when the divisor is monic

# Source Reference

Chapter 11: Rings, Section 11.2, page 341.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Simple, explicit definition
- Uncertainties: None
- Cross-reference status: Verified
