---
concept: Content of a Polynomial
slug: content-of-polynomial
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
  - gcd-in-ring
extends: []
related:
  - primitive-polynomial
  - gauss-lemma
contrasts_with: []
answers_questions:
  - "What is the content of a polynomial?"
---

# Quick Definition
The content of a polynomial $p(x) \in R[x]$ (R a UFD) is the greatest common divisor of its coefficients.

# Core Definition
Let R be a UFD and $p(x) = a_nx^n + \cdots + a_0 \in R[x]$. The *content* of $p(x)$ is $\gcd(a_n, \ldots, a_0)$, the greatest common divisor of all coefficients (Dummit & Foote, pp. 303-304).

# Prerequisites
- **Polynomial ring** — Content is defined for polynomials
- **Unique factorization domain** — GCD of coefficients requires UFD
- **GCD in ring** — Content is a GCD

# Key Properties
1. $p(x) = d \cdot p'(x)$ where d is the content and $p'(x)$ is primitive
2. This decomposition is unique up to units in R
3. Content is multiplicative (Gauss): content$(fg)$ = content$(f)$ $\cdot$ content$(g)$ (up to units)

# Examples
**Example 1**: Content of $6x^2 + 10x + 4$ is $\gcd(6, 10, 4) = 2$.

**Example 2**: Content of $x^3 - 3x - 1$ is $\gcd(1, -3, -1) = 1$ (primitive).

# Relationships

## Related
- **primitive-polynomial** — Content = 1 means primitive
- **gauss-lemma** — Content is multiplicative

# Source Reference
Chapter 9, Section 9.3, pages 303-304.

# Verification Notes
- Definition: Synthesized from pp. 303-304
- Confidence: HIGH — clear from context
