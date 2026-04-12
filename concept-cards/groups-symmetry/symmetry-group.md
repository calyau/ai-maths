---
# === CORE IDENTIFICATION ===
concept: Symmetry Group
slug: symmetry-group

# === CLASSIFICATION ===
category: symmetry-groups
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
  - group of symmetries
  - rotational symmetry group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - symmetry
  - composition-of-symmetries
  - identity-symmetry
  - inverse-symmetry
extends: []
related:
  - group
  - dihedral-group
  - tetrahedron-symmetry-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
  - "What distinguishes a group from a set with an operation?"
---

# Quick Definition

The symmetry group of a geometric object is the set of all symmetries of that object together with the algebraic structure given by composing symmetries. It captures not just how many symmetries exist, but how they interact.

# Core Definition

The symmetry group of a figure consists of all its symmetries together with the operation of composition. Armstrong states: "The twelve symmetries of the tetrahedron together with this algebraic structure make up its rotational symmetry group" (Armstrong, Ch. 1, p. 11). The algebraic structure includes composition, the identity, inverses, and associativity.

# Prerequisites

- **Symmetry** — The elements of the group are symmetries
- **Composition of Symmetries** — The group operation is composition
- **Identity Symmetry** — Every symmetry group contains the identity
- **Inverse Symmetry** — Every symmetry has an inverse in the group

# Key Properties

1. The group operation is composition of symmetries
2. Composition is associative: (uv)w = u(vw)
3. The identity symmetry e satisfies ue = u = eu for all symmetries u
4. Every symmetry u has an inverse u^{-1} with uu^{-1} = e = u^{-1}u
5. The composition of any two symmetries is again a symmetry of the same object
6. Objects with the same number of symmetries may have non-isomorphic symmetry groups

# Construction / Recognition

## To Construct:
1. Identify all symmetries of the geometric object (rotations, reflections as applicable)
2. Verify that composition of any two symmetries yields another symmetry
3. Verify that the identity is included
4. Verify that every symmetry has an inverse among the identified symmetries
5. Record how the symmetries combine (e.g., via a multiplication table)

# Context & Application

The symmetry group is the motivating example for the abstract definition of a group in Chapter 2. Armstrong's key pedagogical point is that simply counting symmetries is insufficient: "To obtain a decent measure of symmetry, simply counting symmetries is not enough; we must also take into consideration how they combine with each other" (Ch. 1, p. 10).

# Examples

**Example 1** (p. 8-11): The rotational symmetry group of the regular tetrahedron has 12 elements. It is non-abelian (composition is not commutative).

**Example 2** (p. 8): The hexagonal plate has 12 rotational symmetries forming a different group from the tetrahedron's, despite having the same count.

**Example 3** (p. 8): The 12-sided pyramid has 12 rotational symmetries forming a commutative (abelian) group, distinguished from the other two by the fact that all its symmetries commute.

# Relationships

## Builds Upon
- **Symmetry** — Elements of the group
- **Composition of Symmetries** — The group operation

## Enables
- **Group** — The abstract definition of a group generalizes symmetry groups
- **Dihedral Group** — A specific family of symmetry groups

## Related
- **Tetrahedron Symmetry Group** — A specific symmetry group with 12 elements

# Common Errors

- **Error**: Assuming two objects have the "same symmetry" because they have the same number of symmetries
  **Correction**: The group structure (how symmetries combine) must also match

# Common Confusions

- **Confusion**: Thinking the symmetry group is just a set of symmetries
  **Clarification**: The symmetry group includes both the set and the composition operation; the algebraic structure is essential

# Source Reference

Chapter 1: Symmetries of the Tetrahedron, pages 1-5 (pdf pp. 8-12).

# Verification Notes

- Definition source: Direct quote from p. 11 plus synthesized context
- Confidence rationale: High — explicitly defined and extensively discussed
- Uncertainties: None
- Cross-reference status: Verified
