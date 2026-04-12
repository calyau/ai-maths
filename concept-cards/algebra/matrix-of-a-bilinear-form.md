---
# === CORE IDENTIFICATION ===
concept: Matrix of a Bilinear Form
slug: matrix-of-a-bilinear-form

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
section: "8.1 Bilinear Forms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bilinear-form
extends: []
related:
  - symmetric-bilinear-form
  - hermitian-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How is a bilinear form represented by a matrix?"
  - "How does the matrix of a bilinear form change under a change of basis?"
---

# Quick Definition

The matrix of a bilinear form with respect to a basis B = (v_1, ..., v_n) is the n x n matrix A = (a_ij) where a_ij = (v_i, v_j). The form is then computed as (v, w) = X^t A Y using coordinate vectors.

# Core Definition

Given a bilinear form ( , ) on a vector space V and a basis B = (v_1, ..., v_n), the matrix of the form is A = (a_ij) where a_ij = (v_i, v_j). If X and Y are the coordinate vectors of v and w respectively, then (v, w) = X^t A Y (Artin, Proposition 8.1.5, p. 241). Under a change of basis B' = BP, the matrix transforms as A' = P^t A P (Artin, Proposition 8.1.7, p. 241).

# Prerequisites

- **Bilinear form** — The form whose matrix is being computed
- **Change of basis** — Needed to understand how the matrix transforms

# Key Properties

1. Entries are a_ij = (v_i, v_j), the form applied to pairs of basis vectors
2. The form is recovered as (v, w) = X^t A Y
3. Under change of basis B' = BP, the matrix becomes A' = P^t A P
4. The matrices representing the same form are exactly P^t A P for invertible P (Corollary 8.1.8)
5. A symmetric form has a symmetric matrix; a skew-symmetric form has a skew-symmetric matrix

# Construction / Recognition

## To Construct:
1. Choose a basis B = (v_1, ..., v_n)
2. Compute a_ij = (v_i, v_j) for all i, j
3. Assemble into the matrix A = (a_ij)

## To Recognize:
1. An n x n matrix A such that (v, w) = X^t A Y for coordinate vectors X, Y

# Context & Application

The matrix representation reduces the study of bilinear forms to matrix algebra. The classification of forms up to change of basis becomes the problem of classifying matrices up to the equivalence A ~ P^t A P. This is distinct from the similarity equivalence P^{-1}AP used for linear operators.

# Examples

**Example 1** (p. 240): The matrix of dot product on R^n with respect to the standard basis is the identity matrix I.

**Example 2** (p. 241): The Lorentz form on R^4 has matrix diag(1, 1, 1, -1) with respect to the standard basis.

# Relationships

## Builds Upon
- **Bilinear form** — The form whose matrix representation this is

## Enables
- **Positive definite form** — Characterized by properties of its matrix
- **Signature** — Determined by the diagonal form of the matrix
- **Non-degenerate form** — Equivalent to the matrix being invertible

## Related
- **Symmetric bilinear form** — Has a symmetric matrix

# Common Errors

- **Error**: Using P^{-1}AP instead of P^t A P for change of basis
  **Correction**: For bilinear forms, the transformation rule is A' = P^t A P, not the similarity transformation used for linear operators

# Common Confusions

- **Confusion**: Thinking any symmetric matrix represents the same form regardless of basis
  **Clarification**: The matrix depends on the choice of basis; different bases yield congruent but generally different matrices

# Source Reference

Chapter 8: Bilinear Forms, Section 8.1, Propositions 8.1.5, 8.1.7, Corollary 8.1.8, pages 241-242.

# Verification Notes

- Definition source: Direct from (8.1.4) and Proposition 8.1.5
- Confidence rationale: Explicitly defined with proofs
- Uncertainties: None
- Cross-reference status: Verified
