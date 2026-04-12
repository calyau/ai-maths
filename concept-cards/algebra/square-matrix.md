---
concept: Square Matrix
slug: square-matrix
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
aliases: []
prerequisites:
  - matrix
extends: []
related:
  - identity-matrix
  - invertible-matrix
  - determinant
contrasts_with: []
answers_questions:
  - "What is a matrix and what are its basic operations?"
---

# Quick Definition

An n x n matrix is called a square matrix. Square matrices can be multiplied by each other, may have inverses, and have determinants.

# Core Definition

An n x n matrix is called a square matrix (Artin, p. 12). Square matrices have the same number of rows and columns, which makes operations like determinants, eigenvalues, and inverses meaningful.

# Prerequisites

- **Matrix** — A square matrix is a special case

# Key Properties

1. Same number of rows and columns
2. Can be multiplied by any other n x n matrix (both AB and BA are defined)
3. Has a determinant
4. May be invertible
5. Has eigenvalues (when considered over an algebraically closed field)

# Construction / Recognition

## To Construct:
1. Choose a dimension n
2. Fill in n^2 entries arranged in n rows and n columns

## To Recognize:
1. The number of rows equals the number of columns

# Context & Application

Square matrices are the most important class of matrices. They are the elements of the general linear group, they represent linear operators (maps from a space to itself), and they carry the richest algebraic structure.

# Examples

**Example 1** (p. 12): A 2x2 matrix [[a,b],[c,d]] is square.

# Relationships

## Builds Upon
- **Matrix** — Special case where m = n

## Enables
- **Determinant** — Defined only for square matrices
- **Invertible matrix** — Only square matrices can be invertible
- **Eigenvalue** — Defined for square matrices/operators

# Common Errors

- **Error**: Attempting to compute the determinant of a non-square matrix
  **Correction**: Determinants are only defined for square matrices

# Common Confusions

- **Confusion**: Thinking all square matrices are invertible
  **Clarification**: A square matrix is invertible only if its determinant is nonzero

# Source Reference

Chapter 1: Matrices, Section 1.1, page 12.

# Verification Notes

- Definition source: Direct from p. 12
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
