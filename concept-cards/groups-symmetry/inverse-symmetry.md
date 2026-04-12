---
# === CORE IDENTIFICATION ===
concept: Inverse Symmetry
slug: inverse-symmetry

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
  - inverse rotation
  - inverse transformation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - symmetry
  - identity-symmetry
extends: []
related:
  - inverse-element
  - composition-of-symmetries
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an inverse symmetry?"
  - "What is a group?"
---

# Quick Definition

The inverse of a symmetry u, denoted u^{-1}, is the symmetry that undoes u: composing u with u^{-1} (in either order) yields the identity. For a rotation, the inverse rotates about the same axis through the same angle in the opposite sense.

# Core Definition

Each rotation u has a "so-called inverse u^{-1}, which is also a symmetry of T and which satisfies u^{-1}u = e and uu^{-1} = e. To obtain u^{-1}, just rotate about the same axis and through the same angle as for u, but in the opposite sense" (Armstrong, Ch. 1, p. 11).

# Prerequisites

- **Symmetry** — The inverse is defined for a symmetry
- **Identity Symmetry** — The inverse is characterized by its relationship to the identity

# Key Properties

1. u^{-1}u = e and uu^{-1} = e
2. The inverse rotates about the same axis as u
3. The inverse uses the same angle as u but in the opposite sense
4. The inverse of u^{-1} is u itself
5. The inverse of the identity is the identity

# Construction / Recognition

## To Construct:
1. Identify the axis and angle of the original rotation u
2. Rotate about the same axis through the same angle in the opposite direction
3. Verify that composing u with this rotation yields the identity

# Context & Application

The existence of inverses is the third key algebraic property Armstrong identifies in symmetry groups, leading to group axiom (c). The concept appears throughout group theory as a fundamental structural requirement.

# Examples

**Example 1** (p. 11): The inverse of the rotation r (through 2pi/3 about axis L of the tetrahedron) is rr = r^2 (through 4pi/3 about the same axis), because applying r three times gives the identity: r^3 = e, so r^{-1} = r^2.

**Example 2** (Exercise 1.5, p. 12): The inverse of s (rotation through pi about axis m) is s itself, since s^2 = e. The inverse of rs is sr^2, and the inverse of sr is r^2s.

# Relationships

## Builds Upon
- **Symmetry** — Inverses are defined for symmetries
- **Identity Symmetry** — Inverses are defined relative to the identity

## Enables
- **Group** — The inverse axiom is one of the three group axioms
- **Inverse Element** — Generalizes inverse symmetry to abstract groups

## Related
- **Composition of Symmetries** — Inverses interact with composition

# Common Errors

- **Error**: Assuming the inverse of a rotation always has a different axis
  **Correction**: The inverse rotates about the same axis, just in the opposite direction

# Common Confusions

- **Confusion**: Believing every symmetry is its own inverse
  **Clarification**: Only symmetries of order 2 (like rotation through pi) are their own inverses; rotations through 2pi/3 have inverses that are rotations through 4pi/3

# Source Reference

Chapter 1: Symmetries of the Tetrahedron, pages 4-5 (pdf pp. 11-12). See also Exercise 1.5.

# Verification Notes

- Definition source: Direct quote from p. 11
- Confidence rationale: High — explicitly defined with notation
- Uncertainties: None
- Cross-reference status: Verified
