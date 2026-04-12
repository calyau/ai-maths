---
concept: Content of a Polynomial
slug: content-of-polynomial
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
aliases:
  - "content"
prerequisites:
  - polynomial-ring
  - greatest-common-divisor
extends: []
related:
  - primitive-polynomial
  - gauss-lemma
contrasts_with: []
answers_questions:
  - "What is the content of a polynomial?"
---

# Quick Definition

Every rational polynomial of positive degree factors uniquely as f(x) = c * f_0(x) where c is a rational number and f_0 is primitive. The rational number c is essentially the content (the gcd of the coefficients, up to sign).

# Core Definition

Every polynomial f(x) of positive degree with rational coefficients can be written uniquely as a product f(x) = c * f_0(x), where c is a rational number and f_0(x) is a primitive polynomial. If f is an integer polynomial, then c is an integer, and up to sign, c is the greatest common divisor of the coefficients of f (Artin, Lemma 12.3.5, p. 380).

# Prerequisites

- **Polynomial ring** -- Content is defined for rational polynomials
- **Greatest common divisor** -- The content is the gcd of coefficients

# Key Properties

1. The factorization f = c * f_0 is unique
2. c is an integer iff f is an integer polynomial
3. The content is multiplicative (follows from Gauss's Lemma)

# Examples

**Example 1** (p. 379): 6x^3 + 9x^2 + 9x + 3 = 3 * (2x^3 + 3x^2 + 3x + 1). The content is 3.

# Relationships

## Builds Upon
- **Greatest common divisor** -- Content = gcd of coefficients

## Related
- **Primitive polynomial** -- f_0 is the primitive part
- **Gauss's Lemma** -- Content is multiplicative

# Source Reference

Chapter 12: Factoring, Section 12.3, Lemma 12.3.5, page 380.

# Verification Notes

- Definition source: Direct from Lemma 12.3.5
- Confidence rationale: Explicit statement
- Uncertainties: None
- Cross-reference status: Verified
