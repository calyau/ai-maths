---
concept: Lattice (Geometric)
slug: lattice-geometric
category: symmetry
subcategory: crystallographic-groups
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Symmetry"
chapter_number: 6
pdf_page: 162
section: "6.5 Discrete Groups of Isometries"
extraction_confidence: high
aliases:
  - "lattice"
  - "translation lattice"
prerequisites:
  - discrete-group-of-isometries
extends: []
related:
  - crystallographic-group
  - point-group
contrasts_with: []
answers_questions:
  - "What is a lattice in the geometric sense?"
  - "What are the possible discrete subgroups of the translation group?"
---

# Quick Definition

A lattice is the set of integer combinations L = Za + Zb = {ma + nb | m, n in Z} of two linearly independent vectors a and b in the plane. It is the translation group of a crystallographic group.

# Core Definition

A discrete subgroup L of the additive group of translation vectors V+ is one of: (a) the zero group {0}, (b) integer multiples Za of a single nonzero vector, or (c) integer combinations Za + Zb of two linearly independent vectors a and b (Artin, Theorem 6.5.5, p. 180). Groups of type (c) are called lattices, and (a, b) is called a lattice basis.

# Prerequisites

- **Discrete group of isometries** — Lattices are translation groups of discrete groups

# Key Properties

1. L = Za + Zb for linearly independent a, b
2. Every vector v decomposes uniquely as v = x + v_0 with x in L and v_0 in the fundamental parallelogram
3. A bounded region contains only finitely many lattice points (Lemma 6.5.7)
4. The point group operates on L (Proposition 6.5.11)
5. Lattice bases are related by integer matrices with determinant +/- 1

# Construction / Recognition

## To Construct:
1. Choose two linearly independent vectors a and b
2. L = {ma + nb | m, n in Z}

## To Recognize:
1. A discrete set of points closed under addition and negation
2. Spanning the plane (not all on a single line)

# Context & Application

Lattices are the translation groups of crystallographic groups. The shape of the lattice (square, rectangular, hexagonal, etc.) constrains which point groups can occur, leading to the crystallographic restriction.

# Examples

**Example 1** (p. 180): The integer lattice Z^2 with basis (e_1, e_2).

**Example 2** (p. 185): A square lattice with basis (e_1, e_2) must have a square fundamental domain when the point group is C_4 or D_4.

# Relationships

## Builds Upon
- **Discrete group of isometries** — Lattice is the translation group

## Enables
- **Crystallographic group** — Defined when the translation group is a lattice
- **Crystallographic restriction** — Constrains the point group

# Common Errors

- **Error**: Assuming any two vectors generate a lattice
  **Correction**: The vectors must be linearly independent; one vector generates only Za

# Common Confusions

- **Confusion**: Confusing lattice (geometric) with lattice (order theory)
  **Clarification**: Here "lattice" means a discrete translation group in R^2, not a partially ordered set

# Source Reference

Chapter 6: Symmetry, Section 6.5, Theorem 6.5.5, pages 180-182.

# Verification Notes

- Definition source: Direct from Theorem 6.5.5(c)
- Confidence rationale: Explicitly defined and classified
- Uncertainties: None
- Cross-reference status: Verified
