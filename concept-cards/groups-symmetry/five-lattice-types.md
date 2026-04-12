---
# === CORE IDENTIFICATION ===
concept: Five Lattice Types
slug: five-lattice-types

# === CLASSIFICATION ===
category: crystallography
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Lattices and Point Groups"
chapter_number: 25
pdf_page: 152
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - Bravais lattices in 2D
  - lattice classification

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lattice
  - wallpaper-group
extends:
  - lattice
related:
  - point-group
  - crystallographic-restriction
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes the five types of lattices?"
  - "How do lattices and point groups constrain wallpaper patterns?"
---

# Quick Definition

Every lattice in a wallpaper group is one of five types -- oblique, rectangular, centred rectangular, square, or hexagonal -- determined by the relative lengths and angles of the basis vectors a and b.

# Core Definition

Armstrong classifies lattices "into five different types according to the shape of the basic parallelogram determined by the vectors a and b" (Ch. 25, p. 155). After normalizing so that ||a - b|| <= ||a + b||, the five types are defined by the following conditions (Armstrong, p. 155):

- **(a) Oblique**: ||a|| < ||b|| < ||a - b|| < ||a + b||
- **(b) Rectangular**: ||a|| < ||b|| < ||a - b|| = ||a + b||
- **(c) Centred Rectangular**: ||a|| < ||b|| = ||a - b|| < ||a + b||
- **(d) Square**: ||a|| = ||b|| < ||a - b|| = ||a + b||
- **(e) Hexagonal**: ||a|| = ||b|| = ||a - b|| < ||a + b||

# Prerequisites

- **Lattice** -- This card classifies lattices
- **Wallpaper group** -- Each wallpaper group has one of these lattice types

# Key Properties

1. The oblique lattice has the least symmetry (parallelogram with no special angles or lengths)
2. The rectangular lattice has a rectangular basic cell (a perpendicular to b)
3. The centred rectangular lattice has a rhombic cell, equivalent to a rectangle with a centre point
4. The square lattice has a square basic cell (|a| = |b|, right angle)
5. The hexagonal lattice has |a| = |b| and 60-degree angle between a and b
6. A rhombus (|a| = |b| with non-right angle) is actually a centred rectangular lattice (Exercise 25.10)
7. The lattice type constrains which point groups are compatible

# Construction / Recognition

## To Determine the Lattice Type
1. Find the lattice basis vectors a and b (a shortest, b next shortest skew to a)
2. Replace b by -b if necessary so that ||a - b|| <= ||a + b||
3. Compare ||a||, ||b||, ||a - b||, ||a + b||
4. Match to one of the five cases

# Context & Application

The lattice type is the first organizing principle in the wallpaper classification. Each lattice type admits only certain point groups:
- Oblique: only {I} or {+/- I}
- Rectangular: subgroups of {I, -I, B_0, B_pi}
- Centred rectangular: same possibilities as rectangular
- Square: subgroups of D_4 (order-8 dihedral)
- Hexagonal: subgroups of D_6 (order-12 dihedral)

# Examples

**Example 1** (p. 155, Figure 25.5): Armstrong provides diagrams of all five lattice types showing the shape of the basic parallelogram.

**Example 2** (Exercise 25.10, p. 160): Tilting a square lattice 45 degrees produces a centred rectangular structure.

**Example 3** (Exercise 25.2, p. 160): a = (-1, -sqrt(3)), b = (1, -sqrt(3)) gives a hexagonal lattice.

# Relationships

## Builds Upon
- **Lattice** -- This classifies lattices into types

## Enables
- **Seventeen wallpaper groups** -- The classification proceeds lattice type by lattice type

## Related
- **Point group** -- Each lattice type constrains the possible point groups
- **Crystallographic restriction** -- Connected via lattice symmetry constraints

# Common Errors

- **Error**: Forgetting to normalize the choice of b so that ||a - b|| <= ||a + b||
  **Correction**: Always replace b by -b if needed before classifying

- **Error**: Classifying a rhombic lattice (|a| = |b|, non-right angle) as a separate type
  **Correction**: A rhombus is a centred rectangular lattice; the rectangle is based on the diagonals a - b and a + b

# Common Confusions

- **Confusion**: Thinking "centred rectangular" means a rectangle with a point in the center
  **Clarification**: It is more naturally described as a rhombic lattice, but the rectangular perspective (with centre) gives it the name

- **Confusion**: Believing there should be a sixth "rhombic" type
  **Clarification**: The rhombus case reduces to centred rectangular, as Armstrong explains on p. 155

# Source Reference

Chapter 25: Lattices and Point Groups, pages 155-156 (pdf pp. 155-156). Classification conditions on p. 155; Figure 25.5 illustrates all five types.

# Verification Notes

- Classification: Directly from Armstrong p. 155, all five conditions quoted
- Rhombus reduction: Explicitly discussed on p. 155
- Confidence: HIGH -- complete explicit classification
- Cross-references: Verified against planned extractions
- Uncertainties: None
