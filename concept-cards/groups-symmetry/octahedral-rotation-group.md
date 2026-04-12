---
# === CORE IDENTIFICATION ===
concept: Octahedral Rotation Group
slug: octahedral-rotation-group

# === CLASSIFICATION ===
category: symmetry-groups
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Finite Rotation Groups"
chapter_number: 19
pdf_page: 111
section: "Case (c)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "S_4 as rotation group"
  - "cubic rotation group"
  - "chiral octahedral group"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - finite-subgroups-of-so3
extends: []
related:
  - tetrahedral-rotation-group
  - icosahedral-rotation-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the rotational symmetry group of a regular octahedron (or cube)?"
---

# Quick Definition

The rotational symmetry group of a regular octahedron (equivalently, a cube) is isomorphic to $S_4$ (the symmetric group on 4 letters), a group of order 24. In the classification, it corresponds to Case (c) with stabilizer orders $(2, 3, 4)$.

# Core Definition

In the proof of Theorem 19.2, Case (c) gives $|G_x| = 2$, $|G_y| = 3$, $|G_z| = 4$, hence $|G| = 24$. The 6 poles in the orbit of $z$ are vertices of a regular octahedron, and $G$ is its rotational symmetry group (Armstrong, p. 115).

# Prerequisites

- **Finite subgroups of SO(3)** -- this is one of the classification cases

# Key Properties

1. Order 24
2. Isomorphic to $S_4$ (the cube has 4 main diagonals, permuted by rotations)
3. Three orbits of poles: 12 edge-midpoint poles, 8 vertex poles (of the cube), 6 face-centre poles (of the cube)
4. The cube and octahedron are dual solids sharing this rotation group
5. $-u = g^2(u)$ for antipodal poles in the orbit of $z$

# Context & Application

The octahedral/cubic rotation group is the symmetry group most commonly encountered in crystallography and chemistry for cubic symmetry.

# Examples

**Case (c)** (p. 115): The orbit of $z$ has 6 points. Choosing $u$ not equal to $\pm z$, the four points $u, g(u), g^2(u), g^3(u)$ form a square (where $g$ generates $G_z \cong \mathbb{Z}_4$). With $z$ and $-z$ included, all six form the vertices of a regular octahedron.

# Relationships

## Related
- **Tetrahedral rotation group** -- the smaller exceptional case ($A_4$)
- **Icosahedral rotation group** -- the larger exceptional case ($A_5$)

# Source Reference

Chapter 19: Finite Rotation Groups, Case (c), page 115.

# Verification Notes

- Construction: Direct from p. 115
- Confidence: HIGH -- explicit geometric construction
