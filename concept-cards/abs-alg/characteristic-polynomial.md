---
concept: Characteristic Polynomial
slug: characteristic-polynomial
category: linear-algebra
subcategory: canonical-forms
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Modules over Principal Ideal Domains"
chapter_number: 12
pdf_page: 475
section: "12.2 The Rational Canonical Form"
extraction_confidence: high
aliases:
  - "char poly"
prerequisites:
  - determinant
  - linear-transformation
extends: []
related:
  - minimal-polynomial
  - eigenvalue
  - cayley-hamilton-theorem
contrasts_with:
  - minimal-polynomial
answers_questions:
  - "What is the characteristic polynomial?"
---

# Quick Definition
The characteristic polynomial of T is $c_T(x) = \det(xI - T)$, a monic polynomial of degree $n = \dim V$. Its roots are the eigenvalues of T.

# Core Definition
Let T be a linear transformation of an n-dimensional vector space V over F. The characteristic polynomial of T is $c_T(x) = \det(xI - T)$, a monic polynomial of degree n in F[x]. For a matrix A, $c_A(x) = \det(xI - A)$. The eigenvalues of T are exactly the roots of $c_T(x)$. The characteristic polynomial equals the product of the invariant factors (Dummit & Foote, pp. 475-476).

# Prerequisites
- **determinant** — Used in the definition
- **linear-transformation** — Characteristic polynomial of a transformation

# Key Properties
1. Monic of degree $n = \dim V$
2. Roots are eigenvalues; $\lambda$ is an eigenvalue iff $c_T(\lambda) = 0$
3. $c_T(x) = a_1(x) a_2(x) \cdots a_m(x)$ (product of invariant factors)
4. $c_T(T) = 0$ (Cayley-Hamilton Theorem)
5. $m_T(x) \mid c_T(x)$ and they have the same irreducible factors

# Relationships
## Builds Upon
- **determinant**, **linear-transformation**

## Related
- **minimal-polynomial** — Divides the characteristic polynomial
- **eigenvalue** — Roots of the characteristic polynomial

## Contrasts With
- **minimal-polynomial** — Minimal poly is the last invariant factor; char poly is the product of all

# Source Reference
Chapter 12, Section 12.2, pp. 475-476.

# Verification Notes
- Confidence: HIGH — standard definition
