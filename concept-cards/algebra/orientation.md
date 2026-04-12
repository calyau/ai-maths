---
concept: Orientation
slug: orientation
category: symmetry
subcategory: geometric-symmetry
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Symmetry"
chapter_number: 6
pdf_page: 162
section: "6.2 Isometries"
extraction_confidence: high
aliases:
  - "orientation-preserving"
  - "orientation-reversing"
prerequisites:
  - orthogonal-operator
  - isometry
extends: []
related:
  - rotation-plane
  - reflection-isometry
contrasts_with: []
answers_questions:
  - "What does it mean for an isometry to be orientation-preserving or orientation-reversing?"
---

# Quick Definition

An isometry is orientation-preserving if its orthogonal part has determinant +1, and orientation-reversing if the determinant is -1. This divides isometries into two classes: rotations/translations (preserving) and reflections/glides (reversing).

# Core Definition

The determinant of an orthogonal operator phi is +/- 1. The operator is orientation-preserving if det phi = 1 and orientation-reversing if det phi = -1. An isometry f = t_a * phi is orientation-preserving or -reversing according to phi. The map sigma: M_n -> {+/- 1} sending each isometry to det(phi) is a group homomorphism (Artin, (6.2.13), p. 167).

# Prerequisites

- **Orthogonal operator** — Orientation is determined by the linear part
- **Isometry** — Orientation classifies isometries

# Key Properties

1. Orientation is determined by det(phi) = +/- 1
2. sigma: M_n -> {+/- 1} is a homomorphism
3. Composition of two orientation-preserving isometries preserves orientation
4. Composition of two orientation-reversing isometries preserves orientation
5. In the plane: orientation-preserving = translations and rotations; orientation-reversing = reflections and glide reflections

# Construction / Recognition

## To Determine:
1. Write the isometry as f = t_a * phi
2. Compute det(phi): +1 means preserving, -1 means reversing

# Context & Application

Orientation provides a coarse but important classification of isometries. It is preserved under composition of even numbers of reflections and reversed under odd numbers. The distinction is essential for classifying plane isometries into four types.

# Examples

**Example 1** (p. 169): An isometry of the form t_v * rho_theta preserves orientation (Theorem 6.3.4(a)).

**Example 2** (p. 169): An isometry of the form t_v * rho_theta * r reverses orientation (Theorem 6.3.4(b)).

# Relationships

## Builds Upon
- **Orthogonal operator** — Orientation determined by its determinant

## Enables
- **Classification of plane isometries** — Into four types based on orientation and fixed points

# Common Confusions

- **Confusion**: Thinking orientation depends on the choice of coordinates
  **Clarification**: The sign of the determinant is coordinate-independent

# Source Reference

Chapter 6: Symmetry, Section 6.2, (6.2.13), p. 167.

# Verification Notes

- Definition source: Direct from (6.2.13) and surrounding discussion
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
