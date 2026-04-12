---
concept: Discriminant of a Quadratic Field
slug: discriminant-quadratic-field
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
extraction_confidence: medium
aliases: []
prerequisites:
  - quadratic-field
  - ring-of-integers
extends: []
related:
  - trace-quadratic-field
contrasts_with: []
answers_questions:
  - "What is the discriminant of a quadratic field?"
---

# Quick Definition

The discriminant of a quadratic field Q[sqrt(d)] is related to the area of the fundamental domain of its ring of integers. The lattice area is sqrt(|d|) when d = 2 or 3 mod 4, and sqrt(|d|)/2 when d = 1 mod 4.

# Core Definition

For the ring of integers in Q[sqrt(d)], the area of the fundamental parallelogram is Delta(R) = sqrt(|d|) if d = 2 or 3 mod 4, and Delta(R) = sqrt(|d|)/2 if d = 1 mod 4 (Artin, formula 13.7.9, p. 414). The discriminant of the field is 4d when d = 2 or 3 mod 4, and d when d = 1 mod 4 (implicit from the lattice structure).

# Prerequisites

- **Quadratic field** -- The field Q[sqrt(d)]
- **Ring of integers** -- The lattice structure depends on d mod 4

# Key Properties

1. Controls the Minkowski bound mu = (2/sqrt(3)) * Delta(R) or Delta(R)/sqrt(3)
2. Related to ramification: primes dividing the discriminant ramify
3. Determines the lattice geometry of the ring of integers

# Examples

**Example 1** (p. 414): For d = -5 (which is 3 mod 4), Delta(R) = sqrt(5).

**Example 2** (p. 414): For d = -7 (which is 1 mod 4), Delta(R) = sqrt(7)/2.

# Relationships

## Builds Upon
- **Quadratic field** -- Discriminant is a field invariant
- **Ring of integers** -- Determines lattice area

# Source Reference

Chapter 13: Quadratic Number Fields, Section 13.7, formula 13.7.9, page 414.

# Verification Notes

- Definition source: Synthesized from formula 13.7.9 and lattice discussion
- Confidence rationale: Medium -- Artin gives lattice areas but does not use "discriminant" terminology explicitly in this section
- Uncertainties: The formal discriminant is not boxed as a definition
- Cross-reference status: Verified
