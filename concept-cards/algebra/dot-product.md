---
# === CORE IDENTIFICATION ===
concept: Dot Product
slug: dot-product

# === CLASSIFICATION ===
category: applications-of-linear-algebra
subcategory: inner-products
tier: intermediate

# === PROVENANCE ===
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Applications of Linear Operators"
chapter_number: 5
pdf_page: 143
section: "5.1 Orthogonal Matrices and Rotations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "inner product"
  - "scalar product"

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - orthogonal-vectors
  - orthonormal-basis
  - orthogonal-matrix
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the dot product of two vectors?"
  - "How does the dot product relate to lengths and angles?"
---

# Quick Definition

The dot product of column vectors X and Y in R^n is the scalar X^t Y = x_1 y_1 + ... + x_n y_n. It encodes both the lengths of vectors and the angles between them.

# Core Definition

The dot product of column vectors X = (x_1, ..., x_n)^t and Y = (y_1, ..., y_n)^t in R^n is defined as (X . Y) = x_1 y_1 + ... + x_n y_n, which can be written as the matrix product X^t Y (Artin, p. 143). For vectors in R^2, (X . Y) = |X||Y| cos theta, where theta is the angle between the vectors.

# Prerequisites

This is a foundational concept within the context of Chapter 5, building on basic linear algebra from earlier chapters.

# Key Properties

1. The square of the length of a vector X is (X . X) = X^t X
2. X is orthogonal to Y (written X _|_ Y) if and only if (X . Y) = 0
3. |X| is positive unless X is the zero vector
4. Can be written as the matrix product X^t Y
5. Satisfies the Pythagorean theorem: if X _|_ Y and Z = X + Y, then |Z|^2 = |X|^2 + |Y|^2

# Construction / Recognition

## To Compute:
1. Take two column vectors X and Y of the same dimension
2. Multiply corresponding entries and sum: x_1 y_1 + ... + x_n y_n
3. Alternatively, compute the matrix product X^t Y

## To Recognize:
1. A bilinear form on R^n that is symmetric and positive definite
2. A scalar quantity computed from two vectors

# Context & Application

The dot product is the fundamental tool for studying orthogonality and lengths in R^n. It underpins the entire theory of orthogonal matrices and rotations developed in Chapter 5, and provides the geometric foundation for the study of isometries in Chapter 6.

# Examples

**Example 1** (p. 143): For vectors in R^2, the formula (X . Y) = |X||Y| cos theta follows from the law of cosines applied to the triangle with vertices 0, X, Y.

**Example 2** (p. 143): Pythagoras's theorem (5.1.5): If X _|_ Y and Z = X + Y, then |Z|^2 = |X|^2 + |Y|^2, proved by expanding Z^t Z.

# Relationships

## Builds Upon
- **Matrix multiplication** — The dot product is the matrix product X^t Y

## Enables
- **Orthogonal matrix** — Defined via preservation of the dot product
- **Orthogonal operator** — Preserves dot products
- **Isometry** — Distance-preserving maps defined via the dot product

## Related
- **Orthonormal basis** — Basis of unit vectors that are mutually orthogonal under the dot product

# Common Errors

- **Error**: Computing the dot product of vectors of different dimensions
  **Correction**: The dot product is only defined for vectors in the same R^n

# Common Confusions

- **Confusion**: Conflating the dot product with the cross product
  **Clarification**: The dot product produces a scalar; the cross product (defined only in R^3) produces a vector

# Source Reference

Chapter 5: Applications of Linear Operators, Section 5.1, pages 143-144.

# Verification Notes

- Definition source: Direct from equations (5.1.1) and (5.1.2), p. 143
- Confidence rationale: Explicitly defined with clear formulas
- Uncertainties: None
- Cross-reference status: Verified against planned extractions
