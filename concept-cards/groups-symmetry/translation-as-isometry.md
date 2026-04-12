---
# === CORE IDENTIFICATION ===
concept: Translation
slug: translation-as-isometry

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
  - "(v, I)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - isometry
extends:
  - direct-isometry
related:
  - euclidean-group
  - translation-subgroup
  - glide-reflection
contrasts_with:
  - rotation
  - reflection

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a translation in the Euclidean group?"
  - "How do translations form a normal subgroup of E_2?"
---

# Quick Definition

A translation by vector v is the isometry tau(x) = v + x, represented as the ordered pair (v, I). Translations form a normal subgroup T of the Euclidean group E_2, and their conjugation by an orthogonal transformation f simply rotates/reflects the translation vector.

# Core Definition

"Translation by the vector v is the function tau: R^2 -> R^2 defined by tau(x) = v + x for all x in R^2. Since tau(0) = v, a translation is completely determined if we know where it sends the origin" (Armstrong, Ch. 24, p. 143). In ordered pair notation, a translation is (v, I) where I is the identity matrix.

# Prerequisites

- **Isometry** -- A translation is a type of isometry

# Key Properties

1. Represented by (v, I) in ordered pair notation
2. A direct isometry (det(I) = +1)
3. Has no fixed points (unless v = 0, giving the identity)
4. Has infinite order (unless v = 0)
5. The translations form a subgroup T of E_2
6. T is a normal subgroup of E_2: f * tau * f^{-1} = translation by f(v) for f in O
7. T is isomorphic to the additive group R^2
8. Product of two translations: (u, I)(v, I) = (u + v, I) -- translations commute

# Construction / Recognition

## To Identify a Translation
1. In ordered pair notation: check that M = I
2. In function notation: check that g(x) = v + x for some constant v

## Conjugation by Orthogonal Transformation
f * tau * f^{-1} is translation by f(v). This is why T is normal: conjugating a translation by any element of E_2 produces another translation.

# Context & Application

Translations capture the periodicity of wallpaper patterns. The translation subgroup of a wallpaper group determines its lattice. Armstrong shows that T is normal in E_2 (p. 144), which is essential for the semidirect product decomposition E_2 = T x_phi O.

# Examples

**Example 1** (p. 143): Translation by v is tau(x) = v + x, which sends the origin to v.

**Example 2** (p. 144): The product tau_1 * tau_2^{-1}(x) = (u - v) + x is translation by u - v, confirming T is a subgroup.

**Example 3** (p. 144): Conjugation: f * tau * f^{-1}(x) = f(v) + x for orthogonal f, showing T is normal.

# Relationships

## Builds Upon
- **Direct isometry** -- A translation is a direct isometry with M = I

## Enables
- **Translation subgroup** -- The translation subgroup is the collection of all translations in a wallpaper group
- **Lattice** -- The orbit of the origin under translations

## Contrasts With
- **Rotation** -- Has a fixed point; a translation does not
- **Reflection** -- Has a fixed line; a translation does not

# Common Errors

- **Error**: Treating translations as linear transformations
  **Correction**: Translations are affine, not linear: tau(0) = v (not 0 unless v = 0)

# Common Confusions

- **Confusion**: Thinking the composition of a translation and a rotation is a translation
  **Clarification**: The composition of a non-trivial translation and a non-trivial rotation is a rotation about a different centre

# Source Reference

Chapter 24: The Euclidean Group, pages 143-145 (pdf pp. 143-145).

# Verification Notes

- Definition: Directly from Armstrong p. 143
- Normality proof: From p. 144
- Confidence: HIGH -- explicit definition
- Cross-references: Verified against planned extractions
- Uncertainties: None
