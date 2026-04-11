---
concept: "Fermat's Theorem on Sums of Two Squares"
slug: fermat-sum-of-squares
category: ring-theory
subcategory: factorization
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Euclidean Domains, Principal Ideal Domains, and Unique Factorization Domains"
chapter_number: 8
pdf_page: 293
section: "8.3 Unique Factorization Domains (U.F.D.s)"
extraction_confidence: high
aliases:
  - "Fermat two-square theorem"
prerequisites:
  - gaussian-integers
  - unique-factorization-domain
extends: []
related:
  - gaussian-integers
contrasts_with: []
answers_questions:
  - "Which primes can be written as the sum of two squares?"
---

# Quick Definition
An odd prime p is the sum of two integer squares ($p = a^2 + b^2$) if and only if $p \equiv 1 \pmod{4}$.

# Core Definition
(Proposition 18(1)) The prime p is the sum of two integer squares, $p = a^2 + b^2$, if and only if $p = 2$ or $p \equiv 1 \pmod{4}$. Except for interchanging a and b or changing signs, the representation is unique (Dummit & Foote, pp. 293-294).

# Prerequisites
- **Gaussian integers** — The proof uses the factorization theory of $\mathbb{Z}[i]$
- **Unique factorization domain** — $\mathbb{Z}[i]$ is a UFD

# Key Properties
1. A prime $p \equiv 1 \pmod{4}$ splits in $\mathbb{Z}[i]$: $p = (a+bi)(a-bi)$
2. A prime $p \equiv 3 \pmod{4}$ remains irreducible in $\mathbb{Z}[i]$
3. $2 = -i(1+i)^2$ (ramifies in $\mathbb{Z}[i]$)
4. An integer $n$ is a sum of two squares iff all primes $\equiv 3 \pmod{4}$ in its factorization appear to even power (Corollary 19)

# Examples
**Example** (p. 295): $493 = 17 \cdot 29 = 18^2 + 13^2 = 22^2 + 3^2$ has $4(1+1)(1+1) = 16$ representations.

# Relationships

## Related
- **gaussian-integers** — The proof relies on the arithmetic of $\mathbb{Z}[i]$

# Source Reference
Chapter 8, Section 8.3, Proposition 18, pages 293-294; Corollary 19, pages 295-296.

# Verification Notes
- Definition: Direct from Proposition 18, pp. 293-294
- Confidence: HIGH — classical theorem with complete proof
