---
# === CORE IDENTIFICATION ===
concept: Bilinear Form
slug: bilinear-form

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
  - dot-product
extends: []
related:
  - symmetric-bilinear-form
  - hermitian-form
  - skew-symmetric-form
  - matrix-of-a-bilinear-form
contrasts_with:
  - hermitian-form

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a bilinear form?"
  - "How do bilinear forms relate to inner products?"
---

# Quick Definition

A bilinear form on a real vector space V is a real-valued function of two vector variables that is linear in each variable separately. The dot product on R^n is the most familiar example.

# Core Definition

Let V be a real vector space. A bilinear form on V is a map V x V -> R, denoted (v, w), that is linear in each variable: (rv_1, w_1) = r(v_1, w_1) and (v_1 + v_2, w_1) = (v_1, w_1) + (v_2, w_1), and similarly in the second variable (Artin, p. 240). Equivalently, the form is compatible with linear combinations: (sum x_i v_i, w) = sum x_i (v_i, w) and (v, sum w_j y_j) = sum (v, w_j) y_j.

# Prerequisites

- **Dot product** — The dot product is the prototypical bilinear form; bilinear forms generalize it
- **Vector space** — Bilinear forms are defined on vector spaces
- **Linear map** — Bilinearity means linearity in each variable separately

# Key Properties

1. Linear in the first variable: (rv_1, w) = r(v_1, w) and (v_1 + v_2, w) = (v_1, w) + (v_2, w)
2. Linear in the second variable: (v, rw_1) = r(v, w_1) and (v, w_1 + w_2) = (v, w_1) + (v, w_2)
3. On R^n, every bilinear form has the form (X, Y) = X^t A Y for some n x n matrix A
4. The matrix of a bilinear form transforms as A' = P^t A P under change of basis B' = BP
5. The theory of bilinear forms is NOT equivalent to the theory of linear operators, despite both being described by matrices — the change-of-basis rules differ

# Construction / Recognition

## To Construct:
1. Choose a basis B = (v_1, ..., v_n) for V
2. Define an n x n matrix A = (a_ij) where a_ij = (v_i, v_j)
3. The form is then (v, w) = X^t A Y where X, Y are coordinate vectors

## To Recognize:
1. A function of two vector variables that produces a scalar
2. Check linearity in each variable separately
3. Verify it can be expressed as X^t A Y for some matrix A

# Context & Application

Bilinear forms are central to geometry and linear algebra. They generalize the dot product to allow non-standard notions of length, angle, and orthogonality. The Lorentz form in special relativity is a key example of an indefinite bilinear form. Artin's Chapter 8 develops bilinear forms as a bridge between linear algebra and geometry.

# Examples

**Example 1** (p. 240): The dot product (X . Y) = X^t I Y on R^n is the bilinear form with matrix A = I (the identity).

**Example 2** (p. 241): The form (X, Y) = X^t A Y for any n x n matrix A is a bilinear form on R^n.

# Relationships

## Builds Upon
- **Dot product** — The dot product is the special case A = I

## Enables
- **Symmetric bilinear form** — A bilinear form with (v, w) = (w, v)
- **Skew-symmetric form** — A bilinear form with (v, w) = -(w, v)
- **Matrix of a bilinear form** — The matrix representation of a bilinear form

## Related
- **Hermitian form** — The complex analogue, conjugate-linear in first variable

## Contrasts With
- **Hermitian form** — Hermitian forms are conjugate-linear in the first variable, not linear

# Common Errors

- **Error**: Assuming bilinear forms transform like linear operators under change of basis (P^{-1}AP)
  **Correction**: Bilinear forms transform as A' = P^t A P, not P^{-1}AP (Artin, p. 242)

# Common Confusions

- **Confusion**: Thinking the theory of bilinear forms and linear operators are equivalent because both use matrices
  **Clarification**: The change-of-basis rules differ: P^t A P for forms vs P^{-1}AP for operators. The resulting matrices are generally different (Artin, p. 242).

# Source Reference

Chapter 8: Bilinear Forms, Section 8.1, pages 240-242.

# Verification Notes

- Definition source: Direct from (8.1.1) and (8.1.2), p. 240
- Confidence rationale: Explicitly defined with clear formulas and examples
- Uncertainties: None
- Cross-reference status: Verified against planned extractions
