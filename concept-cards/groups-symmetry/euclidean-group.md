---
# === CORE IDENTIFICATION ===
concept: Euclidean Group
slug: euclidean-group

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
  - "E_2"
  - "E(2)"
  - isometry group of the plane

# === TYPED RELATIONSHIPS ===
prerequisites:
  - isometry
  - semidirect-product
  - orthogonal-group
extends:
  - group
related:
  - translation-subgroup
  - point-group
  - wallpaper-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Euclidean group?"
  - "How is the Euclidean group structured as a semidirect product?"
---

# Quick Definition

The Euclidean group E_2 is the group of all distance-preserving transformations (isometries) of the plane R^2, under composition of functions. It is a semidirect product of the translation group by the orthogonal group.

# Core Definition

"The isometries of the plane form a group under composition of functions, the so called Euclidean group E_2. A function g: R^2 -> R^2 belongs to E_2, provided it preserves distance; that is to say ||g(x) - g(y)|| = ||x - y|| for every pair of points x, y in R^2" (Armstrong, Ch. 24, p. 143). Armstrong shows that E_2 = TO where T is the translation subgroup and O is the orthogonal group, and that E_2 is isomorphic to the semidirect product T x_phi O, equivalently R^2 x_psi O_2 (Armstrong, p. 143-145).

# Prerequisites

- **Isometry** -- E_2 consists of all isometries of the plane
- **Semidirect product** -- E_2 is a semidirect product T x_phi O
- **Orthogonal group** -- O_2 is the subgroup of isometries fixing the origin

# Key Properties

1. Every element g of E_2 can be written uniquely as g = tau . f where tau is a translation and f is an orthogonal transformation
2. E_2 = TO with T intersect O = {identity}
3. T is a normal subgroup of E_2; O is not normal
4. E_2 is isomorphic to R^2 x_psi O_2, the semidirect product with psi the natural action of O_2 on R^2
5. Each isometry is represented as an ordered pair (v, M) where v in R^2 and M in O_2
6. Multiplication rule: (v, M)(v_1, M_1) = (v + f_M(v_1), MM_1)
7. (v, M) is direct when det(M) = +1 and opposite when det(M) = -1

# Construction / Recognition

## Ordered Pair Representation
1. Given an isometry g, determine where it sends the origin: g(0) = v
2. Compute f = tau^{-1} . g where tau is translation by v
3. Then f fixes the origin and is therefore orthogonal, represented by a matrix M in O_2
4. The isometry g corresponds to the ordered pair (v, M)

# Context & Application

The Euclidean group is the foundation for the classification of wallpaper groups in Chapters 25-26. Armstrong demonstrates that every isometry of the plane can be decomposed into an orthogonal transformation followed by a translation. The ordered-pair notation (v, M) is used throughout the remainder of the text for concrete calculations with wallpaper patterns.

# Examples

**Example 1** (p. 145): Translation by v is the ordered pair (v, I) where I is the 2x2 identity matrix.

**Example 2** (p. 145): Rotation anticlockwise through theta about the origin is (0, A) where A is the rotation matrix.

**Example 3** (p. 145): Rotation through theta about a point c is (c - f_A(c), A).

**Example 4** (p. 145): Reflection in a line through the origin is (0, B) where B is the appropriate reflection matrix.

# Relationships

## Builds Upon
- **Semidirect product** -- E_2 = T x_phi O is the motivating example

## Enables
- **Wallpaper group** -- Wallpaper groups are subgroups of E_2
- **Point group** -- Defined via projection pi: E_2 -> O_2
- **Translation subgroup** -- The kernel of pi

## Related
- **Orthogonal group** -- O_2 sits inside E_2 as the stabilizer of the origin

# Common Errors

- **Error**: Confusing the order of composition -- applying translation then rotation vs rotation then translation
  **Correction**: In the ordered pair notation (v, M), the isometry applies M first (orthogonal), then translates by v: g(x) = v + xM^t

# Common Confusions

- **Confusion**: Thinking E_2 is a direct product T x O
  **Clarification**: E_2 is a semidirect product because conjugating a translation by an orthogonal transformation rotates the translation vector: f tau f^{-1} is translation by f(v)

# Source Reference

Chapter 24: The Euclidean Group, pages 143-151 (pdf pp. 143-151). Key results: decomposition E_2 = TO, normality of T, ordered-pair notation.

# Verification Notes

- Definition: Directly quoted from Armstrong p. 143
- Semidirect product structure: Established on pp. 144-145
- Ordered pair notation: Introduced on p. 145
- Confidence: HIGH -- explicit definition and thorough development
- Cross-references: Verified against planned extractions
- Uncertainties: None
