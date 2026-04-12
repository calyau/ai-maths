---
concept: Row Echelon Form
slug: row-echelon-form
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
  - "echelon form"
  - "reduced row echelon form"
  - "row echelon matrix"
prerequisites:
  - matrix
  - elementary-row-operations
  - row-reduction
extends: []
related:
  - pivot
  - rank
contrasts_with: []
answers_questions:
  - "How do I row-reduce a matrix?"
---

# Quick Definition

A row echelon matrix satisfies: (a) zero rows are at the bottom, (b) the first nonzero entry of each nonzero row is 1 (a pivot), (c) each pivot is to the right of the one above, (d) entries above pivots are zero.

# Core Definition

A row echelon matrix is a matrix with these properties (Artin, p. 20, formula 1.2.12):
(a) If row i is zero, then row j is zero for all j > i.
(b) If row i is nonzero, its first nonzero entry is 1 (called a pivot).
(c) If row (i+1) is nonzero, its pivot is to the right of the pivot in row i.
(d) The entries above a pivot are zero (entries below are automatically zero by (c)).

Every matrix can be reduced to a unique row echelon form.

# Prerequisites

- **Matrix** — The object being reduced
- **Elementary row operations** — Used to achieve this form
- **Row reduction** — The process that produces this form

# Key Properties

1. Every matrix has a unique row echelon form
2. The number of pivots equals the rank of the matrix
3. A square row echelon matrix is either I or has a zero bottom row (Lemma 1.2.15)
4. Allows direct reading of solutions to AX = B (Proposition 1.2.13)

# Construction / Recognition

## To Construct:
1. Perform row reduction on the matrix
2. Result satisfies all four properties (a)-(d)

## To Recognize:
1. Check all four properties: zero rows at bottom, pivots are 1, staircase pattern, zeros above pivots

# Context & Application

Row echelon form is the standard simplified form used to solve linear systems, determine rank, and test invertibility. Proposition 1.2.13 shows how to read solutions directly from the echelon form.

# Examples

**Example 1** (p. 19): [[1,0,-1,0,3],[0,1,3,0,1],[0,0,0,1,1]] is in row echelon form with pivots in columns 1, 2, 4.

# Relationships

## Builds Upon
- **Row reduction** — The process that produces echelon form

## Enables
- **Rank** — Number of pivots in echelon form
- **System of linear equations** — Solutions read from echelon form

## Related
- **Pivot** — The leading 1 in each nonzero row

# Common Errors

- **Error**: Forgetting to clear entries above pivots
  **Correction**: Property (d) requires all entries above each pivot to be zero

# Common Confusions

- **Confusion**: Confusing row echelon form with upper triangular form
  **Clarification**: Row echelon form has specific staircase structure with pivots equal to 1; it may not be square

# Source Reference

Chapter 1: Matrices, Section 1.2, page 20.

# Verification Notes

- Definition source: Direct from (1.2.12), p. 20
- Confidence rationale: Explicitly defined with all four properties
- Uncertainties: None
- Cross-reference status: Verified
