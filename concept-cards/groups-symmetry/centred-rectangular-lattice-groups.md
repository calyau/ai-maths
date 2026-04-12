---
# === CORE IDENTIFICATION ===
concept: Centred Rectangular Lattice Groups
slug: centred-rectangular-lattice-groups

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
section: "Case (c)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "cm and c2mm"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - wallpaper-group
  - five-lattice-types
extends:
  - seventeen-wallpaper-groups
related:
  - rectangular-lattice-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What wallpaper groups arise from a centred rectangular lattice?"
  - "What distinguishes cm from pm?"
---

# Quick Definition

A centred rectangular lattice admits two new wallpaper groups: cm (reflections with interleaved glides) and c2mm (reflections in two perpendicular directions with half-turns).

# Core Definition

"Case (c). The lattice of G is centred rectangular. The orthogonal transformations which preserve L are the same as in the rectangular case. Therefore, the point group must again be a subgroup of {I, -I, B_0, B_pi}" (Armstrong, Ch. 26, p. 166).

**cm**: Point group {I, B_0}. Contains reflections in horizontal mirrors through lattice points, plus interleaved glide reflections along lines midway between lattice points. The key distinction from pm: cm contains glides whose constituent parts (the reflection and the translation) do not separately belong to cm (Armstrong, p. 168).

**c2mm**: Point group {I, -I, B_0, B_pi}. Both B_0 and B_pi are realized by reflections.

# Prerequisites

- **Wallpaper group** -- cm and c2mm are wallpaper groups
- **Five lattice types** -- Centred rectangular is case (c)

# Key Properties

1. The centred rectangular lattice has the same symmetry-preserving orthogonal transformations as the rectangular lattice
2. cm has reflections and glides; the vertical direction is determined by 2b - a
3. The "c" indicates the centred (non-primitive) lattice
4. In cm, some glides cannot be decomposed into a reflection and translation both in the group
5. c2mm has reflections in both horizontal and vertical directions

# Construction / Recognition

## cm vs pm (from Theorem 26.1)
- Both contain reflections and glide reflections
- In pm, every glide can be decomposed as a reflection followed by a translation, both in the group
- In cm, certain glides have constituent parts that do not belong to cm
- This structural difference makes them non-isomorphic

# Context & Application

The centred rectangular case contributes only two new groups because the point group options are the same as for rectangular lattices. The "c" prefix distinguishes these from the "p" (primitive) groups. The distinction between cm and pm is one of the subtler points in the classification.

# Examples

**Example 1** (p. 168, Theorem 26.1): The glide (a/2 + (2b-a)/2, B_0) in cm has constituent parts -- the reflection (0, B_0) and translation (a/2 + (2b-a)/2, I) -- that do not both belong to cm.

# Relationships

## Builds Upon
- **Five lattice types** -- Centred rectangular is case (c)

## Related
- **Rectangular lattice groups** -- Same point group possibilities but different lattice

# Common Errors

- **Error**: Assuming cm is just pm with a different lattice choice
  **Correction**: cm and pm are non-isomorphic groups; the structural difference in glide decomposability distinguishes them

# Common Confusions

- **Confusion**: Confusing the centred rectangular lattice with a rectangular lattice plus a centre point
  **Clarification**: The centred rectangular lattice is equivalently described as a rhombic lattice; the "centred rectangle" viewpoint uses a non-primitive cell

# Source Reference

Chapter 26: Wallpaper Patterns, Case (c), pages 166-167 (pdf pp. 166-167). Distinctness proof in Theorem 26.1, p. 168.

# Verification Notes

- Description: From Armstrong pp. 166-167
- Distinctness: Theorem 26.1
- Confidence: HIGH -- detailed case analysis
- Cross-references: Verified against planned extractions
- Uncertainties: None
