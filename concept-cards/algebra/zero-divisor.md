---
concept: Zero Divisor
slug: zero-divisor
category: ring-theory
subcategory: basic-structures
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Rings"
chapter_number: 11
pdf_page: 339
section: "Fractions"
extraction_confidence: high
aliases: []
prerequisites:
  - ring
extends: []
related:
  - integral-domain
contrasts_with:
  - unit-element
answers_questions:
  - "What is a zero divisor?"
---

# Quick Definition

A zero divisor is a nonzero element a of a ring such that ab = 0 for some nonzero b. An integral domain is a nonzero ring with no zero divisors.

# Core Definition

An element a of a ring is called a zero divisor if it is nonzero, and if there is another nonzero element b such that ab = 0. An integral domain is a nonzero ring which contains no zero divisors (Artin, p. 360).

# Prerequisites

- **Ring** -- Zero divisors are elements of a ring

# Key Properties

1. Zero divisors prevent the cancellation law from holding
2. A ring with zero divisors cannot have fractions defined in the usual way
3. Zero itself is NOT called a zero divisor (by convention)

# Examples

**Example 1** (p. 360): In Z/(6), both 2 and 3 are zero divisors since 2 * 3 = 0.

**Example 2** (p. 360): In R x R', the idempotents (1,0) and (0,1) are zero divisors.

# Relationships

## Builds Upon
- **Ring** -- Zero divisors are ring elements

## Related
- **Integral domain** -- Defined as rings without zero divisors

## Contrasts With
- **Unit element** -- A unit cannot be a zero divisor

# Source Reference

Chapter 11: Rings, Section 11.7, page 360.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
