---
# === CORE IDENTIFICATION ===
concept: Unitary Matrix
slug: unitary-matrix

# === CLASSIFICATION ===
category: bilinear-forms
subcategory: null
tier: intermediate

# === PROVENANCE ===
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Bilinear Forms"
chapter_number: 8
pdf_page: 240
section: "8.3 Hermitian Forms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - hermitian-form
extends: []
related:
  - unitary-group
  - orthogonal-matrix
  - spectral-theorem-unitary
contrasts_with:
  - orthogonal-matrix

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a unitary matrix?"
---

# Quick Definition

A complex matrix P is unitary if P*P = I, equivalently P* = P^{-1}. Unitary matrices preserve the standard Hermitian form and have columns that form an orthonormal set.

# Core Definition

A matrix P is unitary if P*P = I, or equivalently P* = P^{-1} (Artin, (8.3.13), p. 245). P is unitary if and only if its columns are orthonormal with respect to the standard Hermitian form: P*_i P_i = 1 and P*_i P_j = 0 for i != j. A change of basis in C^n preserves the standard Hermitian form X* Y if and only if the change-of-basis matrix is unitary.

# Prerequisites

- **Hermitian form** — Unitary matrices preserve the standard Hermitian form

# Key Properties

1. P*P = I (equivalently P* = P^{-1})
2. Columns are orthonormal with respect to the standard Hermitian form
3. Eigenvalues have absolute value 1
4. |det P| = 1
5. Preserves the standard Hermitian form: (PX)*(PY) = X*Y
6. The set of unitary matrices forms a group (the unitary group U_n)

# Construction / Recognition

## To Construct:
1. Choose n orthonormal vectors in C^n (with respect to X*Y)
2. Use them as columns of P

## To Recognize:
1. Check P*P = I
2. Or check that columns are orthonormal under X*Y

# Context & Application

Unitary matrices are the complex analogue of orthogonal matrices. They play a central role in the spectral theorem (diagonalizing normal, Hermitian, and unitary matrices), quantum mechanics, and representation theory. Every finite subgroup of GL_n is conjugate to a subgroup of U_n.

# Examples

**Example 1** (p. 245): The matrix (1/sqrt(2)) [[1, 1],[i, -i]] is unitary.

# Relationships

## Builds Upon
- **Hermitian form** — Unitary matrices preserve it

## Enables
- **Unitary group** — The group of all unitary matrices
- **Spectral theorem** — Uses unitary matrices for diagonalization

## Contrasts With
- **Orthogonal matrix** — The real analogue; satisfies P^t P = I instead of P*P = I

# Common Errors

- **Error**: Using P^t instead of P* for the unitarity condition
  **Correction**: For complex matrices, use the conjugate transpose P*, not just the transpose

# Common Confusions

- **Confusion**: Thinking every unitary matrix is orthogonal
  **Clarification**: A real unitary matrix is orthogonal, but complex unitary matrices involve conjugation

# Source Reference

Chapter 8: Bilinear Forms, Section 8.3, pages 245-246.

# Verification Notes

- Definition source: Direct from (8.3.13), p. 245
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
