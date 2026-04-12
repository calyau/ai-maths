---
concept: Rank
slug: rank
category: linear-algebra
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Operators"
chapter_number: 4
pdf_page: 113
section: "4.1 The Dimension Formula"
extraction_confidence: high
aliases:
  - "rank of a matrix"
  - "rank of a linear transformation"
prerequisites:
  - linear-transformation
  - dimension
extends: []
related:
  - null-space
  - rank-nullity-theorem
  - row-echelon-form
contrasts_with: []
answers_questions:
  - "What is a linear transformation?"
---

# Quick Definition

The rank of a linear transformation T (or matrix A) is the dimension of its image (column space). For a matrix, the rank equals the number of pivots in its row echelon form, and equals the row rank (Theorem 4.2.14).

# Core Definition

The rank of a linear transformation T: V -> W is the dimension of its image im(T) (Artin, p. 114). For a matrix A, this equals the dimension of the column space. The rank of A equals the rank of A^t (row rank = column rank, Theorem 4.2.14).

# Prerequisites

- **Linear transformation** — Rank is defined for linear maps
- **Dimension** — Rank is the dimension of the image

# Key Properties

1. rank(A) = number of pivots in echelon form
2. rank(A) = rank(A^t) (row rank = column rank)
3. nullity + rank = n (number of columns)
4. A is invertible iff rank = n (for square n x n A)

# Construction / Recognition

## To Construct:
1. Row-reduce A and count pivots
2. Or find a basis for the column space

## To Recognize:
1. The dimension of the column space or image

# Context & Application

Rank is the fundamental measure of how "large" the image of a linear transformation is. Together with nullity, it completely describes the transformation's behavior via the dimension formula.

# Examples

**Example 1** (p. 114): An m x n matrix of rank r has nullity n - r.

**Example 2** (p. 118): Theorem 4.2.14: rank(A) = rank(A^t).

# Relationships

## Builds Upon
- **Dimension** — Rank is a dimension

## Enables
- **Rank-nullity theorem** — rank + nullity = dim V

## Related
- **Row echelon form** — Rank = number of pivots

# Common Errors

- **Error**: Confusing rank with the number of nonzero rows after reduction
  **Correction**: This is correct only if reduction is complete (echelon form)

# Common Confusions

- **Confusion**: Thinking row rank and column rank can differ
  **Clarification**: They are always equal (Theorem 4.2.14)

# Source Reference

Chapter 4: Linear Operators, Section 4.1, pages 114-118.

# Verification Notes

- Definition source: Direct from Section 4.1
- Confidence rationale: Central concept
- Uncertainties: None
- Cross-reference status: Verified
