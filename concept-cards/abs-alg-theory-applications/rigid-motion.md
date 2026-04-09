---
# === CORE IDENTIFICATION ===
concept: Rigid Motion
slug: rigid-motion

# === CLASSIFICATION ===
category: group-theory
subcategory: group-examples
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Groups"
chapter_number: 3
pdf_page: 44
section: "Integer Equivalence Classes and Symmetries"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - isometry

# === TYPED RELATIONSHIPS ===
prerequisites:
  - mapping
extends: []
related:
  - symmetry
  - permutation
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What must I know before studying groups?"
---

# Quick Definition

A rigid motion is a map from the plane to itself that preserves distances and the symmetry of a geometric object. Rigid motions include rotations and reflections.

# Core Definition

"A map from the plane to itself preserving the symmetry of an object is called a rigid motion" (Judson, p. 44).

# Prerequisites

- **Mapping** — A rigid motion is a function from the plane to itself

# Key Properties

1. Preserves distances between points
2. Preserves angles
3. Preserves the arrangement of sides and vertices
4. Includes rotations and reflections
5. Rigid motions of a figure compose to give rigid motions (closure)

# Context & Application

Rigid motions of geometric figures form symmetry groups. The rigid motions of a rectangle form a group of order 4, while those of an equilateral triangle form $S_3$ (order 6).

# Examples

**Example 1** (p. 44): For a rectangle, the rigid motions are: identity, 180-degree rotation, horizontal reflection, and vertical reflection (4 symmetries).

**Example 2** (p. 45-46): For an equilateral triangle, there are 6 rigid motions: identity, two rotations (120 and 240 degrees), and three reflections.

# Relationships

## Related
- **symmetry** — A rigid motion that preserves a figure is a symmetry
- **permutation** — Each rigid motion induces a permutation of vertices

# Source Reference

Chapter 3: Groups, Section 3.1, page 44.

# Verification Notes

- Definition source: Direct from p. 44
- Confidence: HIGH — explicit definition
- Cross-reference status: Verified
- Uncertainties: None
