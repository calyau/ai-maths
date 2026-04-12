---
concept: Fundamental Theorem of Arithmetic
slug: fundamental-theorem-of-arithmetic
category: factorization
subcategory: basic-divisibility
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Factoring"
chapter_number: 12
pdf_page: 370
section: "Factoring Integers"
extraction_confidence: high
aliases: []
prerequisites:
  - unique-factorization-domain
extends: []
related:
  - prime-element
contrasts_with: []
answers_questions:
  - "What is unique factorization in Z?"
---

# Quick Definition

Every positive integer a != 1 can be written as a product a = p_1 ... p_k of positive primes, and this expression is unique up to ordering.

# Core Definition

(Fundamental Theorem of Arithmetic) Every positive integer a != 1 can be written as a product a = p_1 ... p_k, where the p_i are positive prime integers and k >= 0. This expression is unique except for the ordering of the prime factors (Artin, Theorem 12.1.2(d), p. 370).

# Prerequisites

- **Unique factorization domain** -- Z is a UFD

# Key Properties

1. Z is a Euclidean domain, hence PID, hence UFD
2. The theorem follows from the chain: Euclidean => PID => UFD
3. Every ideal of Z is principal (Theorem 12.1.2(a))
4. gcd(a,b) exists and equals ra + sb for some integers r, s

# Examples

**Example 1** (p. 370): 12 = 2^2 * 3, uniquely.

# Relationships

## Builds Upon
- **Unique factorization domain** -- Z is the prototypical UFD

# Source Reference

Chapter 12: Factoring, Section 12.1, Theorem 12.1.2, page 370.

# Verification Notes

- Definition source: Direct from Theorem 12.1.2
- Confidence rationale: Explicit statement
- Uncertainties: None
- Cross-reference status: Verified
