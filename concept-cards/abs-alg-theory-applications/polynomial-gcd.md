---
# === CORE IDENTIFICATION ===
concept: Greatest Common Divisor of Polynomials
slug: polynomial-gcd

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
  - "GCD of polynomials"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - polynomial-ring
  - division-algorithm-polynomials
  - monic-polynomial
extends: []
related:
  - relatively-prime-polynomials
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the GCD of two polynomials?"
  - "How do you compute the GCD of polynomials?"
---

# Quick Definition

The greatest common divisor of polynomials $p(x)$ and $q(x)$ over a field $F$ is the monic polynomial $d(x)$ of highest degree that divides both, with the Bezout property: $d(x) = r(x)p(x) + s(x)q(x)$.

# Core Definition

"A monic polynomial $d(x)$ is a greatest common divisor of polynomials $p(x), q(x) \in F[x]$ if $d(x)$ evenly divides both $p(x)$ and $q(x)$; and, if for any other polynomial $d'(x)$ dividing both $p(x)$ and $q(x)$, $d'(x) | d(x)$" (Judson, p. 228). The GCD is unique and satisfies $d(x) = r(x)p(x) + s(x)q(x)$ for some $r(x), s(x) \in F[x]$ (Proposition 17.10).

# Prerequisites

- **Polynomial ring** — GCDs are computed in $F[x]$
- **Division algorithm** — Used to compute GCDs via the Euclidean algorithm
- **Monic polynomial** — GCDs are normalized to be monic

# Key Properties

1. GCD is unique and monic
2. Bezout property: $d(x) = r(x)p(x) + s(x)q(x)$
3. Computed via the Euclidean algorithm for polynomials
4. Two polynomials are relatively prime iff $\gcd(p(x), q(x)) = 1$

# Construction / Recognition

## To Compute:
1. Apply the Euclidean algorithm: repeatedly divide and take remainders
2. The last nonzero remainder (made monic) is the GCD
3. Back-substitute to find the Bezout coefficients

# Context & Application

Polynomial GCDs are essential for testing irreducibility, simplifying rational expressions, and proving that $F[x]$ is a PID.

# Examples

**Example 1** (p. 228): The Euclidean algorithm for polynomials works analogously to the integer case.

# Relationships

## Builds Upon
- **Division algorithm** — The Euclidean algorithm uses repeated division

## Enables
- **Relatively prime polynomials** — Defined as $\gcd = 1$

# Common Errors

- **Error**: Forgetting to normalize the GCD to be monic
  **Correction**: By convention, the GCD is always taken to be monic

# Common Confusions

- **Confusion**: Thinking GCDs exist for polynomials over any ring
  **Clarification**: The Euclidean algorithm requires a field; GCDs in $\mathbb{Z}[x]$ are more subtle

# Source Reference

Chapter 17: Polynomials, Section 17.2, Proposition 17.10, pages 228-229.

# Verification Notes

- Definition source: Direct from p. 228
- Confidence: HIGH — explicit definition and proposition
- Cross-reference status: Verified
- Uncertainties: None
