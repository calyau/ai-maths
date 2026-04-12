---
# === CORE IDENTIFICATION ===
concept: Normal Operator
slug: normal-operator

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
  - "normal matrix"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - adjoint-operator
extends: []
related:
  - self-adjoint-operator
  - unitary-operator
  - spectral-theorem-normal
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a normal operator?"
---

# Quick Definition

A normal matrix is a complex matrix that commutes with its adjoint: A*A = AA*. Normal matrices are exactly those that can be diagonalized by a unitary matrix. They include Hermitian and unitary matrices as special cases.

# Core Definition

A complex matrix A is normal if A*A = AA* (Artin, p. 258). A linear operator T on a Hermitian space is normal if T*T = TT*. The class of normal matrices includes Hermitian matrices (A* = A) and unitary matrices (A* = A^{-1}). The Spectral Theorem asserts that normal matrices are exactly those diagonalizable by a unitary matrix.

# Prerequisites

- **Adjoint operator** — Normality is defined in terms of commutativity with the adjoint

# Key Properties

1. A*A = AA*
2. If P is unitary and A is normal, then P*AP is normal (Lemma 8.6.2)
3. Hermitian matrices are normal (A* = A implies A*A = A^2 = AA*)
4. Unitary matrices are normal (A*A = I = AA*)
5. (Tv, Tw) = (T*v, T*w) for all v, w (Proposition 8.6.3(b))

# Construction / Recognition

## To Recognize:
1. Check A*A = AA*
2. Or check that A is diagonalizable by a unitary matrix

# Context & Application

The class of normal operators is the natural setting for the Spectral Theorem. It is the broadest class of operators on a Hermitian space that admits an orthonormal basis of eigenvectors.

# Examples

**Example 1** (p. 258): Any Hermitian matrix (A* = A) is normal.

**Example 2** (p. 258): Any unitary matrix (A* = A^{-1}) is normal.

# Relationships

## Builds Upon
- **Adjoint operator** — Normality is commutativity with the adjoint

## Enables
- **Spectral theorem for normal operators** — Normal operators have orthonormal eigenbases

## Related
- **Self-adjoint operator** — A special case (T* = T)
- **Unitary operator** — A special case (T*T = I)

# Common Errors

- **Error**: Assuming any diagonalizable matrix is normal
  **Correction**: A matrix can be diagonalizable (by a non-unitary matrix) without being normal

# Common Confusions

- **Confusion**: Thinking normal means diagonalizable
  **Clarification**: Normal means diagonalizable by a UNITARY matrix, which is a stronger condition than general diagonalizability

# Source Reference

Chapter 8: Bilinear Forms, Section 8.6, pages 258-259.

# Verification Notes

- Definition source: Direct from p. 258
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
