---
# === CORE IDENTIFICATION ===
concept: Ordered Pair Notation
slug: ordered-pair-notation

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
  - "(v, M) notation"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - euclidean-group
  - isometry
extends: []
related:
  - semidirect-product
  - isometry-classification-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How are isometries represented as ordered pairs?"
  - "How do I compute the product of two isometries?"
---

# Quick Definition

Every isometry of the plane can be represented as an ordered pair (v, M) where v is a vector in R^2 and M is a 2x2 orthogonal matrix. The isometry sends x to v + xM^t, and pairs multiply via (v, M)(v_1, M_1) = (v + f_M(v_1), MM_1).

# Core Definition

"We may therefore think of each isometry as an ordered pair (v, M) in which v in R^2 and M in O_2, with multiplication given by (v, M)(v_1, M_1) = (v + f_M(v_1), MM_1)" (Armstrong, Ch. 24, p. 145). The formula for the isometry is g(x) = v + xM^t. This notation identifies E_2 with the semidirect product R^2 x_psi O_2.

# Prerequisites

- **Euclidean group** -- The notation represents elements of E_2
- **Isometry** -- Each ordered pair represents an isometry

# Key Properties

1. g(x) = v + f_M(x) = v + xM^t for all x in R^2
2. Product: (v, M)(v_1, M_1) = (v + f_M(v_1), MM_1)
3. Identity: (0, I)
4. Inverse: (v, M)^{-1} = (-f_{M^{-1}}(v), M^{-1})
5. (v, M) is direct when det(M) = +1, opposite when det(M) = -1
6. Translations: (v, I); rotations about origin: (0, A); reflections through origin: (0, B)
7. Rotation about point c: (c - f_A(c), A)
8. Reflection in line through a: (2a, B) where f_B(a) = -a

# Construction / Recognition

## Standard Forms
- **Translation by v**: (v, I)
- **Rotation through theta about origin**: (0, A) where A = [[cos theta, -sin theta], [sin theta, cos theta]]
- **Rotation about c**: (c - f_A(c), A)
- **Reflection in line through origin at angle phi/2**: (0, B) where B = [[cos phi, sin phi], [sin phi, -cos phi]]
- **Reflection in line m**: (2a, B) where a is perpendicular from origin to m
- **Glide reflection**: (2a + b, B) where f_B(b) = b and b is non-zero

# Context & Application

This notation is Armstrong's primary computational tool for Chapters 24-26. All calculations with wallpaper groups, isometry classification, and the verification of the seventeen wallpaper groups are carried out using ordered pairs.

# Examples

**Example 1** (p. 145): Rotation anticlockwise through theta about the origin is (0, A) with A the standard rotation matrix.

**Example 2** (p. 145): Reflection in the line m (not through origin) is (2a, B) where a is the perpendicular from origin to m.

**Example 3** (p. 146): The worked example shows g(x,y) = (1 + (x-y)/sqrt(2), ...) corresponds to (v, M) with v = (1, 1-sqrt(2)) and M the pi/4 rotation matrix.

# Relationships

## Related
- **Semidirect product** -- The ordered pair notation encodes the semidirect product R^2 x_psi O_2
- **Isometry classification theorem** -- Uses ordered pairs to classify isometries

# Common Errors

- **Error**: Computing the product as (v + v_1, MM_1) rather than (v + f_M(v_1), MM_1)
  **Correction**: The first coordinate involves applying f_M to v_1 before adding v; this is the "twist" from the semidirect product

# Common Confusions

- **Confusion**: Confusing (v, M) with applying M then translating vs translating then applying M
  **Clarification**: The convention is g(x) = v + xM^t: first apply the orthogonal transformation, then translate

# Source Reference

Chapter 24: The Euclidean Group, pages 145-148 (pdf pp. 145-148). Formula and multiplication rule on p. 145.

# Verification Notes

- Notation: Directly from Armstrong p. 145
- Multiplication rule: Directly quoted
- Confidence: HIGH -- explicit formula and rule
- Cross-references: Verified against planned extractions
- Uncertainties: None
