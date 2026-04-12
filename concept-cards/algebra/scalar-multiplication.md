---
# === CORE IDENTIFICATION ===
concept: Scalar Multiplication
slug: scalar-multiplication

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
aliases:
  - "scalar multiplication of a matrix"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - matrix
extends: []
related:
  - matrix-addition
  - matrix-multiplication
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a matrix and what are its basic operations?"
---

# Quick Definition

Scalar multiplication multiplies every entry of a matrix by a given scalar (number). If A = (a_ij) and c is a scalar, then cA = (ca_ij).

# Core Definition

The result of multiplying an m x n matrix A by a scalar c is another m x n matrix B = (b_ij) where b_ij = ca_ij for all i, j. Numbers used as multipliers are called scalars (Artin, p. 13).

# Prerequisites

- **Matrix** — Must know what a matrix is

# Key Properties

1. Preserves the dimensions of the matrix
2. Compatible with matrix multiplication: c(AB) = (cA)B = A(cB)
3. Distributes over matrix addition: c(A + B) = cA + cB

# Construction / Recognition

## To Construct:
1. Given scalar c and matrix A = (a_ij)
2. Multiply every entry by c: b_ij = ca_ij

## To Recognize:
1. Every entry of the result is the same multiple of the corresponding entry of the original

# Context & Application

Together with matrix addition, scalar multiplication gives the set of m x n matrices the structure of a vector space.

# Examples

**Example 1** (p. 13): 2 * [[2,1,0],[1,3,5]] = [[4,2,0],[2,6,10]].

# Relationships

## Builds Upon
- **Matrix** — Operates on matrices

## Enables
- **Linear combination** — Scalar multiplication combined with addition

## Related
- **Matrix addition** — The other vector space operation on matrices

# Common Errors

- **Error**: Forgetting to multiply every entry
  **Correction**: Scalar multiplication applies to all entries

# Common Confusions

- **Confusion**: Conflating scalar multiplication with matrix multiplication
  **Clarification**: Scalar multiplication involves a number and a matrix; matrix multiplication involves two matrices

# Source Reference

Chapter 1: Matrices, Section 1.1, page 13.

# Verification Notes

- Definition source: Direct from p. 13
- Confidence rationale: Explicitly defined with example
- Uncertainties: None
- Cross-reference status: Verified
