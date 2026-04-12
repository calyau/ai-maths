---
# === CORE IDENTIFICATION ===
concept: Abelian Group
slug: abelian-group

# === CLASSIFICATION ===
category: fundamentals
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Numbers"
chapter_number: 3
pdf_page: 18
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - commutative group

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends:
  - group
related:
  - commutativity-of-symmetries
  - additive-group-of-integers
  - cyclic-group
contrasts_with:
  - dihedral-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
  - "What is a cyclic group?"
---

# Quick Definition

An abelian (or commutative) group is a group in which xy = yx for any two elements x and y. The term honors the mathematician Niels Henrik Abel.

# Core Definition

"A group is commutative, or **abelian**, if xy = yx for any two of its elements" (Armstrong, Ch. 3, p. 19). This is an additional property beyond the three group axioms; not all groups are abelian.

# Prerequisites

- **Group** — An abelian group is a group with an extra property

# Key Properties

1. xy = yx for all elements x and y
2. Every group of number-arithmetic type (Z, Q, R, C under addition; non-zero Q, R, C under multiplication) is abelian
3. Cyclic groups are always abelian
4. Dihedral groups D_n (n >= 3) are not abelian
5. The symmetry group of the 12-sided pyramid is abelian (all rotations share one axis)

# Construction / Recognition

## To Verify:
1. Check that xy = yx for all pairs of elements
2. If the group is given by generators, it suffices to check commutativity of generators (with care)
3. Alternatively, check if the multiplication table is symmetric about the main diagonal

# Context & Application

Armstrong introduces the term in the context of number groups, where commutativity is a familiar property of addition and multiplication. The contrast with non-abelian groups (like dihedral groups and the tetrahedron symmetry group) is a recurring theme.

# Examples

**Example 1** (p. 19): All number groups in the Chapter 3 list are abelian because x + y = y + x and x * y = y * x for real and complex numbers.

**Example 2** (p. 19): Z_n is abelian because x +_n y = y +_n x.

**Example 3** (p. 9, Ch. 1): The symmetries of the 12-sided pyramid form an abelian group because all rotations share the same axis.

# Relationships

## Builds Upon
- **Group** — An abelian group is a group with commutativity

## Enables
- **Cyclic Group** — Every cyclic group is abelian

## Related
- **Commutativity of Symmetries** — The concrete precursor to the abstract notion
- **Additive Group of Integers** — A canonical abelian group

## Contrasts With
- **Dihedral Group** — D_n for n >= 3 is non-abelian

# Common Errors

- **Error**: Assuming every group is abelian
  **Correction**: Many important groups (dihedral groups, matrix groups, symmetry groups of solids) are non-abelian

# Common Confusions

- **Confusion**: Thinking "abelian" and "group" are synonymous
  **Clarification**: Abelian is an additional property; non-abelian groups are equally legitimate groups

# Source Reference

Chapter 3: Numbers, page 12 (pdf p. 19). Term introduced alongside number examples.

# Verification Notes

- Definition source: Direct quote from p. 19
- Confidence rationale: High — explicitly defined with boldface
- Uncertainties: None
- Cross-reference status: Verified
