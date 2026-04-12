---
# === CORE IDENTIFICATION ===
concept: Spectral Theorem for Hermitian Operators
slug: spectral-theorem-hermitian

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
  - self-adjoint-operator
extends:
  - spectral-theorem-normal
related:
  - spectral-theorem-symmetric
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the spectral theorem for Hermitian operators?"
---

# Quick Definition

Every Hermitian operator on a Hermitian space has an orthonormal basis of eigenvectors with real eigenvalues. In matrix form: every Hermitian matrix A can be written as P*AP = D where P is unitary and D is a real diagonal matrix.

# Core Definition

Corollary 8.6.7: Let T be a Hermitian operator on a Hermitian space V. (i) There is an orthonormal basis of V consisting of eigenvectors of T. (ii) The eigenvalues of T are real. Matrix form: Let A be a Hermitian matrix. There is a unitary P such that P*AP is a real diagonal matrix (Artin, p. 260).

# Prerequisites

- **Spectral theorem for normal operators** — This is a corollary
- **Self-adjoint operator** — The operator must satisfy T* = T

# Key Properties

1. All eigenvalues are real
2. Eigenvectors can be chosen orthonormal
3. P*AP is a REAL diagonal matrix (stronger than general normal case)
4. The diagonalizing matrix P is unitary

# Construction / Recognition

## To Apply:
1. Verify A* = A
2. Find eigenvalues (they will be real)
3. Find orthonormal eigenvectors
4. Assemble into P

# Context & Application

This is the most commonly used form of the spectral theorem. It applies to quantum mechanical observables, principal axis theorems, and the classification of quadratic forms.

# Examples

**Example 1** (p. 260): M = [[2, i],[-i, 2]] is Hermitian. Eigenvalues are 3 and 1 (real). P = (1/sqrt(2))[[1,1],[-i,i]] gives P*MP = diag(3,1).

# Relationships

## Builds Upon
- **Spectral theorem for normal operators** — This is a special case

## Related
- **Spectral theorem for symmetric operators** — The real analogue

# Common Errors

- **Error**: Expecting complex eigenvalues from a Hermitian matrix
  **Correction**: Eigenvalues are always real for Hermitian matrices

# Common Confusions

- **Confusion**: Thinking a Hermitian matrix with repeated eigenvalues cannot be diagonalized
  **Clarification**: The spectral theorem guarantees diagonalizability even with repeated eigenvalues

# Source Reference

Chapter 8: Bilinear Forms, Section 8.6, Corollary 8.6.7, page 260.

# Verification Notes

- Definition source: Direct from Corollary 8.6.7
- Confidence rationale: Explicitly stated
- Uncertainties: None
- Cross-reference status: Verified
