---
concept: Division Algorithm for Polynomials
slug: division-algorithm-polynomials
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
aliases:
  - "polynomial long division"
prerequisites:
  - polynomial-ring-over-field
extends: []
related:
  - euclidean-domain
  - roots-of-polynomial
contrasts_with: []
answers_questions:
  - "How does long division work for polynomials?"
  - "Is the division algorithm unique for polynomials over fields?"
---

# Quick Definition
For polynomials $a(x), b(x) \in F[x]$ with $b(x) \neq 0$ (F a field), there exist unique $q(x), r(x)$ with $a(x) = q(x)b(x) + r(x)$ and $r = 0$ or $\deg r < \deg b$.

# Core Definition
(Theorem 3) Let F be a field. If $a(x)$ and $b(x)$ are in $F[x]$ with $b(x) \neq 0$, then there exist *unique* $q(x)$ and $r(x)$ in $F[x]$ such that $a(x) = q(x)b(x) + r(x)$ with $r(x) = 0$ or $\deg r(x) < \deg b(x)$ (Dummit & Foote, p. 299).

# Prerequisites
- **Polynomial ring over field** — Coefficients must be from a field for the algorithm to work

# Key Properties
1. Both quotient and remainder are unique (unlike in $\mathbb{Z}$)
2. The algorithm requires dividing by the leading coefficient of $b(x)$, hence needs a field
3. The quotient and remainder are independent of field extensions (p. 301)
4. $b(x) \mid a(x)$ in $F[x]$ iff $r(x) = 0$

# Construction / Recognition
## To Perform:
1. If $\deg a < \deg b$: $q = 0$, $r = a$
2. Otherwise: compute $a'(x) = a(x) - \frac{a_n}{b_m}x^{n-m}b(x)$ (cancels leading term)
3. Recurse with $a'(x)$ in place of $a(x)$
4. Accumulate quotient terms

# Examples
**Example 1** (p. 301): In $\mathbb{Q}[x]$, dividing $x^3 - 2$ by $x + 1$: $x^3 - 2 = (x^2 - x + 1)(x + 1) + (-3)$.

# Relationships

## Related
- **euclidean-domain** — Makes $F[x]$ into a Euclidean Domain
- **roots-of-polynomial** — Division by $(x - \alpha)$ gives remainder $f(\alpha)$

# Common Errors
- **Error**: Attempting polynomial division over $\mathbb{Z}$ when the leading coefficient doesn't divide
  **Correction**: Polynomial long division requires field coefficients

# Source Reference
Chapter 9, Section 9.2, Theorem 3, pages 299-300.

# Verification Notes
- Definition: Direct from Theorem 3, p. 299
- Confidence: HIGH — complete proof given
