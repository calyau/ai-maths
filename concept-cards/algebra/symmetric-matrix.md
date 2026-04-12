---
concept: Symmetric Matrix
slug: symmetric-matrix
category: matrices
subcategory: special-matrices
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.3 The Matrix Transpose"
extraction_confidence: high
aliases: []
prerequisites:
  - matrix
  - transpose
extends: []
related:
  - transpose
contrasts_with: []
answers_questions:
  - "What is a matrix and what are its basic operations?"
---

# Quick Definition

A symmetric matrix is a square matrix that equals its transpose: A = A^t, meaning a_ij = a_ji for all i, j.

# Core Definition

A matrix B is symmetric if B = B^t (Artin, Exercise 3.1, p. 25). This means every entry equals its mirror image across the diagonal: b_ij = b_ji.

# Prerequisites

- **Matrix** — Must be a square matrix
- **Transpose** — Symmetry is defined via the transpose

# Key Properties

1. A = A^t
2. For any square matrix B, BB^t and B + B^t are symmetric
3. The product AB of symmetric matrices is symmetric iff AB = BA

# Construction / Recognition

## To Construct:
1. Choose values for entries on and above the diagonal
2. Set a_ji = a_ij for entries below the diagonal

## To Recognize:
1. Check that A^t = A, i.e., a_ij = a_ji for all i, j

# Context & Application

Symmetric matrices appear throughout linear algebra and are especially important in bilinear forms (Chapter 8) and in applications to geometry and physics. Their eigenvalues are always real when the entries are real.

# Examples

**Example 1** (p. 25): [[1,3],[3,4]] is symmetric since transposing leaves it unchanged.

# Relationships

## Builds Upon
- **Transpose** — Defined as A = A^t

## Related
- **Transpose** — The operation that tests symmetry

# Common Errors

- **Error**: Assuming a symmetric matrix must be diagonal
  **Correction**: Off-diagonal entries can be nonzero as long as a_ij = a_ji

# Common Confusions

- **Confusion**: Confusing symmetric matrices with diagonal matrices
  **Clarification**: Diagonal matrices are symmetric, but symmetric matrices can have nonzero off-diagonal entries

# Source Reference

Chapter 1: Matrices, Section 1.3, page 25 (Exercise 3.1).

# Verification Notes

- Definition source: From Exercise 3.1, p. 25
- Confidence rationale: Standard definition, referenced in exercises
- Uncertainties: None
- Cross-reference status: Verified
