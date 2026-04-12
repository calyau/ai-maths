---
# === CORE IDENTIFICATION ===
concept: Orthonormal Basis
slug: orthonormal-basis

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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - dot-product
extends: []
related:
  - orthogonal-matrix
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an orthonormal basis?"
  - "How do orthonormal bases relate to orthogonal matrices?"
---

# Quick Definition

An orthonormal basis of R^n is a basis of mutually orthogonal unit vectors. The condition is (v_i . v_j) = delta_{ij}, where delta_{ij} is the Kronecker delta.

# Core Definition

An orthonormal basis B = (v_1, ..., v_n) of R^n is a basis of orthogonal unit vectors, meaning (v_i . v_j) = delta_{ij}, where delta_{ij} is the Kronecker delta (equal to 1 if i = j and 0 otherwise) (Artin, (5.1.8), p. 144). Any set of orthogonal nonzero vectors is linearly independent (Lemma 5.1.7).

# Prerequisites

- **Dot product** — Orthogonality and unit length defined via the dot product

# Key Properties

1. (v_i . v_j) = delta_{ij} for all i, j
2. Each basis vector has unit length
3. Any set of orthogonal nonzero vectors is independent (Lemma 5.1.7)
4. Columns of an orthogonal matrix form an orthonormal basis (Lemma 5.1.10)

# Construction / Recognition

## To Construct:
1. Start with any basis and apply Gram-Schmidt orthogonalization
2. Or take the columns of any orthogonal matrix

## To Recognize:
1. Verify each vector has unit length
2. Verify each pair of distinct vectors has dot product 0

# Context & Application

Orthonormal bases simplify computation in R^n since coordinates can be computed by dot products. The relationship between orthonormal bases and orthogonal matrices (Lemma 5.1.10) is key to the theory of rotations and isometries.

# Examples

**Example 1** (p. 144): The standard basis (e_1, ..., e_n) is the simplest orthonormal basis.

**Example 2** (p. 144): If (v_1, ..., v_k) are orthogonal and w = v_1 + ... + v_k, then |w|^2 = |v_1|^2 + ... + |v_k|^2 (Pythagoras).

# Relationships

## Builds Upon
- **Dot product** — Defines the orthonormality condition

## Enables
- **Orthogonal matrix** — Columns form an orthonormal basis

# Common Errors

- **Error**: Forgetting to normalize vectors after orthogonalizing
  **Correction**: Orthogonal vectors must also have unit length to be orthonormal

# Common Confusions

- **Confusion**: Conflating orthogonal and orthonormal
  **Clarification**: Orthogonal means perpendicular; orthonormal adds the unit length condition

# Source Reference

Chapter 5: Applications of Linear Operators, Section 5.1, (5.1.8), Lemma 5.1.7, Lemma 5.1.10, p. 144.

# Verification Notes

- Definition source: Direct from (5.1.8)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
