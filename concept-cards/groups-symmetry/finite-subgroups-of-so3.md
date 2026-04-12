---
# === CORE IDENTIFICATION ===
concept: Finite Subgroups of SO(3)
slug: finite-subgroups-of-so3

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
section: "Theorem 19.2"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "classification of finite rotation groups"
  - "finite rotation groups in 3D"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - counting-theorem
  - orbit-stabilizer-theorem
  - poles-of-rotation
  - finite-subgroups-of-o2
extends:
  - finite-subgroups-of-o2
related:
  - finite-subgroups-of-o3
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are all finite subgroups of SO(3)?"
  - "What are the finite rotation groups in three dimensions?"
---

# Quick Definition

A finite subgroup of $SO_3$ is isomorphic to either a cyclic group, a dihedral group, or the rotational symmetry group of one of the regular solids (tetrahedron $A_4$, octahedron/cube $S_4$, or icosahedron/dodecahedron $A_5$).

# Core Definition

**(19.2) Theorem.** A finite subgroup of $SO_3$ is isomorphic either to a cyclic group, a dihedral group, or the rotational symmetry group of one of the regular solids (Armstrong, p. 112).

The five possibilities are:
- **Cyclic group** $\mathbb{Z}_n$ (order $n$, any $n \ge 1$)
- **Dihedral group** $D_n$ (order $2n$, any $n \ge 2$)
- **Tetrahedral group** $A_4$ (order 12)
- **Octahedral group** $S_4$ (order 24)
- **Icosahedral group** $A_5$ (order 60)

# Prerequisites

- **Counting theorem** -- applied to the action on poles to derive the Diophantine equation
- **Orbit-Stabilizer theorem** -- used throughout the proof
- **Poles of rotation** -- the geometric objects whose orbits are analysed
- **Finite subgroups of O(2)** -- the $N = 2$ case reduces to this

# Key Properties

1. The proof produces a Diophantine equation from the Counting Theorem applied to poles
2. The number of pole orbits $N$ is either 2 or 3
3. $N = 2$ yields cyclic groups
4. $N = 3$ yields four cases based on stabilizer orders:
   - $(2, 2, n)$: dihedral group $D_n$ (order $2n$)
   - $(2, 3, 3)$: $A_4$ (order 12)
   - $(2, 3, 4)$: $S_4$ (order 24)
   - $(2, 3, 5)$: $A_5$ (order 60)
5. In each case, the poles are identified as vertices/edge-midpoints/face-centres of a regular solid

# Construction / Recognition

## Proof Structure (pp. 112--117):
1. Let $G$ be a finite subgroup of $SO_3$ and $X$ the set of poles of non-identity elements
2. $G$ acts on $X$; apply the Counting Theorem: $N = \frac{1}{|G|}\{2(|G|-1) + |X|\}$
3. Rearrange to: $2(1 - 1/|G|) = \sum_{i=1}^{N}(1 - 1/|G_{x_i}|)$
4. Since $1 \le \text{LHS} < 2$ and each summand is $\ge 1/2$, we get $N = 2$ or $N = 3$
5. Enumerate all solutions $(|G_{x_1}|, |G_{x_2}|, |G_{x_3}|)$ when $N = 3$
6. For each case, construct the regular solid from the pole configuration

# Context & Application

This is one of the most beautiful classification theorems in algebra. It connects finite group theory with the geometry of Platonic solids, showing that the five types of finite rotation groups in 3D correspond precisely to the regular solids known since antiquity.

# Examples

**Case (a)** (p. 113): Stabilizer orders $(2, 2, n)$ give the dihedral group. The poles form a regular $n$-gon plus its centre axis.

**Case (b)** (p. 114): Stabilizer orders $(2, 3, 3)$ give $|G| = 12$. The 4 poles with stabilizer of order 3 are vertices of a regular tetrahedron. $G \cong A_4$.

**Case (c)** (p. 115): Stabilizer orders $(2, 3, 4)$ give $|G| = 24$. The 6 poles with stabilizer of order 4 are vertices of a regular octahedron. $G \cong S_4$.

**Case (d)** (p. 115): Stabilizer orders $(2, 3, 5)$ give $|G| = 60$. The 12 poles with stabilizer of order 5 are vertices of a regular icosahedron. $G \cong A_5$.

# Relationships

## Builds Upon
- **Counting theorem** -- produces the Diophantine equation
- **Orbit-Stabilizer theorem** -- determines orbit and stabilizer sizes
- **Poles of rotation** -- the geometric objects analysed
- **Finite subgroups of O(2)** -- handles the $N = 2$ case

## Enables
- **Finite subgroups of O(3)** -- extends to the full orthogonal group (Exercise 19.5)

## Related
- **Regular solids** -- the classification is tied to Platonic solids

# Common Errors

- **Error**: Forgetting that the dihedral groups include $D_2 \cong \mathbb{Z}_2 \times \mathbb{Z}_2$ (Klein's four-group).
  **Correction**: Case (a) with $n = 2$ gives Klein's group, which Armstrong treats as a degenerate dihedral group.

# Common Confusions

- **Confusion**: Thinking the list includes a "dodecahedral group" separate from the icosahedral group.
  **Clarification**: The icosahedron and dodecahedron are dual solids sharing the same rotation group $A_5$.

# Source Reference

Chapter 19: Finite Rotation Groups, Theorem 19.2, pages 112--117. Proof spans Cases (a)--(d) with geometric constructions.

# Verification Notes

- Theorem and proof: Direct from pp. 112--117
- All four cases verified against source
- Confidence: HIGH -- the central theorem of the chapter, proved in detail
