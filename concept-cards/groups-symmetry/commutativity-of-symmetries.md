---
# === CORE IDENTIFICATION ===
concept: Commutativity of Symmetries
slug: commutativity-of-symmetries

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
  - commuting symmetries

# === TYPED RELATIONSHIPS ===
prerequisites:
  - composition-of-symmetries
extends: []
related:
  - abelian-group
  - symmetry-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What distinguishes a group from a set with an operation?"
  - "What is a dihedral group?"
---

# Quick Definition

Two symmetries commute if performing them in either order produces the same result: uv = vu. A symmetry group in which all pairs of elements commute is called commutative (abelian); otherwise, it is non-commutative.

# Core Definition

Armstrong introduces commutativity through the contrast between the pyramid and the tetrahedron: "the symmetries of the pyramid all commute with each other. That is to say, if we take any two and perform one rotation after the other, the effect on the pyramid is the same no matter which one we choose to do first... This is not the case for the tetrahedron or the plate" (Armstrong, Ch. 1, p. 9).

# Prerequisites

- **Composition of Symmetries** — Commutativity concerns the order of composition

# Key Properties

1. Two symmetries u, v commute if uv = vu
2. All rotations sharing the same axis commute with each other
3. Rotations about different axes generally do not commute
4. The identity commutes with every symmetry
5. Whether a symmetry group is commutative is a distinguishing structural property

# Construction / Recognition

## To Test Commutativity:
1. Choose two symmetries u and v
2. Compute uv (first v, then u)
3. Compute vu (first u, then v)
4. Compare the results: if they match for all pairs, the group is commutative

# Context & Application

Commutativity is one of the structural differences Armstrong uses to distinguish symmetry groups with the same number of elements. The 12-sided pyramid has a commutative symmetry group, while the tetrahedron and hexagonal plate do not. This distinction motivates the general notion of an abelian group in Chapter 2.

# Examples

**Example 1** (p. 9): The symmetries of the 12-sided pyramid all commute because they share the same axis. Rotating through pi/3 then 5pi/6 gives 7pi/6, the same result as 5pi/6 then pi/3.

**Example 2** (p. 10): For the tetrahedron, let r be rotation through 2pi/3 about axis L and s be rotation through pi about axis m. Then rs takes vertex 2 back to its starting position, but sr moves vertex 2 to the position of vertex 4. So rs does not equal sr.

# Relationships

## Builds Upon
- **Composition of Symmetries** — Commutativity is a property of composition

## Enables
- **Abelian Group** — The abstract formulation of commutativity

## Related
- **Symmetry Group** — Commutativity distinguishes between symmetry groups

# Common Errors

- **Error**: Testing commutativity on only a few pairs and concluding the group is commutative
  **Correction**: A single non-commuting pair suffices to show the group is non-commutative, but commutativity requires all pairs to commute

# Common Confusions

- **Confusion**: Believing that non-commutativity means no pairs commute
  **Clarification**: In a non-commutative group, some pairs may still commute (e.g., every element commutes with the identity and with itself)

# Source Reference

Chapter 1: Symmetries of the Tetrahedron, pages 2-4 (pdf pp. 9-11).

# Verification Notes

- Definition source: Direct quote from p. 9
- Confidence rationale: High — explicitly described with concrete examples
- Uncertainties: None
- Cross-reference status: Verified
