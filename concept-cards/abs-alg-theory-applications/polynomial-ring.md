---
# === CORE IDENTIFICATION ===
concept: Polynomial Ring
slug: polynomial-ring

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
  - commutative-ring
  - ring-with-unity
extends:
  - ring
related:
  - polynomial-over-ring
  - integral-domain
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a polynomial ring?"
  - "When is a polynomial ring an integral domain?"
---

# Quick Definition

The polynomial ring $R[x]$ over a commutative ring $R$ with identity consists of all polynomials in indeterminate $x$ with coefficients in $R$, under polynomial addition and multiplication.

# Core Definition

Given a commutative ring $R$ with identity, the set $R[x]$ of all polynomials $f(x) = \sum_{i=0}^n a_i x^i$ with coefficients in $R$ forms a commutative ring with identity (Judson, Theorem 17.3, p. 224). If $R$ is an integral domain, then $R[x]$ is also an integral domain and $\deg(p(x)q(x)) = \deg p(x) + \deg q(x)$ (Proposition 17.4, p. 225).

# Prerequisites

- **Commutative ring** — Coefficients come from a commutative ring with identity
- **Ring with unity** — $R$ must have a multiplicative identity

# Key Properties

1. $R[x]$ is a commutative ring with identity (the constant polynomial $1$)
2. Addition: add corresponding coefficients
3. Multiplication: $c_i = \sum_{k=0}^i a_k b_{i-k}$ (convolution)
4. If $R$ is an integral domain, so is $R[x]$ (Proposition 17.4)
5. $\deg(pq) = \deg p + \deg q$ when $R$ is an integral domain
6. Can extend to $R[x_1, \ldots, x_n]$ for multiple indeterminates

# Construction / Recognition

## To Construct:
1. Start with a commutative ring $R$ with identity
2. Form all finite formal sums $a_0 + a_1 x + \cdots + a_n x^n$ with $a_i \in R$
3. Define addition and multiplication as formal polynomial operations

# Context & Application

Polynomial rings are fundamental in algebra, providing the setting for factorization theory, the division algorithm (over fields), and construction of algebraic extensions. The ring $\mathbb{Z}[x]$ is the prototypical example of a UFD that is not a PID.

# Examples

**Example 1** (p. 224): In $\mathbb{Z}[x]$, $(3 + 2x^3)(2 - x^2 + 4x^4) = 6 - 3x^2 + 4x^3 + 12x^4 - 2x^5 + 8x^7$.

**Example 2** (p. 224): In $\mathbb{Z}_{12}[x]$, $(3 + 3x^3)(4 + 4x^2 + 4x^4) = 0$, showing $\mathbb{Z}_{12}[x]$ has zero divisors.

# Relationships

## Builds Upon
- **Commutative ring** — $R[x]$ inherits properties from $R$

## Enables
- **Division algorithm for polynomials** — Works in $F[x]$ when $F$ is a field
- **Irreducible polynomial** — Factorization theory in $R[x]$

# Common Errors

- **Error**: Assuming the degree formula $\deg(pq) = \deg p + \deg q$ always holds
  **Correction**: This requires $R$ to be an integral domain; in $\mathbb{Z}_{12}[x]$, nonzero polynomials can multiply to zero

# Common Confusions

- **Confusion**: Thinking $R[x]$ inherits all properties of $R$
  **Clarification**: $R[x]$ is never a field even if $R$ is (polynomials of degree $\geq 1$ have no inverses)

# Source Reference

Chapter 17: Polynomials, Section 17.1, pages 223-226. See Theorem 17.3 and Proposition 17.4.

# Verification Notes

- Definition source: Direct from pp. 223-224
- Confidence: HIGH — explicit construction and theorem
- Cross-reference status: Verified
- Uncertainties: None
