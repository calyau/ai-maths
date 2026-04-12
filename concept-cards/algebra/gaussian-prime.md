---
concept: Gaussian Prime
slug: gaussian-prime
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
  - "Gauss prime"
prerequisites:
  - gaussian-integer
  - norm-gaussian-integers
  - prime-element
extends: []
related:
  - unique-factorization-domain
contrasts_with: []
answers_questions:
  - "What are the Gaussian primes?"
---

# Quick Definition

The Gaussian primes are the prime elements of Z[i]. An integer prime p is a Gaussian prime iff p = 3 mod 4. Primes p = 1 mod 4 (and p = 2) factor as products of conjugate Gaussian primes: p = pi * pi-bar.

# Core Definition

A Gaussian prime is a prime element of Z[i] (Artin, Section 12.5, p. 386). Theorem 12.5.2 classifies them: (a) If pi is a Gaussian prime, then pi*pi-bar is either a prime integer or the square of a prime. (b) An integer prime p is either itself a Gaussian prime, or the product of a Gaussian prime and its conjugate. (c) The primes p that are Gaussian primes are those congruent to 3 mod 4. (d) A prime p factors as pi*pi-bar iff p = 1 mod 4 or p = 2, iff p = a^2 + b^2.

# Prerequisites

- **Gaussian integer** -- Primes live in Z[i]
- **Norm (Gaussian integers)** -- Used to analyze factorization
- **Prime element** -- Gaussian primes are prime elements of Z[i]

# Key Properties

1. p = 2: factors as -i(1+i)^2, so 1+i is a Gaussian prime
2. p = 1 mod 4: p = pi * pi-bar where pi is a Gaussian prime
3. p = 3 mod 4: p remains a Gaussian prime in Z[i]
4. The factorization condition p = a^2 + b^2 determines which primes split

# Examples

**Example 1** (p. 386): 5 = (2+i)(2-i), so 2+i and 2-i are Gaussian primes.

**Example 2** (p. 386): 3 has no proper factor in Z[i], so 3 is a Gaussian prime.

**Example 3** (p. 386): 2 = -i(1+i)^2, so 1+i is a Gaussian prime.

# Relationships

## Builds Upon
- **Gaussian integer** -- Z[i] is the ambient ring
- **Norm (Gaussian integers)** -- Key tool for the classification

## Related
- **Unique factorization domain** -- Z[i] has unique factorization

# Source Reference

Chapter 12: Factoring, Section 12.5 "Gauss Primes," Theorem 12.5.2, pages 386-390.

# Verification Notes

- Definition source: Direct from Theorem 12.5.2
- Confidence rationale: Explicit classification theorem
- Uncertainties: None
- Cross-reference status: Verified
