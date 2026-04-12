---
concept: Plane Crystallographic Group
slug: crystallographic-group
category: symmetry
subcategory: crystallographic-groups
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Symmetry"
chapter_number: 6
pdf_page: 162
section: "6.6 Plane Crystallographic Groups"
extraction_confidence: high
aliases:
  - "wallpaper group"
  - "two-dimensional crystallographic group"
prerequisites:
  - lattice-geometric
  - point-group
  - crystallographic-restriction
extends:
  - discrete-group-of-isometries
related:
  - frieze-group
contrasts_with: []
answers_questions:
  - "What is a crystallographic group?"
  - "How many types of wallpaper groups are there?"
---

# Quick Definition

A plane crystallographic group is a discrete group of isometries whose translation group is a lattice (two linearly independent translation vectors). There are exactly 17 types.

# Core Definition

When the translation group L of a discrete group G of isometries is a lattice, G is called a two-dimensional crystallographic group (Artin, p. 184). The crystallographic groups are the symmetry groups of two-dimensional crystals and wallpaper patterns. They can be classified into 17 types based on the point group, lattice shape, and how reflections in the point group lift to the full group.

# Prerequisites

- **Lattice (geometric)** — Translation group must be a 2D lattice
- **Point group** — Must be C_n or D_n with n = 1, 2, 3, 4, or 6
- **Crystallographic restriction** — Limits allowed point groups

# Key Properties

1. Exactly 17 types of plane crystallographic groups
2. Point group and lattice don't fully determine the group
3. A reflection in the point group may be represented by glides (no actual reflections) in G
4. The lattice shape is constrained by the point group (e.g., C_4 forces a square lattice)

# Construction / Recognition

## To Classify:
1. Identify the rotational symmetries to determine n
2. Check for reflections/glides to distinguish C_n from D_n
3. Determine the lattice shape
4. Check whether reflections lift to reflections or glides

# Context & Application

The 17 wallpaper groups classify all possible symmetries of periodic 2D patterns. They appear in crystals, Islamic art, Escher's work, and physical chemistry. The classification is a beautiful application of the interplay between algebra and geometry.

# Examples

**Example 1** (p. 184): The brick wall pattern has point group D_2 but contains no reflections -- only glide reflections. This shows the point group alone doesn't determine the crystallographic group.

**Example 2** (p. 185): When the point group contains a 4-fold rotation, the lattice must be square (Lemma 6.6.2).

# Relationships

## Builds Upon
- **Lattice (geometric)** — The translation group
- **Point group** — The rotational/reflective symmetry type
- **Crystallographic restriction** — Limits the possibilities

## Related
- **Frieze group** — The 1D analogue (infinite strip patterns)

# Common Errors

- **Error**: Assuming the point group and lattice determine the crystallographic group
  **Correction**: One must also determine how reflections in the point group lift (as reflections or glides)

# Common Confusions

- **Confusion**: Thinking there are 17 lattice types
  **Clarification**: There are 5 lattice types (Bravais lattices) but 17 crystallographic group types

# Source Reference

Chapter 6: Symmetry, Section 6.6, pages 184-186.

# Verification Notes

- Definition source: From p. 184
- Confidence rationale: Major classification result
- Uncertainties: None
- Cross-reference status: Verified
