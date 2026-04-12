---
# === CORE IDENTIFICATION ===
concept: Central Inversion
slug: central-inversion

# === CLASSIFICATION ===
category: structure-theory
subcategory: symmetry-operations
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Products"
chapter_number: 10
pdf_page: 59
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "f_J"
  - "inversion through the origin"
  - "-I"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonal-group
extends: []
related:
  - direct-product
  - full-symmetry-groups-of-solids
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is central inversion?"
  - "Which Platonic solids have central inversion as a symmetry?"
---

# Quick Definition

Central inversion is the linear transformation $f_J: \mathbb{R}^3 \to \mathbb{R}^3$ sending each vector $\mathbf{x}$ to $-\mathbf{x}$, represented by the matrix $J = -I_3$.

# Core Definition

"The linear transformation $f_J: \mathbb{R}^3 \to \mathbb{R}^3$ sends each vector $\mathbf{x}$ to $-\mathbf{x}$ and is called *central inversion*" (Armstrong, p. 62). The matrix $J = -I_3$ satisfies $J^2 = I$, so $\{I, J\}$ forms a subgroup of $O_3$ isomorphic to $\mathbb{Z}_2$. Both $I$ and $J$ commute with every element of $O_3$.

# Prerequisites

- **Orthogonal group** — Central inversion is an element of $O_3$

# Key Properties

1. $J = -I_3$ has determinant $(-1)^3 = -1$ (in $O_3$ but not $SO_3$)
2. $J^2 = I$ (order 2)
3. $J$ commutes with every element of $O_3$
4. $\{I, J\} \cong \mathbb{Z}_2$
5. All Platonic solids except the tetrahedron have central inversion as a symmetry
6. Central inversion sends each vertex to the diametrically opposite vertex

# Construction / Recognition

## To Identify Central Inversion:
1. For a solid centred at the origin, check if $-\mathbf{x}$ is a vertex whenever $\mathbf{x}$ is
2. If so, the solid has central inversion symmetry

# Context & Application

Central inversion is the key ingredient for decomposing the full symmetry groups of regular solids as direct products. Since $J$ commutes with everything and has order 2, Theorem 10.2 allows writing the full symmetry group as a direct product of the rotation group and $\{I, J\} \cong \mathbb{Z}_2$ -- provided the solid has central inversion symmetry.

# Examples

**Example** (p. 62): The cube has central inversion: each vertex $(x, y, z)$ pairs with $(-x, -y, -z)$.

**Example** (p. 62): The tetrahedron does NOT have central inversion, which is why its full symmetry group is $S_4$ rather than $A_4 \times \mathbb{Z}_2$.

# Relationships

## Related
- **Direct product** — Enables the decomposition $G \cong H \times \mathbb{Z}_2$
- **Full symmetry groups of solids** — Central inversion determines whether the full group is a direct product

# Common Errors

- **Error**: Assuming all regular solids have central inversion.
  **Correction**: The tetrahedron is the exception. It does not have central inversion because no vertex is diametrically opposite another vertex.

# Common Confusions

- **Confusion**: Confusing central inversion with reflection.
  **Clarification**: Central inversion ($\mathbf{x} \mapsto -\mathbf{x}$) negates all coordinates simultaneously. A reflection negates only the component perpendicular to the reflection plane. In 3D, central inversion has determinant $-1$ and is orientation-reversing.

# Source Reference

Chapter 10: Products, page 62 (pdf p. 62).

# Verification Notes

- Definition: Direct from p. 62
- Exception for tetrahedron: Stated on p. 62
- Confidence: HIGH — explicit definition and treatment
