---
# === CORE IDENTIFICATION ===
concept: O_3 Decomposition
slug: o3-decomposition

# === CLASSIFICATION ===
category: matrix-groups
subcategory: classification
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
  - "decomposition of O_3 elements"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonal-group
  - special-orthogonal-group
  - rotation-group-in-3d
extends: []
related:
  - central-inversion
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the elements of O_3 that are not rotations?"
  - "How can non-rotation elements of O_3 be decomposed?"
---

# Quick Definition

Every element of $O_3$ with determinant $-1$ can be written as a rotation followed by a specific reflection. Specifically, if $A \in O_3$ with $\det(A) = -1$, then $f_A = f_{AU} \circ f_U$ where $U$ represents a reflection.

# Core Definition

Armstrong shows (p. 55) that if $A \in O_3$ but $A \notin SO_3$ (i.e., $\det(A) = -1$), then $AU \in SO_3$ where
$$U = \begin{bmatrix} 1 & 0 & 0 \\ 0 & 1 & 0 \\ 0 & 0 & -1 \end{bmatrix}.$$
Note that $U$ represents reflection in the $(x,y)$ plane. Writing $A = (AU)U$ gives $f_A = f_{AU} \circ f_U$. Since $AU \in SO_3$, $f_{AU}$ is a rotation. Therefore, $f_A$ is reflection in the $(x,y)$ plane followed by a rotation.

# Prerequisites

- **Orthogonal group** — This classifies certain elements of $O_3$
- **Special orthogonal group** — Uses the rotation characterization
- **Rotation group in 3D** — $SO_3$ elements are rotations

# Key Properties

1. If $A \in O_3$ with $\det(A) = -1$, then $A = (AU)U$ where $AU \in SO_3$
2. $f_A$ is a reflection followed by a rotation
3. This generalizes to: every isometry fixing the origin is either a rotation or a reflection-rotation

# Construction / Recognition

## To Decompose $A \in O_3$ with $\det(A) = -1$:
1. Compute $AU$ where $U = \text{diag}(1, 1, -1)$
2. $AU$ has determinant $+1$, so it is a rotation
3. $A = (AU)U$ decomposes $A$ as rotation $\circ$ reflection

# Context & Application

This decomposition is important for understanding full symmetry groups of solids. The full symmetry group of a solid centred at the origin is a subgroup of $O_3$, and this result shows how non-rotational symmetries decompose into rotations and reflections.

# Examples

**Example** (p. 56): The reflection of the tetrahedron in the plane through $P$, $Q$, and $O$ has matrix $\begin{bmatrix} 0 & 1 & 0 \\ 1 & 0 & 0 \\ 0 & 0 & 1 \end{bmatrix}$, which has determinant $-1$ and represents an element of $O_3 \setminus SO_3$.

# Relationships

## Builds Upon
- **Rotation group in 3D** — $SO_3$ provides the rotation factor
- **Orthogonal group** — $O_3$ is decomposed

## Related
- **Central inversion** — The matrix $-I$ is a special case (Chapter 10)

# Common Errors

- **Error**: Thinking the decomposition is unique.
  **Correction**: The specific reflection $U$ is chosen for convenience; different choices of reflection give different rotation factors.

# Common Confusions

- **Confusion**: Thinking elements of $O_3 \setminus SO_3$ are just reflections.
  **Clarification**: They are reflection-rotations (also called improper rotations). A pure reflection is a special case where the rotation factor is trivial.

# Source Reference

Chapter 9: Matrix Groups, page 55 (pdf p. 55).

# Verification Notes

- Decomposition: Explicit on p. 55
- Example: From pp. 55-56
- Confidence: HIGH — explicit construction with proof
