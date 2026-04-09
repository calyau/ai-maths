---
# === CORE IDENTIFICATION ===
concept: Motion Group of a Cube
slug: motion-group-of-a-cube

# === CLASSIFICATION ===
category: permutation-groups
subcategory: null
tier: foundational

# === PROVENANCE ===
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Permutation Groups"
chapter_number: 5
pdf_page: 82
section: "The Motion Group of a Cube"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - rotation group of a cube

# === TYPED RELATIONSHIPS ===
prerequisites:
  - symmetric-group
  - transposition
extends: []
related:
  - dihedral-group
  - permutation-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the motion group of a cube?"
  - "How is the motion group of a cube related to $S_4$?"
---

# Quick Definition

The group of rigid motions of a cube has 24 elements and is isomorphic to $S_4$. The isomorphism arises by labeling the four diagonals and observing that every rigid motion permutes them.

# Core Definition

"The group of rigid motions of a cube contains 24 elements" (Proposition 5.26, p. 82). "The group of rigid motions of a cube is $S_4$" (Theorem 5.27, p. 82). The proof labels the four diagonals of the cube and shows that rotations about axes joining midpoints of opposite edges produce all transpositions, generating all of $S_4$.

# Prerequisites

- **Symmetric Group** — The motion group is shown to be $S_4$
- **Transposition** — Transpositions are obtained via 180-degree rotations about edge midpoint axes

# Key Properties

1. The group has 24 elements (same as $|S_4| = 4! = 24$)
2. It is isomorphic to $S_4$
3. Rigid motions permute the four diagonals of the cube
4. There are six axes joining midpoints of opposite edges, giving all six transpositions in $S_4$

# Construction / Recognition

## To See the Isomorphism:
1. Label the four diagonals of the cube 1, 2, 3, 4
2. Each rigid motion permutes these diagonals
3. 180-degree rotations about edge-midpoint axes produce transpositions
4. Since all transpositions are obtained, and they generate $S_4$, the groups are isomorphic

# Context & Application

This is a striking example of how the abstract symmetric group $S_4$ arises as a concrete symmetry group of a geometric object.

# Examples

**Example 1** (p. 82): A cube has 6 faces. Fixing a face on top gives 4 rotations, so $6 \times 4 = 24$ total rigid motions.

# Relationships

## Builds Upon
- **Symmetric Group** — The motion group is isomorphic to $S_4$
- **Transposition** — Key to the proof of the isomorphism

## Related
- **Dihedral Group** — Another geometric symmetry group
- **Permutation Group** — The motion group is a permutation group on the diagonals

# Common Errors

- **Error**: Including reflections (improper rotations) in the motion group
  **Correction**: The motion group consists of rigid motions (proper rotations) only

# Common Confusions

- **Confusion**: Thinking the cube's symmetry group permutes its 6 faces or 8 vertices directly as $S_6$ or $S_8$
  **Clarification**: While faces and vertices are permuted, the key insight is that the 4 diagonals are permuted, giving $S_4$

# Source Reference

Chapter 5: Permutation Groups, Section 5.2, Proposition 5.26, Theorem 5.27, pages 82-83.

# Verification Notes

- Definition source: Direct from Proposition 5.26 and Theorem 5.27
- Confidence rationale: Explicit theorem statements
- Uncertainties: None
- Cross-reference status: Verified
