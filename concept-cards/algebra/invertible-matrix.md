---
concept: Invertible Matrix
slug: invertible-matrix
category: matrices
subcategory: special-matrices
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.1 The Basic Operations"
extraction_confidence: high
aliases:
  - "nonsingular matrix"
prerequisites:
  - matrix
  - matrix-multiplication
  - identity-matrix
extends: []
related:
  - matrix-inverse
  - determinant
  - general-linear-group
  - row-reduction
contrasts_with:
  - singular-matrix
answers_questions:
  - "How do row operations relate to matrix invertibility?"
---

# Quick Definition

A square matrix A is invertible if there exists a matrix B such that AB = I and BA = I. The matrix B is the inverse of A, denoted A^(-1).

# Core Definition

Let A be a square n x n matrix. If there is a matrix B such that AB = I_n and BA = I_n, then B is called the inverse of A and is denoted A^(-1). The matrix A is then called invertible. The inverse is unique (Lemma 1.1.15). A square matrix is invertible if and only if its determinant is nonzero (Corollary 1.4.15), if and only if it can be row-reduced to I (Theorem 1.2.16), if and only if AX = 0 has only the trivial solution (Theorem 1.2.21) (Artin, pp. 16-22).

# Prerequisites

- **Matrix** — Must be a square matrix
- **Matrix multiplication** — Inverse defined via multiplication
- **Identity matrix** — AA^(-1) = I

# Key Properties

1. Only square matrices can be invertible
2. The inverse is unique (Lemma 1.1.15)
3. A is invertible iff det(A) != 0
4. A is invertible iff it can be row-reduced to I
5. A is invertible iff AX = 0 has only the trivial solution
6. (AB)^(-1) = B^(-1)A^(-1)
7. A matrix with a row or column of zeros is not invertible

# Construction / Recognition

## To Construct:
1. Row-reduce [A|I] to [I|A^(-1)]

## To Recognize:
1. Check det(A) != 0, or row-reduce and see if result is I

# Context & Application

Invertible matrices are central to solving AX = B (unique solution X = A^(-1)B). The set of all invertible n x n matrices forms the general linear group GL_n.

# Examples

**Example 1** (p. 17): [[2,1],[5,3]] is invertible with inverse [[3,-1],[-5,2]].

**Example 2** (p. 17): For [[a,b],[c,d]], the inverse is (1/(ad-bc))[[d,-b],[-c,a]] when ad-bc != 0.

# Relationships

## Builds Upon
- **Matrix multiplication** — Inverse defined by multiplication
- **Identity matrix** — AA^(-1) = I

## Enables
- **General linear group** — Group of all invertible matrices
- **System of linear equations** — Unique solution when A is invertible

## Contrasts With
- **Singular matrix** — A matrix that is not invertible

# Common Errors

- **Error**: Assuming every square matrix is invertible
  **Correction**: Only those with nonzero determinant

- **Error**: Computing (AB)^(-1) as A^(-1)B^(-1)
  **Correction**: (AB)^(-1) = B^(-1)A^(-1) — order reverses

# Common Confusions

- **Confusion**: Thinking left and right inverses can differ for square matrices
  **Clarification**: For square matrices, a left inverse equals the right inverse (Lemma 1.1.15)

# Source Reference

Chapter 1: Matrices, Sections 1.1-1.2, pages 16-22.

# Verification Notes

- Definition source: Direct from (1.1.12)-(1.1.13), p. 17
- Confidence rationale: Extensively discussed with multiple characterizations
- Uncertainties: None
- Cross-reference status: Verified
