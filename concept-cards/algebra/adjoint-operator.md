---
# === CORE IDENTIFICATION ===
concept: Adjoint Operator
slug: adjoint-operator

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
  - "adjoint"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - hermitian-space
extends: []
related:
  - self-adjoint-operator
  - normal-operator
  - unitary-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the adjoint of a linear operator?"
---

# Quick Definition

The adjoint operator T* of a linear operator T on a Hermitian space is the operator whose matrix with respect to an orthonormal basis is the conjugate transpose A* of T's matrix. It satisfies (Tv, w) = (v, T*w).

# Core Definition

Let T: V -> V be a linear operator on a Hermitian space V, and let A be the matrix of T with respect to an orthonormal basis B. The adjoint operator T*: V -> V is the operator whose matrix with respect to B is A* (the conjugate transpose). The definition is independent of the choice of orthonormal basis (Artin, p. 257). The key property is (Tv, w) = (v, T*w) and (v, Tw) = (T*v, w) (Proposition 8.6.3(a)).

# Prerequisites

- **Hermitian space** — The adjoint is defined on Hermitian spaces using orthonormal bases

# Key Properties

1. (Tv, w) = (v, T*w) for all v, w (Proposition 8.6.3(a))
2. (T+U)* = T* + U*, (TU)* = U*T*, T** = T (8.6.1)
3. Independent of the choice of orthonormal basis
4. T is Hermitian iff T* = T
5. T is unitary iff T*T = I
6. T is normal iff T*T = TT*

# Construction / Recognition

## To Construct:
1. Choose an orthonormal basis
2. Write T as a matrix A
3. T* has matrix A* (conjugate transpose)

## To Recognize:
1. The unique operator satisfying (Tv, w) = (v, T*w)

# Context & Application

The adjoint is the key ingredient in the spectral theorem. The condition T* = T (self-adjoint/Hermitian) or T*T = TT* (normal) determines which operators can be diagonalized by unitary transformations. The adjoint also appears in quantum mechanics as the relationship between observables and their adjoints.

# Examples

**Example 1** (p. 257): If A = [[2, i],[-i, 2]], then A* = A, so the operator is Hermitian (self-adjoint).

# Relationships

## Builds Upon
- **Hermitian space** — Provides the setting

## Enables
- **Self-adjoint operator** — T* = T
- **Normal operator** — T*T = TT*
- **Unitary operator** — T*T = I

# Common Errors

- **Error**: Computing the adjoint with respect to a non-orthonormal basis
  **Correction**: The formula T* has matrix A* only works for orthonormal bases

# Common Confusions

- **Confusion**: Confusing the adjoint with the transpose
  **Clarification**: The adjoint is the conjugate transpose, not just the transpose (for complex matrices)

# Source Reference

Chapter 8: Bilinear Forms, Section 8.6, pages 257-258. Proposition 8.6.3.

# Verification Notes

- Definition source: Direct from p. 257
- Confidence rationale: Explicitly defined with key properties proved
- Uncertainties: None
- Cross-reference status: Verified
