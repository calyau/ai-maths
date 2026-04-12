---
# === CORE IDENTIFICATION ===
concept: Wallpaper Isomorphism Theorem
slug: wallpaper-isomorphism-theorem

# === CLASSIFICATION ===
category: crystallography
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Lattices and Point Groups"
chapter_number: 25
pdf_page: 152
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Theorem 25.5"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - wallpaper-group
  - isometry-classification-theorem
extends: []
related:
  - point-group
  - translation-subgroup
  - seventeen-wallpaper-groups
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does an isomorphism between wallpaper groups preserve?"
  - "How do I determine the wallpaper group of a pattern?"
---

# Quick Definition

An isomorphism between wallpaper groups sends translations to translations, rotations to rotations, reflections to reflections, and glide reflections to glide reflections. Consequently, isomorphic wallpaper groups have isomorphic point groups.

# Core Definition

"(25.5) Theorem. An isomorphism between wallpaper groups takes translations to translations, rotations to rotations, reflections to reflections and glide reflections to glide reflections" (Armstrong, Ch. 25, p. 159). The proof uses order considerations (translations and glides have infinite order; rotations and reflections have finite order) and commutativity arguments to distinguish among the types. Corollary 25.6 follows: isomorphic wallpaper groups have isomorphic point groups.

# Prerequisites

- **Wallpaper group** -- The theorem applies to wallpaper groups
- **Isometry classification theorem** -- The four types that must be preserved

# Key Properties

1. Isomorphisms preserve the isometry type of each element
2. In particular, the translation subgroup maps to the translation subgroup
3. Corollary (25.6): Isomorphic wallpaper groups have isomorphic point groups
4. The contrapositive is the main tool: non-isomorphic point groups imply non-isomorphic wallpaper groups

# Construction / Recognition

## Proof Strategy
1. Translations and glides have infinite order; rotations and reflections have finite order
2. Show translations map to translations (not glides) by a commutativity argument
3. Show reflections map to reflections (not half-turns) by another commutativity argument
4. Rotations are then forced to map to rotations

# Context & Application

This theorem is the key tool for proving the seventeen wallpaper groups are genuinely distinct. It reduces the problem: groups with non-isomorphic point groups are automatically non-isomorphic. For groups with the same point group, one must find finer invariants (presence or absence of reflections, behavior of glides, etc.).

# Examples

**Example 1** (Ch. 26): The groups pm and pg both have point group Z_2, but pg has no reflections while pm does, so they are not isomorphic.

**Example 2** (Ch. 26, Theorem 26.1): Among p2, pm, pg, cm (all with point group Z_2 or Z_2-related), the theorem helps distinguish them by tracking which isometry types are present.

# Relationships

## Builds Upon
- **Wallpaper group** -- The theorem characterizes isomorphisms between wallpaper groups
- **Isometry classification theorem** -- The four isometry types that are preserved

## Enables
- **Seventeen wallpaper groups** -- Used to prove the 17 groups are distinct

# Common Errors

- **Error**: Assuming any group isomorphism between wallpaper groups is "geometric"
  **Correction**: The theorem proves that any abstract group isomorphism automatically preserves geometric type -- this is a non-trivial result

# Common Confusions

- **Confusion**: Thinking the theorem is obvious because isomorphisms "preserve structure"
  **Clarification**: It is not obvious a priori that a purely algebraic isomorphism must respect the geometric classification of elements; the proof requires careful argument

# Source Reference

Chapter 25: Lattices and Point Groups, Theorem 25.5 and Corollary 25.6, pages 159-160 (pdf pp. 159-160).

# Verification Notes

- Theorem: Directly quoted from Armstrong p. 159
- Proof: Complete in source
- Confidence: HIGH -- named theorem with complete proof
- Cross-references: Verified against planned extractions
- Uncertainties: None
