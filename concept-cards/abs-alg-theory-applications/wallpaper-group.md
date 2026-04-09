---
concept: Wallpaper Group
slug: wallpaper-group
category: matrix-groups
subcategory: crystallographic-groups
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Matrix Groups and Symmetry"
chapter_number: 12
pdf_page: 163
section: "The Wallpaper Groups"
extraction_confidence: high
aliases:
  - "plane crystallographic group"
  - "plane symmetry group"
prerequisites:
  - euclidean-group
  - symmetry-group
  - lattice-in-rn
extends: []
related:
  - finite-symmetry-groups-in-r2
  - space-group
contrasts_with: []
answers_questions:
  - "What is a wallpaper group?"
  - "How many wallpaper groups exist?"
---

# Quick Definition

A wallpaper group is a symmetry group of a repeating pattern in the plane, which is a subgroup of $E(2)$ whose translations form a lattice. There are exactly 17 distinct wallpaper groups.

# Core Definition

A wallpaper group is a subgroup $G \subset E(2)$ whose translations form a lattice $L = \{(I, \mathbf{t}) : \mathbf{t} \in L\}$. A space group is composed of a translation subgroup (infinite abelian, isomorphic to $\mathbb{Z} \times \mathbb{Z}$) and a point group (a finite subgroup of $O(2)$). **Theorem 12.23**: "There are exactly 17 wallpaper groups" (Judson, p. 166).

# Prerequisites

- **Euclidean group** — Wallpaper groups are subgroups of $E(2)$
- **Symmetry group** — They are symmetry groups of repeating patterns
- **Lattice** — Translations form a lattice

# Key Properties

1. There are exactly 17 wallpaper groups
2. Every translation group in $\mathbb{R}^2$ is isomorphic to $\mathbb{Z} \times \mathbb{Z}$ (Theorem 12.19)
3. The point group is isomorphic to $\mathbb{Z}_n$ or $D_n$ where $n = 1, 2, 3, 4, 6$ (Theorem 12.20)
4. If $T$ is the translation subgroup of $G$, then $G/T \cong G_0$ (the point group)
5. Lattice cell shapes: parallelogram, rectangular, square, rhombic, hexagonal

# Context & Application

Wallpaper groups classify all possible symmetries of repeating patterns in the plane. The analogous classification in $\mathbb{R}^3$ gives 230 space groups (crystal structures). In $\mathbb{R}^4$ there are 4783. The mathematical classification preceded the physical discovery of all crystal types.

# Relationships

## Builds Upon
- **Euclidean group** — Wallpaper groups are subgroups of $E(2)$

## Related
- **Finite symmetry groups in R2** — Point groups are these finite groups

# Source Reference

Chapter 12: Matrix Groups and Symmetry, Section 12.2, pages 163-167. Table 12.22 lists all 17 groups. Theorems 12.19, 12.20, 12.23.

# Verification Notes

- Definition source: Synthesized from discussion pp. 163-166
- Confidence: HIGH — explicit theorem (17 groups)
