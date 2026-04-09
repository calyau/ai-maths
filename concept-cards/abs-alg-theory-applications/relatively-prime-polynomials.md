---
# === CORE IDENTIFICATION ===
concept: Relatively Prime Polynomials
slug: relatively-prime-polynomials

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
pdf_page: 228
section: "17.2 The Division Algorithm"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "coprime polynomials"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - polynomial-gcd
extends: []
related:
  - irreducible-polynomial
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "When are two polynomials relatively prime?"
---

# Quick Definition

Two polynomials $p(x)$ and $q(x)$ in $F[x]$ are relatively prime if their greatest common divisor is $1$: $\gcd(p(x), q(x)) = 1$.

# Core Definition

"Two polynomials $p(x)$ and $q(x)$ are relatively prime if $\gcd(p(x), q(x)) = 1$" (Judson, p. 228).

# Prerequisites

- **Polynomial GCD** — Relative primality is defined via the GCD

# Key Properties

1. $\gcd(p(x), q(x)) = 1$
2. Equivalent to: there exist $r(x), s(x)$ with $r(x)p(x) + s(x)q(x) = 1$
3. $p(x)$ and $q(x)$ share no common nonconstant factor

# Construction / Recognition

## To Verify:
1. Compute $\gcd(p(x), q(x))$ using the Euclidean algorithm
2. If the result is $1$ (a constant), they are relatively prime

# Context & Application

Relatively prime polynomials share no common roots. This concept is used in partial fraction decomposition and in proving uniqueness results in factorization.

# Examples

**Example 1**: $x^2 + 1$ and $x - 1$ in $\mathbb{R}[x]$ are relatively prime since they share no roots.

# Relationships

## Builds Upon
- **Polynomial GCD** — Defined as GCD being $1$

# Common Errors

- **Error**: Assuming polynomials with no common roots are always relatively prime
  **Correction**: Over non-algebraically closed fields, this is correct; over algebraically closed fields, no common roots implies relatively prime

# Common Confusions

- **Confusion**: Confusing "relatively prime" with "irreducible"
  **Clarification**: A single polynomial is irreducible; two polynomials are relatively prime

# Source Reference

Chapter 17: Polynomials, Section 17.2, page 228.

# Verification Notes

- Definition source: Direct from p. 228
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
