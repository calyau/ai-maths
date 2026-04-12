---
# === CORE IDENTIFICATION ===
concept: Tetrahedral Rotation Group
slug: tetrahedral-rotation-group

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
section: "Case (b)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "A_4 as rotation group"
  - "chiral tetrahedral group"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - finite-subgroups-of-so3
extends: []
related:
  - octahedral-rotation-group
  - icosahedral-rotation-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the rotational symmetry group of a regular tetrahedron?"
---

# Quick Definition

The rotational symmetry group of a regular tetrahedron is isomorphic to $A_4$ (the alternating group on 4 letters), a group of order 12. In the classification of finite subgroups of $SO_3$, it corresponds to Case (b) with stabilizer orders $(2, 3, 3)$.

# Core Definition

In the proof of Theorem 19.2, Case (b) gives $|G_x| = 2$, $|G_y| = |G_z| = 3$, hence $|G| = 12$. The orbit of $z$ has 4 points which form the vertices of a regular tetrahedron, and $G$ is its rotational symmetry group, isomorphic to $A_4$ (Armstrong, p. 114).

# Prerequisites

- **Finite subgroups of SO(3)** -- this is one of the cases in the classification

# Key Properties

1. Order 12 ($= 2 \cdot 3 \cdot 2 = 12$ from the stabilizer analysis)
2. Three orbits of poles: 6 edge-midpoint poles, 4 vertex poles (with stabilizer $\mathbb{Z}_3$), 4 face-centre poles (with stabilizer $\mathbb{Z}_3$)
3. Isomorphic to $A_4$
4. Contains no element of order 6

# Context & Application

The tetrahedral rotation group is the smallest exceptional (non-cyclic, non-dihedral) finite rotation group. It appears in both the classification of finite rotation groups and the classification of groups of order 12.

# Examples

**Case (b)** (p. 114): Choose $u$ in the orbit of $z$ with $0 < \|z - u\| < 2$, and a generator $g$ of $G_z$. Then $u, g(u), g^2(u)$ form an equilateral triangle equidistant from $z$, and $z, u, g(u), g^2(u)$ are vertices of a regular tetrahedron.

# Relationships

## Related
- **Octahedral rotation group** -- the next exceptional case ($S_4$, order 24)
- **Icosahedral rotation group** -- the largest exceptional case ($A_5$, order 60)

# Source Reference

Chapter 19: Finite Rotation Groups, Case (b), page 114.

# Verification Notes

- Construction: Direct from p. 114
- Confidence: HIGH -- explicit geometric construction
