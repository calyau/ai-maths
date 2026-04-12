---
# === CORE IDENTIFICATION ===
concept: Composition of Symmetries
slug: composition-of-symmetries

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
  - product of symmetries
  - combining symmetries
  - group multiplication (symmetry context)

# === TYPED RELATIONSHIPS ===
prerequisites:
  - symmetry
extends: []
related:
  - associativity
  - commutativity-of-symmetries
  - identity-symmetry
  - inverse-symmetry
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
  - "What distinguishes a group from a set with an operation?"
---

# Quick Definition

Composition of symmetries is the operation of performing one symmetry after another. Given symmetries u and v, the product uv means "first do v, then do u," following the convention for function composition.

# Core Definition

Given two rotations u and v, "we can combine them, by first doing v, then doing u, to produce a new rotation which also takes T to itself, and which we write uv" (Armstrong, Ch. 1, p. 11). This convention follows the standard notation for function composition, where fg means "first apply g, then apply f."

# Prerequisites

- **Symmetry** — Composition operates on symmetries

# Key Properties

1. The product uv means "first v, then u" (right-to-left convention)
2. The result of composing two symmetries is always another symmetry of the same object
3. Composition is associative: (uv)w = u(vw)
4. Composition is generally not commutative: uv may differ from vu
5. The product is uniquely determined by the two factors

# Construction / Recognition

## To Compute:
1. Apply symmetry v to the object
2. Then apply symmetry u to the result
3. Identify which single symmetry produces the same overall effect
4. Record this as the product uv

# Context & Application

Composition is the fundamental operation that gives symmetry groups their algebraic structure. Armstrong emphasizes the right-to-left convention early, noting its consistency with function composition. This convention carries throughout the text and into the abstract group definition.

# Examples

**Example 1** (p. 10): For the tetrahedron with vertices labelled as in Figure 1.4, let r be rotation through 2pi/3 about axis L and s be rotation through pi about axis m. Then rs (first s, then r) takes vertex 2 back to its initial position and gives a rotation about axis n. But sr (first r, then s) moves vertex 2 to the place originally occupied by 4, showing that rs is not equal to sr.

**Example 2** (p. 11): (uv)w = u(vw) for any three symmetries u, v, w of the tetrahedron — the associative law holds.

# Relationships

## Builds Upon
- **Symmetry** — Composition acts on symmetries

## Enables
- **Symmetry Group** — Composition is the group operation
- **Group** — Abstract group multiplication generalizes composition

## Related
- **Associativity** — Composition is associative
- **Commutativity of Symmetries** — Composition may or may not commute

# Common Errors

- **Error**: Reading uv as "first u, then v"
  **Correction**: uv means "first v, then u" — the right-to-left convention matches function composition

- **Error**: Carrying axes of rotation along with the object during composition
  **Correction**: Each rotation has a fixed axis in space; apply each with respect to its own fixed axis

# Common Confusions

- **Confusion**: Assuming composition is always commutative
  **Clarification**: For most symmetry groups (e.g., tetrahedron, hexagonal plate), composition is not commutative — the order matters

# Source Reference

Chapter 1: Symmetries of the Tetrahedron, pages 4-5 (pdf pp. 11-12).

# Verification Notes

- Definition source: Direct quote from p. 11
- Confidence rationale: High — explicitly defined with convention explained
- Uncertainties: None
- Cross-reference status: Verified
