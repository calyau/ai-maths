---
# === CORE IDENTIFICATION ===
concept: Isometry Classification Theorem
slug: isometry-classification-theorem

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
  - "Theorem 24.1"
  - classification of plane isometries

# === TYPED RELATIONSHIPS ===
prerequisites:
  - direct-isometry
  - opposite-isometry
  - euclidean-group
extends: []
related:
  - translation
  - rotation
  - reflection
  - glide-reflection
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What are the four types of plane isometries?"
  - "How do I determine the type of an isometry from its ordered pair representation?"
---

# Quick Definition

Every isometry of the plane is exactly one of: a translation, a rotation, a reflection, or a glide reflection. This is Theorem 24.1 in Armstrong.

# Core Definition

"(24.1) Theorem. Every direct isometry is a translation or a rotation. Every opposite isometry is a reflection or a glide reflection" (Armstrong, Ch. 24, p. 146). The proof proceeds by analyzing the ordered pair (v, M): for direct isometries (det M = +1), either M = I (translation) or I - M is invertible (rotation with a unique centre); for opposite isometries (det M = -1), either f_M(v) = -v (reflection) or the remainder is a glide reflection.

# Prerequisites

- **Direct isometry** -- One of the two classes (translations and rotations)
- **Opposite isometry** -- The other class (reflections and glide reflections)
- **Euclidean group** -- The theorem classifies all elements of E_2

# Key Properties

1. Every plane isometry falls into exactly one of four types
2. Translations: (v, I), direct, no fixed points (unless v = 0)
3. Rotations: (v, A) with A not I and det A = +1, direct, one fixed point (the centre)
4. Reflections: (v, B) with det B = -1 and f_B(v) = -v, opposite, a line of fixed points
5. Glide reflections: (v, B) with det B = -1 and f_B(v) not equal to -v, opposite, no fixed points

# Construction / Recognition

## Decision Procedure for an Isometry (v, M)
1. Compute det(M)
2. If det(M) = +1 (direct):
   - If M = I: translation by v
   - If M is not I: rotation; solve c(I - M^t) = v for centre c
3. If det(M) = -1 (opposite):
   - Compute f_M(v) = vM^t
   - If f_M(v) = -v: reflection in line through v/2
   - If f_M(v) is not -v: glide reflection; decompose v = 2a + b

# Context & Application

This theorem is the complete classification of plane isometries, analogous to classifying elements of a group. It provides the foundation for the wallpaper group classification: each element of a wallpaper group is one of these four types, and isomorphisms between wallpaper groups must respect these types (Theorem 25.5).

# Examples

**Example 1** (p. 146): g(x,y) = (1 + (x-y)/sqrt(2), 1 - sqrt(2) + (x+y)/sqrt(2)) has det(M) = +1, M is not I, so it is a rotation. Centre found to be (1,1), angle pi/4.

**Example 2** (p. 147): h(x,y) = (-(x + sqrt(3)y)/2, 4 + (y - sqrt(3)x)/2) has det(M) = -1 and f_M(v) is not -v, so it is a glide reflection along sqrt(3)x + y = 2.

# Relationships

## Builds Upon
- **Direct isometry** and **Opposite isometry** -- The two main classes

## Enables
- **Wallpaper group classification** -- Theorem 25.5 shows isomorphisms preserve isometry types

## Related
- **Translation**, **Rotation**, **Reflection**, **Glide reflection** -- The four types

# Common Errors

- **Error**: Classifying a glide reflection as a reflection because it involves a reflection
  **Correction**: A glide reflection is a distinct isometry type with no fixed points; check whether f_B(v) = -v

# Common Confusions

- **Confusion**: Thinking there might be other types of isometries not listed
  **Clarification**: The theorem is exhaustive -- every plane isometry is one of these four types

# Source Reference

Chapter 24: The Euclidean Group, Theorem 24.1 and proof, pages 146-148 (pdf pp. 146-148).

# Verification Notes

- Theorem statement: Directly quoted from Armstrong p. 146
- Proof: Complete in source
- Confidence: HIGH -- named theorem with complete proof
- Cross-references: Verified against planned extractions
- Uncertainties: None
