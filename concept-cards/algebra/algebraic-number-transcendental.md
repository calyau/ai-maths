---
concept: Transcendental Number
slug: algebraic-number-transcendental
category: ring-theory
subcategory: basic-structures
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Rings"
chapter_number: 11
pdf_page: 339
section: "Definition of a Ring"
extraction_confidence: high
aliases:
  - "transcendental"
prerequisites:
  - algebraic-number
extends: []
related:
  - polynomial-ring
contrasts_with:
  - algebraic-number
answers_questions:
  - "What is a transcendental number?"
---

# Quick Definition

A complex number is transcendental if it is not algebraic -- it is not a root of any nonzero polynomial with integer coefficients. When alpha is transcendental, Z[alpha] is isomorphic to the polynomial ring Z[x].

# Core Definition

If there is no polynomial with integer coefficients having alpha as a root, alpha is transcendental. When alpha is transcendental, two distinct polynomial expressions represent distinct complex numbers, and Z[alpha] corresponds bijectively to Z[x] (Artin, p. 339).

# Prerequisites

- **Algebraic number** -- Transcendental is defined by contrast with algebraic

# Key Properties

1. The numbers e and pi are transcendental (though hard to prove)
2. When alpha is transcendental, Z[alpha] ~ Z[x] as rings
3. When alpha is algebraic, Z[alpha] is a quotient of Z[x]

# Examples

**Example 1** (p. 339): e and pi are transcendental.

**Example 2** (p. 339): Z[pi] ~ Z[x] since pi is transcendental.

# Relationships

## Contrasts With
- **Algebraic number** -- Algebraic numbers ARE roots of polynomials

# Source Reference

Chapter 11: Rings, Section 11.1, page 339.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
