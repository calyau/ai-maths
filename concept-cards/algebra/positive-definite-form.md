---
# === CORE IDENTIFICATION ===
concept: Positive Definite Form
slug: positive-definite-form

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
section: "8.2 Symmetric Forms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "positive definite"
  - "positive definite bilinear form"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - symmetric-bilinear-form
  - hermitian-form
extends:
  - symmetric-bilinear-form
related:
  - orthonormal-basis
  - euclidean-space
  - hermitian-space
contrasts_with:
  - indefinite-form
  - negative-definite-form

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a positive definite form?"
  - "When does an orthonormal basis exist?"
---

# Quick Definition

A symmetric or Hermitian form is positive definite if (v, v) > 0 for every nonzero vector v. Positive definite forms provide the notions of length and angle in a vector space.

# Core Definition

A symmetric form on a real vector space is positive definite if (v, v) > 0 for all nonzero vectors v. Similarly, a Hermitian form is positive definite if (v, v) > 0 for all nonzero v. A symmetric real matrix A is positive definite if X^t A X > 0 for all nonzero column vectors X (Artin, p. 242). Theorem 8.2.5 states that a real matrix A is positive definite and symmetric if and only if there exists an invertible P with A = P^t P, if and only if the form X^t A Y represents dot product with respect to some basis.

# Prerequisites

- **Symmetric bilinear form** — Positive definiteness is a property of symmetric (or Hermitian) forms
- **Hermitian form** — The complex case

# Key Properties

1. (v, v) > 0 for all nonzero v
2. Equivalent to: matrix A can be written as P^t P for invertible P (Theorem 8.2.5)
3. Equivalent to: all leading principal minors have positive determinant (Theorem 8.4.19)
4. Equivalent to: all eigenvalues are positive (for symmetric matrices)
5. Implies nondegeneracy — the nullspace is {0}
6. Orthonormal bases exist if and only if the form is positive definite

# Construction / Recognition

## To Construct:
1. Take any invertible matrix P and form A = P^t P — this is always positive definite
2. Or use the identity matrix (dot product)

## To Recognize:
1. Check det A_k > 0 for k = 1, ..., n where A_k is the k x k leading minor (Theorem 8.4.19)
2. Or compute eigenvalues and check all are positive

# Context & Application

Positive definite forms define the geometry of Euclidean and Hermitian spaces. They provide lengths, angles, and orthogonality. The Gram-Schmidt process requires positive definiteness. Most applications in geometry, physics, and statistics use positive definite forms.

# Examples

**Example 1** (p. 240): Dot product on R^n is positive definite: X^t X = x_1^2 + ... + x_n^2 > 0 for X != 0.

**Example 2** (p. 255): The matrix [[2, 1],[1, 1]] is positive definite because det[2] = 2 > 0 and det A = 1 > 0.

# Relationships

## Builds Upon
- **Symmetric bilinear form** — Positive definiteness is a property of symmetric forms

## Enables
- **Euclidean space** — A real vector space with a positive definite symmetric form
- **Hermitian space** — A complex vector space with a positive definite Hermitian form
- **Orthonormal basis** — Exists if and only if the form is positive definite
- **Gram-Schmidt process** — Requires positive definiteness

## Contrasts With
- **Indefinite form** — Has both positive and negative values of (v, v)
- **Negative definite form** — Has (v, v) < 0 for all nonzero v

# Common Errors

- **Error**: Checking only that diagonal entries of A are positive
  **Correction**: Must check all leading principal minors, or equivalently all eigenvalues

# Common Confusions

- **Confusion**: Thinking positive semi-definite and positive definite are the same
  **Clarification**: Positive semi-definite allows (v, v) = 0 for nonzero v; positive definite requires strict inequality

# Source Reference

Chapter 8: Bilinear Forms, Sections 8.2 and 8.4, pages 242-243, 254-256.

# Verification Notes

- Definition source: Direct from p. 242 and Theorem 8.2.5
- Confidence rationale: Explicitly defined with multiple equivalent characterizations
- Uncertainties: None
- Cross-reference status: Verified
