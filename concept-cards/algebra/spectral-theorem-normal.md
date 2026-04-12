---
# === CORE IDENTIFICATION ===
concept: Spectral Theorem for Normal Operators
slug: spectral-theorem-normal

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
section: "8.6 The Spectral Theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "spectral theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - normal-operator
  - hermitian-space
extends: []
related:
  - spectral-theorem-hermitian
  - spectral-theorem-symmetric
  - spectral-theorem-unitary
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the spectral theorem?"
---

# Quick Definition

The Spectral Theorem for normal operators states that every normal operator on a Hermitian space has an orthonormal basis of eigenvectors. In matrix form: every normal matrix can be diagonalized by a unitary matrix.

# Core Definition

Theorem 8.6.6 (Spectral Theorem for Normal Operators): (a) Let T be a normal operator on a Hermitian space V. There is an orthonormal basis of V consisting of eigenvectors for T. (b) Matrix form: Let A be a normal matrix. There is a unitary matrix P such that P*AP is diagonal (Artin, p. 259).

# Prerequisites

- **Normal operator** — The operator must commute with its adjoint
- **Hermitian space** — The form must be positive definite (used crucially in the proof)

# Key Properties

1. Applies to ALL normal operators (including Hermitian and unitary as special cases)
2. The eigenvectors can be chosen orthonormal
3. The diagonalizing matrix P is unitary
4. The proof relies on: (i) eigenvectors of T are also eigenvectors of T* (Theorem 8.6.5), (ii) eigenspaces are T*-invariant, hence their orthogonal complements are T-invariant
5. Positive definiteness of the form is essential (used in Theorem 8.6.5)

# Construction / Recognition

## To Apply:
1. Verify the operator/matrix is normal (A*A = AA*)
2. Find eigenvalues
3. Find orthonormal eigenvectors (eigenvectors for distinct eigenvalues are automatically orthogonal)
4. Assemble into a unitary diagonalizing matrix P

# Context & Application

The Spectral Theorem is one of the most powerful tools in linear algebra. It is the basis for principal component analysis, quantum mechanics, and the classification of quadratic forms. As Artin notes: "When faced with a Hermitian operator or matrix, it should be an automatic response to apply that theorem" (p. 260).

# Examples

**Example 1** (p. 260): The Hermitian matrix M = [[2, i],[-i, 2]] has eigenvectors v_1 = (1, -i)^t and v_2 = (1, i)^t with eigenvalues 3 and 1. Normalizing and forming P = (1/sqrt(2))[[1,1],[-i,i]], we get P*MP = diag(3, 1).

# Relationships

## Builds Upon
- **Normal operator** — The hypothesis of the theorem
- **Hermitian space** — Provides the positive definite form

## Enables
- **Classification of conics** — Via diagonalizing the quadratic form
- **Principal axis theorem** — The spectral theorem applied to quadratic forms

## Related
- **Spectral theorem for Hermitian operators** — The special case when T* = T
- **Spectral theorem for unitary matrices** — The special case when T*T = I
- **Spectral theorem for symmetric operators** — The real analogue

# Common Errors

- **Error**: Applying the spectral theorem to a non-normal matrix
  **Correction**: The matrix must satisfy A*A = AA*; otherwise there may be no orthonormal eigenbasis

# Common Confusions

- **Confusion**: Thinking the spectral theorem says every matrix is diagonalizable
  **Clarification**: Only normal matrices are guaranteed to be diagonalizable by a unitary matrix

# Source Reference

Chapter 8: Bilinear Forms, Section 8.6, Theorem 8.6.6, pages 259-260.

# Verification Notes

- Definition source: Direct from Theorem 8.6.6
- Confidence rationale: Major theorem, fully stated and proved
- Uncertainties: None
- Cross-reference status: Verified
