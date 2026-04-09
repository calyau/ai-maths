---
# === CORE IDENTIFICATION ===
concept: Degree of a Polynomial
slug: degree-of-polynomial

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
extends: []
related:
  - monic-polynomial
  - leading-coefficient
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the degree of a polynomial?"
  - "How do degrees behave under multiplication?"
---

# Quick Definition

The degree of a polynomial $f(x) = a_0 + a_1x + \cdots + a_nx^n$ with $a_n \neq 0$ is $n$, the highest power of $x$ with a nonzero coefficient. The zero polynomial has degree $-\infty$.

# Core Definition

"If $n$ is the largest nonnegative number for which $a_n \neq 0$, we say that the degree of $f$ is $n$ and write $\deg f(x) = n$. If no such $n$ exists --- that is, if $f = 0$ is the zero polynomial --- then the degree of $f$ is defined to be $-\infty$" (Judson, p. 224).

# Prerequisites

- **Polynomial ring** — Degree is defined for polynomials in $R[x]$

# Key Properties

1. $\deg(f + g) \leq \max(\deg f, \deg g)$
2. Over an integral domain: $\deg(fg) = \deg f + \deg g$ (Proposition 17.4)
3. The zero polynomial has degree $-\infty$ by convention
4. A constant nonzero polynomial has degree $0$

# Construction / Recognition

## To Determine:
1. Write the polynomial in standard form
2. Find the highest power of $x$ with nonzero coefficient

# Context & Application

Degree is the primary measure of polynomial complexity. It controls the division algorithm (remainder has smaller degree), bounds the number of zeros (Corollary 17.9), and determines factorization behavior.

# Examples

**Example 1** (p. 224): $\deg(3 + 2x^3) = 3$ and $\deg(2 - x^2 + 4x^4) = 4$.

**Example 2** (p. 224): In $\mathbb{Z}_{12}[x]$, $\deg(3 + 3x^3) \cdot \deg(4 + 4x^2 + 4x^4)$ does not satisfy the additivity formula since the product is zero (non-integral domain).

# Relationships

## Related
- **Monic polynomial** — A polynomial whose leading coefficient is $1$
- **Division algorithm** — Remainder has degree less than the divisor

# Common Errors

- **Error**: Assuming $\deg(fg) = \deg f + \deg g$ in all rings
  **Correction**: This only holds when $R$ is an integral domain

# Common Confusions

- **Confusion**: Thinking the degree of the zero polynomial is $0$
  **Clarification**: The zero polynomial has degree $-\infty$, not $0$; constant nonzero polynomials have degree $0$

# Source Reference

Chapter 17: Polynomials, Section 17.1, page 224.

# Verification Notes

- Definition source: Direct from p. 224
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
