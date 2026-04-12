---
concept: Cofactor Matrix
slug: cofactor-matrix
category: matrices
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.6 Other Formulas for the Determinant"
extraction_confidence: high
aliases:
  - "adjoint matrix"
  - "adjugate"
prerequisites:
  - determinant
  - cofactor-expansion
extends: []
related:
  - matrix-inverse
contrasts_with: []
answers_questions:
  - "How do I compute a determinant?"
---

# Quick Definition

The cofactor matrix cof(A) of an n x n matrix A has (i,j) entry (-1)^(i+j) det(A_ji), the signed minor of the transposed position. It satisfies CA = AC = (det A)I, giving the inverse formula A^(-1) = (1/det A) cof(A).

# Core Definition

The cofactor matrix of an n x n matrix A is cof(A) with (i,j) entry cof(A)_ij = (-1)^(i+j) det(A_ji), where A_ji is obtained by deleting row j and column i. It satisfies cof(A) * A = A * cof(A) = (det A) * I. If det(A) != 0, then A^(-1) = (1/det A) cof(A) (Theorem 1.6.9, Artin, pp. 32-33).

# Prerequisites

- **Determinant** — Entries of the cofactor matrix are signed minors
- **Cofactor expansion** — The cofactor matrix collects all cofactors

# Key Properties

1. cof(A) * A = (det A) * I
2. If det(A) != 0, then A^(-1) = (1/det(A)) * cof(A)
3. For 2x2: cof([[a,b],[c,d]]) = [[d,-c],[-b,a]]

# Construction / Recognition

## To Construct:
1. Compute all (n-1)x(n-1) minors det(A_ij)
2. Apply signs (-1)^(i+j)
3. Transpose the result

## To Recognize:
1. A matrix whose product with A gives (det A)I

# Context & Application

The cofactor formula A^(-1) = (1/det(A)) cof(A) is theoretically important (e.g., Cramer's rule) but computationally expensive for large n. For 2x2 matrices, it gives the standard inverse formula.

# Examples

**Example 1** (p. 33): For A = [[1,1,2],[0,2,1],[1,0,2]], the cofactor matrix is computed in three steps (minors, signs, transpose) yielding cof(A) = [[4,-2,-3],[1,0,-1],[-2,1,2]]. Since det(A) = 1, A^(-1) = cof(A).

# Relationships

## Builds Upon
- **Determinant** — Entries are signed determinants of submatrices
- **Cofactor expansion** — Collects all cofactors into a matrix

## Enables
- **Matrix inverse** — A^(-1) = (1/det(A)) cof(A)

# Common Errors

- **Error**: Forgetting to transpose after computing signed minors
  **Correction**: The cofactor matrix involves A_ji (note the transposed indices)

# Common Confusions

- **Confusion**: Confusing the cofactor matrix with the matrix of minors
  **Clarification**: The cofactor matrix includes both the alternating signs and the transpose

# Source Reference

Chapter 1: Matrices, Section 1.6, pages 32-33.

# Verification Notes

- Definition source: Direct from (1.6.7) and Theorem 1.6.9
- Confidence rationale: Explicitly defined with worked example
- Uncertainties: None
- Cross-reference status: Verified
