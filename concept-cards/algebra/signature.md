---
# === CORE IDENTIFICATION ===
concept: Signature
slug: signature

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
aliases:
  - "signature of a form"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonal-basis
  - non-degenerate-form
extends: []
related:
  - sylvesters-law-of-inertia
  - positive-definite-form
  - indefinite-form
  - lorentz-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the signature of a bilinear form?"
---

# Quick Definition

The signature of a nondegenerate symmetric form is the pair (p, m) where p is the number of positive and m the number of negative diagonal entries when the form is written in diagonal form with entries 1, -1.

# Core Definition

Let ( , ) be a nondegenerate symmetric or Hermitian form. Using an orthogonal basis scaled so that diagonal entries are 1 or -1 (Corollary 8.4.15), the matrix becomes I_{p,m} = diag(1,...,1,-1,...,-1) with p ones and m minus-ones. The pair (p, m) is the signature of the form. By Sylvester's Law, the signature is independent of the choice of orthogonal basis (Artin, p. 254).

# Prerequisites

- **Orthogonal basis** — Needed to diagonalize the form
- **Non-degenerate form** — Signature is defined for nondegenerate forms

# Key Properties

1. p + m = n (the dimension of V) for nondegenerate forms
2. The form is positive definite iff signature is (n, 0)
3. The form is negative definite iff signature is (0, n)
4. The form is indefinite iff both p > 0 and m > 0
5. Sylvester's Law: the signature is invariant under change of basis
6. The notation I_{p,m} denotes the diagonal matrix diag(I_p, -I_m)

# Construction / Recognition

## To Construct:
1. Find an orthogonal basis
2. Count positive and negative values of (v_i, v_i)

## To Recognize:
1. Diagonalize the matrix and count positive and negative eigenvalues

# Context & Application

The signature completely classifies nondegenerate symmetric forms up to change of basis. The Lorentz form has signature (3,1). Signature determines the type of conic or quadric in the classification.

# Examples

**Example 1** (p. 254): Dot product on R^n has signature (n, 0).

**Example 2** (p. 242): The Lorentz form on R^4 has signature (3, 1).

# Relationships

## Builds Upon
- **Orthogonal basis** — Signature is computed from the diagonal form

## Enables
- **Classification of conics** — The type of conic depends on the signature of the associated form

## Related
- **Sylvester's law of inertia** — Proves the signature is well-defined
- **Positive definite form** — Signature (n, 0)
- **Indefinite form** — Signature (p, m) with both p, m > 0

# Common Errors

- **Error**: Computing signature from the matrix entries directly without diagonalizing
  **Correction**: Signature is determined by eigenvalue signs, not by the entries of a non-diagonal matrix

# Common Confusions

- **Confusion**: Thinking signature depends on the choice of basis
  **Clarification**: Sylvester's Law guarantees the signature is invariant

# Source Reference

Chapter 8: Bilinear Forms, Section 8.4, pages 253-254. Corollary 8.4.15, (8.4.16), (8.4.17).

# Verification Notes

- Definition source: Direct from (8.4.16) and (8.4.17), p. 254
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
