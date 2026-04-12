---
concept: Cancellation Law
slug: cancellation-law
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
  - integral-domain
extends: []
related:
  - zero-divisor
contrasts_with: []
answers_questions:
  - "What is the cancellation law in a ring?"
---

# Quick Definition

In an integral domain, if ab = ac and a != 0, then b = c. This cancellation law is equivalent to having no zero divisors.

# Core Definition

An integral domain R satisfies the cancellation law: if ab = ac and a != 0, then b = c (Artin, formula 11.7.1, p. 360). This follows because a(b-c) = 0 and a != 0 implies b - c = 0 since R has no zero divisors.

# Prerequisites

- **Integral domain** -- Cancellation holds in domains

# Key Properties

1. Equivalent to the absence of zero divisors
2. Essential for defining fractions (transitivity of equivalence requires cancellation)
3. Extends to ideals in quadratic integer rings (Corollary 13.4.9)

# Examples

**Example 1** (p. 360): In Z/(6), cancellation fails: 2*1 = 2*4 but 1 != 4.

# Relationships

## Builds Upon
- **Integral domain** -- Cancellation holds iff no zero divisors

# Source Reference

Chapter 11: Rings, Section 11.7, formula 11.7.1, page 360.

# Verification Notes

- Definition source: Direct from formula 11.7.1
- Confidence rationale: Explicit statement
- Uncertainties: None
- Cross-reference status: Verified
