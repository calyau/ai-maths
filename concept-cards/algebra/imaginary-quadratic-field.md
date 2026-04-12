---
concept: Imaginary Quadratic Field
slug: imaginary-quadratic-field
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
aliases: []
prerequisites:
  - quadratic-field
extends:
  - quadratic-field
related:
  - real-quadratic-field
  - ring-of-integers
contrasts_with:
  - real-quadratic-field
answers_questions:
  - "What is an imaginary quadratic field?"
---

# Quick Definition

An imaginary quadratic field is Q[sqrt(d)] with d < 0, a square-free negative integer. Its ring of integers forms a lattice in the complex plane, and the unit group is finite.

# Core Definition

A quadratic number field Q[sqrt(d)] is imaginary if d < 0 (Artin, p. 394). The algebraic integers form a lattice in the complex plane. The lattice is rectangular when d = 2 or 3 mod 4, and "isosceles triangular" when d = 1 mod 4. The unit group is finite: {+/-1} unless d = -1 or d = -3 (Proposition 13.2.2).

# Prerequisites

- **Quadratic field** -- Imaginary is the case d < 0

# Key Properties

1. The ring of integers is a lattice in C
2. The unit group is finite (unlike real quadratic fields)
3. The norm N(alpha) = |alpha|^2 is always positive for nonzero alpha
4. Factoring terminates (Corollary 13.2.3)
5. Most of Chapter 13 focuses on this case

# Examples

**Example 1** (p. 396): d = -1 gives Z[i] (square lattice). d = -3 gives equilateral triangular lattice.

**Example 2** (p. 396): d = -5 gives Z[sqrt(-5)], the running example with non-unique factorization.

# Relationships

## Builds Upon
- **Quadratic field** -- Imaginary case d < 0

## Enables
- **Ring of integers** -- Forms a lattice in C

## Contrasts With
- **Real quadratic field** -- Real has infinite unit group

# Source Reference

Chapter 13: Quadratic Number Fields, Section 13.1, pages 394-396.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
