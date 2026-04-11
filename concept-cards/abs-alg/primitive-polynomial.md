---
concept: Primitive Polynomial
slug: primitive-polynomial
category: ring-theory
subcategory: polynomial-rings
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Polynomial Rings"
chapter_number: 9
pdf_page: 303
section: "9.3 Polynomial Rings that are Unique Factorization Domains"
extraction_confidence: high
aliases: []
prerequisites:
  - polynomial-ring
  - unique-factorization-domain
  - content-of-polynomial
extends: []
related:
  - gauss-lemma
  - content-of-polynomial
contrasts_with: []
answers_questions:
  - "What is a primitive polynomial?"
  - "What is the content of a polynomial?"
---

# Quick Definition
A polynomial $p(x) \in R[x]$ (R a UFD) is primitive if the greatest common divisor of its coefficients is 1.

# Core Definition
Let R be a UFD and $p(x) \in R[x]$. The greatest common divisor of the coefficients of $p(x)$ is called the *content* of $p(x)$. A polynomial is *primitive* if its content is 1 (equivalently, if no non-unit of R divides all coefficients). Writing $p(x) = d \cdot p'(x)$ where d is the content, $p'(x)$ is the primitive part (Dummit & Foote, pp. 303-304).

# Prerequisites
- **Polynomial ring** — Primitivity is defined for polynomials
- **Unique factorization domain** — GCD of coefficients requires UFD
- **Content of polynomial** — Content = GCD of coefficients

# Key Properties
1. Every polynomial $p(x) = d \cdot p'(x)$ with d = content and $p'(x)$ primitive (unique up to units)
2. A primitive polynomial is irreducible in $R[x]$ iff irreducible in $F[x]$ (Corollary 6, p. 304)
3. Monic polynomials are always primitive

# Context & Application
Primitive polynomials bridge the factorization theory in $R[x]$ and $F[x]$ via Gauss's Lemma.

# Examples
**Example 1**: $6x^2 + 10x + 4 = 2(3x^2 + 5x + 2)$ has content 2; the primitive part is $3x^2 + 5x + 2$.

**Example 2**: $x^3 - 3x - 1$ is primitive in $\mathbb{Z}[x]$ (GCD of $1, -3, -1$ is 1).

# Relationships

## Related
- **gauss-lemma** — Applies to primitive polynomials
- **content-of-polynomial** — Primitive means content = 1

# Source Reference
Chapter 9, Section 9.3, pages 303-304.

# Verification Notes
- Definition: Synthesized from pp. 303-304
- Confidence: HIGH — clear from context
