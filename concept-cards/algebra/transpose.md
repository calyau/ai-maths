---
concept: Transpose
slug: transpose
category: matrices
subcategory: matrix-operations
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.3 The Matrix Transpose"
extraction_confidence: high
aliases:
  - "matrix transpose"
  - "A^t"
prerequisites:
  - matrix
extends: []
related:
  - symmetric-matrix
  - determinant
contrasts_with: []
answers_questions:
  - "What is a matrix and what are its basic operations?"
---

# Quick Definition

The transpose of an m x n matrix A is the n x m matrix A^t obtained by reflecting about the diagonal: (A^t)_ij = a_ji. Rows become columns and vice versa.

# Core Definition

The transpose of an m x n matrix A is the n x m matrix A^t = (b_ij) where b_ij = a_ji (Artin, p. 24). Key rules: (AB)^t = B^t A^t, (A+B)^t = A^t + B^t, (cA)^t = cA^t, and (A^t)^t = A (formula 1.3.1).

# Prerequisites

- **Matrix** — The object being transposed

# Key Properties

1. (A^t)^t = A
2. (AB)^t = B^t A^t (reverses order)
3. (A+B)^t = A^t + B^t
4. det(A) = det(A^t) (Corollary 1.4.15)
5. Row operations on A correspond to column operations via transpose

# Construction / Recognition

## To Construct:
1. Given A, write rows of A as columns of A^t
2. Entry (i,j) of A becomes entry (j,i) of A^t

## To Recognize:
1. Rows and columns have been swapped

# Context & Application

The transpose connects row and column operations: facts about rows carry over to columns via A^t. The equality det(A) = det(A^t) means all determinant properties hold for columns as well as rows.

# Examples

**Example 1** (p. 24): [[1,2],[3,4]]^t = [[1,3],[2,4]] and [1,2,3]^t = [1,2,3]^t (column vector).

# Relationships

## Builds Upon
- **Matrix** — Operates on any matrix

## Enables
- **Symmetric matrix** — A is symmetric iff A = A^t
- **Determinant** — det(A) = det(A^t)

# Common Errors

- **Error**: Forgetting that (AB)^t = B^t A^t (not A^t B^t)
  **Correction**: The order reverses when transposing a product

# Common Confusions

- **Confusion**: Thinking transpose changes the entries
  **Clarification**: Transpose only rearranges entries; it does not modify their values

# Source Reference

Chapter 1: Matrices, Section 1.3, page 24.

# Verification Notes

- Definition source: Direct from Section 1.3, p. 24
- Confidence rationale: Explicitly defined with rules
- Uncertainties: None
- Cross-reference status: Verified
