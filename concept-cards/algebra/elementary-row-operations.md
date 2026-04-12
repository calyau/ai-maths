---
concept: Elementary Row Operations
slug: elementary-row-operations
category: matrices
subcategory: matrix-operations
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.2 Row Reduction"
extraction_confidence: high
aliases:
  - "row operations"
prerequisites:
  - matrix
extends: []
related:
  - elementary-matrix
  - row-reduction
contrasts_with: []
answers_questions:
  - "How do I row-reduce a matrix?"
---

# Quick Definition

The three elementary row operations are: (i) add a scalar multiple of one row to another, (ii) interchange two rows, (iii) multiply a row by a nonzero scalar. Each corresponds to left multiplication by an elementary matrix.

# Core Definition

The elementary row operations on a matrix X, corresponding to elementary matrices E, are (Artin, p. 19, formula 1.2.5):
- Type (i): add a times (row j) to (row i)
- Type (ii): interchange (row i) and (row j)
- Type (iii): multiply (row i) by a nonzero scalar c

Each operation is equivalent to left multiplication by the corresponding elementary matrix: EX.

# Prerequisites

- **Matrix** — Operations act on matrices

# Key Properties

1. Each operation is invertible (Lemma 1.2.6)
2. Type (i) does not change the determinant
3. Type (ii) changes the sign of the determinant
4. Type (iii) multiplies the determinant by c
5. Preserve the solution set of AX = B

# Construction / Recognition

## To Construct:
1. Type (i): Replace row_i with row_i + a * row_j
2. Type (ii): Swap row_i and row_j
3. Type (iii): Replace row_i with c * row_i (c != 0)

## To Recognize:
1. A single modification to one or two rows of a matrix

# Context & Application

Elementary row operations are the building blocks of row reduction. They are used to solve systems, compute inverses, determine rank, and prove theorems about invertibility.

# Examples

**Example 1** (p. 19): In reducing [[1,1,2,1,5],[1,1,2,6,10],[1,2,5,2,7]], the first step subtracts row 1 from rows 2 and 3 (Type (i) operations).

# Relationships

## Builds Upon
- **Matrix** — Operations act on matrices

## Enables
- **Row reduction** — Composed of elementary row operations
- **Row echelon form** — Achieved by these operations

## Related
- **Elementary matrix** — Each operation corresponds to an elementary matrix

# Common Errors

- **Error**: Using a zero scalar in Type (iii)
  **Correction**: The scalar must be nonzero to keep the operation invertible

# Common Confusions

- **Confusion**: Mixing up which row is modified in Type (i)
  **Clarification**: In "add a*(row j) to (row i)," row i changes; row j stays the same

# Source Reference

Chapter 1: Matrices, Section 1.2, page 19.

# Verification Notes

- Definition source: Direct from (1.2.5), p. 19
- Confidence rationale: Explicitly enumerated
- Uncertainties: None
- Cross-reference status: Verified
