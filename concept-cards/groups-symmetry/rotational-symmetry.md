---
# === CORE IDENTIFICATION ===
concept: Rotational Symmetry
slug: rotational-symmetry

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
  - rotation
  - rotational symmetry transformation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - symmetry
extends:
  - symmetry
related:
  - axis-of-symmetry
  - identity-symmetry
  - inverse-symmetry
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is rotational symmetry?"
  - "How are rotational symmetries classified?"
---

# Quick Definition

A rotational symmetry of a geometric object is a rotation about some axis through a specific angle that maps the object onto itself. The rotation is a rigid motion that fixes the axis pointwise and moves all other points in circular arcs around it.

# Core Definition

A rotational symmetry is a rotation of space about a fixed axis, through a specific angle, that sends a geometric figure to itself. Armstrong classifies the rotational symmetries of the tetrahedron by their axes: rotations through 2pi/3 and 4pi/3 about axes through vertices (type L), and rotations through pi about axes through midpoints of opposite edges (type M) (Armstrong, Ch. 1, p. 8).

# Prerequisites

- **Symmetry** — Rotational symmetry is a specific kind of symmetry

# Key Properties

1. Each rotation is specified by an axis and an angle
2. The sense of rotation matters: looking along the axis from a chosen direction, the rotation is either clockwise or anticlockwise
3. Rotating through angle theta in one sense equals rotating through 2pi - theta in the opposite sense
4. The composition of two rotations is another rotation (or the identity)
5. Different axes of the same object may permit different rotation angles

# Construction / Recognition

## To Identify Rotational Symmetries:
1. Locate all possible axes of symmetry (through vertices, edge midpoints, face centroids, etc.)
2. For each axis, determine which rotation angles map the object to itself
3. Count each distinct rotation as a separate symmetry
4. Include the identity (rotation through 2pi or 0)

# Context & Application

Rotational symmetry is the primary type of symmetry discussed in Chapters 1 and 4. Armstrong restricts attention to rotational symmetry initially, deferring reflections to later discussion. The rotational symmetries of a solid or plate form a group under composition.

# Examples

**Example 1** (p. 8): The tetrahedron has two types of rotation axes. Axes of type L pass through a vertex and the centroid of the opposite face, allowing rotations of 2pi/3 and 4pi/3. Axes of type M are determined by midpoints of opposite edges, allowing rotation through pi only.

**Example 2** (p. 8): A hexagonal plate has rotations of pi/3, 2pi/3, pi, 4pi/3, 5pi/3 about its central perpendicular axis, plus rotations of pi about six axes in its plane.

**Example 3** (p. 8): A right regular pyramid on a 12-sided base has rotations through k*pi/6 (1 <= k <= 12) about a single axis.

# Relationships

## Builds Upon
- **Symmetry** — Rotational symmetry is a specific type of symmetry

## Enables
- **Symmetry Group** — Rotational symmetries combine to form a group
- **Dihedral Group** — Built from rotational symmetries of a plate

## Related
- **Axis of Symmetry** — Each rotation is defined relative to an axis
- **Identity Symmetry** — The trivial rotation (through 0 or 2pi)

# Common Errors

- **Error**: Forgetting the identity when counting rotational symmetries
  **Correction**: The identity (equivalent to rotation through 2pi) must always be included

- **Error**: Double-counting rotations that differ only in sense
  **Correction**: Rotation through theta in one sense equals rotation through 2pi - theta in the opposite sense; count each resulting position once

# Common Confusions

- **Confusion**: Believing all rotational symmetries of an object share the same axis
  **Clarification**: Objects like the tetrahedron have multiple axes of symmetry with different types (vertex-to-face vs. edge-to-edge)

# Source Reference

Chapter 1: Symmetries of the Tetrahedron, pages 1-5 (pdf pp. 8-12).

# Verification Notes

- Definition source: Synthesized from Armstrong's concrete description of tetrahedron rotations
- Confidence rationale: High — extensive concrete examples make the concept clear
- Uncertainties: None
- Cross-reference status: Verified against planned extractions
