---
# === CORE IDENTIFICATION ===
concept: Quadratic Form
slug: quadratic-form

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - symmetric-bilinear-form
extends: []
related:
  - conic
  - quadric
  - signature
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a quadratic form?"
---

# Quick Definition

A quadratic form in n variables is a polynomial each of whose terms has degree 2, written as q(X) = X^t A X for a symmetric matrix A. The classification of quadratic forms by signature is equivalent to the classification of symmetric bilinear forms.

# Core Definition

A quadratic form in n variables is a polynomial q(x_1, ..., x_n) = X^t A X where A is a symmetric matrix (Artin, (8.7.2), (8.7.13), pp. 260, 262). The quadratic form is the degree-2 part of a general quadratic equation. By the spectral theorem, A can be diagonalized by an orthogonal transformation, reducing q to a sum of squares with signs determined by the eigenvalues.

# Prerequisites

- **Symmetric bilinear form** — The matrix A is symmetric; q(X) = X^t A X is the "diagonal" of the bilinear form

# Key Properties

1. q(X) = X^t A X for a symmetric matrix A
2. q(lambda X) = lambda^2 q(X) for any scalar lambda — homogeneity of degree 2
3. The locus {q = 0} is a union of lines through the origin (when q is homogeneous)
4. Can be diagonalized to a sum +/- x_i^2 by a change of basis
5. The bilinear form can be recovered: (X, Y) = (q(X+Y) - q(X) - q(Y))/2

# Construction / Recognition

## To Construct:
1. Choose a symmetric matrix A
2. Define q(X) = X^t A X

## To Recognize:
1. A polynomial in which every term has degree exactly 2

# Context & Application

Quadratic forms arise in geometry (conics, quadrics), number theory (representation of integers), and optimization (second-order conditions). The interplay between a quadratic form and its associated symmetric bilinear form is central to Artin's Chapter 8.

# Examples

**Example 1** (p. 260): q(x_1, x_2) = a_{11}x_1^2 + 2a_{12}x_1 x_2 + a_{22}x_2^2, with A = [[a_{11}, a_{12}],[a_{12}, a_{22}]].

**Example 2** (p. 262): q(x_1, x_2, x_3) = a_{11}x_1^2 + a_{22}x_2^2 - x_3^2, a cone when set to zero.

# Relationships

## Builds Upon
- **Symmetric bilinear form** — The associated form via (X,Y) = X^t A Y

## Enables
- **Conic** — The quadratic part of a conic equation
- **Quadric** — The quadratic part of a quadric equation

## Related
- **Signature** — Classifies the quadratic form

# Common Errors

- **Error**: Forgetting the factor of 2 in the off-diagonal entries of A
  **Correction**: The coefficient of x_i x_j in q is 2a_{ij}, so a_{ij} is half the coefficient

# Common Confusions

- **Confusion**: Thinking a quadratic form is the same as a bilinear form
  **Clarification**: A quadratic form is a function of one variable q(X) = X^t A X; a bilinear form is a function of two variables (X, Y) = X^t A Y

# Source Reference

Chapter 8: Bilinear Forms, Section 8.7, pages 260-263.

# Verification Notes

- Definition source: Direct from (8.7.2) and (8.7.13)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
