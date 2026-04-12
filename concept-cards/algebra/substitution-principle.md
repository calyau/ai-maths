---
concept: Substitution Principle
slug: substitution-principle
category: ring-theory
subcategory: morphisms
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Rings"
chapter_number: 11
pdf_page: 339
section: "Homomorphisms and Ideals"
extraction_confidence: high
aliases:
  - "evaluation homomorphism"
  - "substitution homomorphism"
prerequisites:
  - ring-homomorphism
  - polynomial-ring
extends: []
related:
  - kernel-of-ring-homomorphism
  - ideal
contrasts_with: []
answers_questions:
  - "How do polynomial evaluation maps define homomorphisms?"
---

# Quick Definition

The Substitution Principle states that given a ring homomorphism phi: R -> R' and an element alpha in R', there is a unique homomorphism from R[x] to R' that extends phi and sends x to alpha.

# Core Definition

Let phi: R -> R' be a ring homomorphism, and let R[x] be the polynomial ring with coefficients in R. (a) Let alpha be an element of R'. There is a unique homomorphism Phi: R[x] -> R' that agrees with phi on constant polynomials and sends x to alpha. (b) More generally, given elements alpha_1, ..., alpha_n of R', there is a unique homomorphism from R[x_1, ..., x_n] -> R' (Artin, Proposition 11.3.4, p. 345).

# Prerequisites

- **Ring homomorphism** -- The substitution map extends a given homomorphism
- **Polynomial ring** -- Domain is a polynomial ring

# Key Properties

1. The map is uniquely determined by where it sends x and the coefficients
2. It acts on coefficients via phi and substitutes alpha for x
3. Phi(sum a_i x^i) = sum phi(a_i) alpha^i

# Context & Application

This is the universal property of polynomial rings: R[x] is the "free" ring extension of R by one element. It underlies all substitution and evaluation in algebra.

# Examples

**Example 1** (p. 345): Evaluation at a real number a defines a homomorphism R[x] -> R.

**Example 2** (p. 345): The homomorphism Z[x] -> F_p[x] that reduces coefficients modulo p, sending x to x.

# Relationships

## Builds Upon
- **Ring homomorphism** -- Substitution maps are ring homomorphisms
- **Polynomial ring** -- The domain is R[x]

## Enables
- **Kernel of ring homomorphism** -- The kernel of a substitution map reveals algebraic relations
- **Adjoining elements** -- Constructed via quotients of polynomial rings

# Source Reference

Chapter 11: Rings, Section 11.3, Proposition 11.3.4, pages 345-346.

# Verification Notes

- Definition source: Direct from Proposition 11.3.4
- Confidence rationale: Explicit statement with proof
- Uncertainties: None
- Cross-reference status: Verified
