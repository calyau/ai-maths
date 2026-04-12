---
concept: Primitive Polynomial
slug: primitive-polynomial
category: factorization
subcategory: integer-polynomials
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Factoring"
chapter_number: 12
pdf_page: 370
section: "Gauss's Lemma"
extraction_confidence: high
aliases: []
prerequisites:
  - polynomial-ring
  - greatest-common-divisor
extends: []
related:
  - gauss-lemma
  - content-of-polynomial
contrasts_with: []
answers_questions:
  - "What is a primitive polynomial?"
---

# Quick Definition

A primitive polynomial is an integer polynomial of positive degree with positive leading coefficient whose coefficients have gcd 1. Equivalently, it is not divisible by any prime integer.

# Core Definition

A polynomial f(x) = a_n x^n + ... + a_0 with rational coefficients is called primitive if it is an integer polynomial of positive degree, the gcd of its coefficients a_0, ..., a_n is 1, and its leading coefficient a_n is positive (Artin, p. 379). Equivalently, f is primitive iff it is not divisible by any integer prime p (Lemma 12.3.3).

# Prerequisites

- **Polynomial ring** -- Primitive polynomials are elements of Z[x]
- **Greatest common divisor** -- The gcd of coefficients must be 1

# Key Properties

1. Every rational polynomial of positive degree factors uniquely as c * f_0 where c is rational and f_0 is primitive (Lemma 12.3.5)
2. f is primitive iff its reduction modulo p is nonzero for every prime p
3. The product of primitive polynomials is primitive (Gauss's Lemma)

# Examples

**Example 1** (p. 379): 2x + 1 is primitive; 6x + 9 is not (gcd of coefficients is 3).

# Relationships

## Builds Upon
- **Polynomial ring** -- Elements of Z[x]

## Enables
- **Gauss's Lemma** -- Products of primitives are primitive

# Source Reference

Chapter 12: Factoring, Section 12.3, page 379, Lemma 12.3.3.

# Verification Notes

- Definition source: Direct from text and Lemma 12.3.3
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
