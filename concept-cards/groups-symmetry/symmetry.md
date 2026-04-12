---
# === CORE IDENTIFICATION ===
concept: Symmetry
slug: symmetry

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
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - rigid motion
  - symmetry transformation

# === TYPED RELATIONSHIPS ===
prerequisites: []
extends: []
related:
  - rotational-symmetry
  - axis-of-symmetry
  - symmetry-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a symmetry?"
  - "What distinguishes a group from a set with an operation?"
---

# Quick Definition

A symmetry of a geometric object is a rigid motion of space that sends the object to itself. The collection of all symmetries of an object, together with their algebraic structure, forms the object's symmetry group.

# Core Definition

A symmetry of a geometric figure is a distance-preserving transformation (rigid motion) of space that maps the figure onto itself. Armstrong introduces symmetries concretely through the regular tetrahedron, identifying rotations about various axes that leave the tetrahedron invariant (Armstrong, Ch. 1, p. 8).

# Prerequisites

This is a foundational concept with no prerequisites within this source.

# Key Properties

1. A symmetry maps the object onto itself (the object occupies the same region of space after the transformation)
2. Symmetries preserve distances and angles (they are rigid motions)
3. Two symmetries can be composed to yield another symmetry
4. The identity (doing nothing) is always a symmetry
5. Every symmetry has an inverse symmetry

# Construction / Recognition

## To Identify/Recognize:
1. Determine the geometric object in question
2. Identify all rigid motions (rotations, reflections) that map the object to itself
3. Verify that each transformation leaves the object occupying the same position in space
4. Count distinct symmetries carefully, distinguishing between different axes and angles

# Context & Application

Symmetry is the foundational concept of the entire text. Armstrong uses it to motivate the definition of a group: the algebraic structure that captures how symmetries combine. Symmetry appears throughout mathematics, physics (molecular symmetry, crystallography), and chemistry (e.g., the tetrahedral symmetry of methane CH4).

# Examples

**Example 1** (p. 8): The regular tetrahedron has twelve rotational symmetries: eight rotations about axes through vertices (four axes, two non-trivial rotations each), three rotations about axes through midpoints of opposite edges, and the identity.

**Example 2** (p. 8): A flat hexagonal plate also has twelve rotational symmetries, but they combine differently from those of the tetrahedron.

**Example 3** (p. 8): A right regular pyramid on a twelve-sided base has twelve rotational symmetries, all sharing a single axis.

# Relationships

## Builds Upon
This is a foundational concept.

## Enables
- **Symmetry Group** — The set of all symmetries forms a group
- **Group** — The abstract group axioms are modelled on properties of symmetries

## Related
- **Rotational Symmetry** — A specific type of symmetry
- **Axis of Symmetry** — The geometric axis about which a rotation occurs

# Common Errors

- **Error**: Counting a rotation and its reverse as the same symmetry
  **Correction**: A rotation through 2pi/3 and through 4pi/3 about the same axis are distinct symmetries, even though one is the reverse of the other

- **Error**: Carrying the axis of rotation along when composing symmetries
  **Correction**: Each symmetry has a fixed axis in space; when composing, apply each transformation with its own fixed axis

# Common Confusions

- **Confusion**: Believing that counting the number of symmetries fully describes an object's symmetry
  **Clarification**: Objects with the same number of symmetries (e.g., tetrahedron, hexagonal plate, 12-sided pyramid all have 12) can have fundamentally different symmetry because their symmetries combine differently

# Source Reference

Chapter 1: Symmetries of the Tetrahedron, pages 1-5 (pdf pp. 8-12).

# Verification Notes

- Definition source: Synthesized from Armstrong's concrete discussion; no single explicit definition sentence
- Confidence rationale: Medium — the concept is introduced through examples rather than a formal definition
- Uncertainties: None
- Cross-reference status: Verified against planned extractions
