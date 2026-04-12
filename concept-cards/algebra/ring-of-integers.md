---
concept: Ring of Integers of a Quadratic Field
slug: ring-of-integers
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
  - "ring of integers"
  - "ring of algebraic integers"
prerequisites:
  - quadratic-field
  - algebraic-integer
extends:
  - ring
related:
  - quadratic-integer
  - norm-quadratic-field
contrasts_with: []
answers_questions:
  - "What is the ring of integers of a quadratic field?"
---

# Quick Definition

The ring of integers R of a quadratic field Q[sqrt(d)] consists of all algebraic integers in that field. When d = 2 or 3 mod 4, R = Z[sqrt(d)]. When d = 1 mod 4, R = Z[eta] where eta = (1+sqrt(d))/2.

# Core Definition

The algebraic integers in the quadratic field Q[sqrt(d)] form a ring R, the ring of integers in the field. By Proposition 13.1.6: if d = 2 or 3 mod 4, then a = a + b*sqrt(d) is an algebraic integer iff a and b are integers (so R = Z[sqrt(d)]). If d = 1 mod 4, then a and b are either both integers or both half-integers (so R = Z[eta] where eta = (1+sqrt(d))/2) (Artin, Proposition 13.1.6, p. 395).

# Prerequisites

- **Quadratic field** -- The ring of integers lives inside Q[sqrt(d)]
- **Algebraic integer** -- Elements of R are algebraic integers

# Key Properties

1. R is always a ring (closed under addition and multiplication)
2. When d < 0, R forms a lattice in the complex plane
3. When d = -1, R = Z[i] (Gaussian integers)
4. When d = -3, R = Z[omega] where omega = e^{2pi i/3}

# Examples

**Example 1** (p. 395): For d = -5 (which is 3 mod 4), R = Z[sqrt(-5)] = {a + b*sqrt(-5) | a, b in Z}.

**Example 2** (p. 395): For d = -7 (which is 1 mod 4), R = Z[(1+sqrt(-7))/2].

**Example 3** (p. 395): For d = -1, R = Z[i] is the ring of Gaussian integers.

# Relationships

## Builds Upon
- **Quadratic field** -- R is the ring of integers in Q[sqrt(d)]
- **Algebraic integer** -- Elements of R

## Enables
- **Ideal factorization** -- Unique factorization of ideals in R
- **Class group** -- Measures failure of unique factorization in R

# Source Reference

Chapter 13: Quadratic Number Fields, Section 13.1, Proposition 13.1.6, pages 395-396.

# Verification Notes

- Definition source: Direct from Proposition 13.1.6
- Confidence rationale: Explicit characterization by d mod 4
- Uncertainties: None
- Cross-reference status: Verified
