---
# === CORE IDENTIFICATION ===
concept: Matrix Multiplication
slug: matrix-multiplication

# === CLASSIFICATION ===
category: matrices
subcategory: matrix-operations
tier: foundational

# === PROVENANCE ===
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.1 The Basic Operations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - matrix
  - row-vector
  - column-vector
extends: []
related:
  - matrix-addition
  - scalar-multiplication
  - identity-matrix
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a matrix and what are its basic operations?"
---

# Quick Definition

The product of an l x m matrix A and an m x n matrix B is an l x n matrix P whose (i,j) entry is the sum of products of the ith row of A with the jth column of B: p_ij = sum of a_iv * b_vj for v = 1 to m.

# Core Definition

If A = (a_ij) is an l x m matrix and B = (b_ij) is an m x n matrix, their product AB is the l x n matrix P = (p_ij) defined by p_ij = a_i1*b_1j + a_i2*b_2j + ... + a_im*b_mj. The number of columns of A must equal the number of rows of B. Matrix multiplication is associative and distributes over addition, but is NOT commutative in general (Artin, pp. 13-15).

# Prerequisites

- **Matrix** — The objects being multiplied
- **Row vector** — Rows of the left factor
- **Column vector** — Columns of the right factor

# Key Properties

1. Defined when the number of columns of A equals the number of rows of B
2. Associative: (AB)C = A(BC)
3. Distributive: A(B + B') = AB + AB' and (A + A')B = AB + A'B
4. NOT commutative: AB != BA in general
5. Compatible with scalar multiplication: c(AB) = (cA)B = A(cB)

# Construction / Recognition

## To Construct:
1. Verify A is l x m and B is m x n
2. For each entry p_ij, compute the dot product of row i of A and column j of B
3. The result is l x n

## To Recognize:
1. An operation combining an l x m and an m x n matrix into an l x n matrix

# Context & Application

Matrix multiplication is the most important operation in linear algebra. It encodes composition of linear transformations, systems of linear equations (AX = B), and is the basis for defining groups of invertible matrices. Artin illustrates it concretely with a candy bar cost example.

# Examples

**Example 1** (p. 13): [1,3,5] * [1,-1,4]^t = 1 - 3 + 20 = 18 (row times column).

**Example 2** (p. 15): [[1,1],[0,0]] * [[2,0],[1,1]] = [[3,1],[0,0]], while [[2,0],[1,1]] * [[1,1],[0,0]] = [[2,2],[1,1]]. Not commutative.

# Relationships

## Builds Upon
- **Matrix** — The objects being multiplied

## Enables
- **Invertible matrix** — Defined via matrix multiplication
- **System of linear equations** — Written as AX = B
- **Determinant** — det(AB) = det(A)det(B)

## Contrasts With
- **Matrix addition** — Addition is commutative; multiplication is not

# Common Errors

- **Error**: Attempting to multiply matrices with incompatible dimensions
  **Correction**: The inner dimensions must match: (l x m)(m x n) = (l x n)

- **Error**: Assuming AB = BA
  **Correction**: Matrix multiplication is not commutative

# Common Confusions

- **Confusion**: Thinking matrix multiplication is entry-wise
  **Clarification**: It uses the row-by-column dot product rule

# Source Reference

Chapter 1: Matrices, Section 1.1, pages 13-16.

# Verification Notes

- Definition source: Direct from (1.1.3), p. 14
- Confidence rationale: Extensively defined with multiple examples
- Uncertainties: None
- Cross-reference status: Verified
