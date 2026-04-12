---
concept: Quadratic Number Field
slug: quadratic-field
category: number-theory
subcategory: quadratic-fields
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Quadratic Number Fields"
chapter_number: 13
pdf_page: 394
section: "Algebraic Integers"
extraction_confidence: high
aliases:
  - "quadratic field"
  - "Q[sqrt(d)]"
prerequisites:
  - field-of-fractions
  - algebraic-number
extends: []
related:
  - quadratic-integer
  - ring-of-integers
  - real-quadratic-field
  - imaginary-quadratic-field
contrasts_with: []
answers_questions:
  - "What is a quadratic number field?"
---

# Quick Definition

A quadratic number field is Q[sqrt(d)] where d is a square-free integer. Its elements are a + b*sqrt(d) with a, b in Q. It is real if d > 0 and imaginary if d < 0.

# Core Definition

A quadratic number field is a field of the form Q[sqrt(d)], where d is a fixed integer, positive or negative, which is not a square in Q. Its elements are complex numbers a + b*sqrt(d) with a, b in Q. The field is real if d > 0 and imaginary if d < 0 (Artin, p. 394).

# Prerequisites

- **Field of fractions** -- Q[sqrt(d)] is a field extension of Q
- **Algebraic number** -- Elements are algebraic numbers

# Key Properties

1. d is assumed square-free (no square integer factor other than 1)
2. d can be -1, +/-2, +/-3, +/-5, +/-6, +/-7, ...
3. Q[sqrt(d)] is isomorphic to Q[x]/(x^2 - d)
4. Each element a + b*sqrt(d) has conjugate a - b*sqrt(d)

# Examples

**Example 1** (p. 394): Q[sqrt(-1)] = Q[i] is an imaginary quadratic field.

**Example 2** (p. 394): Q[sqrt(2)] is a real quadratic field.

**Example 3** (p. 394): Q[sqrt(-5)] is the quadratic field studied extensively in Ch. 12-13.

# Relationships

## Builds Upon
- **Algebraic number** -- Elements are algebraic

## Enables
- **Ring of integers** -- The algebraic integers in Q[sqrt(d)]
- **Quadratic integer** -- Integer elements of the field

# Source Reference

Chapter 13: Quadratic Number Fields, Section 13.1, page 394.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
