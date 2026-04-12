---
# === CORE IDENTIFICATION ===
concept: Isometry Group
slug: isometry-group

# === CLASSIFICATION ===
category: fundamentals
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Groups and Symmetry"
source_slug: groups-symmetry
authors: "M.A. Armstrong"
chapter: "Axioms"
chapter_number: 2
pdf_page: 13
section: null

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS (authority control) ===
aliases:
  - group of isometries

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends:
  - group
related:
  - similarity-group
  - symmetry-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
---

# Quick Definition

The isometry group of the plane consists of all distance-preserving functions (isometries) from the plane to itself, forming a group under composition of functions. Every isometry is a bijection.

# Core Definition

"A function from the plane to itself which preserves the distance between any two points is called an isometry" (Armstrong, Exercise 2.5, Ch. 2, p. 17). Armstrong asserts that every isometry must be a bijection and that the collection of all isometries forms a group under composition.

# Prerequisites

- **Group** — The isometry group is an instance of a group

# Key Properties

1. An isometry preserves the distance between every pair of points
2. Every isometry is a bijection (one-to-one and onto)
3. The composition of two isometries is an isometry
4. The inverse of an isometry is an isometry
5. The identity map is an isometry
6. The isometry group is a subgroup of the similarity group

# Construction / Recognition

## To Verify:
1. Show that composition of two distance-preserving maps preserves distance
2. Show that the identity preserves distance
3. Show that the inverse of a distance-preserving bijection also preserves distance
4. Associativity follows from function composition

# Context & Application

Isometries include rotations, reflections, translations, and glide reflections. The isometry group is fundamental to the study of Euclidean geometry and appears extensively in later chapters on wallpaper patterns and the Euclidean group (Chapters 24-26).

# Examples

**Example 1** (Exercise 2.5, p. 17): Isometries of the plane form a group under composition.

**Example 2** (Exercise 2.6, p. 17): The rotations of the plane about a fixed point P form a subgroup of the isometry group.

# Relationships

## Builds Upon
- **Group** — This is a group under composition

## Related
- **Similarity Group** — The isometry group is a subgroup (scaling factor = 1)
- **Symmetry Group** — Symmetry groups are subgroups of the isometry group

# Common Errors

- **Error**: Forgetting to verify that every isometry is a bijection
  **Correction**: This must be proved; it is not immediately obvious that a distance-preserving function is surjective

# Common Confusions

- **Confusion**: Thinking isometries are the same as rotations
  **Clarification**: Isometries include rotations, reflections, translations, and glide reflections

# Source Reference

Chapter 2: Axioms, Exercise 2.5 (pdf p. 17).

# Verification Notes

- Definition source: Direct quote from Exercise 2.5
- Confidence rationale: Medium — defined in an exercise rather than the main text
- Uncertainties: None
- Cross-reference status: Verified
