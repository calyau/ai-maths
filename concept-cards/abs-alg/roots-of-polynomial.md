---
concept: Roots of a Polynomial
slug: roots-of-polynomial
category: ring-theory
subcategory: polynomial-rings
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Polynomial Rings"
chapter_number: 9
pdf_page: 306
section: "9.4 Irreducibility Criteria"
extraction_confidence: high
aliases:
  - "zeros of a polynomial"
prerequisites:
  - polynomial-ring-over-field
  - division-algorithm-polynomials
extends: []
related:
  - irreducible-polynomial
  - evaluation-homomorphism
contrasts_with: []
answers_questions:
  - "What is a root of a polynomial?"
  - "How do roots relate to factors?"
---

# Quick Definition
An element $\alpha \in F$ is a root (or zero) of $p(x) \in F[x]$ if $p(\alpha) = 0$, which occurs if and only if $(x - \alpha)$ divides $p(x)$.

# Core Definition
(Proposition 9) Let F be a field. Then $p(x) \in F[x]$ has a factor of degree one if and only if $p(x)$ has a root in F, i.e., there is an $\alpha \in F$ with $p(\alpha) = 0$ (Dummit & Foote, p. 306).

# Prerequisites
- **Polynomial ring over field** — Roots are defined for polynomials over fields
- **Division algorithm** — Used to show $p(\alpha) = 0$ implies $(x-\alpha) \mid p(x)$

# Key Properties
1. $\alpha$ is a root iff $(x - \alpha) \mid p(x)$ (Proposition 9)
2. A degree 2 or 3 polynomial is reducible iff it has a root (Proposition 10, p. 306)
3. A polynomial of degree n has at most n roots in a field (p. 306)
4. Rational Root Test: for $p(x) \in \mathbb{Z}[x]$, rational root $r/s$ satisfies $r \mid a_0$ and $s \mid a_n$ (Proposition 11, p. 307)

# Construction / Recognition
## To Find Roots:
1. For $p(x) \in \mathbb{Z}[x]$: use the Rational Root Test (Proposition 11)
2. For $p(x) \in \mathbb{F}_p[x]$: test all $p$ elements of $\mathbb{F}_p$

# Examples
**Example 1** (p. 307): $x^3 - 3x - 1 \in \mathbb{Z}[x]$ has no rational roots (candidates $\pm 1$ fail).

**Example 2** (p. 308): $x^2 + 1$ has root $1$ in $\mathbb{Z}/2\mathbb{Z}$ but no root in $\mathbb{Z}/3\mathbb{Z}$.

# Relationships

## Related
- **irreducible-polynomial** — Root test is an irreducibility criterion for degree 2-3
- **evaluation-homomorphism** — Roots correspond to kernel elements

# Common Errors
- **Error**: Concluding irreducibility from "no roots" for degree $\geq 4$
  **Correction**: A degree 4 polynomial can factor into two quadratics with no linear factors

# Source Reference
Chapter 9, Section 9.4, Propositions 9-11, pages 306-307.

# Verification Notes
- Definition: Direct from Proposition 9, p. 306
- Confidence: HIGH — explicit propositions
