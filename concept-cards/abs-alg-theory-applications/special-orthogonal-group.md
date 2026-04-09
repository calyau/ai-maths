---
concept: Special Orthogonal Group
slug: special-orthogonal-group
category: matrix-groups
subcategory: classical-matrix-groups
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Matrix Groups and Symmetry"
chapter_number: 12
pdf_page: 160
section: "Matrix Groups"
extraction_confidence: high
aliases:
  - "SO(n)"
  - "rotation group"
prerequisites:
  - orthogonal-group
  - special-linear-group
extends:
  - orthogonal-group
related:
  - isometry
  - symmetry-group
contrasts_with:
  - orthogonal-group
answers_questions:
  - "What is the special orthogonal group?"
  - "How does SO(n) differ from O(n)?"
---

# Quick Definition

The special orthogonal group $SO(n)$ consists of all orthogonal matrices with determinant 1. It is the intersection $O(n) \cap SL_n(\mathbb{R})$ and represents pure rotations (without reflections).

# Core Definition

"The **special orthogonal group**, $SO(n)$, is just the intersection of $O(n)$ and $SL_n(\mathbb{R})$; that is, those elements in $O(n)$ with determinant one" (Judson, p. 160).

# Prerequisites

- **Orthogonal group** — $SO(n) \leq O(n)$
- **Special linear group** — $SO(n) = O(n) \cap SL_n(\mathbb{R})$

# Key Properties

1. $SO(n)$ is a normal subgroup of $O(n)$ (as $SO(n) = \ker(\det|_{O(n)})$)
2. $[O(n):SO(n)] = 2$
3. Elements of $SO(2)$ are rotations: $\begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$
4. $SO(2)$ is abelian; $SO(n)$ is non-abelian for $n \geq 3$

# Examples

**Example 1** (p. 160): In $O(2)$, the rotations $R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}$ form $SO(2)$, with $\det(R_\theta) = 1$.

# Relationships

## Builds Upon
- **Orthogonal group** — $SO(n)$ is the "rotation part" of $O(n)$

## Contrasts With
- **Orthogonal group** — $O(n)$ includes reflections; $SO(n)$ does not

# Source Reference

Chapter 12: Matrix Groups and Symmetry, Section 12.1, p. 160.

# Verification Notes

- Definition source: Direct quote from p. 160
- Confidence: HIGH — explicit definition
