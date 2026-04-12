---
concept: Unique Factorization in Quadratic Fields
slug: unique-factorization-in-quadratic-fields
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
  - unique-factorization-domain
  - class-group
extends: []
related:
  - ideal-factorization
contrasts_with: []
answers_questions:
  - "Which quadratic integer rings have unique factorization?"
---

# Quick Definition

The ring of integers in an imaginary quadratic field Q[sqrt(d)] has unique factorization of elements if and only if d is one of: -1, -2, -3, -7, -11, -19, -43, -67, -163. For all other d, unique factorization fails.

# Core Definition

The ring of integers R in the imaginary quadratic field Q[sqrt(d)] is a UFD if and only if d is one of -1, -2, -3, -7, -11, -19, -43, -67, -163 (Artin, Theorem 13.2.5, p. 398). Moreover, R is a UFD iff it is a PID iff the class group C is trivial (Theorem 13.5.6, p. 406).

# Prerequisites

- **Ring of integers** -- R is the ring of integers
- **Unique factorization domain** -- Testing whether R is a UFD
- **Class group** -- C trivial iff R is a UFD

# Key Properties

1. Exactly 9 values of d give unique factorization (Heegner-Baker-Stark theorem)
2. R is a UFD iff PID iff class number 1
3. For d = 3 mod 4 and d < -1, R is never a UFD (Proposition 13.2.4)
4. This was conjectured by Gauss and fully proved in the mid-20th century

# Examples

**Example 1** (p. 398): d = -1: Z[i] is a UFD (Euclidean domain).

**Example 2** (p. 398): d = -5: Z[sqrt(-5)] is NOT a UFD (2*3 = (1+sqrt(-5))(1-sqrt(-5))).

**Example 3** (p. 416): d = -163: Z[(1+sqrt(-163))/2] is a UFD (class number 1).

# Relationships

## Builds Upon
- **Ring of integers** -- R is the object of study
- **Class group** -- Class number 1 characterizes UFDs

## Related
- **Ideal factorization** -- Ideals always factor uniquely, even when elements don't

# Source Reference

Chapter 13: Quadratic Number Fields, Section 13.2, Theorem 13.2.5, page 398; Section 13.5, Theorem 13.5.6, page 406.

# Verification Notes

- Definition source: Direct from Theorems 13.2.5 and 13.5.6
- Confidence rationale: Famous theorem, explicitly stated
- Uncertainties: Baker-Heegner-Stark proof not given
- Cross-reference status: Verified
