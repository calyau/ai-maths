---
concept: Triangular Matrix
slug: triangular-matrix
category: matrices
subcategory: special-matrices
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
  - "upper triangular matrix"
  - "lower triangular matrix"
prerequisites:
  - matrix
  - diagonal-matrix
extends:
  - diagonal-matrix
related:
  - row-echelon-form
  - eigenvalue
contrasts_with: []
answers_questions:
  - "What is a matrix and what are its basic operations?"
---

# Quick Definition

An upper triangular matrix has all entries below the diagonal equal to zero. A lower triangular matrix has all entries above the diagonal equal to zero.

# Core Definition

A square matrix A is called upper triangular if a_ij = 0 whenever i > j (entries below the diagonal are zero). Lower triangular is defined analogously with entries above the diagonal zero. Artin uses * to indicate arbitrary undetermined entries and shows that the product of upper triangular matrices is upper triangular (Artin, p. 16).

# Prerequisites

- **Matrix** — Must understand square matrices
- **Diagonal matrix** — Triangular generalizes diagonal

# Key Properties

1. The product of upper (lower) triangular matrices is upper (lower) triangular
2. The determinant of a triangular matrix is the product of its diagonal entries
3. The eigenvalues of a triangular matrix are its diagonal entries (Corollary 4.5.10)
4. A triangular matrix is invertible iff all diagonal entries are nonzero

# Construction / Recognition

## To Construct:
1. For upper triangular: set a_ij = 0 for all i > j
2. For lower triangular: set a_ij = 0 for all i < j

## To Recognize:
1. Check that all entries on one side of the diagonal are zero

# Context & Application

Triangular matrices arise naturally from row reduction and from the triangularization theorem (Proposition 4.6.1): every complex matrix is similar to an upper triangular matrix. The characteristic polynomial of a triangular matrix is easily read from its diagonal.

# Examples

**Example 1** (p. 16): Upper triangular matrices appear in the row reduction (1.2.8).

**Example 2** (Section 4.6): Every complex matrix is similar to an upper triangular matrix (Proposition 4.6.1).

# Relationships

## Builds Upon
- **Diagonal matrix** — A diagonal matrix is both upper and lower triangular

## Enables
- **Row echelon form** — A special type of upper triangular form
- **Triangular form** — Proposition 4.6.1: every complex matrix can be triangularized

## Related
- **Eigenvalue** — The diagonal entries of a triangular matrix are its eigenvalues

# Common Errors

- **Error**: Thinking the inverse of a triangular matrix is not triangular
  **Correction**: The inverse of an upper triangular matrix is upper triangular

# Common Confusions

- **Confusion**: Confusing upper and lower triangular
  **Clarification**: "Upper" means the nonzero entries are on or above the diagonal; "lower" means on or below

# Source Reference

Chapter 1: Matrices, Section 1.1, page 16; Chapter 4, Section 4.6.

# Verification Notes

- Definition source: From p. 16 and Section 4.6
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
