---
concept: Prime Ideal
slug: prime-ideal
category: number-theory
subcategory: ideal-theory
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Quadratic Number Fields"
chapter_number: 13
pdf_page: 394
section: "Factoring Ideals"
extraction_confidence: high
aliases: []
prerequisites:
  - ideal
  - integral-domain
extends:
  - ideal
related:
  - maximal-ideal
  - prime-element
  - ideal-factorization
contrasts_with:
  - maximal-ideal
answers_questions:
  - "What is a prime ideal?"
  - "How do prime ideals relate to integral domains?"
---

# Quick Definition

A prime ideal P is a proper ideal such that R/P is an integral domain: if ab is in P, then a is in P or b is in P. In the ring of integers of a quadratic field, prime ideals are the same as maximal ideals.

# Core Definition

The following conditions on an ideal P are equivalent (defining a prime ideal): (a) R/P is an integral domain, (b) P != R and if ab in P then a in P or b in P, (c) P != R and if AB subset P for ideals A, B, then A subset P or B subset P (Artin, Proposition 13.5.1, p. 405).

# Prerequisites

- **Ideal** -- Prime ideals are special ideals
- **Integral domain** -- R/P is a domain iff P is prime

# Key Properties

1. Every maximal ideal is prime (Corollary 13.5.2)
2. (0) is prime iff R is a domain
3. (a) is prime iff a is a prime element
4. In the ring of integers of a quadratic field, nonzero prime = maximal (Lemma 13.5.4)

# Examples

**Example 1** (p. 405): In Z, the prime ideals are (0) and (p) for prime p.

**Example 2** (p. 402): In Z[sqrt(-5)], the ideals A = (2, 1+delta) and B = (3, 1+delta) are prime ideals.

# Relationships

## Builds Upon
- **Ideal** -- Prime ideals are special ideals

## Enables
- **Ideal factorization** -- Ideals factor uniquely into prime ideals
- **Class group** -- Prime ideals generate the class group

## Contrasts With
- **Maximal ideal** -- Every maximal is prime; in quadratic integer rings they coincide (for nonzero ideals)

# Source Reference

Chapter 13: Quadratic Number Fields, Section 13.5, Proposition 13.5.1, pages 405-406.

# Verification Notes

- Definition source: Direct from Proposition 13.5.1
- Confidence rationale: Explicit equivalent conditions
- Uncertainties: None
- Cross-reference status: Verified
