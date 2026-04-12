---
concept: System of Linear Equations
slug: system-of-linear-equations
category: matrices
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.1 The Basic Operations"
extraction_confidence: high
aliases:
  - "linear system"
  - "AX = B"
prerequisites:
  - matrix
  - matrix-multiplication
  - column-vector
extends: []
related:
  - row-reduction
  - augmented-matrix
  - homogeneous-system
  - invertible-matrix
contrasts_with: []
answers_questions:
  - "What is a matrix and what are its basic operations?"
---

# Quick Definition

A system of linear equations can be written in matrix notation as AX = B, where A is the coefficient matrix, X is the column vector of unknowns, and B is the column vector of constants.

# Core Definition

A system of m linear equations in n unknowns a_i1 x_1 + ... + a_in x_n = b_i (for i = 1,...,m) can be written as AX = B where A is the m x n coefficient matrix, X is the unknown column vector, and B is the column vector of constants (Artin, p. 14, formula 1.1.5).

# Prerequisites

- **Matrix** — The coefficient matrix
- **Matrix multiplication** — AX is a matrix product
- **Column vector** — X and B are column vectors

# Key Properties

1. Solved by row-reducing the augmented matrix [A|B]
2. If A is square and invertible, there is a unique solution X = A^(-1)B (Theorem 1.2.21)
3. If m < n, the homogeneous system AX = 0 always has nontrivial solutions (Corollary 1.2.14)
4. Solutions of AX = B form a coset of the nullspace: X_0 + N

# Construction / Recognition

## To Construct:
1. Write the coefficients as a matrix A
2. Write unknowns as column vector X
3. Write constants as column vector B
4. The system is AX = B

## To Recognize:
1. A collection of linear equations sharing the same unknowns

# Context & Application

Systems of linear equations are the primary motivation for matrix algebra. Row reduction provides a systematic method for solving them, and the theory of determinants gives criteria for when solutions exist and are unique.

# Examples

**Example 1** (p. 14): 2x_1 + x_2 = 1, x_1 + 3x_2 + 5x_3 = 18, written as AX = B with A = [[2,1,0],[1,3,5]].

**Example 2** (pp. 19-20): The system (1.2.11) is solved by row-reducing its augmented matrix.

# Relationships

## Builds Upon
- **Matrix multiplication** — The system is AX = B

## Enables
- **Row reduction** — The method for solving
- **Rank** — Determines the dimension of the solution space

## Related
- **Augmented matrix** — [A|B] used in row reduction
- **Homogeneous system** — The special case B = 0

# Common Errors

- **Error**: Assuming every system has a solution
  **Correction**: A system AX = B has no solution if the echelon form reveals an inconsistency (0 = 1)

# Common Confusions

- **Confusion**: Thinking a unique solution always exists
  **Clarification**: Unique solutions require A to be invertible (square with nonzero determinant)

# Source Reference

Chapter 1: Matrices, Sections 1.1-1.2, pages 14, 19-22.

# Verification Notes

- Definition source: Direct from (1.1.5), p. 14
- Confidence rationale: Central topic with extensive treatment
- Uncertainties: None
- Cross-reference status: Verified
