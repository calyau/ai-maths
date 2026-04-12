---
# === CORE IDENTIFICATION ===
concept: Orthogonal Operator
slug: orthogonal-operator

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
  - orthogonal-matrix
extends: []
related:
  - isometry
  - orthogonal-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an orthogonal operator?"
  - "How do orthogonal operators relate to orthogonal matrices?"
---

# Quick Definition

An orthogonal operator T on R^n is a linear operator that preserves the dot product: (TX . TY) = (X . Y) for all vectors X, Y. Equivalently, it preserves lengths of vectors.

# Core Definition

An orthogonal operator T on R^n is a linear operator that preserves the dot product: for every pair X, Y of vectors, (TX . TY) = (X . Y) (Artin, Definition 5.1.12, p. 144). By Proposition 5.1.13, a linear operator is orthogonal if and only if it preserves lengths. By Proposition 5.1.14, T is orthogonal if and only if its matrix with respect to the standard basis is an orthogonal matrix.

# Prerequisites

- **Dot product** — The defining property involves preservation of the dot product
- **Orthogonal matrix** — The matrix representation of an orthogonal operator

# Key Properties

1. Preserves dot products: (TX . TY) = (X . Y)
2. Preserves lengths: |TX| = |X| for all X
3. Matrix with respect to any orthonormal basis is orthogonal
4. Is an isometry that fixes the origin

# Construction / Recognition

## To Construct:
1. Define a linear map whose matrix with respect to the standard basis is orthogonal

## To Recognize:
1. Check that the operator preserves dot products, or equivalently, preserves lengths
2. Check that its matrix is orthogonal

# Context & Application

Orthogonal operators are the distance-preserving linear maps of R^n. They are the building blocks of all isometries, since every isometry is a composition of an orthogonal operator and a translation (Corollary 6.2.7).

# Examples

**Example 1** (p. 144): In R^2, orthogonal operators are either rotations (determinant 1) or reflections (determinant -1), as classified by Theorem 5.1.17.

**Example 2** (p. 162): Orthogonal operators are isometries that fix the origin (Theorem 6.2.3).

# Relationships

## Builds Upon
- **Orthogonal matrix** — Matrix representation of orthogonal operators

## Enables
- **Isometry** — Every isometry decomposes as an orthogonal operator composed with a translation
- **Symmetry group** — Symmetries of bounded figures are orthogonal operators

## Related
- **Orthogonal group** — The group of all orthogonal operators

# Common Errors

- **Error**: Assuming orthogonal operators must fix the origin
  **Correction**: Orthogonal operators as linear maps do fix the origin; isometries that fix the origin are orthogonal operators

# Common Confusions

- **Confusion**: Conflating orthogonal operators with all isometries
  **Clarification**: Orthogonal operators are the isometries that fix the origin; general isometries also include translations

# Source Reference

Chapter 5: Applications of Linear Operators, Section 5.1, Definition 5.1.12, Propositions 5.1.13-5.1.14, pages 144-145.

# Verification Notes

- Definition source: Direct from Definition 5.1.12
- Confidence rationale: Explicitly defined with multiple equivalent characterizations
- Uncertainties: None
- Cross-reference status: Verified
