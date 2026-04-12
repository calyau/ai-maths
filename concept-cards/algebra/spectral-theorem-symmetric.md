---
# === CORE IDENTIFICATION ===
concept: Spectral Theorem for Symmetric Operators
slug: spectral-theorem-symmetric

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
  - "principal axis theorem"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - spectral-theorem-hermitian
  - euclidean-space
extends:
  - spectral-theorem-hermitian
related:
  - classification-of-conics
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the spectral theorem for real symmetric matrices?"
---

# Quick Definition

Every real symmetric matrix can be diagonalized by an orthogonal matrix: there exists orthogonal P such that P^t AP is a real diagonal matrix. Equivalently, every symmetric operator on a Euclidean space has an orthonormal basis of eigenvectors with real eigenvalues.

# Core Definition

Theorem 8.6.10: Let T be a symmetric operator on a Euclidean space V. (i) There is an orthonormal basis of V consisting of eigenvectors of T. (ii) The eigenvalues are real. Matrix form: Let A be a real symmetric matrix. There is an orthogonal matrix P such that P^t AP is a real diagonal matrix (Artin, p. 260).

# Prerequisites

- **Spectral theorem for Hermitian operators** — The real case follows the complex case
- **Euclidean space** — Provides the setting

# Key Properties

1. All eigenvalues are real (Corollary 8.3.12)
2. Eigenvectors can be chosen orthonormal
3. The diagonalizing matrix P is orthogonal (real)
4. P^t AP is a real diagonal matrix

# Construction / Recognition

## To Apply:
1. Verify A^t = A (symmetric)
2. Find eigenvalues (all real)
3. Find orthonormal eigenvectors
4. Assemble into orthogonal P

# Context & Application

This is the form of the spectral theorem used for classifying conics and quadrics, for the principal axis theorem in mechanics, and for principal component analysis in statistics.

# Examples

**Example 1** (p. 260): The matrix [[1,1],[1,-1]] is symmetric with eigenvalues +/- sqrt(2). It can be diagonalized by an orthogonal matrix.

# Relationships

## Builds Upon
- **Spectral theorem for Hermitian operators** — The real case is a corollary

## Enables
- **Classification of conics** — Diagonalizes the quadratic form
- **Classification of quadrics** — Extends to higher dimensions

# Common Errors

- **Error**: Trying to diagonalize a non-symmetric real matrix by an orthogonal matrix
  **Correction**: Only symmetric real matrices are guaranteed to be orthogonally diagonalizable

# Common Confusions

- **Confusion**: Thinking the spectral theorem for symmetric matrices is independent of the complex case
  **Clarification**: The proof relies on the result that eigenvalues of real symmetric matrices are real, which is proved by going to complex matrices (Corollary 8.3.12)

# Source Reference

Chapter 8: Bilinear Forms, Section 8.6, Theorem 8.6.10, page 260.

# Verification Notes

- Definition source: Direct from Theorem 8.6.10
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
