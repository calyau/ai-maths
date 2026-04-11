---
concept: Determinant
slug: determinant
category: linear-algebra
subcategory: determinants
tier: intermediate
source: "Abstract Algebra"
source_slug: abs-alg
authors: "David S. Dummit, Richard M. Foote"
chapter: "Vector Spaces"
chapter_number: 11
pdf_page: 432
section: "11.4 Determinants"
extraction_confidence: high
aliases:
  - "det"
prerequisites:
  - alternating-map
  - matrix-of-linear-transformation
extends: []
related:
  - characteristic-polynomial
  - exterior-algebra
contrasts_with: []
answers_questions:
  - "What is a determinant?"
---

# Quick Definition
The determinant is the unique n-multilinear alternating form on $R^n$ (viewing matrix columns as vectors) that evaluates to 1 on the identity matrix. It is computed by $\det(\alpha_{ij}) = \sum_{\sigma \in S_n} \epsilon(\sigma) \alpha_{\sigma(1)1} \cdots \alpha_{\sigma(n)n}$.

# Core Definition
An $n \times n$ determinant function on a commutative ring R is a function $\det: M_{n \times n}(R) \to R$ that is (1) an n-multilinear alternating form on the columns, and (2) satisfies $\det(I) = 1$. There is a unique such function, given by $\det(\alpha_{ij}) = \sum_{\sigma \in S_n} \epsilon(\sigma) \alpha_{\sigma(1)1} \alpha_{\sigma(2)2} \cdots \alpha_{\sigma(n)n}$ (Dummit & Foote, Theorem 24, p. 434).

# Prerequisites
- **alternating-map** — The determinant is alternating
- **matrix-of-linear-transformation** — Determinant of a matrix

# Key Properties
1. $\det A = \det A^t$ (Corollary 25)
2. $\det(AB) = \det(A)\det(B)$
3. A is invertible iff $\det A$ is a unit in R
4. Cramer's Rule for solving systems (Theorem 26)
5. Determinant is both column-multilinear and row-multilinear

# Examples
**Example** (p. 433): The $2 \times 2$ determinant is $ad - bc$.

# Relationships
## Builds Upon
- **alternating-map**, **matrix-of-linear-transformation**

## Enables
- **characteristic-polynomial** — $\det(xI - A)$
- **exterior-algebra** — Determinant as a top exterior power

# Source Reference
Chapter 11, Section 11.4, Theorem 24, pp. 432-440.

# Verification Notes
- Confidence: HIGH — unique characterization theorem
