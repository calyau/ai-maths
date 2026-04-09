---
concept: Translation Subgroup
slug: translation-subgroup
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
extraction_confidence: high
aliases: []
prerequisites:
  - space-group
  - lattice-in-rn
extends: []
related:
  - point-group
  - wallpaper-group
contrasts_with:
  - point-group
answers_questions:
  - "What is the translation subgroup of a space group?"
---

# Quick Definition

The translation subgroup of a space group $G$ is the set $\{(I, \mathbf{t}) : \mathbf{t} \in L\}$ where $L$ is a lattice. It is an infinite abelian normal subgroup, isomorphic to $\mathbb{Z} \times \mathbb{Z}$ in 2D.

# Core Definition

"A space group is a subgroup of $G \subset E(2)$ whose translations are a set of the form $\{(I, \mathbf{t}) : \mathbf{t} \in L\}$, where $L$ is a lattice" (Judson, p. 165). By Theorem 12.19: "Every translation group in $\mathbb{R}^2$ is isomorphic to $\mathbb{Z} \times \mathbb{Z}$."

# Prerequisites

- **Space group** — The translation subgroup is part of a space group
- **Lattice** — Translations form a lattice

# Key Properties

1. Isomorphic to $\mathbb{Z} \times \mathbb{Z}$ in 2D (Theorem 12.19)
2. Infinite abelian group
3. Normal subgroup of the space group
4. $G/T \cong G_0$ (the point group)

# Relationships

## Related
- **Point group** — $G/T \cong G_0$

## Contrasts With
- **Point group** — Translation subgroup is infinite; point group is finite

# Source Reference

Chapter 12: Matrix Groups and Symmetry, Section 12.2, p. 165. Theorem 12.19.

# Verification Notes

- Definition source: Direct from p. 165
- Confidence: HIGH
