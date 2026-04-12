---
concept: Cofactor Expansion
slug: cofactor-expansion
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
  - "expansion by minors"
  - "Laplace expansion"
prerequisites:
  - determinant
extends: []
related:
  - cofactor-matrix
contrasts_with: []
answers_questions:
  - "How do I compute a determinant?"
---

# Quick Definition

Cofactor expansion computes a determinant by expanding along any row or column, using the minors (determinants of submatrices) with alternating signs.

# Core Definition

Expansion by minors on the jth column: det(A) = sum of (-1)^(v+j) * a_vj * det(A_vj) for v = 1 to n. Expansion on the ith row: det(A) = sum of (-1)^(i+v) * a_iv * det(A_iv) for v = 1 to n. Here A_ij is the submatrix obtained by deleting row i and column j (Artin, pp. 31-32, formulas 1.6.1-1.6.2).

# Prerequisites

- **Determinant** — Cofactor expansion is a method for computing determinants

# Key Properties

1. Works on any row or any column
2. Alternating sign pattern: (-1)^(i+j)
3. Reduces an n x n determinant to (n-1) x (n-1) determinants
4. Most efficient when expanding along a row or column with many zeros

# Construction / Recognition

## To Construct:
1. Choose a row or column (preferably one with many zeros)
2. For each nonzero entry a_ij, compute (-1)^(i+j) * a_ij * det(A_ij)
3. Sum all terms

## To Recognize:
1. A determinant computation that reduces to smaller determinants via one row or column

# Context & Application

Cofactor expansion is the standard recursive method for computing determinants. It gives both the recursive definition (on column 1) and alternative formulas (on any row or column). The alternating signs follow the checkerboard pattern +, -, +, -, ...

# Examples

**Example 1** (p. 32): Expansion on the second row of [[1,1,2],[0,2,1],[1,0,2]]: -0*det([[1,2],[0,2]]) + 2*det([[1,2],[1,2]]) - 1*det([[1,1],[1,0]]) = 0 + 0 - (-1) = 1.

# Relationships

## Builds Upon
- **Determinant** — Method for computing it

## Enables
- **Cofactor matrix** — Built from the signed minors

# Common Errors

- **Error**: Getting the sign pattern wrong
  **Correction**: Use (-1)^(i+j); the checkerboard starts with + at position (1,1)

# Common Confusions

- **Confusion**: Thinking expansion on different rows gives different values
  **Clarification**: All expansions give the same determinant

# Source Reference

Chapter 1: Matrices, Sections 1.4 and 1.6, pages 24-26, 31-32.

# Verification Notes

- Definition source: Direct from (1.6.1)-(1.6.2)
- Confidence rationale: Explicitly defined with examples
- Uncertainties: None
- Cross-reference status: Verified
