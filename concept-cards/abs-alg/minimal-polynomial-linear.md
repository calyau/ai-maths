---
concept: Minimal Polynomial (Linear Transformation)
slug: minimal-polynomial-linear
category: linear-algebra
subcategory: canonical-forms
tier: advanced
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Modules over Principal Ideal Domains"
chapter_number: 12
pdf_page: 476
section: "12.2 The Rational Canonical Form"
extraction_confidence: high
aliases:
  - "minimal polynomial of a matrix"
  - "minimal polynomial of T"
prerequisites:
  - fx-module
  - characteristic-polynomial
extends: []
related:
  - rational-canonical-form
  - cayley-hamilton-theorem
  - invariant-factors
contrasts_with:
  - characteristic-polynomial
answers_questions:
  - "What is the minimal polynomial of a linear transformation?"
---

# Quick Definition
The minimal polynomial $m_T(x)$ of T is the unique monic polynomial of smallest degree such that $m_T(T) = 0$. It equals the last (largest) invariant factor and divides the characteristic polynomial.

# Core Definition
The minimal polynomial $m_T(x)$ is the unique monic generator of $\text{Ann}(V)$ in F[x], where V is viewed as an F[x]-module via T. Equivalently, it is the monic polynomial of smallest degree with $m_T(T) = 0$, and any polynomial annihilating T is divisible by $m_T(x)$. The minimal polynomial equals the last invariant factor $a_m(x)$ (Dummit & Foote, p. 476, Proposition 13).

# Prerequisites
- **fx-module** — V as an F[x]-module; $m_T(x)$ generates the annihilator
- **characteristic-polynomial** — $m_T(x) \mid c_T(x)$

# Key Properties
1. $m_T(x) \mid c_T(x)$ (Cayley-Hamilton consequence)
2. $m_T(x)$ and $c_T(x)$ have the same irreducible factors
3. T is diagonalizable iff $m_T(x)$ has no repeated roots
4. $m_T(x)$ equals the last invariant factor

# Relationships
## Builds Upon
- **fx-module**, **characteristic-polynomial**

## Related
- **rational-canonical-form**, **cayley-hamilton-theorem**

## Contrasts With
- **characteristic-polynomial** — Same roots but potentially different multiplicities

# Source Reference
Chapter 12, Section 12.2, p. 476, Proposition 13.

# Verification Notes
- Confidence: HIGH — explicit definition
