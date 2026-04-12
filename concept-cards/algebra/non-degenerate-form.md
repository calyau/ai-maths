---
# === CORE IDENTIFICATION ===
concept: Non-degenerate Form
slug: non-degenerate-form

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
  - "nondegenerate form"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bilinear-form
  - nullspace-of-a-form
extends: []
related:
  - orthogonal-complement
  - positive-definite-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does it mean for a form to be nondegenerate?"
---

# Quick Definition

A symmetric or Hermitian form is nondegenerate if its nullspace is {0}, meaning for every nonzero vector v there exists a vector v' with (v, v') != 0. Equivalently, the matrix of the form is invertible.

# Core Definition

The form on V is nondegenerate if its nullspace is the zero space {0}, meaning that for every nonzero vector v, there is a vector v' such that (v, v') != 0 (Artin, p. 248). A form that is not nondegenerate is degenerate. By Proposition 8.4.4, the form is nondegenerate if and only if the matrix A is invertible.

# Prerequisites

- **Bilinear form** — Nondegeneracy is a property of forms
- **Nullspace of a form** — Nondegeneracy means the nullspace is trivial

# Key Properties

1. Nullspace N = {0}
2. Equivalent to: the matrix of the form is invertible (Proposition 8.4.4)
3. Implies V = W direct-sum W^perp for any subspace W on which the form is also nondegenerate
4. Positive definite forms are always nondegenerate
5. The equality criterion: if (v, w) = (v', w) for all w, then v = v' (Proposition 8.4.3)

# Construction / Recognition

## To Recognize:
1. Check that the matrix A is invertible (det A != 0)
2. Or check that the equation AY = 0 has only the trivial solution

# Context & Application

Nondegeneracy is the key condition ensuring that orthogonal complements behave well. Most interesting forms (dot product, Lorentz form, symplectic forms) are nondegenerate. Degeneracy indicates redundancy in the form.

# Examples

**Example 1** (p. 248): Dot product on R^n is nondegenerate (matrix I is invertible).

**Example 2** (p. 248): The Lorentz form is nondegenerate (matrix diag(1,1,1,-1) is invertible).

# Relationships

## Builds Upon
- **Nullspace of a form** — Nondegeneracy means nullspace = {0}

## Enables
- **Orthogonal complement** — Orthogonal decomposition V = W + W^perp requires nondegeneracy
- **Orthogonal projection** — Exists when the form is nondegenerate on a subspace

## Related
- **Positive definite form** — Always nondegenerate

# Common Errors

- **Error**: Assuming nondegeneracy on V implies nondegeneracy on every subspace
  **Correction**: The form may be degenerate on a subspace even when nondegenerate on V

# Common Confusions

- **Confusion**: Confusing nondegenerate with positive definite
  **Clarification**: Positive definite implies nondegenerate, but not conversely — the Lorentz form is nondegenerate but indefinite

# Source Reference

Chapter 8: Bilinear Forms, Section 8.4, pages 248-249. Proposition 8.4.4.

# Verification Notes

- Definition source: Direct from p. 248
- Confidence rationale: Explicitly defined with equivalent conditions
- Uncertainties: None
- Cross-reference status: Verified
