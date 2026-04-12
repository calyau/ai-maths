---
concept: Real Quadratic Field
slug: real-quadratic-field
category: number-theory
subcategory: quadratic-fields
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Quadratic Number Fields"
chapter_number: 13
pdf_page: 394
section: "Real Quadratic Fields"
extraction_confidence: high
aliases: []
prerequisites:
  - quadratic-field
  - ring-of-integers
extends:
  - quadratic-field
related:
  - fundamental-unit
  - imaginary-quadratic-field
contrasts_with:
  - imaginary-quadratic-field
answers_questions:
  - "What is a real quadratic field?"
---

# Quick Definition

A real quadratic field is Q[sqrt(d)] where d is a positive square-free integer. Unlike imaginary quadratic fields, its ring of integers always contains infinitely many units.

# Core Definition

A quadratic number field Q[sqrt(d)] is real if d > 0 (Artin, p. 394). The ring of integers R can be represented as a lattice in R^2 via the embedding (u, v) = (a + b*sqrt(d), a - b*sqrt(d)). The norm N(alpha) = a^2 - b^2*d can be negative. The group of units is always infinite (Theorem 13.9.9, p. 418).

# Prerequisites

- **Quadratic field** -- Real quadratic fields are a special case
- **Ring of integers** -- The integers form a lattice in R^2

# Key Properties

1. The norm N(alpha) = a^2 - b^2*d can be positive or negative
2. Units satisfy uv = +/-1 (lying on hyperbolas in the (u,v)-plane)
3. The group of units is infinite (Theorem 13.9.9)
4. Unique factorization of ideals still holds
5. It is conjectured that infinitely many values of d give class number 1

# Examples

**Example 1** (p. 417): R = Z[sqrt(2)]. The element 1 + sqrt(2) has infinite order as a unit since N(1+sqrt(2)) = -1.

**Example 2** (p. 418): The powers (1+sqrt(2))^n give infinitely many units.

# Relationships

## Builds Upon
- **Quadratic field** -- Real case d > 0

## Related
- **Fundamental unit** -- Generator of the unit group

## Contrasts With
- **Imaginary quadratic field** -- The imaginary case has finite unit group

# Source Reference

Chapter 13: Quadratic Number Fields, Section 13.9, pages 417-422.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Explicit discussion
- Uncertainties: None
- Cross-reference status: Verified
