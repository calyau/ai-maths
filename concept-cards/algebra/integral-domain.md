---
concept: Integral Domain
slug: integral-domain
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
aliases:
  - "domain"
prerequisites:
  - ring
extends:
  - ring
related:
  - zero-divisor
  - field-of-fractions
  - cancellation-law
contrasts_with:
  - zero-divisor
answers_questions:
  - "What is an integral domain?"
  - "How do prime ideals relate to integral domains?"
---

# Quick Definition

An integral domain is a nonzero ring in which the product of two nonzero elements is always nonzero. Equivalently, it has no zero divisors.

# Core Definition

An integral domain R, or just a domain for short, is a ring with this property: R is not the zero ring, and if a and b are elements of R whose product ab is zero, then a = 0 or b = 0 (Artin, p. 360).

# Prerequisites

- **Ring** -- An integral domain is a ring with an additional property

# Key Properties

1. No zero divisors: ab = 0 implies a = 0 or b = 0
2. Satisfies the cancellation law: ab = ac and a != 0 implies b = c
3. Any subring of a field is a domain
4. If R is a domain, R[x] is a domain
5. A quotient ring R/P is a domain if and only if P is a prime ideal

# Context & Application

Integral domains are the natural setting for factorization theory, since they guarantee the cancellation law and prevent pathological behavior with zero divisors. Fractions can only be formed in domains.

# Examples

**Example 1** (p. 360): Z is an integral domain.

**Example 2** (p. 360): Z/(6) is NOT an integral domain since 2 * 3 = 0.

**Example 3** (p. 360): A product R x R' of nonzero rings is never an integral domain.

# Relationships

## Builds Upon
- **Ring** -- A domain is a ring without zero divisors

## Enables
- **Field of fractions** -- Every domain embeds in its fraction field
- **Unique factorization domain** -- UFDs are special domains

## Related
- **Zero divisor** -- Absence of zero divisors defines domains
- **Prime ideal** -- R/P is a domain iff P is prime

## Contrasts With
- **Zero divisor** -- Domains have no zero divisors

# Source Reference

Chapter 11: Rings, Section 11.7 "Fractions," page 360.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
