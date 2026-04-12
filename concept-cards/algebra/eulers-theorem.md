---
# === CORE IDENTIFICATION ===
concept: "Euler's Theorem (Rotations)"
slug: eulers-theorem

# === CLASSIFICATION ===
category: applications-of-linear-algebra
subcategory: orthogonal-matrices
tier: intermediate

# === PROVENANCE ===
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Applications of Linear Operators"
chapter_number: 5
pdf_page: 143
section: "5.1 Orthogonal Matrices and Rotations"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rotation-3d
  - special-orthogonal-group
extends: []
related:
  - orthogonal-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What does Euler's theorem say about 3x3 rotation matrices?"
  - "Why is the composition of two rotations in R^3 always a rotation?"
---

# Quick Definition

Euler's Theorem states that the 3x3 rotation matrices are precisely the orthogonal 3x3 matrices with determinant 1, i.e., the elements of SO_3. A remarkable consequence is that the composition of rotations about any two axes is a rotation about some third axis.

# Core Definition

The 3x3 rotation matrices are the orthogonal 3x3 matrices with determinant 1, the elements of the special orthogonal group SO_3 (Artin, Theorem 5.1.25, p. 148). The proof relies on Lemma 5.1.29, which shows that every 3x3 orthogonal matrix with determinant 1 has eigenvalue 1, providing the axis of rotation.

# Prerequisites

- **Rotation of R^3** — The theorem characterizes rotations as elements of SO_3
- **Special orthogonal group** — SO_3 is exactly the rotation group

# Key Properties

1. SO_3 = {3x3 rotation matrices}
2. Composition of rotations is a rotation (Corollary 5.1.26)
3. Every element of SO_3 has eigenvalue 1
4. The trace of a rotation with angle alpha is 1 + 2 cos alpha
5. Conjugation preserves the angle of rotation and transforms the pole

# Construction / Recognition

## To Verify:
1. Show that a rotation matrix has determinant 1 and satisfies A^t A = I
2. Conversely, given M in SO_3, find the eigenvector with eigenvalue 1 to identify the rotation axis

# Context & Application

Euler's Theorem is fundamental to understanding 3D rotational symmetry. It guarantees that SO_3 is the rotation group, enabling the classification of all finite subgroups of rotations (cyclic, dihedral, tetrahedral, octahedral, icosahedral) in Section 6.12.

# Examples

**Example 1** (p. 148): The proof uses the fact that for 3x3 orthogonal M with det M = 1, det(M - I) = det(I - M) (since n=3 is odd), forcing M - I to be singular.

**Example 2** (p. 147): The 4x4 case shows the theorem fails in higher dimensions: an element of SO_4 can rotate two orthogonal planes by different angles.

# Relationships

## Builds Upon
- **Rotation of R^3** — The theorem classifies these
- **Special orthogonal group** — Identifies SO_3 with rotations

## Enables
- **Finite subgroups of rotation group** — Classification depends on SO_3 being the rotation group

# Common Errors

- **Error**: Attempting to apply Euler's Theorem in dimension 4 or higher
  **Correction**: The theorem is specific to dimension 3; in R^4, not every element of SO_4 is a simple rotation about an axis

# Common Confusions

- **Confusion**: Thinking the theorem is about Euler angles
  **Clarification**: Euler's Theorem characterizes SO_3; Euler angles are a parametrization of rotations

# Source Reference

Chapter 5: Applications of Linear Operators, Section 5.1, Theorem 5.1.25, Corollaries 5.1.26 and 5.1.28, pages 148-149.

# Verification Notes

- Definition source: Direct from Theorem 5.1.25
- Confidence rationale: Explicitly stated and proved theorem
- Uncertainties: None
- Cross-reference status: Verified
