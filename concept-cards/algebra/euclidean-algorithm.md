---
concept: Euclidean Algorithm
slug: euclidean-algorithm
category: factorization
subcategory: algorithms
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Factoring"
chapter_number: 12
pdf_page: 370
section: "Unique Factorization Domains"
extraction_confidence: high
aliases: []
prerequisites:
  - euclidean-domain
  - greatest-common-divisor
extends: []
related:
  - division-with-remainder
contrasts_with: []
answers_questions:
  - "How do I compute the greatest common divisor?"
---

# Quick Definition

The Euclidean algorithm computes the gcd of two elements in a Euclidean domain by repeated division with remainder: gcd(f, g) = gcd(f, r) where g = fq + r, continuing until the remainder is zero.

# Core Definition

The Euclidean algorithm for computing gcd(f, g) in a Euclidean domain: suppose deg g >= deg f. Write g = fq + r. Then gcd(f, g) = gcd(f, r). If r = 0, gcd = f. Otherwise replace f and g by r and f, and repeat. Since sizes decrease, the process terminates (Artin, p. 377).

# Prerequisites

- **Euclidean domain** -- Requires division with remainder
- **Greatest common divisor** -- The algorithm computes the gcd

# Key Properties

1. Terminates because the size function strictly decreases
2. Also produces the linear combination d = rf + sg
3. Works in Z, F[x], Z[i], and any Euclidean domain

# Examples

**Example 1** (p. 377): To find gcd of polynomials, divide and replace until remainder is 0.

# Relationships

## Builds Upon
- **Euclidean domain** -- Requires the division-with-remainder property
- **Greatest common divisor** -- Output of the algorithm

# Source Reference

Chapter 12: Factoring, Section 12.2, page 377.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Explicit description of algorithm
- Uncertainties: None
- Cross-reference status: Verified
