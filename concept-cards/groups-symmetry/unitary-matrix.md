---
# === CORE IDENTIFICATION ===
concept: Unitary Matrix
slug: unitary-matrix

# === CLASSIFICATION ===
category: matrix-groups
subcategory: definitions
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Matrix Groups"
chapter_number: 9
pdf_page: 51
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - general-linear-group
extends: []
related:
  - unitary-group
  - special-unitary-group
contrasts_with:
  - orthogonal-matrix

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a unitary matrix?"
  - "What is the complex analogue of an orthogonal matrix?"
---

# Quick Definition

A complex matrix $U$ is unitary if $U^{*t}U = I_n$, where $*$ denotes complex conjugation. Unitary matrices preserve length in $\mathbb{C}^n$.

# Core Definition

"A complex matrix $U$ is called a *unitary matrix* if $U^{*t}U$ is the identity matrix, and the unitary matrices are precisely those whose corresponding linear transformations preserve length in $\mathbb{C}^n$" (Armstrong, p. 56). Here, if $\mathbf{z} \in \mathbb{C}^n$, the length of $\mathbf{z}$ is $\sqrt{\mathbf{z}\mathbf{z}^*}$.

# Prerequisites

- **General linear group** — Unitary matrices are elements of $GL_n(\mathbb{C})$

# Key Properties

1. $U^{*t}U = I_n$ (equivalently, $U^{-1} = U^{*t}$)
2. Columns form an orthonormal basis for $\mathbb{C}^n$ with respect to the Hermitian inner product
3. $|\det(U)| = 1$ (determinant has modulus 1)
4. The corresponding linear transformation preserves length in $\mathbb{C}^n$
5. For real matrices, unitarity reduces to orthogonality ($U^{*t} = U^t$ when entries are real)

# Construction / Recognition

## To Check Unitarity:
1. Compute $U^{*t}$ (conjugate transpose)
2. Compute $U^{*t}U$
3. If the result is $I_n$, the matrix is unitary

# Context & Application

Unitary matrices are the complex analogue of orthogonal matrices. Just as orthogonal matrices preserve the real inner product, unitary matrices preserve the Hermitian inner product. They are fundamental in quantum mechanics, where physical symmetries are represented by unitary operators.

# Examples

**Example** (Exercise 9.14): Elements of $U_2$ have the form
$$\begin{bmatrix} z & w \\ -e^{i\theta}w^* & e^{i\theta}z^* \end{bmatrix}$$
where $zz^* + ww^* = 1$.

# Relationships

## Enables
- **Unitary group** — The collection of all unitary matrices
- **Special unitary group** — Unitary matrices with det $= 1$

## Contrasts With
- **Orthogonal matrix** — Real analogue ($A^tA = I$)

# Common Errors

- **Error**: Using transpose instead of conjugate transpose.
  **Correction**: Unitarity requires $U^{*t}U = I$, not $U^tU = I$. For complex matrices these differ.

# Common Confusions

- **Confusion**: Thinking unitary matrices must be real.
  **Clarification**: Unitary matrices are complex in general. Real unitary matrices are precisely the orthogonal matrices.

# Source Reference

Chapter 9: Matrix Groups, page 56 (pdf p. 56).

# Verification Notes

- Definition: Direct from p. 56
- Confidence: HIGH — explicit definition
