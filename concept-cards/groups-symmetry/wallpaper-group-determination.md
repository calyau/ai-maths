---
# === CORE IDENTIFICATION ===
concept: Wallpaper Group Determination
slug: wallpaper-group-determination

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
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - wallpaper group identification

# === TYPED RELATIONSHIPS ===
prerequisites:
  - seventeen-wallpaper-groups
  - five-lattice-types
  - point-group
  - crystallographic-restriction
extends: []
related:
  - wallpaper-notation
  - wallpaper-isomorphism-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do I determine the wallpaper group of a pattern?"
---

# Quick Definition

To determine the wallpaper group of a repeating pattern, identify the lattice type, determine the point group (rotation orders and reflection/glide content), and distinguish between reflections and glide reflections to select among the seventeen groups.

# Core Definition

Armstrong's classification in Chapter 26 proceeds by: (1) identifying the lattice type (oblique, rectangular, centred rectangular, square, or hexagonal), (2) determining which orthogonal transformations preserve the lattice (giving the maximal possible point group), (3) identifying the actual point group as a subgroup, and (4) distinguishing whether each reflection in the point group is realized as a true reflection or a glide reflection in the wallpaper group. This procedure is synthesized from Armstrong's case-by-case analysis, Ch. 26, pp. 162-170.

# Prerequisites

- **Seventeen wallpaper groups** -- The target of the identification
- **Five lattice types** -- The first classification step
- **Point group** -- The second classification step
- **Crystallographic restriction** -- Constrains possible point groups

# Key Properties

1. The lattice type is determined by the translation subgroup
2. The point group is determined by the rotation and reflection content
3. Groups with non-isomorphic point groups are automatically distinct
4. Groups with the same point group are distinguished by reflection vs. glide realization
5. Theorems 26.1-26.4 prove the 17 groups are genuinely distinct

# Construction / Recognition

## Step-by-Step Determination
1. **Find the lattice**: Identify two independent translations. Determine their lengths and the angle between them. Classify the lattice as oblique, rectangular, centred rectangular, square, or hexagonal.
2. **Find the highest rotation order**: Look for rotational symmetry of order 2, 3, 4, or 6.
3. **Check for reflections**: Look for lines of mirror symmetry.
4. **Check for glide reflections**: Look for glide symmetry (reflection + parallel translation).
5. **Match to the table**:
   - No rotation, no reflection: p1
   - Half-turns only: p2
   - Reflections, no rotation beyond order 2: pm, pg, cm, p2mm, p2mg, p2gg, c2mm
   - Order-4 rotation: p4, p4mm, p4gm
   - Order-3 rotation: p3, p3m1, p31m
   - Order-6 rotation: p6, p6mm
6. **Distinguish within each set** using reflection/glide analysis

# Context & Application

Armstrong's approach is constructive: he builds each group from its lattice and point group data, then proves distinctness. Exercise 26.2 asks the reader to determine the wallpaper group of given patterns. The determination procedure is implicit in Armstrong's case analysis rather than stated as an explicit algorithm.

# Examples

**Example 1** (Exercise 26.2, p. 170): Armstrong provides patterns from various cultures and asks the reader to determine their wallpaper groups.

**Example 2** (p. 163): A pattern with only two independent translations and no rotations or reflections has group p1.

**Example 3** (p. 165): A pattern with horizontal mirrors and vertical glides has group p2mg.

# Relationships

## Builds Upon
- **Five lattice types** -- First classification step
- **Point group** -- Second classification step
- **Crystallographic restriction** -- Constrains rotation orders

## Related
- **Wallpaper notation** -- The naming system used for the result
- **Wallpaper isomorphism theorem** -- Ensures the classification is well-defined

# Common Errors

- **Error**: Stopping at the point group without checking reflection vs. glide realization
  **Correction**: Multiple groups share the same point group; the final distinction requires checking whether B_0 is realized as a reflection or only as a glide

- **Error**: Misidentifying the lattice type by choosing non-optimal basis vectors
  **Correction**: Always choose a as shortest non-zero lattice vector, then b as shortest vector skew to a

# Common Confusions

- **Confusion**: Thinking the pattern itself determines the wallpaper group uniquely
  **Clarification**: Different patterns can share the same wallpaper group; the group captures the symmetry type, not the visual design

# Source Reference

Chapter 26: Wallpaper Patterns, pages 162-170 (pdf pp. 162-170). Synthesized from Armstrong's case-by-case classification.

# Verification Notes

- Procedure: Synthesized from Armstrong's case analysis; not stated as an explicit algorithm in the source
- Confidence: MEDIUM -- the procedure is implicit in the source rather than explicitly stated
- Cross-references: Verified against planned extractions
- Uncertainties: The step-by-step procedure is a synthesis, not a direct quote
