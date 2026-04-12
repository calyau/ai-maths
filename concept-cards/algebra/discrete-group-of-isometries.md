---
concept: Discrete Group of Isometries
slug: discrete-group-of-isometries
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
  - isometry-group
  - symmetry-group
extends: []
related:
  - lattice-geometric
  - point-group
  - crystallographic-group
  - frieze-group
contrasts_with: []
answers_questions:
  - "What makes a group of isometries discrete?"
---

# Quick Definition

A group G of isometries is discrete if it contains no arbitrarily small translations or rotations -- there is a positive lower bound epsilon on the length of nonzero translation vectors and on nonzero rotation angles.

# Core Definition

A group G of isometries of the plane P is discrete if there is a positive real number epsilon so that: (i) if an element of G is translation by a nonzero vector a, then |a| >= epsilon, and (ii) if an element of G is rotation through a nonzero angle theta about some point, then |theta| >= epsilon (Artin, Definition 6.5.1, p. 178).

# Prerequisites

- **Isometry group** — Discrete groups are subgroups of M
- **Symmetry group** — Symmetry groups of periodic patterns are discrete

# Key Properties

1. No small translations or rotations
2. Analyzed via three tools: translation group L, point group G-bar, and action of G-bar on L
3. If L is trivial, G is finite (cyclic or dihedral)
4. If L is infinite cyclic, G is a frieze group
5. If L is a lattice, G is a crystallographic group

# Construction / Recognition

## To Recognize:
1. Check that the group has no arbitrarily small translations
2. Check that it has no arbitrarily small rotation angles

# Context & Application

Discrete groups of isometries are the mathematically precise version of "symmetry groups of patterns." The condition prevents pathological groups that arise from irrational angles. All symmetry groups of physical patterns (wallpaper, crystals) are discrete.

# Examples

**Example 1** (p. 178): The symmetry group of a frieze pattern is a discrete group with L = Za.

**Example 2** (p. 178): A kaleidoscope with mirrors at angle pi/6 generates a dihedral group D_6.

# Relationships

## Enables
- **Crystallographic group** — Discrete groups with a lattice translation group
- **Frieze group** — Discrete groups with cyclic translation group

## Related
- **Lattice (geometric)** — The translation group L when it is 2D
- **Point group** — The image of G in O_2

# Common Confusions

- **Confusion**: Thinking discrete means finite
  **Clarification**: Discrete groups can be infinite (frieze and wallpaper groups are)

# Source Reference

Chapter 6: Symmetry, Section 6.5, Definition 6.5.1, pages 178-183.

# Verification Notes

- Definition source: Direct from Definition 6.5.1
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
