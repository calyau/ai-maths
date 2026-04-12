---
concept: Greatest Common Divisor
slug: greatest-common-divisor
category: factorization
subcategory: basic-divisibility
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Factoring"
chapter_number: 12
pdf_page: 370
section: "Unique Factorization Domains"
extraction_confidence: high
aliases:
  - "gcd"
prerequisites:
  - divisibility
  - integral-domain
extends: []
related:
  - euclidean-algorithm
  - relatively-prime
contrasts_with: []
answers_questions:
  - "What is a greatest common divisor?"
---

# Quick Definition

A greatest common divisor of a and b in an integral domain is an element d that divides both a and b, and is itself divisible by any other common divisor. In a PID, d generates the ideal (a, b) and can be written as d = ra + sb.

# Core Definition

A greatest common divisor d of elements a and b (not both zero) in an integral domain is an element satisfying: (a) d divides a and b, and (b) if e divides a and b, then e divides d (Artin, p. 372). In a PID, the gcd exists and generates the ideal (a, b): d = ra + sb (Proposition 12.2.8).

# Prerequisites

- **Divisibility** -- GCD is defined via divisibility
- **Integral domain** -- Context for the definition

# Key Properties

1. Any two gcds are associates
2. In a PID, gcd always exists and is a linear combination ra + sb
3. In a UFD, gcd exists but may not be expressible as ra + sb
4. Elements are relatively prime if gcd = 1

# Examples

**Example 1** (p. 372): In Z[sqrt(-5)], gcd of 6 and 2+2sqrt(-5) does not exist (2 and 1+sqrt(-5) are both maximal common divisors but neither divides the other).

**Example 2** (p. 377): In Z[x], gcd(2, x) = 1, but 1 cannot be written as r*2 + s*x with r, s in Z[x].

# Relationships

## Builds Upon
- **Divisibility** -- GCD is a divisibility concept

## Enables
- **Euclidean algorithm** -- Computes the gcd
- **Relatively prime** -- gcd(a,b) = 1

# Source Reference

Chapter 12: Factoring, Section 12.2, Proposition 12.2.8, pages 372-373.

# Verification Notes

- Definition source: Direct from text and Proposition 12.2.8
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
