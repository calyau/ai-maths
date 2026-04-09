---
concept: Point Group
slug: point-group
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
  - orthogonal-group
  - space-group
extends: []
related:
  - translation-subgroup
  - wallpaper-group
contrasts_with:
  - translation-subgroup
answers_questions:
  - "What is a point group?"
---

# Quick Definition

The point group of a space group $G$ is $G_0 = \{A : (A, \mathbf{b}) \in G \text{ for some } \mathbf{b}\}$, the collection of linear parts. It is a finite subgroup of $O(n)$. In 2D, point groups are $\mathbb{Z}_n$ or $D_n$ for $n = 1, 2, 3, 4, 6$.

# Core Definition

"The point group of $G$ is $G_0 = \{A : (A, \mathbf{b}) \in G \text{ for some } \mathbf{b}\}$. In particular, $G_0$ must be a subgroup of $O(2)$" (Judson, p. 165). By Theorem 12.20, "The point group in the wallpaper groups is isomorphic to $\mathbb{Z}_n$ or $D_n$, where $n = 1, 2, 3, 4, 6$."

# Prerequisites

- **Orthogonal group** — $G_0 \leq O(n)$
- **Space group** — The point group is part of a space group

# Key Properties

1. $G_0$ is a finite subgroup of $O(n)$
2. $G/T \cong G_0$ where $T$ is the translation subgroup
3. In 2D: $G_0 \in \{\mathbb{Z}_1, \mathbb{Z}_2, \mathbb{Z}_3, \mathbb{Z}_4, \mathbb{Z}_6, D_1, D_2, D_3, D_4, D_6\}$

# Relationships

## Related
- **Translation subgroup** — The other component of a space group

## Contrasts With
- **Translation subgroup** — Point group is finite; translation group is infinite

# Source Reference

Chapter 12: Matrix Groups and Symmetry, Section 12.2, p. 165. Theorem 12.20.

# Verification Notes

- Definition source: Direct from p. 165
- Confidence: HIGH
