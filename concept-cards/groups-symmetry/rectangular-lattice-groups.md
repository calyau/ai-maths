---
# === CORE IDENTIFICATION ===
concept: Rectangular Lattice Groups
slug: rectangular-lattice-groups

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
section: "Case (b)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "pm, pg, p2mm, p2mg, p2gg"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - wallpaper-group
  - five-lattice-types
  - glide-reflection
extends:
  - seventeen-wallpaper-groups
related:
  - oblique-lattice-groups
  - centred-rectangular-lattice-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What wallpaper groups arise from a rectangular lattice?"
  - "What distinguishes pm from pg?"
  - "What distinguishes a direct product from a semidirect product?"
---

# Quick Definition

A rectangular lattice admits five wallpaper groups beyond p1 and p2: pm (mirrors), pg (glides only), p2mm (two mirror directions), p2mg (one mirror, one glide direction), and p2gg (two glide directions, no mirrors).

# Core Definition

"Case (b). The lattice of G is rectangular. There are now four orthogonal transformations which preserve L; namely, the identity, a half turn about 0, reflection in the x-axis, and reflection in the y-axis. Therefore, the point group of G is a subgroup of {I, -I, B_0, B_pi}" (Armstrong, Ch. 26, p. 164).

The five groups are distinguished by which reflections in the point group are realized as actual reflections vs. glide reflections in G:
- **pm**: J = {I, B_0}, realized by reflections
- **pg**: J = {I, B_0}, no reflections in G (only glides)
- **p2mm**: J = {I, -I, B_0, B_pi}, both B_0 and B_pi realized by reflections
- **p2mg**: J = {I, -I, B_0, B_pi}, one mirror direction, one glide direction
- **p2gg**: J = {I, -I, B_0, B_pi}, no reflections in G

# Prerequisites

- **Wallpaper group** -- These are wallpaper groups with rectangular lattice
- **Five lattice types** -- Rectangular is case (b)
- **Glide reflection** -- Essential for distinguishing pg from pm

# Key Properties

1. pm: horizontal mirrors through and between lattice points; parallel glides exist
2. pg: only horizontal glide reflections with glide length a/2; no reflections
3. p2mm: both horizontal and vertical mirrors; half-turns at intersections
4. p2mg: horizontal mirrors, vertical glides (or vice versa); half-turns present
5. p2gg: no mirrors at all; horizontal and vertical glides; half-turns present
6. Interchanging horizontal/vertical for {I, B_pi} gives groups isomorphic to those for {I, B_0}

# Construction / Recognition

## pg Construction (Armstrong, p. 164)
1. Point group {I, B_0} with no reflections in G
2. G contains a glide (ka/2, B_0); k must be odd
3. The basic glide is (a/2, B_0) with glide length a/2
4. All non-translations are glides ((m + 1/2)a + nb, B_0)

## p2mg Construction (Armstrong, p. 165)
1. Choose origin at intersection of horizontal mirror and vertical glide line
2. G contains (0, B_0) (reflection) and (b/2, B_pi) (glide)
3. Their product (b/2, -I) is a half-turn about b/4
4. Four cosets: H, H(0, B_0), H(b/2, B_pi), H(b/2, -I)

# Context & Application

The rectangular case produces the largest number of new groups (five) of any single lattice type. The key distinction between groups with the same point group is whether orthogonal transformations are realized as reflections or glides.

# Examples

**Example 1** (p. 164): In pg, the elements not in H have the form ((m + 1/2)a + nb, B_0), all glides along horizontal lines.

**Example 2** (p. 165): In p2mg, horizontal lines carry reflections and vertical lines carry glides; half-turn centres are offset from lattice points.

# Relationships

## Builds Upon
- **Five lattice types** -- Rectangular lattice is case (b)

## Related
- **Centred rectangular lattice groups** -- cm and c2mm
- **Glide reflection** -- Distinguishing feature between pm/pg and p2mm/p2mg/p2gg

# Common Errors

- **Error**: Assuming pg and pm are the same because they have the same point group Z_2
  **Correction**: pg has no reflections (only glide reflections); pm contains actual reflections

# Common Confusions

- **Confusion**: Thinking p2mg and p2gm are different groups
  **Clarification**: Interchanging the roles of horizontal and vertical yields isomorphic groups, so there is no separate "p2gm"

# Source Reference

Chapter 26: Wallpaper Patterns, Case (b), pages 163-166 (pdf pp. 163-166).

# Verification Notes

- Description: From Armstrong pp. 163-166
- Confidence: HIGH -- detailed case analysis in source
- Cross-references: Verified against planned extractions
- Uncertainties: None
