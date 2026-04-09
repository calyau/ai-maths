---
# === CORE IDENTIFICATION ===
concept: Division Algorithm for Polynomials
slug: division-algorithm-polynomials

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
pdf_page: 226
section: "17.2 The Division Algorithm"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "polynomial long division"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - polynomial-ring
  - field
extends: []
related:
  - zero-of-polynomial
  - factor-theorem
  - polynomial-gcd
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the division algorithm for polynomials?"
  - "When can you divide polynomials?"
---

# Quick Definition

If $F$ is a field and $f(x), g(x) \in F[x]$ with $g(x) \neq 0$, then there exist unique polynomials $q(x)$ (quotient) and $r(x)$ (remainder) such that $f(x) = g(x)q(x) + r(x)$ where $\deg r(x) < \deg g(x)$ or $r(x) = 0$.

# Core Definition

"Let $f(x)$ and $g(x)$ be polynomials in $F[x]$, where $F$ is a field and $g(x)$ is a nonzero polynomial. Then there exist unique polynomials $q(x), r(x) \in F[x]$ such that $f(x) = g(x)q(x) + r(x)$, where either $\deg r(x) < \deg g(x)$ or $r(x)$ is the zero polynomial" (Judson, Theorem 17.6, p. 227).

# Prerequisites

- **Polynomial ring** — Division is performed in $F[x]$
- **Field** — The coefficients must come from a field (to divide by leading coefficients)

# Key Properties

1. Requires $F$ to be a field (for division by leading coefficients)
2. Quotient $q(x)$ and remainder $r(x)$ are unique
3. $\deg r(x) < \deg g(x)$ or $r(x) = 0$
4. Does not hold over $\mathbb{Z}[x]$ in general
5. Analogous to the division algorithm for integers

# Construction / Recognition

## To Perform:
1. Divide the leading term of $f(x)$ by the leading term of $g(x)$
2. Multiply $g(x)$ by this quotient term and subtract from $f(x)$
3. Repeat with the remainder until $\deg r < \deg g$

# Context & Application

The division algorithm is the foundation of polynomial theory over fields. It enables the Euclidean algorithm for polynomial GCDs, shows $F[x]$ is a PID, and underlies the Factor Theorem.

# Examples

**Example 1** (p. 227): Dividing $x^3 - x^2 + 2x - 3$ by $x - 2$ gives $x^3 - x^2 + 2x - 3 = (x-2)(x^2 + x + 4) + 5$.

# Relationships

## Builds Upon
- **Field** — Requires division by leading coefficients

## Enables
- **Factor Theorem** — $p(\alpha) = 0$ iff $(x - \alpha) | p(x)$
- **Polynomial GCD** — Computed via the Euclidean algorithm
- **$F[x]$ is a PID** — Every ideal in $F[x]$ is principal

# Common Errors

- **Error**: Applying the division algorithm over $\mathbb{Z}[x]$
  **Correction**: The algorithm requires a field for coefficients; it fails over $\mathbb{Z}[x]$ because we cannot always divide leading coefficients

# Common Confusions

- **Confusion**: Thinking the division algorithm works over any ring
  **Clarification**: It requires a field; over $\mathbb{Z}$, dividing $x$ by $2x$ fails since $1/2 \notin \mathbb{Z}$

# Source Reference

Chapter 17: Polynomials, Section 17.2, Theorem 17.6, pages 226-228.

# Verification Notes

- Definition source: Direct from Theorem 17.6
- Confidence: HIGH — explicit theorem with proof
- Cross-reference status: Verified
- Uncertainties: None
