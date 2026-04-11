---
concept: Reduction Modulo a Prime
slug: reduction-mod-p
category: ring-theory
subcategory: polynomial-rings
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Polynomial Rings"
chapter_number: 9
pdf_page: 308
section: "9.4 Irreducibility Criteria"
extraction_confidence: high
aliases:
  - "mod p reduction"
  - "reduction criterion"
prerequisites:
  - polynomial-ring
  - prime-ideal
  - irreducible-polynomial
extends: []
related:
  - eisenstein-criterion
  - gauss-lemma
contrasts_with: []
answers_questions:
  - "How can reducing modulo a prime help determine irreducibility?"
---

# Quick Definition
If a monic polynomial $p(x) \in R[x]$ remains irreducible when its coefficients are reduced modulo a proper ideal I, then $p(x)$ is irreducible in $R[x]$.

# Core Definition
(Proposition 12) Let I be a proper ideal in the integral domain R and let $p(x)$ be a nonconstant monic polynomial in $R[x]$. If the image of $p(x)$ in $(R/I)[x]$ cannot be factored into two polynomials of smaller degree, then $p(x)$ is irreducible in $R[x]$ (Dummit & Foote, p. 308).

# Prerequisites
- **Polynomial ring** — Applied to polynomials
- **Prime ideal** — Typically reduce mod a prime ideal
- **Irreducible polynomial** — The conclusion is irreducibility

# Key Properties
1. The converse is NOT true: $x^4 + 1$ is irreducible in $\mathbb{Z}[x]$ but reducible mod every prime (p. 308)
2. Must check that reduction does not "collapse" the degree
3. For several variables: must check that nonunit factors don't become units after reduction (p. 308)

# Construction / Recognition
## To Apply:
1. Choose a prime $p$ (or prime ideal I)
2. Reduce coefficients of $f(x)$ modulo p
3. If $\bar{f}(x)$ is irreducible in $\mathbb{F}_p[x]$ and has same degree, then $f(x)$ is irreducible

# Examples
**Example 1** (p. 308): $x^2 + x + 1$ is irreducible in $\mathbb{Z}[x]$ since it's irreducible in $\mathbb{F}_2[x]$.

**Example 2** (p. 308): $x^2 + 1$ is irreducible in $\mathbb{Z}[x]$ since it's irreducible in $\mathbb{F}_3[x]$.

# Relationships

## Related
- **eisenstein-criterion** — Another irreducibility criterion
- **gauss-lemma** — Connects $R[x]$ and $F[x]$ irreducibility

# Common Errors
- **Error**: Concluding reducibility because the reduced polynomial is reducible
  **Correction**: The reduction test only gives sufficient conditions for irreducibility, not necessary

# Source Reference
Chapter 9, Section 9.4, Proposition 12, page 308.

# Verification Notes
- Definition: Direct from Proposition 12, p. 308
- Confidence: HIGH — explicit proposition
