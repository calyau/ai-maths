---
concept: Polynomial Ring
slug: polynomial-ring
category: ring-theory
subcategory: ring-constructions
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Introduction to Rings"
chapter_number: 7
pdf_page: 235
section: "7.2 Examples: Polynomial Rings, Matrix Rings, and Group Rings"
extraction_confidence: high
aliases:
  - "ring of polynomials"
prerequisites:
  - commutative-ring
  - ring-with-identity
extends:
  - ring
related:
  - polynomial-ring-over-field
  - degree-of-polynomial
  - evaluation-homomorphism
contrasts_with:
  - matrix-ring
  - group-ring
answers_questions:
  - "What is a polynomial ring?"
  - "How is a polynomial ring constructed?"
---

# Quick Definition
The polynomial ring $R[x]$ is the set of all formal sums $a_n x^n + \cdots + a_1 x + a_0$ with coefficients $a_i \in R$, under componentwise addition and the usual "expand and collect" multiplication.

# Core Definition
Fix a commutative ring R with identity. The *polynomial ring* $R[x]$ in the indeterminate x consists of all formal sums $a_n x^n + a_{n-1}x^{n-1} + \cdots + a_1 x + a_0$ with $n \geq 0$ and each $a_i \in R$. Addition is componentwise and multiplication is defined by $(ax^i)(bx^j) = abx^{i+j}$ extended by distributivity (Dummit & Foote, pp. 235-236).

# Prerequisites
- **Commutative ring** — The coefficient ring is assumed commutative
- **Ring with identity** — R is assumed to have an identity

# Key Properties
1. $R[x]$ is a commutative ring with identity (the identity 1 from R)
2. If R is an integral domain, then: degree $p(x)q(x)$ = degree $p(x)$ + degree $q(x)$, the units of $R[x]$ are exactly the units of R, and $R[x]$ is an integral domain (Proposition 4, p. 236)
3. R appears as the subring of constant polynomials
4. If R has zero divisors, so does $R[x]$

# Construction / Recognition
## To Construct:
1. Start with a commutative ring R with identity
2. Introduce an indeterminate x
3. Form all finite formal sums with coefficients in R
4. Define addition componentwise and multiplication by expanding

# Context & Application
Polynomial rings are one of the most important ring constructions. They are studied extensively in Chapters 9 and beyond. $F[x]$ for a field F is a Euclidean Domain, PID, and UFD.

# Examples
**Example 1** (p. 237): $\mathbb{Z}[x]$ is the ring of polynomials with integer coefficients; it is an integral domain but not a PID.

**Example 2** (p. 237): $\mathbb{Q}[x]$ is a PID (since $\mathbb{Q}$ is a field).

**Example 3** (p. 237): In $\mathbb{Z}/2\mathbb{Z}[x]$, $(x+1)^2 = x^2 + 1$ since $2 = 0$.

# Relationships

## Builds Upon
- **ring** — Polynomial rings are constructed from an existing ring

## Enables
- **polynomial-ring-over-field** — When R is a field, $R[x]$ is a Euclidean Domain
- **evaluation-homomorphism** — Substituting values for x

## Contrasts With
- **matrix-ring** — Another fundamental ring construction, but noncommutative
- **group-ring** — A ring construction from a group and coefficient ring

# Common Errors
- **Error**: Assuming $R[x]$ is a PID for any integral domain R
  **Correction**: $\mathbb{Z}[x]$ is not a PID; $R[x]$ is a PID only if R is a field

# Common Confusions
- **Confusion**: Confusing polynomials with polynomial functions
  **Clarification**: Polynomials are formal sums; over finite fields, distinct polynomials can define the same function

# Source Reference
Chapter 7, Section 7.2, pages 235-237. See also Chapter 9 for extensive treatment.

# Verification Notes
- Definition: Direct from pp. 235-236
- Confidence: HIGH — explicit, detailed construction
