---
# === CORE IDENTIFICATION ===
concept: Octahedron Symmetry Group
slug: octahedron-symmetry-group

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
  - "rotational symmetry group of the octahedron"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - cube-symmetry-group
  - dual-solids
extends: []
related:
  - platonic-solids
contrasts_with:
  - dodecahedron-symmetry-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the rotational symmetry group of the octahedron?"
---

# Quick Definition

The rotational symmetry group of the octahedron is isomorphic to $S_4$, the same as the cube, because the cube and octahedron are dual solids.

# Core Definition

Armstrong establishes: "Without further ado we can say that the rotational symmetry groups of the cube and the octahedron are isomorphic" (p. 46). This follows from the fact that they are dual solids: any symmetry of the cube is a symmetry of the inscribed octahedron, and vice versa.

# Prerequisites

- **Cube symmetry group** — The octahedron group is identified via duality with the cube
- **Dual solids** — The cube and octahedron are dual

# Key Properties

1. The octahedron has 24 rotational symmetries
2. The rotational symmetry group is isomorphic to $S_4$
3. The identification follows from duality with the cube

# Construction / Recognition

## To Verify:
1. Inscribe an octahedron in a cube (join centres of adjacent faces)
2. Observe that every rotation of the cube permutes the octahedron's vertices
3. Conclude the symmetry groups are identical

# Context & Application

The octahedron symmetry group exemplifies the power of duality: rather than analyzing the octahedron's symmetries directly, Armstrong deduces the result immediately from the cube analysis.

# Examples

**Example** (p. 46): Figure 8.3 shows the octahedron inscribed in a cube, with vertices at face centres.

# Relationships

## Builds Upon
- **Cube symmetry group** — Same group via duality
- **Dual solids** — The geometric relationship

## Contrasts With
- **Dodecahedron symmetry group** — $A_5$ rather than $S_4$

# Common Errors

- **Error**: Trying to analyze the octahedron's symmetries from scratch.
  **Correction**: Use duality with the cube to immediately conclude the group is $S_4$.

# Common Confusions

- **Confusion**: Thinking the octahedron has a different symmetry group from the cube because it has different faces.
  **Clarification**: Dual solids always have the same symmetry groups, regardless of face shape differences.

# Source Reference

Chapter 8: Plato's Solids and Cayley's Theorem, page 46 (pdf p. 46).

# Verification Notes

- Identification: Via duality, stated on p. 46
- Confidence: HIGH — explicit statement
