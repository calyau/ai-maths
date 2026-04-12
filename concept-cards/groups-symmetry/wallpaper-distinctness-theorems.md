---
# === CORE IDENTIFICATION ===
concept: Wallpaper Distinctness Theorems
slug: wallpaper-distinctness-theorems

# === CLASSIFICATION ===
category: crystallography
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Wallpaper Patterns"
chapter_number: 26
pdf_page: 162
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Theorems 26.1-26.4"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - seventeen-wallpaper-groups
  - wallpaper-isomorphism-theorem
extends: []
related:
  - point-group
  - glide-reflection
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do we know the 17 wallpaper groups are genuinely distinct?"
---

# Quick Definition

Theorems 26.1-26.4 prove that no two of the seventeen wallpaper groups are isomorphic, by exploiting structural differences in how reflections, glides, and rotations interact within each group.

# Core Definition

Armstrong proves distinctness through four theorems:

**(26.1)** "No two of p2, pm, pg, cm are isomorphic" -- distinguished by presence/absence of rotations, reflections, and the decomposability of glides (p. 168).

**(26.2)** "No two of p2mm, p2mg, p2gg, c2mm are isomorphic" -- distinguished by reflection content and products of reflections (p. 169).

**(26.3)** "p4mm is not isomorphic to p4gm" -- in p4mm every order-4 rotation factors as two reflections; in p4gm some do not (p. 169).

**(26.4)** "p3m1 is not isomorphic to p31m" -- in p31m every order-3 rotation factors as two reflections; in p3m1 some do not (p. 169).

# Prerequisites

- **Seventeen wallpaper groups** -- The groups being shown distinct
- **Wallpaper isomorphism theorem** -- Ensures isomorphisms preserve isometry types

# Key Properties

1. Groups with different point groups are automatically non-isomorphic (Corollary 25.6)
2. The hard cases involve groups with the same point group
3. Theorem 26.1 handles the four groups with point group Z_2
4. Theorem 26.2 handles the four groups with point group Z_2 x Z_2
5. Theorem 26.3 handles the two groups with point group D_4
6. Theorem 26.4 handles the two groups with point group D_3
7. Key technique: analyzing whether rotations factor as products of reflections within the group

# Construction / Recognition

## Distinguishing Criteria
- **p2 vs pm/pg/cm**: Only p2 contains rotations among the Z_2-point-group groups
- **pg vs pm/cm**: pg contains no reflections
- **pm vs cm**: In pm, every glide decomposes into a reflection and translation both in pm; cm has glides whose parts are not in cm
- **p2gg vs p2mm/p2mg/c2mm**: p2gg has no reflections
- **p2mm vs p2mg/c2mm**: In p2mm, every glide decomposes into parts in the group
- **p2mg vs c2mm**: In p2mg all mirrors are parallel; in c2mm there are perpendicular mirrors
- **p4mm vs p4gm**: In p4mm, every order-4 rotation = product of two reflections in the group
- **p3m1 vs p31m**: In p31m, every order-3 rotation = product of two reflections in the group

# Context & Application

These distinctness proofs complete the wallpaper classification. Armstrong's approach is to find structural properties that distinguish groups with the same point group. The technique of checking whether rotations factor as products of reflections is particularly elegant for the D_4 and D_3 cases.

# Examples

**Example 1** (p. 168): In cm, the glide (a/2 + (2b-a)/2, B_0) has parts that do not belong to cm, unlike in pm.

**Example 2** (p. 169): In p4gm, the rotation (a, A_{pi/2}) cannot be written as the product of two reflections in the group.

# Relationships

## Builds Upon
- **Wallpaper isomorphism theorem** -- Ensures isomorphisms preserve isometry types
- **Seventeen wallpaper groups** -- The groups being distinguished

## Related
- **Glide reflection** -- Central to many distinctness arguments

# Common Errors

- **Error**: Assuming distinct names automatically mean distinct groups
  **Correction**: The names come from the construction; distinctness requires proof (which Theorems 26.1-26.4 provide)

# Common Confusions

- **Confusion**: Thinking distinctness follows from having different lattice types
  **Clarification**: Some groups with different lattice types could a priori be isomorphic (e.g., pm on rectangular lattice and cm on centred rectangular); the proofs must rule this out

# Source Reference

Chapter 26: Wallpaper Patterns, Theorems 26.1-26.4, pages 168-170 (pdf pp. 168-170).

# Verification Notes

- Theorems: All four directly from Armstrong pp. 168-170
- Proofs: Complete in source
- Confidence: HIGH -- named theorems with proofs
- Cross-references: Verified against planned extractions
- Uncertainties: None
