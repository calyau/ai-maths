---
# === CORE IDENTIFICATION ===
concept: Orthogonal Basis
slug: orthogonal-basis

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
section: "8.4 Orthogonality"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonality-bilinear-forms
extends: []
related:
  - orthonormal-basis
  - signature
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Does every symmetric form have an orthogonal basis?"
---

# Quick Definition

An orthogonal basis B = (v_1, ..., v_n) is a basis whose vectors are mutually orthogonal: (v_i, v_j) = 0 for i != j. The matrix of the form with respect to an orthogonal basis is diagonal.

# Core Definition

An orthogonal basis B = (v_1, ..., v_n) of V is a basis whose vectors are mutually orthogonal: (v_i, v_j) = 0 for all i != j (Artin, p. 248). Theorem 8.4.10 states that every symmetric or Hermitian form on a finite-dimensional vector space has an orthogonal basis. Orthogonal bases do NOT exist for skew-symmetric forms.

# Prerequisites

- **Orthogonality (bilinear forms)** — Orthogonal basis requires mutual orthogonality

# Key Properties

1. (v_i, v_j) = 0 for i != j
2. The matrix of the form is diagonal: diag((v_1,v_1), ..., (v_n,v_n))
3. Exists for every symmetric or Hermitian form (Theorem 8.4.10)
4. Does NOT exist for skew-symmetric forms
5. The form is nondegenerate iff all diagonal entries are nonzero
6. Can be scaled to make diagonal entries 1, -1, or 0 (Corollary 8.4.15)

# Construction / Recognition

## To Construct:
1. If the form is not identically zero, find v_1 with (v_1, v_1) != 0 (Lemma 8.4.9)
2. Decompose V = span(v_1) direct-sum span(v_1)^perp
3. Recurse on the orthogonal complement

## To Recognize:
1. Check that the matrix of the form with respect to the basis is diagonal

# Context & Application

Orthogonal bases reduce a form to its simplest diagonal shape, revealing the signature and enabling classification. This is the first step in classifying conics and quadrics and in proving the spectral theorem.

# Examples

**Example 1** (p. 252): In R^3 with the form whose matrix has entries, the vectors (1,1,1)^t, (1,-1,0)^t, (1,1,-2)^t form an orthogonal basis with respect to dot product.

# Relationships

## Builds Upon
- **Orthogonality (bilinear forms)** — Mutual orthogonality of basis vectors

## Enables
- **Signature** — Determined by the diagonal entries in an orthogonal basis
- **Sylvester's law of inertia** — The number of positive, negative, and zero diagonal entries is invariant

## Related
- **Orthonormal basis** — An orthogonal basis with (v_i, v_i) = 1 for all i

# Common Errors

- **Error**: Trying to find an orthogonal basis for a skew-symmetric form
  **Correction**: In skew-symmetric forms, every vector is self-orthogonal, so orthogonal bases cannot exist

# Common Confusions

- **Confusion**: Confusing orthogonal basis with orthonormal basis
  **Clarification**: Orthogonal means (v_i, v_j) = 0 for i != j. Orthonormal additionally requires (v_i, v_i) = 1. Orthonormal bases only exist for positive definite forms.

# Source Reference

Chapter 8: Bilinear Forms, Section 8.4, pages 248, 250-251. Theorem 8.4.10.

# Verification Notes

- Definition source: Direct from p. 248 and Theorem 8.4.10
- Confidence rationale: Explicitly defined with existence theorem
- Uncertainties: None
- Cross-reference status: Verified
