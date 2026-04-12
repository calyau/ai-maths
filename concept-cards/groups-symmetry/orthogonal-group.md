---
# === CORE IDENTIFICATION ===
concept: Orthogonal Group
slug: orthogonal-group

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
  - "O_n"
  - "O(n)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonal-matrix
  - general-linear-group
extends:
  - general-linear-group
related:
  - special-orthogonal-group
  - unitary-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the orthogonal group?"
  - "How does the orthogonal group relate to GL_n?"
---

# Quick Definition

The orthogonal group $O_n$ is the subgroup of $GL_n$ consisting of all $n \times n$ orthogonal matrices — those satisfying $A^tA = I_n$.

# Core Definition

"The collection of all $n \times n$ orthogonal matrices is a subgroup of $GL_n$. This subgroup is called the **Orthogonal Group**, $O_n$" (Armstrong, p. 52). The subgroup property is verified: if $A$ and $B$ are orthogonal, then $(AB^{-1})^tAB^{-1} = (B^{-1})^tA^tAB^{-1} = BA^tAB^{-1} = I_n$, so $AB^{-1}$ is orthogonal (p. 52).

# Prerequisites

- **Orthogonal matrix** — Elements of $O_n$ are orthogonal matrices
- **General linear group** — $O_n$ is a subgroup of $GL_n$

# Key Properties

1. $O_n$ is a subgroup of $GL_n$
2. Elements preserve distances, angles, and scalar products
3. Every element has determinant $+1$ or $-1$
4. $O_n$ contains both rotations (det $+1$) and reflections (det $-1$)
5. For odd $n$: $O_n \cong SO_n \times \mathbb{Z}_2$ (Chapter 10)
6. For $n = 2$: elements are either rotations or reflections in lines through the origin
7. Symmetry groups of regular solids (centred at origin) are subgroups of $O_3$

# Construction / Recognition

## To Verify Subgroup Property:
1. Take $A, B \in O_n$
2. Show $AB^{-1}$ is orthogonal: $(AB^{-1})^tAB^{-1} = I_n$
3. Apply the one-step subgroup test

# Context & Application

The orthogonal group is the natural matrix group for studying geometric symmetry. When a regular solid is placed with its centre at the origin in $\mathbb{R}^3$, its full symmetry group is isomorphic to a subgroup of $O_3$, and its rotational symmetry group is isomorphic to a subgroup of $SO_3$ (p. 55).

# Examples

**Example** (pp. 53-54): $O_2$ consists of rotation matrices
$\begin{bmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{bmatrix}$
and reflection matrices
$\begin{bmatrix} \cos\theta & \sin\theta \\ \sin\theta & -\cos\theta \end{bmatrix}$.

# Relationships

## Builds Upon
- **General linear group** — $O_n \le GL_n$

## Enables
- **Special orthogonal group** — $SO_n$ is the subgroup of $O_n$ with det $+1$
- **Full symmetry groups** — Subgroups of $O_3$ for 3D solids

## Related
- **Unitary group** — Complex analogue of $O_n$

# Common Errors

- **Error**: Assuming $O_n$ contains only rotations.
  **Correction**: $O_n$ contains both rotations (det $+1$) and reflections/improper rotations (det $-1$).

# Common Confusions

- **Confusion**: Confusing $O_n$ with $SO_n$.
  **Clarification**: $SO_n$ is the subgroup of $O_n$ with determinant $+1$. $O_n$ also contains elements with determinant $-1$.

# Source Reference

Chapter 9: Matrix Groups, page 52 (pdf p. 52). Definition and subgroup proof.

# Verification Notes

- Definition: Direct from p. 52
- Subgroup verification: Explicit on p. 52
- Confidence: HIGH — explicit definition with proof
