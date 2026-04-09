---
# === CORE IDENTIFICATION ===
concept: Leading Coefficient
slug: leading-coefficient

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
  - degree-of-polynomial
  - monic-polynomial
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the leading coefficient of a polynomial?"
---

# Quick Definition

The leading coefficient of a polynomial $f(x) = a_0 + a_1x + \cdots + a_nx^n$ with $a_n \neq 0$ is $a_n$, the coefficient of the highest-degree term.

# Core Definition

"The coefficient $a_n$ is called the leading coefficient" (Judson, p. 224). If the leading coefficient is $1$, the polynomial is called monic.

# Prerequisites

- **Polynomial ring** — Leading coefficients are defined for polynomials

# Key Properties

1. The leading coefficient of $f(x)$ of degree $n$ is the coefficient of $x^n$
2. Over an integral domain, the leading coefficient of $f(x)g(x)$ is the product of the leading coefficients
3. A polynomial is monic iff its leading coefficient is $1$

# Construction / Recognition

## To Identify:
1. Write polynomial in descending degree order
2. The coefficient of the first (highest degree) term is the leading coefficient

# Context & Application

The leading coefficient determines the behavior of the division algorithm and controls whether degree is additive under multiplication. In the division algorithm over a field, we divide by the leading coefficient to reduce degrees.

# Examples

**Example 1**: The leading coefficient of $3x^2 - 6x + 5$ is $3$.

**Example 2**: The leading coefficient of $x^3 - 3x + 2$ is $1$ (monic).

# Relationships

## Related
- **Degree of polynomial** — The leading coefficient is the coefficient of the degree-$n$ term
- **Monic polynomial** — A polynomial with leading coefficient $1$

# Common Errors

- **Error**: Confusing the leading coefficient with the constant term
  **Correction**: The leading coefficient is the coefficient of the *highest* degree term

# Common Confusions

- **Confusion**: Thinking the leading coefficient is always positive
  **Clarification**: The leading coefficient can be any nonzero element of the coefficient ring

# Source Reference

Chapter 17: Polynomials, Section 17.1, page 224.

# Verification Notes

- Definition source: Direct from p. 224
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
