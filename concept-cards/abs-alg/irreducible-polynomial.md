---
concept: Irreducible Polynomial
slug: irreducible-polynomial
category: ring-theory
subcategory: polynomial-rings
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Polynomial Rings"
chapter_number: 9
pdf_page: 303
section: "9.4 Irreducibility Criteria"
extraction_confidence: high
aliases: []
prerequisites:
  - polynomial-ring
  - irreducible-element
  - field
extends:
  - irreducible-element
related:
  - eisenstein-criterion
  - gauss-lemma
  - roots-of-polynomial
  - reduction-mod-p
contrasts_with: []
answers_questions:
  - "How do I determine whether a polynomial is irreducible?"
  - "What is an irreducible polynomial?"
---

# Quick Definition
A nonconstant polynomial $p(x) \in F[x]$ is irreducible over a field F if it cannot be factored as a product of two polynomials of smaller degree in $F[x]$.

# Core Definition
A nonconstant polynomial $p(x) \in R[x]$ is an irreducible element of R[x] if whenever $p(x) = a(x)b(x)$, one of $a(x)$ or $b(x)$ is a unit. For monic polynomials over an integral domain, this means it cannot be factored into two monic polynomials of smaller degree (Dummit & Foote, pp. 303-304).

# Prerequisites
- **Polynomial ring** — Irreducibility is for polynomials
- **Irreducible element** — An irreducible polynomial is an irreducible element of $R[x]$
- **Field** — Over fields, degree 2-3 polynomials are irreducible iff they have no roots

# Key Properties
1. Over a field: degree 2 or 3 polynomial is irreducible iff it has no root (Proposition 10, p. 306)
2. $F[x]/(f(x))$ is a field iff $f(x)$ is irreducible in $F[x]$ (Exercise 3, p. 301)
3. By Gauss' Lemma: for R a UFD, primitive p(x) is irreducible in $R[x]$ iff irreducible in $F[x]$ (Corollary 6, p. 304)
4. Irreducibility depends on the coefficient ring: $x^2 + 1$ is irreducible over $\mathbb{Q}$ but not over $\mathbb{C}$

# Construction / Recognition
## Methods to Test Irreducibility:
1. **Root test** (degree 2 or 3): check if polynomial has a root in the field
2. **Rational root test** (Proposition 11, p. 307): for $p(x) \in \mathbb{Z}[x]$, rational roots $r/s$ satisfy $r \mid a_0$ and $s \mid a_n$
3. **Reduction mod p** (Proposition 12, p. 308): if $\bar{p}(x)$ is irreducible in $(\mathbb{Z}/p\mathbb{Z})[x]$, then $p(x)$ is irreducible in $\mathbb{Z}[x]$
4. **Eisenstein's Criterion** (Proposition 13, p. 309): prime p divides all coefficients except the leading one, $p^2$ does not divide the constant term

# Context & Application
Determining irreducibility is one of the central computational problems in algebra. Irreducible polynomials are used to construct field extensions and are the basic building blocks for polynomial factorization.

# Examples
**Example 1** (p. 307): $x^3 - 3x - 1$ is irreducible in $\mathbb{Z}[x]$ (no rational roots).

**Example 2** (p. 308): $x^2 + x + 1$ is irreducible in $\mathbb{Z}[x]$ (irreducible mod 2).

**Example 3** (p. 309): $x^4 + 10x + 5$ is irreducible in $\mathbb{Z}[x]$ (Eisenstein with $p = 5$).

**Example 4** (p. 310): $x^4 + 1$ is irreducible in $\mathbb{Z}[x]$ but reducible mod every prime.

# Relationships

## Builds Upon
- **irreducible-element** — Irreducible polynomial is an irreducible in $R[x]$

## Related
- **eisenstein-criterion** — A powerful irreducibility test
- **gauss-lemma** — Connects irreducibility over R and its fraction field F
- **reduction-mod-p** — Reducing coefficients modulo a prime to test irreducibility

# Common Errors
- **Error**: Assuming a polynomial with no rational roots is irreducible over $\mathbb{Q}$
  **Correction**: This works only for degree 2 and 3; degree 4+ polynomials can be reducible with no rational roots

# Common Confusions
- **Confusion**: Thinking irreducibility is independent of the base field/ring
  **Clarification**: $x^2 + 1$ is irreducible over $\mathbb{Q}$ and $\mathbb{R}$ but reducible over $\mathbb{C}$ and $\mathbb{Z}/2\mathbb{Z}$

# Source Reference
Chapter 9, Section 9.4, pages 303-310. See Propositions 9-13.

# Verification Notes
- Definition: Synthesized from discussion in Section 9.4 and Ch 8
- Confidence: HIGH — extensive treatment with multiple criteria
