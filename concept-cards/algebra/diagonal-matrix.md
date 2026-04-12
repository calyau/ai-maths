---
concept: Diagonal Matrix
slug: diagonal-matrix
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
  - triangular-matrix
contrasts_with: []
answers_questions:
  - "What is a matrix and what are its basic operations?"
---

# Quick Definition

A diagonal matrix is a square matrix whose only nonzero entries are on the main diagonal (positions a_ii). The identity matrix is a diagonal matrix with all diagonal entries equal to 1.

# Core Definition

The entries a_ii of a matrix A are its diagonal entries. A matrix A is a diagonal matrix if its only nonzero entries are diagonal entries (Artin, p. 16).

# Prerequisites

- **Matrix** — Must understand square matrices and entries

# Key Properties

1. All off-diagonal entries are zero
2. The product of diagonal matrices is diagonal
3. The inverse of a diagonal matrix (when it exists) is diagonal, with entries 1/a_ii
4. The determinant is the product of the diagonal entries

# Construction / Recognition

## To Construct:
1. Create a square matrix with specified diagonal entries d_1, ..., d_n
2. Set all off-diagonal entries to 0

## To Recognize:
1. All entries a_ij with i != j are zero

# Context & Application

Diagonal matrices are the simplest nontrivial matrices. The goal of diagonalization (Chapter 4) is to find a basis in which a linear operator has a diagonal matrix representation.

# Examples

**Example 1** (p. 16): The identity matrix I is a diagonal matrix with all diagonal entries 1.

# Relationships

## Builds Upon
- **Matrix** — Special case of square matrix

## Enables
- **Identity matrix** — Diagonal matrix with all 1's
- **Diagonalization** — Representing an operator by a diagonal matrix

## Related
- **Triangular matrix** — Generalizes diagonal (allows entries above or below diagonal)

# Common Errors

- **Error**: Assuming all square matrices are diagonal
  **Correction**: Most square matrices have nonzero off-diagonal entries

# Common Confusions

- **Confusion**: Confusing "diagonal" with "triangular"
  **Clarification**: Diagonal means ALL off-diagonal entries are zero; triangular allows entries on one side

# Source Reference

Chapter 1: Matrices, Section 1.1, page 16.

# Verification Notes

- Definition source: Direct from p. 16
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
