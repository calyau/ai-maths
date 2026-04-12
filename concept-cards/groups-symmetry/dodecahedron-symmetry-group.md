---
# === CORE IDENTIFICATION ===
concept: Dodecahedron Symmetry Group
slug: dodecahedron-symmetry-group

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
  - "rotational symmetry group of the dodecahedron"
  - "icosahedron symmetry group"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - alternating-group
  - isomorphism
  - dual-solids
extends: []
related:
  - platonic-solids
  - three-cycle-generation
contrasts_with:
  - cube-symmetry-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the rotational symmetry group of the dodecahedron?"
  - "What is the rotational symmetry group of the icosahedron?"
---

# Quick Definition

The rotational symmetry group of the dodecahedron (and its dual, the icosahedron) has 60 elements and is isomorphic to the alternating group $A_5$.

# Core Definition

Armstrong outlines a proof that the rotational symmetry group of the dodecahedron is isomorphic to $A_5$ (pp. 47-48). The argument proceeds by: (i) counting 60 rotational symmetries, (ii) noting $|A_5| = 60$, (iii) showing that five cubes can be inscribed in the dodecahedron such that rotations permute these cubes, (iv) showing every 3-cycle in $S_5$ arises from a rotation (by considering rotations about vertex axes), and (v) using Theorem 6.5 that 3-cycles generate $A_5$.

# Prerequisites

- **Alternating group** — The dodecahedron group is isomorphic to $A_5$
- **Isomorphism** — The identification is via an isomorphism
- **Dual solids** — The icosahedron has the same group by duality

# Key Properties

1. The dodecahedron has 60 rotational symmetries
2. The rotational symmetry group is isomorphic to $A_5$
3. The icosahedron (dual) has the same rotational symmetry group
4. Five cubes can be inscribed in a dodecahedron
5. Each rotation permutes these five cubes, giving elements of $S_5$
6. All resulting permutations are even (they land in $A_5$)
7. Every 3-cycle arises from a rotation about a vertex-to-vertex axis

# Construction / Recognition

## Proof Outline (p. 47-48):
1. Count 60 rotational symmetries of the dodecahedron
2. Note $|A_5| = 60$
3. Number the five inscribed cubes 1-5
4. Each rotation induces a permutation in $S_5$
5. Show every 3-cycle in $S_5$ is induced by some rotation
6. Since 3-cycles generate $A_5$ (Theorem 6.5), the image contains $A_5$
7. Since both have 60 elements, the map is an isomorphism

# Context & Application

The identification of the dodecahedron symmetry group with $A_5$ is the deepest result in this chapter. It connects beautiful geometry to one of the most important groups in algebra. The simplicity of $A_5$ (proved later) means the dodecahedron/icosahedron have the richest symmetry structure among the Platonic solids.

# Examples

**Example** (p. 47): Figure 8.4 shows a cube inscribed in a dodecahedron, where each edge of the cube is a diagonal of a pentagonal face.

# Relationships

## Builds Upon
- **Alternating group** — The dodecahedron group $\cong A_5$
- **Three-cycle generation** — Used to prove the isomorphism

## Related
- **Platonic solids** — The dodecahedron is one of five
- **Dual solids** — Icosahedron shares the same group

## Contrasts With
- **Cube symmetry group** — Cube rotational symmetries $\cong S_4$, not $A_5$

# Common Errors

- **Error**: Permuting vertices of the dodecahedron (20 vertices) rather than inscribed cubes.
  **Correction**: The key insight is to permute the 5 inscribed cubes, giving elements of $S_5$.

# Common Confusions

- **Confusion**: Thinking $A_5$ has order 120 (confusing with $S_5$).
  **Clarification**: $|A_5| = 5!/2 = 60$, matching the 60 rotational symmetries.

# Source Reference

Chapter 8: Plato's Solids and Cayley's Theorem, pages 47-48 (pdf pp. 47-48). Proof outline with five steps; Figure 8.4.

# Verification Notes

- Count: 60 rotational symmetries, stated on p. 47
- Isomorphism: Outlined on pp. 47-48
- Confidence: HIGH — detailed argument with figures
