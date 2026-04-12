---
# === CORE IDENTIFICATION ===
concept: Orthogonal Matrix
slug: orthogonal-matrix

# === CLASSIFICATION ===
category: applications-of-linear-algebra
subcategory: orthogonal-matrices
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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - dot-product
extends: []
related:
  - orthogonal-operator
  - orthogonal-group
  - special-orthogonal-group
  - orthonormal-basis
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an orthogonal matrix?"
  - "How are orthogonal matrices related to orthonormal bases?"
---

# Quick Definition

A real n x n matrix A is orthogonal if A^t A = I, meaning A is invertible and its inverse is its transpose. Equivalently, its columns form an orthonormal basis of R^n.

# Core Definition

A real n x n matrix A is orthogonal if A^t A = I, which is to say, A is invertible and its inverse is A^t (Artin, Definition 5.1.9, p. 144). By Lemma 5.1.10, an n x n matrix A is orthogonal if and only if its columns form an orthonormal basis of R^n.

# Prerequisites

- **Dot product** — Orthogonality and unit length are defined via the dot product
- **Invertible matrix** — Orthogonal matrices are a special class of invertible matrices

# Key Properties

1. A^t A = I, so A^(-1) = A^t
2. Columns form an orthonormal basis of R^n
3. The product of orthogonal matrices is orthogonal
4. The inverse (transpose) of an orthogonal matrix is orthogonal
5. The determinant of an orthogonal matrix is +/- 1

# Construction / Recognition

## To Construct:
1. Choose n mutually orthogonal unit vectors in R^n
2. Place them as columns of a matrix

## To Recognize:
1. Check that A^t A = I
2. Equivalently, verify columns are mutually orthogonal unit vectors

# Context & Application

Orthogonal matrices represent the distance-preserving linear operators on R^n. They form the orthogonal group O_n, which is central to the study of rotations, reflections, and isometries. In the plane, every orthogonal matrix is either a rotation or a reflection.

# Examples

**Example 1** (p. 144): The 2x2 rotation matrix R = [[cos theta, -sin theta], [sin theta, cos theta]] is orthogonal with determinant 1.

**Example 2** (p. 144): The reflection matrix S_0 = [[1, 0], [0, -1]] is orthogonal with determinant -1.

# Relationships

## Builds Upon
- **Dot product** — Orthogonality defined through the dot product

## Enables
- **Orthogonal group** — The set of all n x n orthogonal matrices
- **Special orthogonal group** — Orthogonal matrices with determinant 1
- **Rotation matrix** — Orthogonal matrices representing rotations

## Related
- **Orthonormal basis** — Columns of an orthogonal matrix form one

# Common Errors

- **Error**: Assuming every orthogonal matrix represents a rotation
  **Correction**: Orthogonal matrices with determinant -1 represent reflections, not rotations

# Common Confusions

- **Confusion**: Thinking orthogonal means the matrix entries are orthogonal
  **Clarification**: It means the columns (or rows) are mutually orthogonal unit vectors

# Source Reference

Chapter 5: Applications of Linear Operators, Section 5.1, Definition 5.1.9, Lemma 5.1.10, Proposition 5.1.11, pages 144-145.

# Verification Notes

- Definition source: Direct quote from Definition 5.1.9
- Confidence rationale: Explicitly defined with clear characterization
- Uncertainties: None
- Cross-reference status: Verified
