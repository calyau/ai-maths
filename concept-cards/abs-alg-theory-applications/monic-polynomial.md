---
# === CORE IDENTIFICATION ===
concept: Monic Polynomial
slug: monic-polynomial

# === CLASSIFICATION ===
category: polynomial-theory
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Polynomials"
chapter_number: 17
pdf_page: 223
section: "17.1 Polynomial Rings"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - polynomial-ring
  - degree-of-polynomial
extends: []
related:
  - leading-coefficient
  - polynomial-gcd
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a monic polynomial?"
---

# Quick Definition

A polynomial is monic if its leading coefficient (the coefficient of the highest-degree term) is $1$.

# Core Definition

"A polynomial is called monic if the leading coefficient is 1" (Judson, p. 224). For example, $x^3 - 2x + 1$ is monic, while $2x^3 - 2x + 1$ is not.

# Prerequisites

- **Polynomial ring** — Monic polynomials live in polynomial rings
- **Degree of polynomial** — The leading coefficient is the coefficient of the highest-degree term

# Key Properties

1. Leading coefficient equals $1$
2. GCDs of polynomials over fields are taken to be monic (by convention)
3. Over a field, any nonzero polynomial can be made monic by dividing by its leading coefficient

# Construction / Recognition

## To Recognize:
1. Identify the leading coefficient
2. If it equals $1$, the polynomial is monic

# Context & Application

Monic polynomials provide canonical representatives. The GCD of two polynomials over a field is defined to be the unique monic polynomial of largest degree dividing both. Monic polynomials simplify statements about factorization and irreducibility.

# Examples

**Example 1**: $x^3 - 3x + 2$ is monic; $3x^2 - 6x + 5$ is not monic.

# Relationships

## Related
- **Polynomial GCD** — GCDs are conventionally chosen to be monic

# Common Errors

- **Error**: Forgetting that "monic" refers specifically to the leading coefficient being $1$
  **Correction**: Even if all other coefficients are $1$, a polynomial is not monic unless the leading coefficient is $1$

# Common Confusions

- **Confusion**: Confusing monic with having all coefficients equal to $1$
  **Clarification**: Only the leading coefficient must be $1$; other coefficients can be anything

# Source Reference

Chapter 17: Polynomials, Section 17.1, page 224.

# Verification Notes

- Definition source: Direct from p. 224
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
