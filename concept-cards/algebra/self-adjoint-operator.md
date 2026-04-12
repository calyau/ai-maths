---
# === CORE IDENTIFICATION ===
concept: Self-Adjoint Operator
slug: self-adjoint-operator

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
  - "Hermitian operator"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - adjoint-operator
extends:
  - normal-operator
related:
  - hermitian-matrix
  - spectral-theorem-hermitian
contrasts_with:
  - unitary-operator

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a self-adjoint operator?"
---

# Quick Definition

A self-adjoint (or Hermitian) operator T on a Hermitian space satisfies T* = T. Equivalently, (Tv, w) = (v, Tw) for all v, w. Self-adjoint operators have real eigenvalues and are diagonalizable by a unitary matrix.

# Core Definition

A linear operator T on a Hermitian space V is Hermitian (or self-adjoint) if T* = T, equivalently if its matrix with respect to an orthonormal basis is Hermitian (Artin, p. 258). By Proposition 8.6.3(c), T is self-adjoint if and only if (Tv, w) = (v, Tw) for all v and w. On a Euclidean space, the analogue is a symmetric operator: T^t = T.

# Prerequisites

- **Adjoint operator** — Self-adjoint means T* = T

# Key Properties

1. T* = T
2. (Tv, w) = (v, Tw) for all v, w
3. All eigenvalues are real
4. Admits an orthonormal basis of eigenvectors (Spectral Theorem)
5. A special case of normal operator

# Construction / Recognition

## To Recognize:
1. Check the matrix is Hermitian (A* = A) with respect to an orthonormal basis
2. Or verify (Tv, w) = (v, Tw) for all v, w

# Context & Application

Self-adjoint operators are the most important class of operators in physics (quantum mechanics observables) and mathematics (the spectral theorem, principal axes of quadratic forms). They are the complex analogue of real symmetric operators.

# Examples

**Example 1** (p. 258): A matrix A = [[2, i],[-i, 3]] is Hermitian and defines a self-adjoint operator on C^2.

# Relationships

## Builds Upon
- **Adjoint operator** — Self-adjoint means equal to its adjoint

## Enables
- **Spectral theorem for Hermitian operators** — Self-adjoint operators are diagonalizable

## Contrasts With
- **Unitary operator** — Satisfies T*T = I instead of T* = T

# Common Errors

- **Error**: Expecting complex eigenvalues from a self-adjoint operator
  **Correction**: All eigenvalues are real

# Common Confusions

- **Confusion**: Confusing "self-adjoint" with "self-inverse"
  **Clarification**: Self-adjoint means T* = T; self-inverse (involution) means T^2 = I

# Source Reference

Chapter 8: Bilinear Forms, Section 8.6, pages 258-259.

# Verification Notes

- Definition source: Direct from p. 258
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
