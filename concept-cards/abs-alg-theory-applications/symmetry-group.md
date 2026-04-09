---
concept: Symmetry Group
slug: symmetry-group
category: matrix-groups
subcategory: geometric-transformations
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Matrix Groups and Symmetry"
chapter_number: 12
pdf_page: 162
section: "Symmetry"
extraction_confidence: high
aliases:
  - "group of symmetries"
prerequisites:
  - isometry
  - group
extends:
  - group
related:
  - euclidean-group
  - dihedral-group
  - finite-symmetry-groups-in-r2
contrasts_with: []
answers_questions:
  - "What is a symmetry group?"
  - "How are symmetry groups related to matrix groups?"
---

# Quick Definition

A symmetry group in $\mathbb{R}^n$ is a subgroup of the group of isometries on $\mathbb{R}^n$ that fixes (maps to itself) a set of points $X \subset \mathbb{R}^n$.

# Core Definition

"A **symmetry group** in $\mathbb{R}^n$ is a subgroup of the group of isometries on $\mathbb{R}^n$ that fixes a set of points $X \subset \mathbb{R}^n$" (Judson, p. 162). The symmetry group depends on both the ambient space $\mathbb{R}^n$ and the set $X$.

# Prerequisites

- **Isometry** — Symmetry groups consist of isometries
- **Group** — A symmetry group is a group

# Key Properties

1. The symmetry group depends on both $\mathbb{R}^n$ and $X$
2. The symmetry group of the origin in $\mathbb{R}^1$ is $\mathbb{Z}_2$; in $\mathbb{R}^2$ it is $O(2)$
3. The only finite symmetry groups in $\mathbb{R}^2$ are $\mathbb{Z}_n$ and $D_n$ (Theorem 12.15)

# Examples

**Example 1** (p. 162): The symmetry group of a regular $n$-gon in $\mathbb{R}^2$ is the dihedral group $D_n$.

**Example 2** (p. 162): A figure with only rotational symmetry has symmetry group $\mathbb{Z}_n$.

# Relationships

## Builds Upon
- **Isometry** — Elements of a symmetry group are isometries

## Related
- **Dihedral group** — $D_n$ is the symmetry group of a regular $n$-gon
- **Finite symmetry groups in R2** — Classified as $\mathbb{Z}_n$ or $D_n$

# Source Reference

Chapter 12: Matrix Groups and Symmetry, Section 12.2, p. 162. Theorem 12.15.

# Verification Notes

- Definition source: Direct quote from p. 162
- Confidence: HIGH
