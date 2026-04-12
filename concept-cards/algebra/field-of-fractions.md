---
concept: Field of Fractions
slug: field-of-fractions
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
aliases:
  - "fraction field"
  - "quotient field"
prerequisites:
  - integral-domain
extends: []
related:
  - rational-function
contrasts_with: []
answers_questions:
  - "What is a field of fractions?"
---

# Quick Definition

The field of fractions of an integral domain R is the smallest field containing R, constructed from equivalence classes of fractions a/b with a, b in R and b != 0.

# Core Definition

Let F be the set of equivalence classes of fractions of elements of an integral domain R (where a_1/b_1 ~ a_2/b_2 if a_1 b_2 = a_2 b_1). Then: (a) F is a field, the fraction field of R; (b) R embeds as a subring via a -> a/1; (c) (Mapping Property) if R embeds in another field F', then F embeds in F' too (Artin, Theorem 11.7.2, p. 361).

# Prerequisites

- **Integral domain** -- The domain property is essential for equivalence to be transitive

# Key Properties

1. Fractions a/b with b != 0, up to cross-multiplication equivalence
2. R embeds in F via a -> a/1
3. F is the "smallest" field containing R
4. The mapping property: any embedding R -> F' extends to F -> F'

# Examples

**Example 1** (p. 361): The fraction field of Z is Q.

**Example 2** (p. 361): The fraction field of K[x] is the field K(x) of rational functions.

# Relationships

## Builds Upon
- **Integral domain** -- Fractions require no zero divisors

## Enables
- **Rational function** -- Fractions of polynomials

# Source Reference

Chapter 11: Rings, Section 11.7 "Fractions," Theorem 11.7.2, pages 360-362.

# Verification Notes

- Definition source: Direct from Theorem 11.7.2
- Confidence rationale: Explicit theorem statement
- Uncertainties: None
- Cross-reference status: Verified
