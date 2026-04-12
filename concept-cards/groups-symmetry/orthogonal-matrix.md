---
# === CORE IDENTIFICATION ===
concept: Orthogonal Matrix
slug: orthogonal-matrix

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
  - orthogonal-group
  - special-orthogonal-group
contrasts_with:
  - unitary-matrix

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an orthogonal matrix?"
  - "What does an orthogonal matrix preserve?"
---

# Quick Definition

An $n \times n$ matrix $A$ is orthogonal if $A^tA = I_n$. Its columns (and rows) form an orthonormal basis, and it has determinant $\pm 1$.

# Core Definition

"An $n \times n$ matrix $A$ is **orthogonal** if $A^tA$ is the identity matrix" (Armstrong, p. 52). This means the columns of $A$ are mutually orthogonal unit vectors (an orthonormal basis for $\mathbb{R}^n$). Since $\det(A^tA) = (\det A)^2 = 1$, the determinant of an orthogonal matrix is either $+1$ or $-1$ (p. 52).

# Prerequisites

- **General linear group** — Orthogonal matrices are elements of $GL_n$

# Key Properties

1. $A^tA = I_n$ (equivalently, $A^t = A^{-1}$)
2. Columns form an orthonormal basis for $\mathbb{R}^n$
3. Rows also form an orthonormal basis for $\mathbb{R}^n$
4. $\det(A) = \pm 1$
5. The corresponding linear transformation $f_A$ preserves distances: $\|f_A(\mathbf{x}) - f_A(\mathbf{y})\| = \|\mathbf{x} - \mathbf{y}\|$
6. $f_A$ preserves the scalar product: $f_A(\mathbf{x}) \cdot f_A(\mathbf{y}) = \mathbf{x} \cdot \mathbf{y}$
7. $f_A$ preserves angles (orthogonality)
8. Conversely, any linear transformation that preserves length corresponds to an orthogonal matrix (p. 53)

# Construction / Recognition

## To Check Orthogonality:
1. Compute $A^tA$
2. If $A^tA = I_n$, the matrix is orthogonal

Alternatively:
1. Verify that each column has unit length
2. Verify that distinct columns are orthogonal

# Context & Application

Orthogonal matrices represent distance-preserving linear transformations (rotations and reflections). They are the natural matrices for studying geometric symmetry. Armstrong shows that for $n = 2$, orthogonal matrices are either rotation matrices (det $+1$) or reflection matrices (det $-1$) (pp. 53-54).

# Examples

**Example** (p. 53): For $n = 2$, orthogonal matrices with det $+1$ have the form
$$\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$$
(rotation through $\theta$), while those with det $-1$ have the form
$$\begin{bmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{bmatrix}$$
(reflection in a line at angle $\theta/2$).

# Relationships

## Enables
- **Orthogonal group** — Collection of all orthogonal matrices
- **Special orthogonal group** — Orthogonal matrices with det $+1$

## Contrasts With
- **Unitary matrix** — Complex analogue: $U^{*t}U = I$

# Common Errors

- **Error**: Checking only that columns have unit length without checking orthogonality.
  **Correction**: Both conditions (unit length and mutual orthogonality) are needed.

# Common Confusions

- **Confusion**: Thinking orthogonal matrices must represent rotations.
  **Clarification**: Orthogonal matrices represent either rotations (det $+1$) or reflections (det $-1$). Only those in $SO_n$ are rotations.

# Source Reference

Chapter 9: Matrix Groups, pages 52-54 (pdf pp. 52-54). Definition on p. 52; preservation properties on pp. 52-53; 2D classification on pp. 53-54.

# Verification Notes

- Definition: Direct from p. 52
- Preservation properties: Proved on pp. 52-53
- Confidence: HIGH — explicit definition with thorough treatment
