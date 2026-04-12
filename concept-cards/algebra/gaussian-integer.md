---
concept: Gaussian Integer
slug: gaussian-integer
category: factorization
subcategory: gaussian-integers
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Factoring"
chapter_number: 12
pdf_page: 370
section: "Gauss Primes"
extraction_confidence: high
aliases:
  - "Gauss integer"
  - "Z[i]"
prerequisites:
  - ring
  - subring
extends:
  - ring
related:
  - norm-gaussian-integers
  - gaussian-prime
  - euclidean-domain
contrasts_with: []
answers_questions:
  - "What are the Gaussian integers?"
---

# Quick Definition

The Gaussian integers Z[i] = {a + bi | a, b in Z} form a subring of C. They form a square lattice in the complex plane and constitute a Euclidean domain with norm N(a+bi) = a^2 + b^2.

# Core Definition

The Gauss integers are the complex numbers of the form a + bi where a and b are integers, forming a subring of C denoted Z[i] (Artin, formula 11.1.1, p. 339). The ring Z[i] is a Euclidean domain with size function sigma(a) = |a|^2 = a^2 + b^2 (Proposition 12.2.5(c), p. 371).

# Prerequisites

- **Ring** -- Z[i] is a ring
- **Subring** -- Z[i] is a subring of C

# Key Properties

1. Elements form a square lattice in C
2. Z[i] is a Euclidean domain (hence PID and UFD)
3. Units are {1, -1, i, -i}
4. The norm N(a+bi) = a^2 + b^2 is multiplicative

# Examples

**Example 1** (p. 339): 3 + 2i, -1 + 4i are Gaussian integers.

**Example 2** (p. 371): Division with remainder: for any beta in Z[i] and nonzero alpha, there exist q, r in Z[i] with beta = alpha*q + r and N(r) < N(alpha).

# Relationships

## Builds Upon
- **Ring** -- Z[i] is a ring

## Enables
- **Gaussian prime** -- Prime elements of Z[i]
- **Norm (Gaussian integers)** -- N(a+bi) = a^2 + b^2

# Source Reference

Chapter 11, Section 11.1, formula 11.1.1, p. 339; Chapter 12, Section 12.2, Proposition 12.2.5, p. 371; Section 12.5, pages 386-390.

# Verification Notes

- Definition source: Direct from formula 11.1.1 and Proposition 12.2.5
- Confidence rationale: Explicit definition at multiple points
- Uncertainties: None
- Cross-reference status: Verified
