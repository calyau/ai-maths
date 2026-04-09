---
# === CORE IDENTIFICATION ===
concept: Irreducible Polynomial
slug: irreducible-polynomial

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
pdf_page: 229
section: "17.3 Irreducible Polynomials"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - polynomial-ring
  - field
extends: []
related:
  - eisensteins-criterion
  - gausss-lemma-polynomials
  - maximal-ideal-polynomial-rings
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an irreducible polynomial?"
  - "How do I test if a polynomial is irreducible?"
---

# Quick Definition

A nonconstant polynomial $f(x) \in F[x]$ is irreducible over a field $F$ if it cannot be written as a product of two polynomials of smaller degree in $F[x]$. Irreducible polynomials are the "primes" of polynomial rings.

# Core Definition

"A nonconstant polynomial $f(x) \in F[x]$ is irreducible over a field $F$ if $f(x)$ cannot be expressed as a product of two polynomials $g(x)$ and $h(x)$ in $F[x]$, where the degrees of $g(x)$ and $h(x)$ are both smaller than the degree of $f(x)$" (Judson, p. 229).

# Prerequisites

- **Polynomial ring** — Irreducibility is defined in $F[x]$
- **Field** — Irreducibility depends on the coefficient field

# Key Properties

1. Irreducibility depends on the field: $x^2 + 1$ is irreducible over $\mathbb{R}$ but not over $\mathbb{C}$
2. $x^2 - 2$ is irreducible over $\mathbb{Q}$ but not over $\mathbb{R}$
3. For degree 2 or 3: irreducible iff no zeros in $F$ (Example 17.12)
4. The ideal $\langle p(x) \rangle$ is maximal iff $p(x)$ is irreducible (Theorem 17.22)
5. $F[x]/\langle p(x) \rangle$ is a field when $p(x)$ is irreducible

# Construction / Recognition

## To Test Irreducibility:
1. **Degree 2 or 3**: Check for zeros in $F$ (no zeros $\Rightarrow$ irreducible)
2. **Over $\mathbb{Q}$**: Try the Rational Root Test (Corollary 17.15), then check quadratic factors
3. **Eisenstein's Criterion**: If a prime $p$ divides all coefficients except the leading one, and $p^2$ does not divide the constant term, then irreducible over $\mathbb{Q}$
4. **Reduction mod $p$**: If $f(x)$ is irreducible mod some prime $p$, it may be irreducible over $\mathbb{Q}$

# Context & Application

Irreducible polynomials are the building blocks of polynomial factorization, analogous to primes in $\mathbb{Z}$. They are used to construct field extensions: $F[x]/\langle p(x) \rangle$ is a field extension of $F$ containing a root of $p(x)$.

# Examples

**Example 1** (p. 229): $x^2 - 2 \in \mathbb{Q}[x]$ is irreducible since it has no rational roots.

**Example 2** (p. 229): $x^2 + 1$ is irreducible over $\mathbb{R}$ (no real roots).

**Example 3** (p. 229): $p(x) = x^3 + x^2 + 2 \in \mathbb{Z}_3[x]$ is irreducible since $p(0) = 2$, $p(1) = 1$, $p(2) = 2$ (no zeros).

**Example 4** (p. 231): $x^4 - 2x^3 + x + 1 \in \mathbb{Q}[x]$ is irreducible by checking no rational roots and no factorization into quadratics over $\mathbb{Z}$.

# Relationships

## Enables
- **Maximal ideal in $F[x]$** — $\langle p(x) \rangle$ is maximal iff $p(x)$ is irreducible
- **Field extension** — $F[x]/\langle p(x) \rangle$ is a field

## Related
- **Eisenstein's Criterion** — A sufficient condition for irreducibility
- **Gauss's Lemma** — Connects irreducibility over $\mathbb{Z}$ and $\mathbb{Q}$

# Common Errors

- **Error**: Concluding irreducibility over $\mathbb{Q}$ from having no integer roots alone for degree $\geq 4$
  **Correction**: For degree $\geq 4$, one must also rule out factorizations into polynomials of degree $\geq 2$

# Common Confusions

- **Confusion**: Thinking irreducibility is an absolute property
  **Clarification**: Irreducibility is relative to the field: $x^2 + 1$ is irreducible over $\mathbb{R}$ but factors as $(x+i)(x-i)$ over $\mathbb{C}$

# Source Reference

Chapter 17: Polynomials, Section 17.3, pages 229-233. See Theorem 17.22.

# Verification Notes

- Definition source: Direct quote from p. 229
- Confidence: HIGH — explicit definition with multiple examples
- Cross-reference status: Verified
- Uncertainties: None
