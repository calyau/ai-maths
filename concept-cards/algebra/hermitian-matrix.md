---
# === CORE IDENTIFICATION ===
concept: Hermitian Matrix
slug: hermitian-matrix

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
aliases:
  - "self-adjoint matrix"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - hermitian-form
extends: []
related:
  - unitary-matrix
  - normal-matrix
  - spectral-theorem-hermitian
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Hermitian matrix?"
  - "Why are eigenvalues of a Hermitian matrix real?"
---

# Quick Definition

A square complex matrix A is Hermitian (or self-adjoint) if A* = A, where A* is the conjugate transpose. Hermitian matrices have real eigenvalues and can be diagonalized by a unitary matrix.

# Core Definition

A square matrix A is Hermitian if A* = A, i.e., the conjugate transpose equals the matrix itself (Artin, (8.3.6), p. 244). The entries satisfy a_ij = conjugate(a_ji), so diagonal entries are real and off-diagonal entries come in conjugate pairs. A real matrix is Hermitian if and only if it is symmetric.

# Prerequisites

- **Hermitian form** — Hermitian matrices arise as matrices of Hermitian forms

# Key Properties

1. A* = A (the matrix equals its conjugate transpose)
2. Diagonal entries are real; a_ij = conjugate(a_ji)
3. Eigenvalues are real (Theorem 8.3.11)
4. Trace and determinant are real
5. Can be diagonalized by a unitary matrix (Spectral Theorem 8.6.7)
6. A real symmetric matrix is a special case

# Construction / Recognition

## To Construct:
1. Choose real diagonal entries and complex off-diagonal entries with a_ij = conjugate(a_ji)

## To Recognize:
1. Check A* = A
2. Or check: diagonal entries are real and a_ij = conjugate(a_ji)

# Context & Application

Hermitian matrices are central to quantum mechanics (observables are Hermitian operators), the spectral theorem, and the theory of positive definite forms. Their real eigenvalues and orthogonal eigenvectors make them the best-behaved class of complex matrices.

# Examples

**Example 1** (p. 244): The matrix [[2, i],[-i, 3]] is Hermitian.

**Example 2** (p. 244): Every real symmetric matrix is Hermitian when viewed as a complex matrix.

# Relationships

## Builds Upon
- **Hermitian form** — A Hermitian matrix is the matrix of a Hermitian form

## Enables
- **Spectral theorem for Hermitian operators** — Hermitian matrices are diagonalizable by unitary matrices

## Related
- **Unitary matrix** — Preserves the Hermitian form; used to diagonalize Hermitian matrices
- **Normal matrix** — Hermitian matrices are a special case of normal matrices

# Common Errors

- **Error**: Expecting complex eigenvalues from a Hermitian matrix
  **Correction**: All eigenvalues of a Hermitian matrix are real (Theorem 8.3.11)

# Common Confusions

- **Confusion**: Confusing Hermitian (A* = A) with unitary (A* = A^{-1})
  **Clarification**: Hermitian means self-adjoint; unitary means the adjoint is the inverse. A matrix cannot be both unless it has eigenvalues +/- 1.

# Source Reference

Chapter 8: Bilinear Forms, Section 8.3, pages 244-246. Theorem 8.3.11 (real eigenvalues).

# Verification Notes

- Definition source: Direct from (8.3.6), p. 244
- Confidence rationale: Explicitly defined with examples and key theorem
- Uncertainties: None
- Cross-reference status: Verified
