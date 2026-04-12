---
concept: Glide Reflection
slug: glide-reflection
category: symmetry
subcategory: geometric-symmetry
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Symmetry"
chapter_number: 6
pdf_page: 162
section: "6.3 Isometries of the Plane"
extraction_confidence: high
aliases:
  - "glide"
  - "glide symmetry"
prerequisites:
  - isometry
  - reflection-isometry
  - translation
extends: []
related:
  - frieze-group
contrasts_with:
  - reflection-isometry
answers_questions:
  - "What is a glide reflection?"
  - "How does a glide reflection differ from a simple reflection?"
---

# Quick Definition

A glide reflection is an orientation-reversing isometry consisting of reflection about a line l followed by translation by a nonzero vector parallel to l. It has no fixed points.

# Core Definition

A glide reflection (or glide for short) is reflection about a line l, followed by translation by a nonzero vector parallel to l (Artin, Theorem 6.3.4(b)(ii), p. 169). The glide line of the isometry t_a * rho_theta * r is parallel to the line of reflection of rho_theta * r (Corollary 6.3.8). Every orientation-reversing isometry is either a reflection or a glide reflection.

# Prerequisites

- **Isometry** — Glide reflections are isometries
- **Reflection (isometry)** — A glide reflection extends a reflection by a translation
- **Translation** — The translational component

# Key Properties

1. Orientation-reversing
2. No fixed points (unlike a pure reflection)
3. The square of a glide reflection is a translation by twice the glide vector
4. The glide line is parallel to the reflection line
5. Every orientation-reversing isometry with no fixed line is a glide reflection

# Construction / Recognition

## To Construct:
1. Choose a line l (the glide line)
2. Choose a nonzero vector v parallel to l
3. The glide reflection is: reflect across l, then translate by v

## To Recognize:
1. An orientation-reversing isometry with no fixed points
2. Its square is a nonzero translation

# Context & Application

Glide reflections appear naturally in frieze and wallpaper patterns. The brick wall pattern is a famous example where the symmetry group contains glide reflections but no pure reflections. This subtlety is important in the classification of crystallographic groups.

# Examples

**Example 1** (p. 163): Figure 6.1.4 shows a pattern with glide symmetry (footprints alternating on either side of a line).

**Example 2** (p. 184): The brick wall pattern has glide symmetry along a dashed horizontal line but no reflection symmetry.

# Relationships

## Builds Upon
- **Reflection (isometry)** — A glide adds translation to reflection
- **Translation** — The translational component parallel to the glide line

## Enables
- **Crystallographic group classification** — Some groups have glides but no reflections

## Contrasts With
- **Reflection (isometry)** — A reflection fixes a line; a glide has no fixed points

# Common Errors

- **Error**: Assuming every orientation-reversing isometry is a reflection
  **Correction**: Glide reflections are orientation-reversing but have no fixed line

# Common Confusions

- **Confusion**: Thinking a glide reflection's square is the identity
  **Clarification**: The square is a translation by twice the glide vector; only a pure reflection has order 2

# Source Reference

Chapter 6: Symmetry, Section 6.3, Theorem 6.3.4(b)(ii), Corollary 6.3.8, pages 169-171.

# Verification Notes

- Definition source: From Theorem 6.3.4(b)(ii)
- Confidence rationale: Part of explicit classification
- Uncertainties: None
- Cross-reference status: Verified
