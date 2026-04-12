---
# === CORE IDENTIFICATION ===
concept: Spectral Theorem for Unitary Matrices
slug: spectral-theorem-unitary

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
  - spectral-theorem-normal
  - unitary-matrix
extends:
  - spectral-theorem-normal
related:
  - unitary-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Can every unitary matrix be diagonalized?"
---

# Quick Definition

Every unitary matrix can be diagonalized by a unitary matrix. Equivalently, every conjugacy class in the unitary group U_n contains a diagonal matrix.

# Core Definition

Corollary 8.6.8: (a) Let A be a unitary matrix. There is a unitary matrix P such that P*AP is diagonal. (b) Every conjugacy class in U_n contains a diagonal matrix (Artin, p. 260).

# Prerequisites

- **Spectral theorem for normal operators** — Unitary matrices are normal
- **Unitary matrix** — The matrices to be diagonalized

# Key Properties

1. Every unitary matrix is diagonalizable by a unitary matrix
2. Eigenvalues have absolute value 1 (lie on the unit circle)
3. Every conjugacy class in U_n contains a diagonal matrix
4. The diagonal entries are the eigenvalues, which are roots of unity for finite-order matrices

# Construction / Recognition

## To Apply:
1. Verify A*A = I (unitary)
2. Find eigenvalues (on the unit circle)
3. Find orthonormal eigenvectors
4. Diagonalize

# Context & Application

This result is used to understand the structure of the unitary group and to classify unitary representations. It shows that conjugacy classes in U_n are determined by the multiset of eigenvalues.

# Examples

**Example 1** (p. 260): Any rotation matrix in SO_2 is unitary (when viewed as a complex 1x1 matrix) and is diagonalizable.

# Relationships

## Builds Upon
- **Spectral theorem for normal operators** — Unitary matrices are normal

## Related
- **Unitary group** — Conjugacy classes contain diagonal matrices

# Common Errors

- **Error**: Expecting real eigenvalues from a unitary matrix
  **Correction**: Eigenvalues of unitary matrices lie on the unit circle (|lambda| = 1) but are generally complex

# Common Confusions

- **Confusion**: Thinking unitary diagonalizability is the same as orthogonal diagonalizability
  **Clarification**: Unitary diagonalization uses complex matrices; orthogonal diagonalization (as in the symmetric spectral theorem) uses real matrices

# Source Reference

Chapter 8: Bilinear Forms, Section 8.6, Corollary 8.6.8, page 260.

# Verification Notes

- Definition source: Direct from Corollary 8.6.8
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
