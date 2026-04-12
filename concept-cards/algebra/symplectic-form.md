---
# === CORE IDENTIFICATION ===
concept: Symplectic Form
slug: symplectic-form

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
section: "8.8 Skew-Symmetric Forms"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - skew-symmetric-form
  - non-degenerate-form
extends:
  - skew-symmetric-form
related:
  - symplectic-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a symplectic form?"
---

# Quick Definition

A symplectic form is a nondegenerate skew-symmetric bilinear form. It exists only on even-dimensional spaces and can always be put in the standard block form S = [[0, I],[-I, 0]].

# Core Definition

A nondegenerate skew-symmetric bilinear form on a vector space V is called a symplectic form. By Theorem 8.8.7 and Corollary 8.8.8, the dimension of V must be even (2n), and there exists a basis in which the matrix of the form is S = [[0, I],[-I, 0]] where I is the n x n identity (Artin, (8.8.9), p. 263).

# Prerequisites

- **Skew-symmetric form** — A symplectic form is a nondegenerate one
- **Non-degenerate form** — The form must have trivial nullspace

# Key Properties

1. Skew-symmetric: (v, w) = -(w, v) and (v, v) = 0
2. Nondegenerate: the matrix is invertible
3. Dimension of V must be even
4. Standard form is S = [[0, I],[-I, 0]]
5. All nondegenerate skew-symmetric forms are equivalent (up to dimension)

# Construction / Recognition

## To Construct:
1. On R^{2n}, use the matrix S = [[0, I],[-I, 0]]

## To Recognize:
1. Check skew-symmetry (A^t = -A) and nondegeneracy (det A != 0)

# Context & Application

Symplectic forms are fundamental to Hamiltonian mechanics, symplectic geometry, and the theory of symplectic groups. They have a much simpler classification than symmetric forms — there is essentially one nondegenerate skew-symmetric form in each even dimension.

# Examples

**Example 1** (p. 261): The determinant form on R^2, (X, Y) = x_1 y_2 - x_2 y_1, with matrix [[0,1],[-1,0]].

# Relationships

## Builds Upon
- **Skew-symmetric form** — A symplectic form is nondegenerate and skew-symmetric

## Enables
- **Symplectic group** — The group preserving a symplectic form

# Common Errors

- **Error**: Trying to define a symplectic form on an odd-dimensional space
  **Correction**: Nondegenerate skew-symmetric forms only exist in even dimensions

# Common Confusions

- **Confusion**: Thinking symplectic forms have a rich classification like symmetric forms
  **Clarification**: Unlike symmetric forms (classified by signature), all nondegenerate skew-symmetric forms on a given space are equivalent

# Source Reference

Chapter 8: Bilinear Forms, Section 8.8, pages 261-263. Theorem 8.8.7, Corollary 8.8.8.

# Verification Notes

- Definition source: Synthesized from Section 8.8
- Confidence rationale: Implicit definition (nondegenerate skew-symmetric) with full classification
- Uncertainties: None
- Cross-reference status: Verified
