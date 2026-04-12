---
# === CORE IDENTIFICATION ===
concept: Conic
slug: conic

# === CLASSIFICATION ===
category: bilinear-forms
subcategory: conics-quadrics
tier: intermediate

# === PROVENANCE ===
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Bilinear Forms"
chapter_number: 8
pdf_page: 240
section: "8.7 Conics and Quadrics"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "conic section"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - spectral-theorem-symmetric
  - symmetric-bilinear-form
extends: []
related:
  - quadric
  - quadratic-form
  - classification-of-conics
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a conic?"
  - "How are conics classified using bilinear forms?"
---

# Quick Definition

Conics are loci in R^2 defined by quadratic equations f(x_1, x_2) = 0. The nondegenerate conics are ellipses, hyperbolas, and parabolas. They are classified using the spectral theorem to diagonalize their quadratic parts.

# Core Definition

Ellipses, hyperbolas, and parabolas are called conics. They are loci in R^2 defined by quadratic equations f = 0, where f(x_1, x_2) = a_{11}x_1^2 + 2a_{12}x_1 x_2 + a_{22}x_2^2 + b_1 x_1 + b_2 x_2 + c (Artin, (8.7.1), p. 260). Written in matrix form as X^t A X + BX + c = 0, where A is the symmetric matrix of the quadratic part. Theorem 8.7.5 classifies all nondegenerate conics up to congruence.

# Prerequisites

- **Spectral theorem for symmetric operators** — Used to diagonalize the quadratic form
- **Symmetric bilinear form** — The matrix A is symmetric

# Key Properties

1. Every nondegenerate conic is congruent to one of: ellipse a_{11}x_1^2 + a_{22}x_2^2 - 1 = 0, hyperbola a_{11}x_1^2 - a_{22}x_2^2 - 1 = 0, or parabola a_{11}x_1^2 - a_{22}x_2 = 0
2. The type is determined by the signature of A: both eigenvalues same sign -> ellipse; opposite signs -> hyperbola; one eigenvalue zero -> parabola
3. Classification proceeds by: (1) orthogonal transformation to diagonalize A, then (2) translation to eliminate linear terms
4. The coefficients are determined by the congruence class

# Construction / Recognition

## To Classify:
1. Write f in matrix form X^t A X + BX + c = 0
2. Diagonalize A by an orthogonal transformation (spectral theorem)
3. Complete the square to eliminate linear terms
4. Identify the type from the resulting standard form

# Context & Application

The classification of conics is a classical application of the spectral theorem. It connects bilinear form theory to geometry. The same method extends to quadrics in three or more dimensions.

# Examples

**Example 1** (p. 261): The quadratic polynomial x_1^2 + 2x_1 x_2 - x_2^2 + 2x_1 + 2x_2 - 1 with A = [[1,1],[1,-1]]. Since A is indefinite, the conic is a hyperbola.

# Relationships

## Builds Upon
- **Spectral theorem for symmetric operators** — Diagonalizes the quadratic form

## Related
- **Quadric** — Higher-dimensional analogue
- **Quadratic form** — The degree-2 part of the equation

# Common Errors

- **Error**: Determining conic type from the original matrix without diagonalizing
  **Correction**: While the signature of A indicates the type, the full classification requires diagonalizing and completing the square

# Common Confusions

- **Confusion**: Thinking all quadratic equations give conics
  **Clarification**: Degenerate cases (pairs of lines, single lines, points, empty sets) are possible

# Source Reference

Chapter 8: Bilinear Forms, Section 8.7, pages 260-262. Theorem 8.7.5.

# Verification Notes

- Definition source: Direct from (8.7.1) and Theorem 8.7.5
- Confidence rationale: Explicitly defined with full classification
- Uncertainties: None
- Cross-reference status: Verified
