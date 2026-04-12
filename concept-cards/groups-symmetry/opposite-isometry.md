---
# === CORE IDENTIFICATION ===
concept: Opposite Isometry
slug: opposite-isometry

# === CLASSIFICATION ===
category: euclidean-geometry
subcategory: null
tier: advanced

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "The Euclidean Group"
chapter_number: 24
pdf_page: 143
section: null

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - orientation-reversing isometry
  - indirect isometry

# === TYPED RELATIONSHIPS ===
prerequisites:
  - isometry
  - euclidean-group
extends:
  - isometry
related:
  - reflection
  - glide-reflection
contrasts_with:
  - direct-isometry

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an opposite isometry?"
  - "What types of opposite isometries exist?"
---

# Quick Definition

An opposite isometry is an isometry (v, M) of the plane for which det(M) = -1. Every opposite isometry is either a reflection or a glide reflection (Theorem 24.1).

# Core Definition

"In the other case, when f is a reflection, g is said to be an opposite isometry" (Armstrong, Ch. 24, p. 144). In ordered pair notation, an opposite isometry has the form (v, B) where B is a reflection matrix with det(B) = -1. Theorem 24.1 states: "Every opposite isometry is a reflection or a glide reflection" (Armstrong, p. 146).

# Prerequisites

- **Isometry** -- An opposite isometry is a type of isometry
- **Euclidean group** -- Opposite isometries form a coset in E_2

# Key Properties

1. Represented by ordered pair (v, B) where B is a reflection matrix (det B = -1)
2. If f_B(v) = -v, the isometry is a reflection
3. If f_B(v) is not equal to -v, the isometry is a glide reflection
4. Opposite isometries reverse orientation
5. The product of two opposite isometries is a direct isometry
6. The opposite isometries do not form a subgroup (they are a coset of the direct isometries)

# Construction / Recognition

## To Classify an Opposite Isometry (v, B)
1. Check det(B) = -1
2. Compute f_B(v)
3. If f_B(v) = -v: reflection in the line through v/2
4. If f_B(v) is not -v: glide reflection; compute w = v - f_B(v), decompose v into components along w and perpendicular to w

# Context & Application

Armstrong distinguishes direct and opposite isometries to completely classify the elements of E_2. The classification is essential for understanding wallpaper groups, which contain specific combinations of these isometry types.

# Examples

**Example 1** (p. 145): Reflection in a line through the origin is (0, B) -- the simplest opposite isometry.

**Example 2** (p. 145): Reflection in a line m not through the origin is (2a, B) where a is the foot of the perpendicular from the origin to m.

**Example 3** (p. 147): h(x,y) = (-(x + sqrt(3)y)/2, 4 + (y - sqrt(3)x)/2) is a glide reflection along sqrt(3)x + y = 2 with glide vector b = (-sqrt(3), 3).

# Relationships

## Builds Upon
- **Isometry** -- An opposite isometry is an orientation-reversing isometry

## Related
- **Reflection** -- An opposite isometry with f_B(v) = -v
- **Glide reflection** -- An opposite isometry with f_B(v) not equal to -v

## Contrasts With
- **Direct isometry** -- Has det(M) = +1; includes translations and rotations

# Common Errors

- **Error**: Assuming a reflection can be recognized just from the matrix M
  **Correction**: The matrix B alone determines the line direction; the vector v determines whether it is a reflection or a glide reflection

# Common Confusions

- **Confusion**: Thinking opposite isometries form a subgroup
  **Clarification**: The composition of two opposite isometries is direct, so opposite isometries form a coset, not a subgroup

# Source Reference

Chapter 24: The Euclidean Group, pages 144-148 (pdf pp. 144-148). Classification in Theorem 24.1, p. 146.

# Verification Notes

- Definition: From Armstrong p. 144
- Classification: Theorem 24.1
- Confidence: HIGH -- explicit definition and classification
- Cross-references: Verified against planned extractions
- Uncertainties: None
