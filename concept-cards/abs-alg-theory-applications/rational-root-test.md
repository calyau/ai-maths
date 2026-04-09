---
# === CORE IDENTIFICATION ===
concept: Rational Root Test
slug: rational-root-test

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
pdf_page: 231
section: "17.3 Irreducible Polynomials"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Rational Root Theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - gausss-lemma-polynomials
extends: []
related:
  - irreducible-polynomial
  - zero-of-polynomial
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I test if a polynomial has rational roots?"
  - "How do I test if a polynomial is irreducible?"
---

# Quick Definition

If a monic polynomial $p(x) = x^n + \cdots + a_0 \in \mathbb{Z}[x]$ has a rational zero, then that zero is an integer dividing $a_0$.

# Core Definition

"Let $p(x) = x^n + a_{n-1}x^{n-1} + \cdots + a_0$ be a polynomial with coefficients in $\mathbb{Z}$ and $a_0 \neq 0$. If $p(x)$ has a zero in $\mathbb{Q}$, then $p(x)$ also has a zero $\alpha$ in $\mathbb{Z}$. Furthermore, $\alpha$ divides $a_0$" (Judson, Corollary 17.15, p. 231).

# Prerequisites

- **Gauss's Lemma** — The Rational Root Test is a corollary

# Key Properties

1. Only finitely many candidates to test: divisors of $a_0$
2. If none work, $p(x)$ has no rational (hence no integer) zeros
3. For degree 2 or 3, no rational zeros implies irreducibility over $\mathbb{Q}$

# Construction / Recognition

## To Apply:
1. List all integer divisors of the constant term $a_0$
2. Evaluate $p(x)$ at each divisor $\pm d$
3. If $p(d) = 0$, then $d$ is a zero; if none, $p(x)$ has no rational zeros

# Context & Application

The Rational Root Test is the standard first step in testing irreducibility over $\mathbb{Q}$. Combined with checking for quadratic factors, it handles most practical cases.

# Examples

**Example 1** (p. 231): For $p(x) = x^4 - 2x^3 + x + 1$, possible integer zeros divide $1$, so candidates are $\pm 1$. Since $p(1) = 1$ and $p(-1) = 3$, there are no rational zeros.

# Relationships

## Builds Upon
- **Gauss's Lemma** — The test follows from Gauss's Lemma

## Enables
- **Irreducibility testing** — Eliminates linear factors

## Related
- **Zero of polynomial** — The test finds rational zeros

# Common Errors

- **Error**: Concluding a polynomial is irreducible after finding no rational roots (for degree $\geq 4$)
  **Correction**: For degree $\geq 4$, must also check for factorizations into polynomials of degree $\geq 2$

# Common Confusions

- **Confusion**: Applying the test to non-monic polynomials without modification
  **Clarification**: For non-monic $a_nx^n + \cdots + a_0$, rational roots $r/s$ satisfy $r | a_0$ and $s | a_n$

# Source Reference

Chapter 17: Polynomials, Section 17.3, Corollary 17.15, page 231.

# Verification Notes

- Definition source: Direct from Corollary 17.15
- Confidence: HIGH — explicit corollary
- Cross-reference status: Verified
- Uncertainties: None
