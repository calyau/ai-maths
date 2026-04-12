---
concept: Norm in a Quadratic Field
slug: norm-quadratic-field
category: number-theory
subcategory: quadratic-fields
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Quadratic Number Fields"
chapter_number: 13
pdf_page: 394
section: "Factoring Algebraic Integers"
extraction_confidence: high
aliases:
  - "norm of an algebraic integer"
  - "N(alpha)"
prerequisites:
  - ring-of-integers
  - quadratic-field
extends: []
related:
  - norm-gaussian-integers
  - norm-of-an-ideal
contrasts_with: []
answers_questions:
  - "What is the norm in a quadratic field?"
---

# Quick Definition

The norm of alpha = a + b*sqrt(d) in a quadratic field is N(alpha) = alpha * alpha-bar = a^2 - b^2*d. For imaginary quadratic fields (d < 0), the norm is always a positive integer for nonzero algebraic integers.

# Core Definition

The norm of alpha = a + b*delta (where delta = sqrt(d)) is N(alpha) = alpha * alpha-bar, where alpha-bar = a - b*delta. Thus N(alpha) = a^2 - b^2*d. It is equal to |alpha|^2 when d < 0. The norm is multiplicative: N(beta*gamma) = N(beta)N(gamma) (Artin, Section 13.2, p. 397).

# Prerequisites

- **Ring of integers** -- Norm is defined for algebraic integers
- **Quadratic field** -- Context is Q[sqrt(d)]

# Key Properties

1. Multiplicative: N(beta*gamma) = N(beta)N(gamma)
2. For d < 0, N(alpha) is a positive integer for nonzero alpha
3. alpha is a unit iff N(alpha) = 1 (Proposition 13.2.2)
4. If alpha = beta*gamma, then N(beta) divides N(alpha)

# Examples

**Example 1** (p. 397): In Z[sqrt(-5)], N(1 + sqrt(-5)) = 1 + 5 = 6.

**Example 2** (p. 397): In Z[sqrt(-5)], N(2) = 4, N(3) = 9.

# Relationships

## Builds Upon
- **Ring of integers** -- Norm measures elements of R

## Enables
- **Factoring algebraic integers** -- Norm controls factorization
- **Units** -- alpha is a unit iff N(alpha) = 1

# Source Reference

Chapter 13: Quadratic Number Fields, Section 13.2, pages 397-398.

# Verification Notes

- Definition source: Direct from Section 13.2
- Confidence rationale: Explicit definition with properties
- Uncertainties: None
- Cross-reference status: Verified
