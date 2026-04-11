---
concept: Quotient of Polynomial Ring
slug: quotient-polynomial-ring
category: ring-theory
subcategory: polynomial-rings
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Polynomial Rings"
chapter_number: 9
pdf_page: 300
section: "9.2 Polynomial Rings over Fields I"
extraction_confidence: high
aliases: []
prerequisites:
  - polynomial-ring-over-field
  - quotient-ring
  - irreducible-polynomial
extends: []
related:
  - field
  - irreducible-polynomial
contrasts_with: []
answers_questions:
  - "When is F[x]/(f(x)) a field?"
  - "What does the quotient of a polynomial ring look like?"
---

# Quick Definition
$F[x]/(f(x))$ is a field if and only if $f(x)$ is irreducible over F. The elements can be represented by polynomials of degree less than $\deg(f)$.

# Core Definition
Let $f(x) \in F[x]$ have degree $n \geq 1$. Every element of $F[x]/(f(x))$ can be uniquely represented by a polynomial of degree $< n$. The quotient ring $F[x]/(f(x))$ is a field if and only if $f(x)$ is irreducible in $F[x]$ (Exercise 3, Dummit & Foote, p. 301; also Proposition 7 of Section 8.2).

# Prerequisites
- **Polynomial ring over field** — $F[x]$ is a PID
- **Quotient ring** — We quotient by a polynomial ideal
- **Irreducible polynomial** — Determines whether the quotient is a field

# Key Properties
1. $F[x]/(f(x))$ has dimension n as a vector space over F (Exercise 1, p. 300)
2. If F is finite with q elements, $F[x]/(f(x))$ has $q^n$ elements (Exercise 2, p. 301)
3. $F[x]/(f(x))$ is a field iff $f$ is irreducible iff $(f(x))$ is maximal (Exercise 3)
4. In $F[x]/(f(x))$, $\bar{x}$ satisfies $f(\bar{x}) = 0$

# Examples
**Example 1** (p. 259): $\mathbb{F}_2[x]/(x^2 + x + 1)$ is a field with 4 elements.

**Example 2**: $\mathbb{Q}[x]/(x^2 + 1) \cong \mathbb{Q}(i)$, the Gaussian rationals.

**Example 3** (p. 259): $\mathbb{Z}[x]/(x^4 - 16)$ has zero divisors since $x^4 - 16$ factors.

# Relationships

## Related
- **field** — $F[x]/(f)$ is a field when f is irreducible
- **irreducible-polynomial** — Determines structure of the quotient

# Common Errors
- **Error**: Forgetting to reduce $\bar{x}^n$ using the relation $f(\bar{x}) = 0$
  **Correction**: In $F[x]/(f(x))$, powers of $\bar{x}$ of degree $\geq n$ reduce using $\bar{x}^n = -(a_{n-1}\bar{x}^{n-1} + \cdots + a_0)$

# Source Reference
Chapter 9, Section 9.2, Exercises 1-3, pages 300-301; Chapter 7, Section 7.4, Exercise 14, pages 258-259.

# Verification Notes
- Definition: Synthesized from Exercises and Proposition 7
- Confidence: HIGH — extensively discussed
