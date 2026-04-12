---
# === CORE IDENTIFICATION ===
concept: Icosahedral Rotation Group
slug: icosahedral-rotation-group

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
section: "Case (d)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "A_5 as rotation group"
  - "chiral icosahedral group"
  - "dodecahedral rotation group"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - finite-subgroups-of-so3
extends: []
related:
  - tetrahedral-rotation-group
  - octahedral-rotation-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the rotational symmetry group of a regular icosahedron (or dodecahedron)?"
---

# Quick Definition

The rotational symmetry group of a regular icosahedron (equivalently, a dodecahedron) is isomorphic to $A_5$ (the alternating group on 5 letters), a group of order 60. It corresponds to Case (d) with stabilizer orders $(2, 3, 5)$.

# Core Definition

In the proof of Theorem 19.2, Case (d) gives $|G_x| = 2$, $|G_y| = 3$, $|G_z| = 5$, hence $|G| = 60$. The 12 poles in the orbit of $z$ are vertices of a regular icosahedron, and $G$ is its rotational symmetry group (Armstrong, pp. 115--117).

# Prerequisites

- **Finite subgroups of SO(3)** -- this is the final case in the classification

# Key Properties

1. Order 60
2. Isomorphic to $A_5$ (the only simple group of order 60)
3. Three orbits of poles: 30 edge-midpoint poles, 20 face-centre poles (stabilizer $\mathbb{Z}_3$), 12 vertex poles (stabilizer $\mathbb{Z}_5$)
4. The orbit of $z$ has 12 points forming two nested pentagons plus $z$ and $-z$
5. The icosahedron and dodecahedron are dual solids sharing this rotation group

# Context & Application

The icosahedral group is the largest finite rotation group and is connected to the non-solvability of the quintic equation (via the simplicity of $A_5$). It also appears in the study of fullerene molecules and virus capsid symmetry.

# Examples

**Case (d)** (pp. 115--117): The 12 poles form two pentagons (one "near" $z$, one "far") plus $\pm z$. The near pentagon vertices are $u, g(u), g^2(u), g^3(u), g^4(u)$ (where $g$ generates $G_z \cong \mathbb{Z}_5$). The far pentagon has vertices $-u, -g(u), \ldots, -g^4(u)$. All 12 points lie at vertices of a regular icosahedron.

# Relationships

## Related
- **Tetrahedral rotation group** -- the smallest exceptional case ($A_4$)
- **Octahedral rotation group** -- the middle exceptional case ($S_4$)

# Source Reference

Chapter 19: Finite Rotation Groups, Case (d), pages 115--117.

# Verification Notes

- Construction: Direct from pp. 115--117
- Confidence: HIGH -- detailed geometric construction in source
