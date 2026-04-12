---
# === CORE IDENTIFICATION ===
concept: Cube Symmetry Group
slug: cube-symmetry-group

# === CLASSIFICATION ===
category: symmetry-groups
subcategory: polyhedra
tier: intermediate

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Plato's Solids and Cayley's Theorem"
chapter_number: 8
pdf_page: 44
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "rotational symmetry group of the cube"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - symmetric-group
  - isomorphism
extends: []
related:
  - octahedron-symmetry-group
  - dual-solids
  - platonic-solids
contrasts_with:
  - dodecahedron-symmetry-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the rotational symmetry group of the cube?"
  - "How many rotational symmetries does a cube have?"
---

# Quick Definition

The rotational symmetry group of the cube has 24 elements and is isomorphic to $S_4$, via the permutation action on the four principal diagonals.

# Core Definition

A cube has 24 rotational symmetries (Armstrong, p. 44). Each rotational symmetry permutes the four principal diagonals of the cube. Armstrong proves this correspondence gives an isomorphism from the cube's symmetry group $G$ to $S_4$ by showing the map $\varphi: G \to S_4$ is surjective (since the rotation $r$ induces the 4-cycle $(1234)$ and the rotation $t$ induces $(12)$, which together generate $S_4$ by Theorem 6.3) and then using the fact that a surjection between finite sets of equal size is a bijection (p. 46).

# Prerequisites

- **Symmetric group** — The cube group is isomorphic to $S_4$
- **Isomorphism** — The identification is via an isomorphism

# Key Properties

1. The cube has 24 rotational symmetries
2. Three types of axes: face-to-face (type L, 3 axes, 9 rotations), edge-to-edge (type M, 6 axes, 6 rotations), vertex-to-vertex (type N, 4 axes, 8 rotations), plus identity
3. The rotational symmetry group is isomorphic to $S_4$
4. The isomorphism sends each rotation to the permutation it induces on the 4 principal diagonals
5. The rotation $r$ about a face axis induces $(1234)$; the rotation $t$ about an edge axis induces $(12)$

# Construction / Recognition

## To Count Rotational Symmetries:
1. Find axes of type L (face-center to face-center): 3 axes, each with rotations through $\pi/2$, $\pi$, $3\pi/2$ (9 total)
2. Find axes of type M (midpoint of edge to midpoint of opposite edge): 6 axes, each with rotation through $\pi$ (6 total)
3. Find axes of type N (vertex to opposite vertex): 4 axes, each with rotations through $2\pi/3$, $4\pi/3$ (8 total)
4. Add identity: $9 + 6 + 8 + 1 = 24$

# Context & Application

The cube symmetry group is one of the most important finite groups studied in this text. Its identification with $S_4$ demonstrates the power of finding the right geometric feature to permute (principal diagonals rather than vertices). The full symmetry group (including reflections) is $S_4 \times \mathbb{Z}_2$ (Chapter 10).

# Examples

**Example** (p. 45-46): The rotation $r$ (about an L-type axis) sends diagonal $N_k$ to $N_{k+1}$ cyclically, giving the permutation $(1234)$. The rotation $s$ (about an N-type axis) gives $(143)$. The rotation $t$ (about an M-type axis) gives $(12)$.

# Relationships

## Builds Upon
- **Symmetric group** — The cube group $\cong S_4$

## Related
- **Octahedron symmetry group** — Also $\cong S_4$ (dual solid)
- **Dual solids** — Cube and octahedron are dual

## Contrasts With
- **Dodecahedron symmetry group** — Rotational symmetries $\cong A_5$, not $S_4$

# Common Errors

- **Error**: Trying to establish the isomorphism by permuting vertices (8 vertices, leading to $S_8$).
  **Correction**: Armstrong notes that permuting the 4 principal diagonals gives a much cleaner isomorphism to $S_4$.

# Common Confusions

- **Confusion**: Confusing the rotational symmetry group ($\cong S_4$, order 24) with the full symmetry group ($\cong S_4 \times \mathbb{Z}_2$, order 48).
  **Clarification**: The rotational group contains only rotations. The full group also includes reflections and improper rotations.

# Source Reference

Chapter 8: Plato's Solids and Cayley's Theorem, pages 44-46 (pdf pp. 44-46). Counting on p. 44; isomorphism argument on pp. 45-46.

# Verification Notes

- Count: 24 rotational symmetries, explicit on p. 44
- Isomorphism: Proved on pp. 45-46
- Confidence: HIGH — detailed proof with figures
