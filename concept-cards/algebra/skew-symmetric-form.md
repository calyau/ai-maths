---
# === CORE IDENTIFICATION ===
concept: Skew-Symmetric Form
slug: skew-symmetric-form

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
aliases:
  - "antisymmetric form"
  - "alternating form"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - bilinear-form
extends:
  - bilinear-form
related:
  - symplectic-form
  - symplectic-group
contrasts_with:
  - symmetric-bilinear-form

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a skew-symmetric form?"
  - "How do skew-symmetric forms differ from symmetric forms?"
---

# Quick Definition

A skew-symmetric bilinear form satisfies (v, v) = 0 for all v, or equivalently (u, v) = -(v, u) for all u, v. Every nondegenerate skew-symmetric form exists only in even dimension and can be put in a standard block-diagonal form.

# Core Definition

A bilinear form ( , ) on a vector space V is skew-symmetric if (v, v) = 0 for all v in V (8.8.1), or equivalently (u, v) = -(v, u) for all u and v in V (8.8.2). These conditions are equivalent when the field has characteristic different from 2 (Artin, p. 261). The matrix of a skew-symmetric form satisfies a_ij = -a_ji and a_ii = 0.

# Prerequisites

- **Bilinear form** — A skew-symmetric form is a special type of bilinear form

# Key Properties

1. (v, v) = 0 for all v — every vector is self-orthogonal
2. (u, v) = -(v, u) for all u, v
3. No orthogonal bases exist (since every vector is self-orthogonal)
4. If nondegenerate, the dimension must be even (Corollary 8.8.8)
5. Any nondegenerate skew-symmetric form can be put in block form with 2x2 blocks [[0,1],[-1,0]] (Theorem 8.8.7)

# Construction / Recognition

## To Construct:
1. Choose a vector space of even dimension 2n
2. Use the standard skew-symmetric matrix S = [[0, I],[-I, 0]]
3. Define (X, Y) = X^t S Y

## To Recognize:
1. Check (v, v) = 0 for all v
2. Or check the matrix satisfies A^t = -A

# Context & Application

Skew-symmetric forms arise in symplectic geometry, Hamiltonian mechanics, and algebraic topology (intersection numbers on surfaces). The determinant form on R^2, (X, Y) = x_1 y_2 - x_2 y_1, is the simplest example. Artin also connects these forms to counting oriented intersections of paths on surfaces (p. 261).

# Examples

**Example 1** (p. 261): The determinant form on R^2: (X, Y) = det[X | Y] = x_1 y_2 - x_2 y_1. Its matrix is [[0,1],[-1,0]].

**Example 2** (p. 261): Intersection numbers of paths on a surface: if path X crosses path Y from right, the contribution is +1; from left, -1. The total intersection number defines a skew-symmetric form on homology.

# Relationships

## Builds Upon
- **Bilinear form** — Skew-symmetric forms are bilinear forms with (v,v) = 0

## Enables
- **Symplectic form** — A nondegenerate skew-symmetric form
- **Symplectic group** — The group preserving a symplectic form

## Contrasts With
- **Symmetric bilinear form** — Has (v, w) = (w, v) rather than (v, w) = -(w, v)

# Common Errors

- **Error**: Looking for an orthogonal basis of a skew-symmetric form
  **Correction**: Every vector is self-orthogonal in a skew-symmetric form, so orthogonal bases cannot exist

# Common Confusions

- **Confusion**: Thinking nondegenerate skew-symmetric forms can exist in odd dimension
  **Clarification**: If A is an invertible skew-symmetric m x m matrix, then m must be even (Corollary 8.8.8)

# Source Reference

Chapter 8: Bilinear Forms, Section 8.8, pages 261-263. Also mentioned in Section 8.1, p. 241.

# Verification Notes

- Definition source: Direct from (8.8.1) and (8.8.2), p. 261
- Confidence rationale: Explicitly defined with full classification theorem
- Uncertainties: None
- Cross-reference status: Verified
