---
concept: Rational Root Theorem
slug: rational-root-theorem
category: ring-theory
subcategory: polynomial-rings
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Polynomial Rings"
chapter_number: 9
pdf_page: 307
section: "9.4 Irreducibility Criteria"
extraction_confidence: high
aliases:
  - "rational root test"
prerequisites:
  - polynomial-ring
  - integral-domain
extends: []
related:
  - roots-of-polynomial
  - irreducible-polynomial
contrasts_with: []
answers_questions:
  - "What are the possible rational roots of a polynomial with integer coefficients?"
---

# Quick Definition
If $r/s$ (in lowest terms) is a rational root of $p(x) = a_nx^n + \cdots + a_0 \in \mathbb{Z}[x]$, then $r \mid a_0$ and $s \mid a_n$.

# Core Definition
(Proposition 11) Let $p(x) = a_nx^n + \cdots + a_0 \in \mathbb{Z}[x]$. If $r/s \in \mathbb{Q}$ is in lowest terms and is a root of $p(x)$, then $r \mid a_0$ and $s \mid a_n$. For monic polynomials, the only possible rational roots are integer divisors of $a_0$ (Dummit & Foote, p. 307).

# Prerequisites
- **Polynomial ring** — Applied to integer polynomials
- **Integral domain** — Uses properties of $\mathbb{Z}$

# Key Properties
1. Limits rational root candidates to a finite set
2. For monic polynomials: rational roots must be integers dividing $a_0$
3. Combined with Proposition 10: proves irreducibility for degree 2-3 polynomials without rational roots

# Construction / Recognition
## To Apply:
1. List all divisors of $a_0$ (for numerators r)
2. List all divisors of $a_n$ (for denominators s)
3. Test each $r/s$ as a root
4. If none work and degree $\leq 3$: conclude irreducible over $\mathbb{Q}$

# Examples
**Example 1** (p. 307): $x^3 - 3x - 1$: candidates are $\pm 1$, neither is a root, so irreducible.

**Example 2** (p. 307): $x^2 - p$ for prime p: candidates $\pm 1, \pm p$, none work, so irreducible.

# Relationships

## Related
- **roots-of-polynomial** — Tests for roots
- **irreducible-polynomial** — Gives irreducibility for degree $\leq 3$

# Source Reference
Chapter 9, Section 9.4, Proposition 11, page 307.

# Verification Notes
- Definition: Direct from Proposition 11, p. 307
- Confidence: HIGH — explicit proposition with proof
