---
concept: Point Group
slug: point-group
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
  - "G-bar"
prerequisites:
  - discrete-group-of-isometries
  - isometry-group
extends: []
related:
  - lattice-geometric
  - crystallographic-restriction
contrasts_with: []
answers_questions:
  - "What is the point group of a discrete group of isometries?"
---

# Quick Definition

The point group G-bar of a discrete group G of isometries is the image of G under the homomorphism pi: M -> O_2 that drops the translation part. It records the angles of rotation and slopes of reflection/glide lines.

# Core Definition

When the homomorphism pi: M -> O_2 (dropping the translation part of each isometry) is restricted to a discrete subgroup G, the image G-bar in O_2 is called the point group (Artin, p. 182). It is a discrete subgroup of O_2 and therefore either cyclic C_n or dihedral D_n (Proposition 6.5.10).

# Prerequisites

- **Discrete group of isometries** — The point group comes from a discrete group
- **Isometry group** — Via the homomorphism pi: M -> O_2

# Key Properties

1. A finite subgroup of O_2
2. Either C_n or D_n
3. Records rotation angles and reflection line slopes
4. Operates on the translation group L (Proposition 6.5.11)
5. Does not change when the origin is shifted (Corollary 6.2.12)

# Construction / Recognition

## To Determine:
1. Look for rotational symmetries of the pattern to find n
2. Check for reflections or glides to distinguish C_n from D_n

# Context & Application

The point group is one of the three main tools for analyzing discrete groups of isometries. Together with the translation group and the action of the point group on translations, it determines the crystallographic group. The crystallographic restriction limits the point group to n = 1, 2, 3, 4, or 6.

# Examples

**Example 1** (p. 184): The brick wall pattern has point group D_2 = {1, rho_pi, r, rho_pi * r}.

**Example 2** (p. 185): A pattern with fourfold rotational symmetry has point group C_4 or D_4.

# Relationships

## Builds Upon
- **Discrete group of isometries** — Point group is the image in O_2

## Enables
- **Crystallographic restriction** — Restricts possible point groups
- **Crystallographic group classification** — Point group is part of the classification data

# Common Confusions

- **Confusion**: Thinking the point group determines the full symmetry group
  **Clarification**: The point group and translation group together still don't determine G completely; the way reflections lift (as reflections or glides) matters

# Source Reference

Chapter 6: Symmetry, Section 6.5, pages 182-183.

# Verification Notes

- Definition source: Synthesized from p. 182
- Confidence rationale: Clearly described, though not given a boxed definition
- Uncertainties: None
- Cross-reference status: Verified
