---
concept: Algebraic Integer
slug: algebraic-integer
category: number-theory
subcategory: algebraic-integers
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Quadratic Number Fields"
chapter_number: 13
pdf_page: 394
section: "Algebraic Integers"
extraction_confidence: high
aliases: []
prerequisites:
  - algebraic-number
  - irreducible-polynomial
extends:
  - algebraic-number
related:
  - ring-of-integers
  - quadratic-integer
contrasts_with: []
answers_questions:
  - "What is an algebraic integer?"
---

# Quick Definition

An algebraic number is an algebraic integer if its monic irreducible polynomial over Q has integer coefficients. A rational number is an algebraic integer if and only if it is an ordinary integer.

# Core Definition

An algebraic number is an algebraic integer if its (monic) irreducible polynomial over Q has integer coefficients (Artin, p. 394). Lemma 13.1.1 states that a rational number is an algebraic integer if and only if it is an ordinary integer.

# Prerequisites

- **Algebraic number** -- Algebraic integers are special algebraic numbers
- **Irreducible polynomial** -- The irreducible polynomial must have integer coefficients

# Key Properties

1. Rational algebraic integers are ordinary integers (Lemma 13.1.1)
2. The algebraic integers in a number field form a ring
3. For a quadratic field Q[sqrt(d)], the integers depend on d mod 4

# Examples

**Example 1** (p. 394): omega = e^{2pi i/3} = (-1 + sqrt(-3))/2 is an algebraic integer (root of x^2 + x + 1).

**Example 2** (p. 394): alpha = (-1 + sqrt(3))/2 is NOT an algebraic integer (root of x^2 - x - 1/2).

# Relationships

## Builds Upon
- **Algebraic number** -- Special case with integer coefficients

## Enables
- **Ring of integers** -- The algebraic integers in a number field form a ring
- **Quadratic integer** -- Algebraic integers in quadratic fields

# Source Reference

Chapter 13: Quadratic Number Fields, Section 13.1, page 394.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
