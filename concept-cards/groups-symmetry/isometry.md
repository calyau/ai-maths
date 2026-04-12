---
# === CORE IDENTIFICATION ===
concept: Isometry
slug: isometry

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
  - distance-preserving transformation
  - rigid motion

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends: []
related:
  - euclidean-group
  - direct-isometry
  - opposite-isometry
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an isometry of the plane?"
  - "How are isometries classified?"
---

# Quick Definition

An isometry of the plane is a distance-preserving function g: R^2 -> R^2, satisfying ||g(x) - g(y)|| = ||x - y|| for all points x, y. Every isometry is a translation, rotation, reflection, or glide reflection.

# Core Definition

A function g: R^2 -> R^2 is an isometry if it "preserves distance; that is to say ||g(x) - g(y)|| = ||x - y|| for every pair of points x, y in R^2" (Armstrong, Ch. 24, p. 143). Armstrong shows that every isometry can be written uniquely as an orthogonal transformation followed by a translation, and classifies all isometries into four types (Theorem 24.1, p. 146).

# Prerequisites

- **Group** -- Isometries form a group under composition

# Key Properties

1. An isometry preserves all distances between points
2. Every isometry is a bijection of R^2 (Armstrong, p. 143)
3. The inverse of an isometry is an isometry
4. The composition of two isometries is an isometry
5. Every isometry can be written uniquely as (v, M) where v in R^2, M in O_2

# Construction / Recognition

## To Classify an Isometry (v, M)
1. Compute det(M)
2. If det(M) = +1: the isometry is direct (translation or rotation)
3. If det(M) = -1: the isometry is opposite (reflection or glide reflection)
4. For direct: if M = I, it is a translation; otherwise it is a rotation (find centre)
5. For opposite: if f_M(v) = -v, it is a reflection; otherwise it is a glide reflection

# Context & Application

Isometries are the fundamental building blocks of the Euclidean group. Armstrong's Chapter 24 systematically classifies all isometries of the plane and develops the ordered-pair notation that is used throughout the wallpaper classification in Chapters 25-26.

# Examples

**Example 1** (p. 146): The function g(x,y) = (1 + (x-y)/sqrt(2), 1 - sqrt(2) + (x+y)/sqrt(2)) is an anticlockwise rotation through pi/4 about the point (1,1).

**Example 2** (p. 147): The function h(x,y) = (-(x + sqrt(3)y)/2, 4 + (y - sqrt(3)x)/2) is a glide reflection along the line sqrt(3)x + y = 2.

# Relationships

## Enables
- **Euclidean group** -- The group of all isometries
- **Direct isometry** -- An isometry with det(M) = +1
- **Opposite isometry** -- An isometry with det(M) = -1

## Related
- **Translation** -- The simplest type of isometry
- **Rotation** -- A direct isometry fixing a single point
- **Reflection** -- An opposite isometry fixing a line
- **Glide reflection** -- An opposite isometry with no fixed points

# Common Errors

- **Error**: Assuming all distance-preserving functions are linear
  **Correction**: Isometries are affine, not linear: g(x) = v + f_M(x). Only the orthogonal part f_M is linear

# Common Confusions

- **Confusion**: Believing that an isometry must fix some point
  **Clarification**: Translations and glide reflections have no fixed points

# Source Reference

Chapter 24: The Euclidean Group, pages 143-151 (pdf pp. 143-151). Definition on p. 143; classification in Theorem 24.1, p. 146.

# Verification Notes

- Definition: Directly quoted from Armstrong p. 143
- Classification: From Theorem 24.1
- Confidence: HIGH -- explicit definition and complete classification theorem
- Cross-references: Verified against planned extractions
- Uncertainties: None
