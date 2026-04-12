---
# === CORE IDENTIFICATION ===
concept: Hermitian Form
slug: hermitian-form

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
  - "Hermitian inner product"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bilinear-form
extends: []
related:
  - hermitian-matrix
  - hermitian-space
  - unitary-matrix
  - positive-definite-form
contrasts_with:
  - symmetric-bilinear-form

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a Hermitian form?"
  - "How do bilinear forms relate to inner products?"
  - "What distinguishes a symmetric form from a Hermitian form?"
---

# Quick Definition

A Hermitian form on a complex vector space V is a map V x V -> C that is conjugate-linear in the first variable, linear in the second, and satisfies (w, v) = conjugate of (v, w). The value (v, v) is always real.

# Core Definition

A Hermitian form on a complex vector space V is a map V x V -> C, denoted (v, w), satisfying: (1) conjugate linearity in the first variable: (cv_1, w) = c-bar (v_1, w); (2) linearity in the second variable: (v, cw_1) = c(v, w_1); and (3) Hermitian symmetry: (w, v) = conjugate of (v, w) (Artin, (8.3.1), p. 243). The standard Hermitian form on C^n is (X, Y) = X* Y = x-bar_1 y_1 + ... + x-bar_n y_n.

# Prerequisites

- **Bilinear form** — Hermitian forms are the complex analogue
- **Complex conjugation** — Required for conjugate linearity

# Key Properties

1. (v, v) is always a real number (follows from Hermitian symmetry)
2. Conjugate-linear in the first variable, linear in the second
3. The matrix A of the form satisfies A* = A (Hermitian matrix)
4. Under change of basis B' = BP, the matrix transforms as A' = P* A P (not P^t A P)
5. The eigenvalues of a Hermitian matrix are real (Theorem 8.3.11)
6. A Hermitian form is positive definite if (v, v) > 0 for all nonzero v

# Construction / Recognition

## To Construct:
1. Choose a Hermitian matrix A (satisfying A* = A)
2. Define (X, Y) = X* A Y on C^n

## To Recognize:
1. Check (w, v) = conjugate of (v, w)
2. Check conjugate-linearity in the first variable
3. Or verify the matrix satisfies A* = A

# Context & Application

Hermitian forms are the natural inner products on complex vector spaces. They make (v, v) positive real, allowing definitions of length and orthogonality. The standard Hermitian form on C^n corresponds to X* Y, relating to dot product via the real-complex correspondence: (X, X) = a_1^2 + b_1^2 + ... + a_n^2 + b_n^2 where x_k = a_k + b_k i (Artin, p. 243).

# Examples

**Example 1** (p. 243): The standard Hermitian form on C^n: (X, Y) = X* Y = x-bar_1 y_1 + ... + x-bar_n y_n.

**Example 2** (p. 244): The matrix [[2, i], [-i, 3]] is Hermitian and defines a Hermitian form on C^2.

# Relationships

## Builds Upon
- **Bilinear form** — Hermitian forms are the complex counterpart

## Enables
- **Hermitian space** — A complex vector space with a positive definite Hermitian form
- **Unitary matrix** — Preserves the standard Hermitian form
- **Spectral theorem for Hermitian operators** — Requires Hermitian forms

## Related
- **Hermitian matrix** — The matrix of a Hermitian form
- **Positive definite form** — A Hermitian form with (v,v) > 0 for nonzero v

## Contrasts With
- **Symmetric bilinear form** — On real spaces, with (v,w) = (w,v) exactly (no conjugation)

# Common Errors

- **Error**: Using P^t A P instead of P* A P for change of basis
  **Correction**: For Hermitian forms, the change-of-basis formula is A' = P* A P (8.3.9)

# Common Confusions

- **Confusion**: Thinking that (X, Y) = X^t Y works on complex spaces
  **Clarification**: Using X^t Y without conjugation would not give (X, X) > 0 for nonzero X. The conjugation in X* Y ensures (X, X) is a positive real number.

# Source Reference

Chapter 8: Bilinear Forms, Section 8.3, pages 243-246.

# Verification Notes

- Definition source: Direct from (8.3.1), p. 243
- Confidence rationale: Explicitly and carefully defined
- Uncertainties: None
- Cross-reference status: Verified
