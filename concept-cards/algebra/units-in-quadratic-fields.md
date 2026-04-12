---
concept: Units in Quadratic Integer Rings
slug: units-in-quadratic-fields
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
aliases: []
prerequisites:
  - ring-of-integers
  - norm-quadratic-field
  - unit-element
extends: []
related:
  - fundamental-unit
contrasts_with: []
answers_questions:
  - "What are the units in a quadratic integer ring?"
---

# Quick Definition

An element alpha of the ring of integers R is a unit iff N(alpha) = +/-1. For imaginary quadratic fields, the unit group is finite: {+/-1} unless d = -1 (units {+/-1, +/-i}) or d = -3 (six units). For real quadratic fields, the unit group is infinite.

# Core Definition

An element alpha of R is a unit if and only if N(alpha) = 1 (for imaginary quadratic fields) or N(alpha) = +/-1 (for real quadratic fields). If so, alpha^{-1} = alpha-bar (or +/- alpha') (Artin, Proposition 13.2.2, p. 397).

# Prerequisites

- **Ring of integers** -- Units are invertible elements of R
- **Norm (quadratic field)** -- Units have norm +/-1
- **Unit element** -- Units are invertible

# Key Properties

1. N(alpha) = 1 iff alpha is a unit (imaginary case)
2. For d = -1: units are {1, -1, i, -i}
3. For d = -3: units are the six powers of e^{2pi i/6}
4. For all other d < 0: units are {+/-1}
5. For d > 0: the unit group is infinite

# Examples

**Example 1** (p. 397): In Z[sqrt(-5)], units are only {+/-1}.

**Example 2** (p. 397): In Z[i], units are {1, -1, i, -i}.

**Example 3** (p. 418): In Z[sqrt(2)], (1+sqrt(2))^n for all n gives infinitely many units.

# Relationships

## Builds Upon
- **Norm (quadratic field)** -- N(alpha) = +/-1 characterizes units

## Related
- **Fundamental unit** -- Generator of the infinite unit group (real case)

# Source Reference

Chapter 13: Quadratic Number Fields, Section 13.2, Proposition 13.2.2, pages 397-398.

# Verification Notes

- Definition source: Direct from Proposition 13.2.2
- Confidence rationale: Explicit characterization
- Uncertainties: None
- Cross-reference status: Verified
