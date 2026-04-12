---
# === CORE IDENTIFICATION ===
concept: Rotation of R^3
slug: rotation-3d

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
aliases:
  - "3D rotation"
  - "rotation about an axis"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - rotation-matrix
  - special-orthogonal-group
extends:
  - rotation-matrix
related:
  - spin
  - eulers-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a rotation of R^3?"
  - "How is a 3D rotation characterized by a pole and angle?"
---

# Quick Definition

A rotation of R^3 about the origin is a linear operator that fixes a unit vector u (the pole) and rotates the orthogonal two-dimensional subspace. It is described by a spin (u, theta).

# Core Definition

A rotation of R^3 about the origin is a linear operator p with these properties: p fixes a unit vector u, called a pole of p, and p rotates the two-dimensional subspace W orthogonal to u. The axis of rotation is the line spanned by u (Artin, Definition 5.1.22, p. 146). The identity operator is also called a rotation, though its axis is indeterminate.

# Prerequisites

- **Rotation matrix** — 2D rotations appear as the restriction to W
- **Special orthogonal group** — 3D rotations form SO_3

# Key Properties

1. Fixes a unit vector u (the pole) and its negative -u
2. Rotates the orthogonal plane W through angle theta
3. Every non-identity rotation has two spins: (u, theta) and (-u, -theta)
4. The trace of the rotation matrix is 1 + 2 cos theta (Corollary 5.1.28)
5. Conjugation by B in SO_3 maps rotation with pole u to rotation with pole Bu

# Construction / Recognition

## To Construct:
1. Choose a unit vector u (pole) and angle theta
2. Choose an orthonormal basis (v_1, v_2, v_3) with v_1 = u
3. The matrix in this basis has form [[1,0,0],[0,cos theta,-sin theta],[0,sin theta,cos theta]]

## To Recognize:
1. Check that the matrix is in SO_3
2. Find an eigenvector with eigenvalue 1 (the pole)

# Context & Application

Three-dimensional rotations are the elements of SO_3. Euler's Theorem establishes the remarkable fact that the composition of two rotations about different axes is itself a rotation about some third axis. This is the foundation for the classification of finite subgroups of SO_3 in Section 6.12.

# Examples

**Example 1** (p. 146): Rotation about the e_1 axis has matrix [[1,0,0],[0,c,-s],[0,s,c]].

**Example 2** (p. 147): The composition of rotations about any two axes is a rotation about some other axis (Corollary 5.1.26).

# Relationships

## Builds Upon
- **Rotation matrix** — 2D rotation appears in the block structure

## Enables
- **Euler's theorem** — Characterizes SO_3 as the rotation group
- **Finite subgroups of rotation group** — Classification in Section 6.12

## Related
- **Spin** — A rotation is described by a pair (pole, angle)

# Common Errors

- **Error**: Forgetting that every non-identity rotation has two spins (u, theta) and (-u, -theta)
  **Correction**: Changing the pole direction reverses the angle sign

# Common Confusions

- **Confusion**: Thinking rotations in R^4 work like R^3 with a single axis
  **Clarification**: In R^4, a rotation can simultaneously rotate two orthogonal 2D subspaces by different angles (5.1.27)

# Source Reference

Chapter 5: Applications of Linear Operators, Section 5.1, Definition 5.1.22, Theorem 5.1.25, pages 146-148.

# Verification Notes

- Definition source: Direct from Definition 5.1.22
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
