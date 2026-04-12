---
# === CORE IDENTIFICATION ===
concept: Wallpaper Notation
slug: wallpaper-notation

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
  - crystallographic notation
  - IUCr notation

# === TYPED RELATIONSHIPS ===
prerequisites:
  - seventeen-wallpaper-groups
extends: []
related:
  - wallpaper-group
  - point-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What do the symbols in wallpaper group names mean?"
  - "How do I determine the wallpaper group of a pattern?"
---

# Quick Definition

Wallpaper group names use internationally recognized symbols: p (primitive lattice), c (centred lattice), m (mirror/reflection), g (glide reflection), and the integers 1, 2, 3, 4, 6 (identity or rotation order).

# Core Definition

"Each wallpaper group has a name made up of several (internationally recognised) symbols p, c, m, g and the integers 1, 2, 3, 4, 6. The letter p refers to the lattice and stands for the word primitive. ... In one case (the centred rectangular lattice) we take a non-primitive cell together with its centre as the basic building block, and use the letter c to denote the resulting centred lattice. The symbol for a reflection is m (for mirror) and g denotes a glide reflection. Finally, 1 is used for the identity transformation and the numbers 2, 3, 4, 6 indicate rotations of the corresponding order" (Armstrong, Ch. 26, p. 162).

# Prerequisites

- **Seventeen wallpaper groups** -- The notation names these groups

# Key Properties

1. First symbol: p (primitive lattice) or c (centred lattice)
2. Number: highest order of rotation (1, 2, 3, 4, or 6)
3. Letters m and g indicate mirror reflections and glide reflections respectively
4. The symbols in Figure 26.1: o (order-2 centre), triangle (order-3), square (order-4), hexagon (order-6)
5. Thick lines represent mirrors; broken lines represent glide axes

# Construction / Recognition

## Reading a Wallpaper Group Name
- p1: primitive lattice, identity only (no rotation, no reflection)
- p2: primitive, half-turns
- pm: primitive, mirror reflections
- pg: primitive, glide reflections
- p2mm: primitive, half-turns, two mirror directions
- p2mg: primitive, half-turns, one mirror direction, one glide direction
- p2gg: primitive, half-turns, two glide directions (no mirrors)
- cm: centred, mirror reflections
- c2mm: centred, half-turns, two mirror directions
- p4: primitive, quarter-turns
- p4mm: primitive, quarter-turns, mirrors
- p4gm: primitive, quarter-turns, glides and mirrors
- p3: primitive, order-3 rotations
- p3m1: primitive, order-3 rotations, mirrors (one orientation)
- p31m: primitive, order-3 rotations, mirrors (other orientation)
- p6: primitive, order-6 rotations
- p6mm: primitive, order-6 rotations, mirrors

# Context & Application

The notation is internationally standardized and used across crystallography, mathematics, and materials science. Armstrong uses these names throughout Chapter 26 and notes that the symbols in Figure 26.1 show the positions of rotation centres, mirrors, and glide lines relative to the basic parallelogram.

# Examples

**Example 1** (p. 162): "Rotations of order two are usually called half turns" -- so p2 indicates a group with half-turn symmetry.

**Example 2** (p. 162): The "c" in cm indicates the centred rectangular lattice, distinguishing it from pm which has a primitive rectangular lattice.

# Relationships

## Related
- **Wallpaper group** -- The notation names wallpaper groups
- **Point group** -- The rotation number reflects the point group structure

# Common Errors

- **Error**: Confusing p3m1 and p31m by assuming the position of "1" is irrelevant
  **Correction**: The position of the "1" distinguishes the orientation of the mirrors relative to the lattice

# Common Confusions

- **Confusion**: Thinking "m" always means the same mirror direction
  **Clarification**: The position of "m" in the name can refer to different mirror orientations depending on the lattice type

# Source Reference

Chapter 26: Wallpaper Patterns, page 162 (pdf p. 162). Notation explanation at the start of the chapter.

# Verification Notes

- Notation: Directly quoted from Armstrong p. 162
- Confidence: HIGH -- explicit explanation in source
- Cross-references: Verified against planned extractions
- Uncertainties: None
