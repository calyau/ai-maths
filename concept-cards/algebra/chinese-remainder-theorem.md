---
concept: Chinese Remainder Theorem
slug: chinese-remainder-theorem
category: ring-theory
subcategory: quotient-constructions
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Rings"
chapter_number: 11
pdf_page: 339
section: "Product Rings"
extraction_confidence: high
aliases:
  - "CRT"
prerequisites:
  - ideal
  - product-ring
  - quotient-ring
extends: []
related:
  - relatively-prime
contrasts_with: []
answers_questions:
  - "What is the Chinese Remainder Theorem for rings?"
---

# Quick Definition

The Chinese Remainder Theorem states: if ideals I and J satisfy I + J = R, then for any a, b in R there exists x with x = a mod I and x = b mod J. If IJ = 0, then R ~ (R/I) x (R/J).

# Core Definition

Let I and J be ideals of a ring R such that I + J = R. Then: (a) IJ = I intersect J, (b) for any pair a, b in R, there exists x such that x = a mod I and x = b mod J, (c) if IJ = 0, then R is isomorphic to the product ring (R/I) x (R/J) (Artin, Exercise 6.8, p. 361).

# Prerequisites

- **Ideal** -- I and J are ideals
- **Product ring** -- The decomposition yields a product
- **Quotient ring** -- Uses quotient ring structure

# Key Properties

1. The condition I + J = R means I and J are "coprime" ideals
2. For Z: (m) + (n) = Z iff gcd(m,n) = 1
3. Simultaneous congruences have solutions iff ideals are coprime

# Examples

**Example 1** (Exercise 12.1.3, p. 391): For relatively prime integers m, n and any a, b, there exists x with x = a mod m and x = b mod n.

**Example 2** (Exercise 6.2, p. 361): Z/(6) ~ Z/(2) x Z/(3).

# Relationships

## Builds Upon
- **Ideal** -- Coprimality of ideals
- **Product ring** -- The decomposition

## Related
- **Relatively prime** -- Coprime ideals

# Source Reference

Chapter 11: Rings, Section 11.6, Exercise 6.8, page 361; Chapter 12, Exercise 1.3, page 391.

# Verification Notes

- Definition source: Synthesized from exercises and discussion
- Confidence rationale: High -- CRT is stated explicitly as an exercise with all parts
- Uncertainties: None
- Cross-reference status: Verified
