---
concept: Finite Subgroups of the Rotation Group
slug: finite-subgroups-of-rotation-group
category: symmetry
subcategory: geometric-symmetry
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Symmetry"
chapter_number: 6
pdf_page: 162
section: "6.12 Finite Subgroups of the Rotation Group"
extraction_confidence: high
aliases: []
prerequisites:
  - special-orthogonal-group
  - counting-formula
  - spin
extends: []
related:
  - tetrahedral-group
  - octahedral-group
  - icosahedral-group
  - dihedral-group
  - cyclic-rotation-group
contrasts_with: []
answers_questions:
  - "What are the finite subgroups of SO_3?"
  - "How do symmetry groups relate to geometric figures?"
---

# Quick Definition

The finite subgroups of SO_3 are: the cyclic groups C_k, the dihedral groups D_k, the tetrahedral group T (order 12), the octahedral group O (order 24), and the icosahedral group I (order 60). These are the rotation groups of the Platonic solids.

# Core Definition

A finite subgroup of SO_3 is one of the following: C_k (rotations by multiples of 2pi/k about a line), D_k (symmetries of a regular k-gon), T (12 rotational symmetries of a tetrahedron), O (24 rotational symmetries of a cube/octahedron), or I (60 rotational symmetries of a dodecahedron/icosahedron) (Artin, Theorem 6.12.1, p. 194).

# Prerequisites

- **Special orthogonal group** — Finite subgroups of SO_3
- **Counting formula** — Used in the classification proof
- **Spin** — Counting spins gives the key equation

# Key Properties

1. Classification is achieved by counting poles (fixed points on the unit sphere)
2. The key equation: sum(1 - 1/r_i) = 2 - 2/N
3. At most 3 orbits of poles
4. The possible orbit data (r_1, r_2, r_3; n_1, n_2, n_3; N) are severely restricted
5. All five types are realized as symmetry groups of the Platonic solids

# Construction / Recognition

## Classification Method:
1. Count poles of group elements on the unit sphere
2. The equation sum(1 - 1/r_i) = 2 - 2/N restricts to at most 3 orbits
3. Enumerate all solutions: cyclic, dihedral, tetrahedral, octahedral, icosahedral

# Context & Application

This classification is one of the most beautiful results in elementary group theory, connecting algebra to the geometry of regular polyhedra. It is proved entirely by counting arguments using the orbit-stabilizer theorem.

# Examples

**Example 1** (p. 195): The tetrahedral group T has 14 poles: 4+4 (faces/vertices, r=3) and 6 (edges, r=2). Data: r_i = 2, 3, 3; n_i = 6, 4, 4; N = 12.

**Example 2** (p. 198): For the icosahedral group: r_i = 2, 3, 5; n_i = 30, 20, 12; N = 60. The 12 poles with r=5 are the vertices of an icosahedron.

# Relationships

## Builds Upon
- **Counting formula** — The classification is a counting argument
- **Spin** — Counting spins yields the key equation

## Enables
- **Simplicity of A_5** — The icosahedral group I is shown simple (Section 7.4)

## Related
- **Platonic solids** — Each finite subgroup is a symmetry group of a regular solid

# Common Errors

- **Error**: Forgetting that dihedral groups are also subgroups of SO_3
  **Correction**: In R^3, reflections of a polygon become rotations by pi about perpendicular axes

# Common Confusions

- **Confusion**: Thinking the octahedral and cube groups are different
  **Clarification**: They are the same group -- the cube and octahedron are dual polyhedra

# Source Reference

Chapter 6: Symmetry, Section 6.12, Theorem 6.12.1, pages 194-199.

# Verification Notes

- Definition source: Direct from Theorem 6.12.1
- Confidence rationale: Major classification theorem
- Uncertainties: None
- Cross-reference status: Verified
