---
concept: Polynomial Ring over a Field
slug: polynomial-ring-over-field
category: ring-theory
subcategory: polynomial-rings
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Polynomial Rings"
chapter_number: 9
pdf_page: 299
section: "9.2 Polynomial Rings over Fields I"
extraction_confidence: high
aliases: []
prerequisites:
  - polynomial-ring
  - field
  - euclidean-domain
extends:
  - polynomial-ring
  - euclidean-domain
related:
  - division-algorithm-polynomials
  - principal-ideal-domain
contrasts_with: []
answers_questions:
  - "Why is F[x] a Euclidean Domain?"
  - "What are the properties of polynomial rings over fields?"
---

# Quick Definition
If F is a field, then $F[x]$ is a Euclidean Domain (hence a PID and UFD) with the degree function as the Euclidean norm.

# Core Definition
(Theorem 3) Let F be a field. The polynomial ring $F[x]$ is a Euclidean Domain. Specifically, if $a(x)$ and $b(x)$ are polynomials with $b(x) \neq 0$, then there are unique $q(x)$ and $r(x)$ with $a(x) = q(x)b(x) + r(x)$ and $r(x) = 0$ or $\deg r(x) < \deg b(x)$ (Dummit & Foote, p. 299).

# Prerequisites
- **Polynomial ring** — $F[x]$ is a polynomial ring
- **Field** — The coefficient ring must be a field
- **Euclidean domain** — $F[x]$ is Euclidean

# Key Properties
1. $F[x]$ is a Euclidean Domain with norm = degree (Theorem 3, p. 299)
2. Division algorithm gives unique quotient and remainder (p. 299)
3. $F[x]$ is a PID and UFD (Corollary 4, p. 300)
4. $R[x]$ is a PID iff R is a field (Corollary 8, p. 284)
5. The ideals of $F[x]$ are $(f(x))$ for polynomials $f(x)$
6. $F[x]/(f(x))$ is a field iff $f(x)$ is irreducible (Exercise 3, p. 301)

# Construction / Recognition
## Division Algorithm:
1. If $\deg a \geq \deg b$, subtract $\frac{a_n}{b_m}x^{n-m}b(x)$ from $a(x)$ (requires F to be a field for division by $b_m$)
2. Repeat with the remainder (which has smaller degree)
3. Terminate when remainder has degree less than $\deg b$

# Context & Application
$F[x]$ is the prototype for Euclidean Domains after $\mathbb{Z}$. Its ideal structure, factorization theory, and quotient rings are fundamental to field theory and Galois theory (Part IV).

# Examples
**Example 1** (p. 300): $\mathbb{Q}[x]$ is a PID; the ideal $(2, x)$ in $\mathbb{Z}[x]$ becomes $(1) = \mathbb{Q}[x]$.

**Example 2** (p. 300): $\mathbb{Z}/p\mathbb{Z}[x]$ is a PID for prime p.

**Example 3** (p. 301): $\mathbb{Q}[x, y] = \mathbb{Q}[x][y]$ is NOT a PID since $\mathbb{Q}[x]$ is not a field.

# Relationships

## Builds Upon
- **polynomial-ring** — Specializing to field coefficients
- **euclidean-domain** — $F[x]$ is a Euclidean Domain

## Enables
- **irreducible-polynomial** — Irreducibility in $F[x]$
- **field** — $F[x]/(f(x))$ is a field when $f$ is irreducible

# Common Errors
- **Error**: Attempting long division in $\mathbb{Z}[x]$ as if it were Euclidean
  **Correction**: $\mathbb{Z}[x]$ is not Euclidean; you cannot divide leading coefficients unless they divide evenly

# Common Confusions
- **Confusion**: Thinking polynomial division works over any ring
  **Clarification**: The division algorithm requires dividing by the leading coefficient, which needs a field

# Source Reference
Chapter 9, Section 9.2, Theorem 3 and Corollary 4, pages 299-300.

# Verification Notes
- Definition: Direct from Theorem 3, p. 299
- Confidence: HIGH — fundamental theorem with complete proof
