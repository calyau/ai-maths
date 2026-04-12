---
# === CORE IDENTIFICATION ===
concept: Direct Isometry
slug: direct-isometry

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
  - orientation-preserving isometry

# === TYPED RELATIONSHIPS ===
prerequisites:
  - isometry
  - euclidean-group
extends:
  - isometry
related:
  - translation
  - rotation
contrasts_with:
  - opposite-isometry

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a direct isometry?"
  - "How do direct and opposite isometries differ?"
---

# Quick Definition

A direct isometry is an isometry (v, M) of the plane for which det(M) = +1. Every direct isometry is either a translation or a rotation (Theorem 24.1).

# Core Definition

"If g = tau f and if f is a rotation, then g is called a direct isometry" (Armstrong, Ch. 24, p. 144). In the ordered pair notation, a direct isometry is represented by (v, A) where A is a rotation matrix with det(A) = +1. Theorem 24.1 establishes: "Every direct isometry is a translation or a rotation" (Armstrong, p. 146).

# Prerequisites

- **Isometry** -- A direct isometry is a special type of isometry
- **Euclidean group** -- Direct isometries form a subgroup of E_2

# Key Properties

1. Represented by ordered pair (v, A) where A is a rotation matrix (det A = +1)
2. When A = I (theta = 0), the isometry is a translation by v
3. When A is not I, the isometry is a rotation about a unique centre c = v(I - A^t)^{-1}
4. Direct isometries preserve orientation
5. The direct isometries form a subgroup of E_2 (of index 2)

# Construction / Recognition

## To Identify a Direct Isometry (v, A)
1. Check det(A) = +1
2. If A = I: the isometry is translation by v
3. If A is not I: solve c - f_A(c) = v for the centre of rotation c

# Context & Application

Direct isometries are the orientation-preserving elements of E_2. They form a normal subgroup of index 2. Armstrong classifies them completely in Theorem 24.1 as either translations or rotations.

# Examples

**Example 1** (p. 145): (v, I) is translation by v -- a direct isometry with trivial orthogonal part.

**Example 2** (p. 145): (0, A) with A the pi/4-rotation matrix is rotation about the origin.

**Example 3** (p. 146): Armstrong works out that g(x,y) = (1 + (x-y)/sqrt(2), 1-sqrt(2) + (x+y)/sqrt(2)) is rotation through pi/4 about (1,1).

# Relationships

## Builds Upon
- **Isometry** -- Direct isometries are isometries with det(M) = +1

## Related
- **Translation** -- A direct isometry with M = I
- **Rotation** -- A direct isometry with M not equal to I

## Contrasts With
- **Opposite isometry** -- Has det(M) = -1; includes reflections and glide reflections

# Common Errors

- **Error**: Assuming every direct isometry has a fixed point
  **Correction**: Translations are direct isometries with no fixed points

# Common Confusions

- **Confusion**: Confusing "direct" with "simple"
  **Clarification**: "Direct" refers specifically to orientation preservation (det = +1), not to simplicity of the transformation

# Source Reference

Chapter 24: The Euclidean Group, pages 144-146 (pdf pp. 144-146). Classification in Theorem 24.1.

# Verification Notes

- Definition: Directly from Armstrong p. 144
- Classification: Theorem 24.1
- Confidence: HIGH -- explicit definition and classification
- Cross-references: Verified against planned extractions
- Uncertainties: None
