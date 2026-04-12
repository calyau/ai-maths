---
concept: Determinant
slug: determinant
category: matrices
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.4 Determinants"
extraction_confidence: high
aliases:
  - "det A"
  - "det"
prerequisites:
  - matrix
  - square-matrix
extends: []
related:
  - cofactor-expansion
  - invertible-matrix
  - permutation
  - sign-of-a-permutation
contrasts_with: []
answers_questions:
  - "What is a determinant and how is it computed?"
  - "How do I compute a determinant?"
---

# Quick Definition

The determinant is a scalar-valued function on square matrices, denoted det(A). For 2x2 matrices, det([[a,b],[c,d]]) = ad - bc. It determines invertibility: A is invertible iff det(A) != 0.

# Core Definition

The determinant is the unique function on n x n matrices satisfying: (i) det(I) = 1, (ii) det is linear in the rows, (iii) if two adjacent rows are equal, det = 0 (Theorem 1.4.7). It is defined recursively by expansion by minors on the first column: det(A) = sum of (-1)^(v+1) * a_v1 * det(A_v1) for v = 1 to n, where A_v1 is the (n-1)x(n-1) matrix obtained by deleting row v and column 1 (Artin, pp. 24-28, formula 1.4.5).

# Prerequisites

- **Matrix** — Must be a square matrix
- **Square matrix** — Determinants are only defined for square matrices

# Key Properties

1. det(I) = 1
2. Linear in each row (multilinear)
3. det = 0 if two rows are equal
4. det(AB) = det(A)det(B) (Theorem 1.4.9)
5. A is invertible iff det(A) != 0 (Corollary 1.4.15)
6. det(A) = det(A^t) (Corollary 1.4.15)
7. Row operations: adding row leaves det unchanged; swapping rows negates det; scaling row by c multiplies det by c

# Construction / Recognition

## To Construct:
1. For 1x1: det([a]) = a
2. For 2x2: det([[a,b],[c,d]]) = ad - bc
3. For larger: expand by minors on any row or column
4. Or use row reduction, tracking sign changes and scalings

## To Recognize:
1. A single scalar value associated to a square matrix
2. Geometric interpretation: absolute value = volume of the image of the unit cube

# Context & Application

The determinant is perhaps the most important single function in linear algebra. It determines invertibility, appears in the formula for the inverse (via cofactors), defines the sign of a permutation, and has geometric meaning as signed volume. Artin emphasizes its uniqueness from three properties.

# Examples

**Example 1** (p. 25): det([[a,b],[c,d]]) = ad - bc. Geometric interpretation: absolute value is the area of the parallelogram image of the unit square.

**Example 2** (p. 26): det([[1,0,3],[2,1,2],[0,5,1]]) = 1*(-9) - 2*(-15) + 0 = 21 by expansion on the first column.

# Relationships

## Builds Upon
- **Square matrix** — Determinants require square matrices

## Enables
- **Invertible matrix** — A is invertible iff det(A) != 0
- **Cofactor matrix** — Used to compute A^(-1) = (1/det(A)) * cof(A)
- **Characteristic polynomial** — det(tI - A) is the characteristic polynomial
- **Sign of a permutation** — det of a permutation matrix

## Related
- **Permutation** — Complete expansion uses permutations

# Common Errors

- **Error**: Forgetting alternating signs in cofactor expansion
  **Correction**: The sign pattern is (-1)^(i+j) for position (i,j)

- **Error**: Applying the Sarrus rule (diagonal products) to 4x4 or larger
  **Correction**: The diagonal trick only works for 3x3 matrices (Artin warns about this)

# Common Confusions

- **Confusion**: Thinking det(A+B) = det(A) + det(B)
  **Clarification**: The determinant is multiplicative (det(AB) = det(A)det(B)), NOT additive

# Source Reference

Chapter 1: Matrices, Sections 1.4 and 1.6, pages 24-33.

# Verification Notes

- Definition source: Direct from (1.4.5) and Theorem 1.4.7
- Confidence rationale: Extensively developed with uniqueness theorem and multiple formulas
- Uncertainties: None
- Cross-reference status: Verified
