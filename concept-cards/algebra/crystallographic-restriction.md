---
concept: Crystallographic Restriction
slug: crystallographic-restriction
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
aliases: []
prerequisites:
  - lattice-geometric
  - point-group
extends: []
related:
  - crystallographic-group
  - dihedral-group
contrasts_with: []
answers_questions:
  - "Why can't wallpaper patterns have five-fold symmetry?"
  - "What rotation orders are compatible with a lattice?"
---

# Quick Definition

The Crystallographic Restriction states that if a discrete group of isometries has a nontrivial translation group (a lattice), then every rotation in its point group has order 1, 2, 3, 4, or 6. In particular, five-fold rotational symmetry is incompatible with translational periodicity.

# Core Definition

Let L be a nontrivial discrete subgroup of V+, and let H be a subgroup of O_2 that preserves L. Then (a) every rotation in H has order 1, 2, 3, 4, or 6, and (b) H is C_n or D_n with n = 1, 2, 3, 4, or 6 (Artin, Theorem 6.5.12, p. 183).

# Prerequisites

- **Lattice (geometric)** — The restriction applies when a lattice exists
- **Point group** — The restriction constrains the point group

# Key Properties

1. Only rotation orders 1, 2, 3, 4, 6 are compatible with a lattice
2. Order 5 is ruled out by a length argument
3. This limits the point group to 10 possibilities: C_1, ..., C_6 and D_1, ..., D_6 (excluding n=5)
4. Combined with the lattice structure, yields 17 wallpaper groups

# Construction / Recognition

## Proof Idea:
1. Let a be a shortest nonzero lattice vector
2. If rho has angle theta, then rho(a) is also in L, so |rho(a) - a| >= |a|
3. This forces theta >= 2pi/6
4. A separate argument eliminates theta = 2pi/5

# Context & Application

The Crystallographic Restriction explains why crystals and wallpaper patterns exhibit only 2-, 3-, 4-, and 6-fold rotational symmetries. Five-fold symmetry, while common in biology (starfish, flowers), cannot appear in periodic patterns. This restriction is the key step toward classifying the 17 wallpaper groups. Note: quasi-periodic patterns can have 5-fold symmetry (Penrose tilings).

# Examples

**Example 1** (p. 183): Geometric proof: if a is a shortest lattice vector and rho has angle theta < 2pi/6, then |rho(a) - a| < |a|, contradicting minimality.

**Example 2** (p. 183): The case theta = 2pi/5 is ruled out separately: rho^2(a) + a is shorter than a.

# Relationships

## Builds Upon
- **Lattice (geometric)** — The restriction comes from lattice preservation
- **Point group** — The restriction limits which point groups can occur

## Enables
- **Wallpaper group classification** — The 17 types follow from this restriction

# Common Errors

- **Error**: Concluding that 5-fold symmetric objects don't exist
  **Correction**: The restriction applies only to periodic (crystallographic) patterns; individual bounded figures like pentagons have 5-fold symmetry

# Common Confusions

- **Confusion**: Thinking quasi-crystals violate the crystallographic restriction
  **Clarification**: Quasi-crystals are not periodic (no lattice), so the restriction doesn't apply

# Source Reference

Chapter 6: Symmetry, Section 6.5, Theorem 6.5.12, p. 183.

# Verification Notes

- Definition source: Direct from Theorem 6.5.12
- Confidence rationale: Named theorem, explicitly stated and proved
- Uncertainties: None
- Cross-reference status: Verified
