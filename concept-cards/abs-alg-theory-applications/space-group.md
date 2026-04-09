---
concept: Space Group
slug: space-group
category: matrix-groups
subcategory: crystallographic-groups
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Matrix Groups and Symmetry"
chapter_number: 12
pdf_page: 165
section: "The Wallpaper Groups"
extraction_confidence: medium
aliases:
  - "crystallographic space group"
prerequisites:
  - wallpaper-group
  - euclidean-group
extends:
  - wallpaper-group
related:
  - point-group
  - translation-subgroup
contrasts_with: []
answers_questions:
  - "What is a space group?"
  - "How are crystals classified mathematically?"
---

# Quick Definition

A space group is the symmetry group of a crystal or lattice, consisting of a translation subgroup (infinite abelian) and a point group (finite rotations/reflections). There are 17 space groups in $\mathbb{R}^2$ and 230 in $\mathbb{R}^3$.

# Core Definition

"A space group is composed of two parts: a **translation subgroup** and a **point group**. The translation subgroup is an infinite abelian subgroup of the space group made up of the translational symmetries of the crystal; the point group is a finite group consisting of rotations and reflections of the crystal about a point" (Judson, p. 165).

# Prerequisites

- **Wallpaper group** — Space groups in 2D are wallpaper groups
- **Euclidean group** — Space groups are subgroups of $E(n)$

# Key Properties

1. Composed of translation subgroup + point group
2. Translation subgroup $\cong \mathbb{Z} \times \mathbb{Z}$ (in 2D)
3. Point group is a finite subgroup of $O(n)$
4. If $T$ is the translation subgroup: $G/T \cong G_0$ (point group)
5. 17 in $\mathbb{R}^2$, 230 in $\mathbb{R}^3$, 4783 in $\mathbb{R}^4$

# Relationships

## Builds Upon
- **Wallpaper group** — 2D space groups

## Related
- **Point group** — The finite part
- **Translation subgroup** — The infinite part

# Source Reference

Chapter 12: Matrix Groups and Symmetry, Section 12.2, p. 165-166.

# Verification Notes

- Definition source: Direct from p. 165
- Confidence: MEDIUM — synthesized from discussion, not a single formal definition
