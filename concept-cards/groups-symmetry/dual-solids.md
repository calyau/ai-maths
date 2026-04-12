---
# === CORE IDENTIFICATION ===
concept: Dual Solids
slug: dual-solids

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
  - "dual polyhedra"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - platonic-solids
extends: []
related:
  - cube-symmetry-group
  - octahedron-symmetry-group
  - dodecahedron-symmetry-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are dual solids?"
  - "Which Platonic solids are dual to each other?"
---

# Quick Definition

Two solids are dual when joining the centres of adjacent faces of one produces the other. Dual solids have identical symmetry groups.

# Core Definition

"By joining up the centres of each pair of adjacent faces of a cube we can produce a regular octahedron inscribed in the cube. The same procedure carried out on an octahedron gives a cube inscribed in the octahedron, and we say that the cube and the octahedron are **dual solids**" (Armstrong, p. 46). "They clearly have the same amount of symmetry. Any symmetry of the cube is a symmetry of the inscribed dual octahedron, and vice versa" (p. 46).

# Prerequisites

- **Platonic solids** — Duality is a relationship between regular solids

# Key Properties

1. Cube and octahedron are dual
2. Dodecahedron and icosahedron are dual
3. The tetrahedron is self-dual (Exercise 8.2)
4. Dual solids have identical rotational symmetry groups
5. Dual solids have identical full symmetry groups
6. The duality operation is an involution (doing it twice returns the original)

# Construction / Recognition

## To Construct the Dual:
1. Take a convex regular solid
2. Place a vertex at the centre of each face
3. Connect vertices whose corresponding faces share an edge
4. The result is the dual solid

# Context & Application

Duality immediately halves the work needed to classify symmetry groups of Platonic solids. Since cube/octahedron are dual and dodecahedron/icosahedron are dual, Armstrong only needs to analyze three solids (tetrahedron, cube, dodecahedron) to determine all five symmetry groups.

# Examples

**Example** (p. 46): The octahedron inscribed in a cube is shown in Figure 8.3. Each vertex of the octahedron is at the centre of a face of the cube.

**Example** (p. 46): The dodecahedron and icosahedron are dual to one another.

# Relationships

## Related
- **Cube symmetry group** — Cube and octahedron are dual, both $\cong S_4$
- **Octahedron symmetry group** — Dual to cube
- **Dodecahedron symmetry group** — Dual to icosahedron, both $\cong A_5$

# Common Errors

- **Error**: Assuming dual solids have the same number of faces.
  **Correction**: Dual solids swap the roles of faces and vertices. The cube (6 faces, 8 vertices) is dual to the octahedron (8 faces, 6 vertices).

# Common Confusions

- **Confusion**: Thinking the tetrahedron must be dual to something else.
  **Clarification**: The tetrahedron is self-dual: joining face centres of a tetrahedron produces another tetrahedron.

# Source Reference

Chapter 8: Plato's Solids and Cayley's Theorem, page 46 (pdf p. 46). Figure 8.3 shows the construction.

# Verification Notes

- Definition: Direct from p. 46
- Duality pairs: Explicit on p. 46
- Confidence: HIGH — clear definition with figure
