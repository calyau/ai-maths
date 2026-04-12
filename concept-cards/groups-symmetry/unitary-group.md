---
# === CORE IDENTIFICATION ===
concept: Unitary Group
slug: unitary-group

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
aliases:
  - "U_n"
  - "U(n)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - general-linear-group
extends: []
related:
  - special-unitary-group
  - orthogonal-group
contrasts_with:
  - orthogonal-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the unitary group?"
  - "What is the complex analogue of the orthogonal group?"
---

# Quick Definition

The unitary group $U_n$ is the subgroup of $GL_n(\mathbb{C})$ consisting of all $n \times n$ unitary matrices — those satisfying $U^{*t}U = I_n$, where $*$ denotes complex conjugation.

# Core Definition

"A complex matrix $U$ is called a *unitary matrix* if $U^{*t}U$ is the identity matrix, and the unitary matrices are precisely those whose corresponding linear transformations preserve length in $\mathbb{C}^n$. The collection of all $n \times n$ unitary matrices forms a subgroup of $GL_n(\mathbb{C})$ called the *Unitary Group*, $U_n$" (Armstrong, p. 56).

# Prerequisites

- **General linear group** — $U_n$ is a subgroup of $GL_n(\mathbb{C})$

# Key Properties

1. $U_n$ is a subgroup of $GL_n(\mathbb{C})$
2. $U^{*t}U = I_n$ (equivalently, $U^{-1} = U^{*t}$)
3. Columns of $U$ form an orthonormal basis for $\mathbb{C}^n$
4. The corresponding linear transformation preserves length in $\mathbb{C}^n$
5. The determinant of a unitary matrix has modulus 1 (Exercise 9.13)
6. $U_n$ is the complex analogue of $O_n$

# Construction / Recognition

## To Check Unitarity:
1. Compute $U^{*t}U$ (conjugate transpose times original)
2. If the result is $I_n$, the matrix is unitary

# Context & Application

The unitary group is the complex analogue of the orthogonal group. Just as orthogonal matrices preserve the real inner product, unitary matrices preserve the Hermitian inner product on $\mathbb{C}^n$. Unitary groups are fundamental in quantum mechanics, where symmetry transformations are represented by unitary operators.

# Examples

**Example** (Exercise 9.14, p. 57): Elements of $U_2$ have the form
$$\begin{bmatrix} z & w \\ -e^{i\theta}w^* & e^{i\theta}z^* \end{bmatrix}$$
where $z, w \in \mathbb{C}$, $\theta \in \mathbb{R}$, and $zz^* + ww^* = 1$.

# Relationships

## Builds Upon
- **General linear group** — $U_n \le GL_n(\mathbb{C})$

## Enables
- **Special unitary group** — $SU_n$ is the subgroup of $U_n$ with det $+1$

## Contrasts With
- **Orthogonal group** — $O_n$ is the real analogue; uses transpose instead of conjugate transpose

# Common Errors

- **Error**: Using transpose instead of conjugate transpose for the unitarity condition.
  **Correction**: Unitarity requires $U^{*t}U = I_n$, not $U^tU = I_n$. For real matrices the conditions coincide, but for complex matrices they differ.

# Common Confusions

- **Confusion**: Thinking unitary matrices must have determinant $+1$.
  **Clarification**: Unitary matrices have determinant of modulus 1 (i.e., $|\det U| = 1$), but the determinant can be any complex number on the unit circle.

# Source Reference

Chapter 9: Matrix Groups, page 56 (pdf p. 56). Definition at the end of the chapter.

# Verification Notes

- Definition: Direct from p. 56
- Confidence: HIGH — explicit definition, though brief treatment
