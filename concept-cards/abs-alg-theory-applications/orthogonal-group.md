---
concept: Orthogonal Group
slug: orthogonal-group
category: matrix-groups
subcategory: classical-matrix-groups
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Matrix Groups and Symmetry"
chapter_number: 12
pdf_page: 157
section: "The Orthogonal Group O(n)"
extraction_confidence: high
aliases:
  - "O(n)"
prerequisites:
  - general-linear-group
  - orthogonal-matrix
extends:
  - general-linear-group
related:
  - special-orthogonal-group
  - euclidean-inner-product
  - isometry
contrasts_with:
  - special-orthogonal-group
answers_questions:
  - "What is the orthogonal group?"
  - "What geometric transformations do orthogonal matrices represent?"
---

# Quick Definition

The orthogonal group $O(n)$ is the group of all $n \times n$ orthogonal matrices (matrices satisfying $A^{-1} = A^t$). These are precisely the linear transformations that preserve distances, lengths, and inner products.

# Core Definition

"The **orthogonal group** consists of the set of all orthogonal matrices. We write $O(n)$ for the $n \times n$ orthogonal group" (Judson, p. 157). A matrix $A$ is orthogonal if $A^{-1} = A^t$. By Theorem 12.8, the following are equivalent: (1) columns form an orthonormal set, (2) $A^{-1} = A^t$, (3) $A$ preserves inner products, (4) $A$ preserves distances, (5) $A$ preserves lengths.

# Prerequisites

- **General linear group** — $O(n) \leq GL_n(\mathbb{R})$
- **Orthogonal matrix** — Elements of $O(n)$

# Key Properties

1. $O(n)$ is a subgroup of $GL_n(\mathbb{R})$
2. $\det(A) = \pm 1$ for all $A \in O(n)$
3. Columns of $A \in O(n)$ form an orthonormal set
4. $O(n)$ preserves the Euclidean inner product: $\langle A\mathbf{x}, A\mathbf{y}\rangle = \langle \mathbf{x}, \mathbf{y}\rangle$
5. Elements of $O(2)$ are either rotations ($\det = 1$) or reflections followed by rotations ($\det = -1$)

# Examples

**Example 1** (p. 157): The matrices $\begin{pmatrix} 3/5 & -4/5 \\ 4/5 & 3/5 \end{pmatrix}$ and $\begin{pmatrix} 1/2 & -\sqrt{3}/2 \\ \sqrt{3}/2 & 1/2 \end{pmatrix}$ are orthogonal.

**Example 2** (p. 160): Elements of $O(2)$ have the form $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ (rotations) or $\begin{pmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{pmatrix}$ (reflections composed with rotations).

# Relationships

## Builds Upon
- **General linear group** — $O(n)$ is a subgroup

## Enables
- **Special orthogonal group** — $SO(n) = O(n) \cap SL_n(\mathbb{R})$
- **Symmetry group** — Finite symmetry groups are subgroups of $O(n)$

## Contrasts With
- **Special orthogonal group** — $SO(n)$ has only rotations ($\det = 1$); $O(n)$ also includes reflections

# Source Reference

Chapter 12: Matrix Groups and Symmetry, Section 12.1, pages 157-160. Theorem 12.8 characterizes orthogonal matrices.

# Verification Notes

- Definition source: Direct quote from p. 157
- Characterization: Theorem 12.8, p. 158-159
- Confidence: HIGH — explicit definition with complete characterization theorem
