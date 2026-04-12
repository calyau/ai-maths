---
# === CORE IDENTIFICATION ===
concept: Tetrahedron Symmetry Group
slug: tetrahedron-symmetry-group

# === CLASSIFICATION ===
category: symmetry-groups
subcategory: polyhedra
tier: foundational

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Symmetries of the Tetrahedron"
chapter_number: 1
pdf_page: 8
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - rotational symmetry group of the tetrahedron
  - "A_4 (alternating group on 4 elements)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - symmetry-group
  - rotational-symmetry
  - axis-of-symmetry
  - composition-of-symmetries
extends:
  - symmetry-group
related:
  - alternating-group
  - dihedral-group
  - group
  - platonic-solids
  - cube-symmetry-group
contrasts_with:
  - cube-symmetry-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
  - "What is a symmetry group?"
  - "What is the rotational symmetry group of the tetrahedron?"
---

# Quick Definition

The rotational symmetry group of the regular tetrahedron consists of exactly 12 rotations: 8 rotations about vertex-to-face axes, 3 rotations about edge-midpoint axes, and the identity. It is non-commutative and isomorphic to $A_4$.

# Core Definition

"The twelve symmetries of the tetrahedron together with this algebraic structure make up its rotational symmetry group" (Armstrong, Ch. 1, p. 11). The group has order 12 and is non-abelian. Its elements can all be expressed in terms of two generators $r$ and $s$, where $r$ is rotation through $2\pi/3$ about a vertex axis and $s$ is rotation through $\pi$ about an edge-midpoint axis.

In Chapter 7 (Example ii, p. 41), Armstrong proves this group is isomorphic to $A_4$ by numbering the vertices 1-4 and showing each rotation induces an even permutation. The full symmetry group (including reflections) is isomorphic to $S_4$ (Exercise 8.11, p. 50).

# Prerequisites

- **Symmetry Group** — This is a specific symmetry group
- **Rotational Symmetry** — Its elements are rotations
- **Axis of Symmetry** — Its rotations are organized by axis type
- **Composition of Symmetries** — Its group operation

# Key Properties

1. Has exactly 12 elements (order 12)
2. Is non-commutative (non-abelian)
3. Contains 4 axes of type L (vertex to opposite face centroid), each supporting 2 non-trivial rotations
4. Contains 3 axes of type M (midpoints of opposite edges), each supporting 1 non-trivial rotation
5. Has 3 elements of order 2 (the rotations through $\pi$ about type-M axes)
6. No single rotation generates the entire group
7. The three order-2 elements commute with one another
8. Isomorphic to $A_4$ via the vertex permutation correspondence (Ch. 7, p. 41)
9. The full symmetry group (rotations + reflections) is isomorphic to $S_4$ (Exercise 8.11)
10. Unlike the cube and dodecahedron, the tetrahedron lacks central inversion symmetry

# Construction / Recognition

## To Construct:
1. Label the four vertices of the tetrahedron (1, 2, 3, 4)
2. Identify 4 axes through each vertex and the centroid of the opposite face
3. For each vertex axis, record rotations of $2\pi/3$ and $4\pi/3$
4. Identify 3 axes through midpoints of opposite edges
5. For each edge axis, record rotation of $\pi$
6. Include the identity
7. Total: $(4 \times 2) + 3 + 1 = 12$

# Context & Application

This is the central motivating example of the book. Armstrong uses it in Chapter 1 to introduce all the key concepts (composition, identity, inverses, associativity, non-commutativity) that become the group axioms in Chapter 2. In later chapters, the tetrahedron serves as the simplest Platonic solid for demonstrating the connection between geometry and algebra.

# Examples

**Example 1** (p. 8): Counting: 4 vertex axes x 2 rotations each = 8, plus 3 edge-midpoint axes x 1 rotation each = 3, plus 1 identity = 12.

**Example 2** (p. 10): With $r$ = rotation through $2\pi/3$ about axis L and $s$ = rotation through $\pi$ about axis M: $rs$ and $sr$ are different symmetries, demonstrating non-commutativity.

**Example 3** (p. 41): Numbering vertices 1-4, the rotation $r$ about the axis through vertex 1 induces the permutation $(234)$, and $s$ induces $(14)(23)$.

# Relationships

## Builds Upon
- **Symmetry Group** — This is a concrete instance

## Enables
- **Group** — Motivates the abstract definition
- **Associativity** — Demonstrated concretely here

## Related
- **Alternating group** — Rotational symmetries $\cong A_4$
- **Platonic solids** — The tetrahedron is one of five
- **Dihedral Group** — Another family of symmetry groups

## Contrasts With
- **Cube symmetry group** — Cube rotational symmetries $\cong S_4$, tetrahedron $\cong A_4$

# Common Errors

- **Error**: Confusing the rotational symmetry group (12 elements, $\cong A_4$) with the full symmetry group including reflections (24 elements, $\cong S_4$).
  **Correction**: Armstrong treats only rotational symmetries in Chapter 1; the full group has 24 elements (Exercise 8.11).

# Common Confusions

- **Confusion**: Expecting the full symmetry group to be $A_4 \times \mathbb{Z}_2$.
  **Clarification**: Unlike the cube and dodecahedron, the tetrahedron lacks central inversion symmetry, so its full group is $S_4$, not $A_4 \times \mathbb{Z}_2$ (Chapter 10).

- **Confusion**: Thinking the tetrahedron has the same symmetry as any other object with 12 symmetries.
  **Clarification**: The hexagonal plate and 12-sided pyramid also have 12 symmetries, but their groups have different algebraic structure.

# Source Reference

Chapter 1: Symmetries of the Tetrahedron, pages 1-5 (pdf pp. 8-12). Chapter 7: Isomorphisms, Example (ii), page 41. Chapter 8: Summary on p. 48. See Figures 1.1, 1.4, and 7.2.

# Verification Notes

- Definition source: Direct quote from p. 11
- Isomorphism with $A_4$: Proved on p. 41 (Chapter 7)
- Full symmetry group: Exercise 8.11, p. 50
- Re-extracted from earlier card; preserved original content and added Ch. 7-8 material
- Confidence: HIGH — primary example treated across multiple chapters
