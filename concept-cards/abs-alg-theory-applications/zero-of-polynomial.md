---
# === CORE IDENTIFICATION ===
concept: Zero of a Polynomial
slug: zero-of-polynomial

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
  - "root of a polynomial"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - polynomial-ring
  - evaluation-homomorphism-polynomials
extends: []
related:
  - factor-theorem
  - irreducible-polynomial
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a zero (root) of a polynomial?"
  - "How many zeros can a polynomial of degree n have?"
---

# Quick Definition

An element $\alpha \in F$ is a zero (or root) of a polynomial $p(x) \in F[x]$ if $p(\alpha) = 0$, i.e., if $\alpha$ is in the kernel of the evaluation homomorphism $\phi_\alpha$.

# Core Definition

"Let $p(x)$ be a polynomial in $F[x]$ and $\alpha \in F$. We say that $\alpha$ is a zero or root of $p(x)$ if $p(x)$ is in the kernel of the evaluation homomorphism $\phi_\alpha$. All we are really saying here is that $\alpha$ is a zero of $p(x)$ if $p(\alpha) = 0$" (Judson, p. 228). A nonzero polynomial of degree $n$ over a field has at most $n$ distinct zeros (Corollary 17.9).

# Prerequisites

- **Polynomial ring** — Zeros are elements where the polynomial vanishes
- **Evaluation homomorphism** — Zeros are in the kernel of evaluation

# Key Properties

1. $\alpha$ is a zero iff $p(\alpha) = 0$
2. $\alpha$ is a zero iff $(x - \alpha) | p(x)$ (Corollary 17.8)
3. A degree $n$ polynomial has at most $n$ zeros over a field (Corollary 17.9)
4. Over non-fields, a polynomial can have more zeros than its degree

# Construction / Recognition

## To Find Zeros:
1. Substitute candidate values $\alpha$ into $p(x)$
2. If $p(\alpha) = 0$, then $\alpha$ is a zero

# Context & Application

Zeros of polynomials are central to algebra and analysis. The Factor Theorem connects zeros to factorization, and the bound on the number of zeros is essential for showing polynomial identity (two polynomials of degree $\leq n$ agreeing at $n+1$ points must be equal).

# Examples

**Example 1** (p. 229): $p(x) = x^3 + x^2 + 2$ over $\mathbb{Z}_3$: $p(0) = 2$, $p(1) = 1$, $p(2) = 2$, so $p(x)$ has no zeros in $\mathbb{Z}_3$.

# Relationships

## Enables
- **Factor Theorem** — $\alpha$ is a zero iff $(x - \alpha)$ divides $p(x)$

## Related
- **Irreducible polynomial** — A polynomial with no zeros of degree $\leq n/2$ may still be reducible via quadratic factors

# Common Errors

- **Error**: Assuming a polynomial of degree $n$ always has exactly $n$ zeros
  **Correction**: It has *at most* $n$ zeros over a field; it may have fewer or none

# Common Confusions

- **Confusion**: Thinking "no zeros" means "irreducible"
  **Clarification**: For degree $\leq 3$, no zeros implies irreducible; for degree $\geq 4$, a polynomial can have no zeros but still factor into quadratics

# Source Reference

Chapter 17: Polynomials, Section 17.2, pages 228-229. See Corollaries 17.8 and 17.9.

# Verification Notes

- Definition source: Direct from p. 228
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
