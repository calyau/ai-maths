---
concept: Algebraic Number
slug: algebraic-number
category: number-theory
subcategory: algebraic-integers
tier: advanced
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Quadratic Number Fields"
chapter_number: 13
pdf_page: 394
section: "Algebraic Integers"
extraction_confidence: high
aliases: []
prerequisites:
  - polynomial-ring
extends: []
related:
  - algebraic-integer
  - transcendental-number
  - irreducible-polynomial
contrasts_with:
  - transcendental-number
answers_questions:
  - "What is an algebraic number?"
---

# Quick Definition

A complex number alpha is algebraic if it is a root of some nonzero polynomial with rational coefficients. If no such polynomial exists, alpha is transcendental.

# Core Definition

A complex number alpha that is the root of a polynomial with rational coefficients is called an algebraic number (Artin, p. 394). The irreducible polynomial for alpha over Q is the monic polynomial of lowest degree in Q[x] having alpha as a root. It generates the kernel of the substitution homomorphism Q[x] -> C sending x to alpha.

# Prerequisites

- **Polynomial ring** -- Algebraic numbers are roots of polynomials

# Key Properties

1. The irreducible polynomial over Q is unique and monic
2. Every rational number is algebraic (root of x - a)
3. The numbers e and pi are transcendental (but this is hard to prove)

# Examples

**Example 1** (p. 339): i + 3, 1/7, 7 + sqrt(2), and cube_root(3) + fifth_root(5) are algebraic.

**Example 2** (p. 339): e and pi are transcendental.

# Relationships

## Builds Upon
- **Polynomial ring** -- Defined via roots of polynomials

## Enables
- **Algebraic integer** -- Algebraic numbers whose irreducible polynomial has integer coefficients

## Contrasts With
- **Transcendental number** -- Not a root of any polynomial with rational coefficients

# Source Reference

Chapter 11, Section 11.1, page 339; Chapter 13, Section 13.1, page 394.

# Verification Notes

- Definition source: Direct from text
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
