---
# === CORE IDENTIFICATION ===
concept: Isometry
slug: isometry

# === CLASSIFICATION ===
category: symmetry
subcategory: geometric-symmetry
tier: intermediate

# === PROVENANCE ===
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Symmetry"
chapter_number: 6
pdf_page: 162
section: "6.2 Isometries"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases:
  - "rigid motion"
  - "distance-preserving map"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonal-operator
  - dot-product
extends: []
related:
  - translation
  - rotation-plane
  - reflection-isometry
  - glide-reflection
  - isometry-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is an isometry?"
  - "How does every isometry decompose into an orthogonal operator and a translation?"
---

# Quick Definition

An isometry of R^n is a distance-preserving map f such that |f(u) - f(v)| = |u - v| for all u, v. Every isometry is uniquely the composition of an orthogonal linear operator and a translation.

# Core Definition

An isometry of n-dimensional space R^n is a distance-preserving map f from R^n to itself: |f(u) - f(v)| = |u - v| for all u and v (Artin, (6.2.1), p. 164). Theorem 6.2.3 shows that an isometry fixing the origin is an orthogonal linear operator. Corollary 6.2.7 shows every isometry f decomposes uniquely as f = t_a * phi, where t_a is translation by a = f(0) and phi is an orthogonal linear operator.

# Prerequisites

- **Orthogonal operator** — The linear part of an isometry
- **Dot product** — Distance is defined via the dot product

# Key Properties

1. Preserves distances: |f(u) - f(v)| = |u - v|
2. Decomposes uniquely as f = t_a * phi (translation times orthogonal operator)
3. An isometry fixing the origin is an orthogonal linear operator (Theorem 6.2.3)
4. The composition of isometries is an isometry
5. Every isometry is invertible
6. Either orientation-preserving (det phi = 1) or orientation-reversing (det phi = -1)

# Construction / Recognition

## To Construct:
1. Choose an orthogonal linear operator phi (rotation or reflection)
2. Choose a translation vector a
3. The isometry is f(x) = phi(x) + a

## To Recognize:
1. Verify |f(u) - f(v)| = |u - v| for all u, v
2. Or verify the map preserves dot products after accounting for translation

# Context & Application

Isometries are the "symmetries of space" -- they preserve all geometric properties defined by distance. The group of all isometries M_n is the setting for the study of symmetry in Chapter 6. In the plane, isometries are classified into four types: translations, rotations, reflections, and glide reflections (Theorem 6.3.4).

# Examples

**Example 1** (p. 164): Orthogonal linear operators are isometries (fixing the origin).

**Example 2** (p. 164): Translation t_a(x) = x + a is an isometry (but not a linear operator unless a = 0).

**Example 3** (p. 165): The decomposition f = t_a * phi is unique because a = f(0) and phi = t_{-a} * f.

# Relationships

## Builds Upon
- **Orthogonal operator** — The linear part of every isometry
- **Translation** — The translational part of every isometry

## Enables
- **Symmetry group** — Groups of isometries preserving a figure
- **Isometry group** — The group M_n of all isometries

## Related
- **Rotation (plane)** — An orientation-preserving isometry fixing a point
- **Glide reflection** — An orientation-reversing isometry

# Common Errors

- **Error**: Assuming isometries are linear operators
  **Correction**: Translations are isometries but not linear operators (they don't fix the origin)

# Common Confusions

- **Confusion**: Thinking distance-preserving automatically means angle-preserving
  **Clarification**: Distance preservation implies angle preservation (and dot product preservation after fixing the origin), but the converse requires care

# Source Reference

Chapter 6: Symmetry, Section 6.2, (6.2.1), Theorem 6.2.3, Corollary 6.2.7, pages 164-166.

# Verification Notes

- Definition source: Direct from (6.2.1)
- Confidence rationale: Explicitly defined with multiple characterizations
- Uncertainties: None
- Cross-reference status: Verified
