---
# === CORE IDENTIFICATION ===
concept: Special Orthogonal Group
slug: special-orthogonal-group

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
  - "SO_n"
  - "SO(n)"
  - "rotation group"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonal-group
extends:
  - orthogonal-group
related:
  - rotation-group-in-3d
  - special-unitary-group
contrasts_with:
  - orthogonal-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the special orthogonal group?"
  - "What is the rotation group?"
---

# Quick Definition

The special orthogonal group $SO_n$ is the subgroup of $O_n$ consisting of orthogonal matrices with determinant $+1$. It represents the group of rotations.

# Core Definition

"Those elements of $O_n$ which have determinant equal to $+1$ form a subgroup of $O_n$ called the **Special Orthogonal Group**, $SO_n$" (Armstrong, p. 52). Armstrong notes that $SO_2$ is isomorphic to the unit circle group $C$ in the complex plane (p. 54), and that each matrix in $SO_3$ represents a rotation of $\mathbb{R}^3$ about an axis through the origin (p. 54).

# Prerequisites

- **Orthogonal group** — $SO_n$ is a subgroup of $O_n$

# Key Properties

1. $SO_n$ is a subgroup of $O_n$ (elements with det $+1$)
2. Elements of $SO_n$ represent rotations
3. $SO_2$ consists of all $2 \times 2$ rotation matrices $\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$
4. $SO_2 \cong C$ (the unit circle group) via $e^{i\theta} \mapsto \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$
5. Every element of $SO_3$ is a rotation about some axis through the origin (p. 54)
6. Rotational symmetry groups of regular solids are subgroups of $SO_3$
7. For odd $n$: $O_n \cong SO_n \times \mathbb{Z}_2$ (Chapter 10)

# Construction / Recognition

## To Check Membership in $SO_n$:
1. Verify $A^tA = I_n$ (orthogonality)
2. Verify $\det(A) = +1$

## To Show $SO_3$ Elements are Rotations (p. 54):
1. The characteristic polynomial has a real eigenvalue with unit modulus
2. Since $\det(A) = +1$, the eigenvalue $+1$ exists
3. The corresponding eigenvector determines the rotation axis
4. The restriction to the perpendicular plane is an element of $SO_2$, hence a rotation

# Context & Application

Armstrong refers to $SO_3$ as the "rotation group in three dimensions" (p. 55). The classification of finite subgroups of $SO_3$ (Chapter 19) shows they are cyclic groups, dihedral groups, or rotational symmetry groups of Platonic solids. This makes $SO_3$ central to the classification of symmetry in three dimensions.

# Examples

**Example** (p. 55): The tetrahedron with vertices at $(1,1,1)$, $(-1,-1,1)$, $(1,-1,-1)$, $(-1,1,-1)$ has rotations represented by matrices in $SO_3$, including:
$$\begin{bmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$$
(rotation about vertex axis, permuting coordinate axes).

**Example** (p. 54): $SO_2 \cong C$ via the correspondence $e^{i\theta} \to \begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$.

# Relationships

## Builds Upon
- **Orthogonal group** — $SO_n \le O_n$

## Enables
- **Rotation group in 3D** — $SO_3$ classifies 3D rotations
- **Symmetry of Platonic solids** — Rotational symmetry groups are subgroups of $SO_3$

## Related
- **Special unitary group** — Complex analogue

## Contrasts With
- **Orthogonal group** — $O_n$ also includes reflections (det $-1$)

# Common Errors

- **Error**: Assuming every element of $SO_n$ has all eigenvalues equal to 1.
  **Correction**: Elements of $SO_n$ are rotations, and their eigenvalues lie on the unit circle. Only the eigenvalue along the rotation axis is necessarily 1 (in odd dimensions).

# Common Confusions

- **Confusion**: Thinking $SO_n$ always equals the "rotation subgroup" of $O_n$.
  **Clarification**: This is correct — $SO_n$ consists precisely of the rotations (orientation-preserving orthogonal transformations).

# Source Reference

Chapter 9: Matrix Groups, pages 52-55 (pdf pp. 52-55). Definition on p. 52; $SO_2$ classification on pp. 53-54; $SO_3$ characterization on p. 54.

# Verification Notes

- Definition: Direct from p. 52
- $SO_3$ rotation characterization: Proved on p. 54
- Confidence: HIGH — explicit definition with thorough analysis
