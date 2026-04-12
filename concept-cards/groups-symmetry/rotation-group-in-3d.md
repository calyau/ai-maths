---
# === CORE IDENTIFICATION ===
concept: Rotation Group in 3D
slug: rotation-group-in-3d

# === CLASSIFICATION ===
category: matrix-groups
subcategory: specific-groups
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
  - "SO_3"
  - "SO(3)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - special-orthogonal-group
extends:
  - special-orthogonal-group
related:
  - cube-symmetry-group
  - dodecahedron-symmetry-group
  - tetrahedron-symmetry-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the rotation group in three dimensions?"
  - "How are 3D rotations represented by matrices?"
---

# Quick Definition

$SO_3$ is the group of all $3 \times 3$ orthogonal matrices with determinant $+1$. Every such matrix represents a rotation of $\mathbb{R}^3$ about an axis through the origin.

# Core Definition

Armstrong proves that each matrix in $SO_3$ represents a rotation about an axis through the origin (p. 54). The proof uses the characteristic polynomial: being cubic, it has a real eigenvalue. Since all eigenvalues have unit modulus and their product is $\det(A) = +1$, the eigenvalue $+1$ exists. The corresponding eigenvector determines the rotation axis. The restriction to the perpendicular plane gives a $2 \times 2$ rotation matrix.

For matrices in $O_3$ but not $SO_3$, the transformation is a reflection followed by a rotation (p. 55).

# Prerequisites

- **Special orthogonal group** — $SO_3$ is a specific instance of $SO_n$

# Key Properties

1. Every element of $SO_3$ is a rotation about an axis through the origin
2. Conversely, every such rotation is represented by a matrix in $SO_3$
3. The eigenvalue $+1$ always exists and determines the axis
4. Finite subgroups of $SO_3$ are cyclic, dihedral, or symmetry groups of Platonic solids (Chapter 19)
5. If $A \in O_3$ but $A \notin SO_3$, then $f_A$ is a reflection followed by a rotation

# Construction / Recognition

## To Find the Rotation Axis of $A \in SO_3$:
1. Solve $A\mathbf{v} = \mathbf{v}$ (find the eigenvector for eigenvalue $+1$)
2. The line through the origin in direction $\mathbf{v}$ is the rotation axis
3. Construct an orthonormal basis starting with $\mathbf{v}/\|\mathbf{v}\|$
4. The matrix of $f_A$ in this basis has the form $\begin{bmatrix} 1 & 0 & 0 \\ 0 & B \end{bmatrix}$ where $B \in SO_2$

# Context & Application

$SO_3$ is the natural setting for studying rotational symmetry in three dimensions. Armstrong places regular solids at the origin so that their rotational symmetry groups become subgroups of $SO_3$. The classification of finite subgroups of $SO_3$ (Chapter 19) is one of the major results of the book.

# Examples

**Example** (p. 55): The tetrahedron with vertices at $(\pm 1, \pm 1, \pm 1)$ (with even sign changes) has rotational symmetries in $SO_3$:
- Rotation about the $z$-axis through $\pi$: $\begin{bmatrix} -1 & 0 & 0 \\ 0 & -1 & 0 \\ 0 & 0 & 1 \end{bmatrix}$
- Rotation about vertex axis (cyclic permutation of coordinates): $\begin{bmatrix} 0 & 0 & 1 \\ 1 & 0 & 0 \\ 0 & 1 & 0 \end{bmatrix}$

# Relationships

## Builds Upon
- **Special orthogonal group** — $SO_3$ is $SO_n$ for $n = 3$

## Related
- **Tetrahedron symmetry group** — Subgroup of $SO_3$, $\cong A_4$
- **Cube symmetry group** — Subgroup of $SO_3$, $\cong S_4$
- **Dodecahedron symmetry group** — Subgroup of $SO_3$, $\cong A_5$

# Common Errors

- **Error**: Assuming every $3 \times 3$ orthogonal matrix represents a rotation.
  **Correction**: Orthogonal matrices with det $-1$ represent reflections (or reflection-rotations), not pure rotations. Only $SO_3$ elements are rotations.

# Common Confusions

- **Confusion**: Thinking a rotation must fix a plane.
  **Clarification**: A 3D rotation fixes an axis (a line), not a plane. The perpendicular plane is rotated within itself.

# Source Reference

Chapter 9: Matrix Groups, pages 54-55 (pdf pp. 54-55). Characterization of $SO_3$ elements as rotations; matrix examples for tetrahedron.

# Verification Notes

- Characterization: Proved on p. 54
- Examples: From pp. 55-56
- Classification reference: Chapter 19, mentioned on p. 56
- Confidence: HIGH — explicit proof
