---
concept: Characteristic of a Ring
slug: characteristic-of-a-ring
category: ring-theory
subcategory: basic-structures
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Rings"
chapter_number: 11
pdf_page: 339
section: "Homomorphisms and Ideals"
extraction_confidence: high
aliases:
  - "ring characteristic"
  - "char R"
prerequisites:
  - ring
  - ring-homomorphism
extends: []
related:
  - field
contrasts_with: []
answers_questions:
  - "What is the characteristic of a ring?"
---

# Quick Definition

The characteristic of a ring R is the non-negative integer n that generates the kernel of the unique homomorphism Z -> R. If n = 0, no positive multiple of 1 is zero; otherwise n is the smallest positive integer such that n * 1 = 0 in R.

# Core Definition

The characteristic of a ring R is the non-negative integer n that generates the kernel of the unique homomorphism phi: Z -> R (Proposition 11.3.10). If n = 0, no positive multiple of 1 in R is zero. Otherwise n is the smallest positive integer such that "n times 1" is zero in R (Artin, p. 350).

# Prerequisites

- **Ring** -- Characteristic is defined for rings
- **Ring homomorphism** -- The unique map Z -> R determines the characteristic

# Key Properties

1. There is exactly one homomorphism Z -> R (Proposition 11.3.10)
2. The characteristic can be any non-negative integer
3. Fields have characteristic 0 or a prime p

# Examples

**Example 1** (p. 350): Z has characteristic 0.

**Example 2** (p. 350): F_p has characteristic p.

# Relationships

## Builds Upon
- **Ring** -- Defined for any ring

# Source Reference

Chapter 11: Rings, Section 11.3, page 350.

# Verification Notes

- Definition source: Direct from text following Proposition 11.3.10
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
