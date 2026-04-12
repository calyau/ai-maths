---
# === CORE IDENTIFICATION ===
concept: Unitary Operator
slug: unitary-operator

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - adjoint-operator
  - hermitian-space
extends:
  - normal-operator
related:
  - unitary-matrix
  - orthogonal-operator
  - spectral-theorem-unitary
contrasts_with:
  - self-adjoint-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a unitary operator?"
---

# Quick Definition

A unitary operator T on a Hermitian space preserves the Hermitian form: (Tv, Tw) = (v, w) for all v and w. Equivalently T*T = I. Unitary operators are the complex analogue of orthogonal operators.

# Core Definition

A linear operator T on a Hermitian space V is unitary if T*T = I (Artin, p. 258). By Proposition 8.6.3(d), T is unitary if and only if (Tv, Tw) = (v, w) for all v and w. A unitary operator preserves lengths and angles. Every unitary matrix is normal, and the Spectral Theorem guarantees it is diagonalizable by a unitary matrix.

# Prerequisites

- **Adjoint operator** — Unitarity is T*T = I
- **Hermitian space** — Provides the form to be preserved

# Key Properties

1. T*T = I (equivalently T* = T^{-1})
2. (Tv, Tw) = (v, w) for all v, w — preserves the form
3. Eigenvalues have absolute value 1
4. Is a normal operator (T*T = I = TT*)
5. Diagonalizable by a unitary matrix (Spectral Theorem)

# Construction / Recognition

## To Recognize:
1. Check T*T = I
2. Or verify (Tv, Tw) = (v, w) for all v, w

# Context & Application

Unitary operators represent symmetries that preserve the geometry of a Hermitian space. They are fundamental to quantum mechanics (time evolution), signal processing (discrete Fourier transform), and representation theory.

# Examples

**Example 1** (p. 258): A unitary matrix P is the matrix of a unitary operator with respect to an orthonormal basis.

# Relationships

## Builds Upon
- **Adjoint operator** — Unitarity is T* = T^{-1}

## Enables
- **Spectral theorem for unitary matrices** — Unitary matrices are diagonalizable

## Related
- **Orthogonal operator** — The real analogue (preserves dot product)

## Contrasts With
- **Self-adjoint operator** — T* = T rather than T* = T^{-1}

# Common Errors

- **Error**: Assuming unitary operators have real eigenvalues
  **Correction**: Eigenvalues of unitary operators have absolute value 1 but are generally complex

# Common Confusions

- **Confusion**: Confusing unitary (T*T = I) with Hermitian (T* = T)
  **Clarification**: The only matrices that are both unitary and Hermitian have eigenvalues +/- 1

# Source Reference

Chapter 8: Bilinear Forms, Section 8.6, pages 258-259.

# Verification Notes

- Definition source: Direct from p. 258
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
