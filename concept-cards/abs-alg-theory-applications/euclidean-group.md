---
concept: Euclidean Group
slug: euclidean-group
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
  - "E(n)"
  - "group of Euclidean motions"
prerequisites:
  - orthogonal-group
  - group
extends:
  - group
related:
  - isometry
  - symmetry-group
  - wallpaper-group
contrasts_with: []
answers_questions:
  - "What is the Euclidean group?"
  - "How are rigid motions represented algebraically?"
---

# Quick Definition

The Euclidean group $E(n)$ consists of ordered pairs $(A, \mathbf{x})$ where $A \in O(n)$ and $\mathbf{x} \in \mathbb{R}^n$, with multiplication $(A, \mathbf{x})(B, \mathbf{y}) = (AB, A\mathbf{y} + \mathbf{x})$. It is the group of all distance-preserving transformations of $\mathbb{R}^n$.

# Core Definition

"The **Euclidean group**, $E(n)$, can be written as ordered pairs $(A, \mathbf{x})$, where $A$ is in $O(n)$ and $\mathbf{x}$ is in $\mathbb{R}^n$. We define multiplication by $(A, \mathbf{x})(B, \mathbf{y}) = (AB, A\mathbf{y} + \mathbf{x})$" (Judson, p. 160).

# Prerequisites

- **Orthogonal group** — The "linear part" $A \in O(n)$
- **Group** — $E(n)$ is a group

# Key Properties

1. Identity: $(I, \mathbf{0})$
2. Inverse: $(A, \mathbf{x})^{-1} = (A^{-1}, -A^{-1}\mathbf{x})$
3. Elements act on $\mathbb{R}^n$ by $\mathbf{v} \mapsto A\mathbf{v} + \mathbf{x}$
4. The group of isometries on $\mathbb{R}^2$ equals $E(2)$ (Theorem 12.14)
5. Translations form a normal subgroup of $E(n)$

# Examples

**Example 1** (p. 160): A rotation by $\theta$ about the origin followed by translation by $\mathbf{x}$ is $(R_\theta, \mathbf{x})$ in $E(2)$.

# Relationships

## Builds Upon
- **Orthogonal group** — The linear part comes from $O(n)$

## Enables
- **Symmetry group** — Symmetry groups are subgroups of $E(n)$
- **Wallpaper group** — Space groups are subgroups of $E(2)$

## Related
- **Isometry** — Elements of $E(n)$ are exactly the isometries of $\mathbb{R}^n$

# Source Reference

Chapter 12: Matrix Groups and Symmetry, Section 12.1, p. 160. Theorem 12.14.

# Verification Notes

- Definition source: Direct quote from p. 160
- Confidence: HIGH
