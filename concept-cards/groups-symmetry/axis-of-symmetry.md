---
# === CORE IDENTIFICATION ===
concept: Axis of Symmetry
slug: axis-of-symmetry

# === CLASSIFICATION ===
category: fundamentals
subcategory: null
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
  - rotation axis
  - axis of rotation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rotational-symmetry
extends: []
related:
  - symmetry
  - symmetry-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an axis of symmetry?"
  - "How do axes determine the symmetries of a solid?"
---

# Quick Definition

An axis of symmetry is a line in space about which a geometric object can be rotated by some angle and mapped onto itself. Each axis may support one or more non-trivial rotation angles.

# Core Definition

An axis of symmetry of a geometric figure is a line such that rotation about that line through certain angles sends the figure to itself. Armstrong identifies two types for the tetrahedron: axis L through a vertex and the centroid of the opposite face (supporting rotations of 2pi/3 and 4pi/3), and axis M through midpoints of a pair of opposite edges (supporting only rotation through pi) (Armstrong, Ch. 1, p. 8).

# Prerequisites

- **Rotational Symmetry** — An axis of symmetry is the line about which a rotational symmetry acts

# Key Properties

1. An axis is fixed pointwise during the rotation
2. Different axes of the same object may permit different numbers of non-trivial rotations
3. The axis is a line in space that remains fixed, not a line attached to the object
4. Every axis supports the identity rotation (through 2pi)

# Construction / Recognition

## To Identify Axes of Symmetry:
1. Look for lines through vertices and centers of opposite faces
2. Look for lines through midpoints of opposite edges
3. Look for perpendicular axes through centers of faces
4. For each candidate axis, test which rotation angles map the object to itself

# Context & Application

Classifying the axes of symmetry is the standard first step in determining the symmetry group of a solid. The number and types of axes distinguish different symmetry groups. For example, the tetrahedron has 4 axes of type L and 3 of type M, giving (4 x 2) + 3 + 1 = 12 rotational symmetries.

# Examples

**Example 1** (p. 8): Axis L of the tetrahedron passes through a vertex and the centroid of the opposite face. There are four such axes, each admitting rotations of 2pi/3 and 4pi/3.

**Example 2** (p. 8): Axis M of the tetrahedron is determined by the midpoints of a pair of opposite edges. There are three such axes, each admitting only rotation through pi.

# Relationships

## Builds Upon
- **Rotational Symmetry** — Axes define where rotational symmetries act

## Enables
- **Symmetry Group** — Cataloguing axes leads to the full symmetry group

## Related
- **Symmetry** — Axes help classify symmetries

# Common Errors

- **Error**: Moving the axis along with the object during a composition of symmetries
  **Correction**: Each symmetry has an axis that is fixed in space; when composing, each rotation uses its own fixed axis (Armstrong, p. 10)

# Common Confusions

- **Confusion**: Assuming all axes of a figure support the same rotation angles
  **Clarification**: Different axis types support different angles; vertex-to-face axes of the tetrahedron allow 120-degree and 240-degree rotations, while edge-midpoint axes allow only 180-degree rotations

# Source Reference

Chapter 1: Symmetries of the Tetrahedron, pages 1-2 (pdf pp. 8-9). See Figure 1.1.

# Verification Notes

- Definition source: Synthesized from Armstrong's description of axes L and M
- Confidence rationale: High — clearly described with figures
- Uncertainties: None
- Cross-reference status: Verified
