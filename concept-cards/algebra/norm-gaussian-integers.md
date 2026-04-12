---
concept: Norm (Gaussian Integers)
slug: norm-gaussian-integers
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
  - "Gaussian norm"
prerequisites:
  - gaussian-integer
extends: []
related:
  - gaussian-prime
  - euclidean-domain
contrasts_with: []
answers_questions:
  - "What is the norm of a Gaussian integer?"
---

# Quick Definition

The norm of a Gaussian integer a + bi is N(a+bi) = a^2 + b^2 = |a+bi|^2. It is multiplicative: N(alpha*beta) = N(alpha)N(beta), and serves as the size function making Z[i] a Euclidean domain.

# Core Definition

For alpha = a + bi in Z[i], the norm is N(alpha) = alpha * alpha-bar = a^2 + b^2 (Artin, p. 371). The norm is multiplicative: N(alpha*beta) = N(alpha)N(beta). It takes values in the non-negative integers, with N(alpha) = 0 iff alpha = 0.

# Prerequisites

- **Gaussian integer** -- Norm is defined for elements of Z[i]

# Key Properties

1. N(alpha) = a^2 + b^2 for alpha = a + bi
2. Multiplicative: N(alpha*beta) = N(alpha)N(beta)
3. N(alpha) = 1 iff alpha is a unit
4. Serves as size function for Euclidean division

# Examples

**Example 1** (p. 386): N(2+i) = 4 + 1 = 5.

**Example 2** (p. 386): N(1+i) = 2, N(3) = 9.

# Relationships

## Builds Upon
- **Gaussian integer** -- Defined for Z[i]

## Enables
- **Euclidean domain** -- N is the size function
- **Gaussian prime** -- Primes are analyzed via their norms

# Source Reference

Chapter 12: Factoring, Sections 12.2 and 12.5, pages 371, 386.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
