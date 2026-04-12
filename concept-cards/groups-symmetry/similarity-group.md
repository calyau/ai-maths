---
# === CORE IDENTIFICATION ===
concept: Similarity Group
slug: similarity-group

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
  - group of similarities

# === TYPED RELATIONSHIPS ===
prerequisites:
  - group
extends:
  - group
related:
  - isometry-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a group?"
---

# Quick Definition

The similarity group of the plane is the group of all similarity transformations (distance-scaling, shape-preserving maps) under composition. It is the group underlying Euclidean geometry in the sense that Euclidean properties are those preserved by similarities.

# Core Definition

"A mathematician thinking about Euclidean geometry finds he is studying those properties of figures which are left unchanged by the elements of a particular group, the group of similarities of the plane. A similarity enlarges or shrinks figures while keeping them the same shape. More precisely, it sends straight-line segments to straight-line segments, multiplying their lengths by a factor which is the same for every segment" (Armstrong, Ch. 2, p. 15).

# Prerequisites

- **Group** — The similarity group is an example of a group

# Key Properties

1. A similarity maps straight-line segments to straight-line segments
2. All lengths are multiplied by the same scaling factor
3. Triangles are mapped to similar triangles
4. Angles are preserved in magnitude (though not necessarily in sense)
5. The composition of two similarities is another similarity
6. Each similarity is a bijection whose inverse is also a similarity

# Construction / Recognition

## To Verify:
1. Show that the composition of two similarities is a similarity (scaling factors multiply)
2. Show that the identity map is a similarity (scaling factor 1)
3. Show that the inverse of a similarity is a similarity (scaling factor is reciprocal)
4. Associativity follows from function composition

# Context & Application

Armstrong uses the similarity group to illustrate how groups arise in geometry. The key insight from Felix Klein's Erlangen Programme is that a geometry can be defined by its group of symmetries: Euclidean geometry studies properties invariant under similarities (or more precisely, under isometries).

# Examples

**Example 1** (p. 15): Similarities send triangles to similar triangles, preserving angles in magnitude.

**Example 2** (Exercise 2.4, p. 17): Every similarity is a bijection, and the inverse function is also a similarity.

# Relationships

## Builds Upon
- **Group** — This is an example of a group

## Related
- **Isometry Group** — Isometries are similarities with scaling factor 1

# Common Errors

- **Error**: Confusing similarities with isometries
  **Correction**: Similarities can change distances (by a uniform scaling factor); isometries preserve all distances

# Common Confusions

- **Confusion**: Thinking similarities always preserve orientation
  **Clarification**: Similarities preserve angles in magnitude but "not necessarily in sense" — reflections composed with scalings are similarities

# Source Reference

Chapter 2: Axioms, page 9 (pdf p. 15). See Exercise 2.4.

# Verification Notes

- Definition source: Direct quote from p. 15
- Confidence rationale: Medium — described but not formally axiom-checked in the text (deferred to exercises)
- Uncertainties: None
- Cross-reference status: Verified
