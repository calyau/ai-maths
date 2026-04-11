---
concept: Polynomial Ring in Several Variables
slug: polynomial-in-several-variables
category: ring-theory
subcategory: polynomial-rings
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Polynomial Rings"
chapter_number: 9
pdf_page: 297
section: "9.1 Definitions and Basic Properties"
extraction_confidence: high
aliases:
  - "multivariate polynomial ring"
prerequisites:
  - polynomial-ring
extends:
  - polynomial-ring
related:
  - polynomial-ring-as-ufd
contrasts_with: []
answers_questions:
  - "What is a polynomial ring in several variables?"
  - "How are multidegree and total degree defined?"
---

# Quick Definition
$R[x_1, \ldots, x_n]$ is defined inductively as $R[x_1, \ldots, x_{n-1}][x_n]$ -- polynomials in $x_n$ with coefficients that are polynomials in $x_1, \ldots, x_{n-1}$.

# Core Definition
The polynomial ring in variables $x_1, \ldots, x_n$ with coefficients in R is defined inductively by $R[x_1, \ldots, x_n] = R[x_1, \ldots, x_{n-1}][x_n]$. A nonzero polynomial is a finite sum of monomial terms $ax_1^{d_1} \cdots x_n^{d_n}$. The *degree* of a term is $d_1 + \cdots + d_n$ and the *multidegree* is $(d_1, \ldots, d_n)$ (Dummit & Foote, pp. 297-298).

# Prerequisites
- **Polynomial ring** — Several-variable rings are iterated polynomial rings

# Key Properties
1. $R[x_1, \ldots, x_n]$ is a commutative ring with identity (if R is)
2. If R is an integral domain, so is $R[x_1, \ldots, x_n]$ (Proposition 1)
3. If R is a UFD, so is $R[x_1, \ldots, x_n]$ (Corollary 8, p. 305)
4. $R[x_1, \ldots, x_n]$ is NOT a PID for $n \geq 2$ (Exercise 7, p. 299)
5. The degree of a polynomial is the maximum degree of its terms
6. A polynomial is *homogeneous* (or a *form*) if all terms have the same degree

# Examples
**Example** (p. 298): In $\mathbb{Z}[x, y]$: $p(x,y) = 2x^3 + xy - y^2$ has degree 3; $q(x,y) = -3xy + 2y^2 + x^2y^3$ has degree 5.

# Relationships

## Builds Upon
- **polynomial-ring** — Iterated polynomial ring construction

## Related
- **polynomial-ring-as-ufd** — $R[x_1, \ldots, x_n]$ is a UFD when R is

# Common Errors
- **Error**: Assuming $R[x, y]$ is a PID when R is a field
  **Correction**: $(x, y)$ is not principal in $F[x, y]$; polynomial rings in $\geq 2$ variables are never PIDs

# Source Reference
Chapter 9, Section 9.1, Definition and examples, pages 297-298.

# Verification Notes
- Definition: Direct from pp. 297-298
- Confidence: HIGH — explicit definition
