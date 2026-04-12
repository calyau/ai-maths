---
# === CORE IDENTIFICATION ===
concept: Full Symmetry Groups of Platonic Solids
slug: full-symmetry-groups-of-solids

# === CLASSIFICATION ===
category: structure-theory
subcategory: classification
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
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - internal-direct-product-criterion
  - central-inversion
  - cube-symmetry-group
  - dodecahedron-symmetry-group
extends: []
related:
  - platonic-solids
  - direct-product
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the full symmetry groups of the Platonic solids?"
  - "How do direct products describe symmetry groups?"
---

# Quick Definition

The full symmetry groups (including reflections) of the Platonic solids are: tetrahedron $\cong S_4$, cube/octahedron $\cong S_4 \times \mathbb{Z}_2$, dodecahedron/icosahedron $\cong A_5 \times \mathbb{Z}_2$.

# Core Definition

Armstrong applies Theorem 10.2 to determine the full symmetry groups of the Platonic solids (p. 62). For solids with central inversion symmetry, the full symmetry group $G$ is isomorphic to $H \times \langle f_J \rangle \cong H \times \mathbb{Z}_2$, where $H$ is the subgroup of rotational symmetries:

- Cube and octahedron: $G \cong S_4 \times \mathbb{Z}_2$
- Dodecahedron and icosahedron: $G \cong A_5 \times \mathbb{Z}_2$

The tetrahedron is the exception: it lacks central inversion, so its full symmetry group is $S_4$ (not $A_4 \times \mathbb{Z}_2$).

# Prerequisites

- **Internal direct product criterion** — Theorem 10.2 provides the decomposition
- **Central inversion** — The $\mathbb{Z}_2$ factor comes from $\{I, -I\}$
- **Cube symmetry group** — Rotational group $\cong S_4$
- **Dodecahedron symmetry group** — Rotational group $\cong A_5$

# Key Properties

1. Tetrahedron full symmetry group: $S_4$ (order 24)
2. Cube full symmetry group: $S_4 \times \mathbb{Z}_2$ (order 48)
3. Octahedron full symmetry group: $S_4 \times \mathbb{Z}_2$ (order 48)
4. Dodecahedron full symmetry group: $A_5 \times \mathbb{Z}_2$ (order 120)
5. Icosahedron full symmetry group: $A_5 \times \mathbb{Z}_2$ (order 120)
6. The tetrahedron is the only Platonic solid without central inversion
7. For solids with central inversion: full group = rotational group $\times \mathbb{Z}_2$

# Construction / Recognition

## To Determine the Full Symmetry Group:
1. Find the rotational symmetry group $H$
2. Check if the solid has central inversion symmetry
3. If yes: full group $\cong H \times \mathbb{Z}_2$
4. If no: analyze the full group separately (as for the tetrahedron)

# Context & Application

This result completes the classification of symmetry groups of all five Platonic solids, bringing together the rotational groups from Chapter 8, the matrix group framework from Chapter 9, and the direct product construction from Chapter 10.

# Examples

**Example** (p. 62): For the cube centred at the origin:
- $H = $ rotational symmetries $\cong S_4$
- $K = \{I, -I\} \cong \mathbb{Z}_2$
- $HK = G$ (full symmetry group)
- $H \cap K = \{I\}$
- $-I$ commutes with everything
- Therefore $G \cong S_4 \times \mathbb{Z}_2$

# Relationships

## Builds Upon
- **Direct product** — Full groups are direct products
- **Central inversion** — The $\mathbb{Z}_2$ factor
- **Rotational symmetry groups** — The other factor

## Related
- **Platonic solids** — The geometric objects being studied

# Common Errors

- **Error**: Applying the direct product decomposition to the tetrahedron.
  **Correction**: The tetrahedron lacks central inversion, so its full group $S_4$ does not decompose as $A_4 \times \mathbb{Z}_2$.

# Common Confusions

- **Confusion**: Thinking the full symmetry group is always double the rotational group.
  **Clarification**: For solids with central inversion, $|G| = 2|H|$, which holds because the direct product with $\mathbb{Z}_2$ doubles the order. For the tetrahedron, $|G| = 2|H|$ also holds but the structure is $S_4$, not $A_4 \times \mathbb{Z}_2$.

# Source Reference

Chapter 10: Products, page 62 (pdf p. 62). Application of Theorem 10.2.

# Verification Notes

- Results: All stated on p. 62
- Tetrahedron exception: Explicit on p. 62
- Confidence: HIGH — definitive classification
