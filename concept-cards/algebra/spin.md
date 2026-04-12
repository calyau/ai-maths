---
# === CORE IDENTIFICATION ===
concept: Spin
slug: spin

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
extends: []
related:
  - eulers-theorem
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a spin in the context of 3D rotations?"
  - "How many spins does a rotation have?"
---

# Quick Definition

A spin is a pair (u, theta) consisting of a pole u (unit vector) and a nonzero angle of rotation theta, which describes a rotation of R^3 that is not the identity. Every non-identity rotation has exactly two spins: (u, theta) and (-u, -theta).

# Core Definition

A rotation that is not the identity is described by the pair (u, theta), called a spin, that consists of a pole u and a nonzero angle of rotation theta (Artin, p. 147). Every rotation p different from the identity has two poles and two spins. If (u, theta) is a spin of p, so is (-u, -theta), and p_{(u,theta)} = p_{(-u,-theta)}.

# Prerequisites

- **Rotation of R^3** — Spins describe non-identity rotations

# Key Properties

1. A spin consists of a pole (unit vector) and a nonzero angle
2. Every non-identity rotation has exactly two spins
3. The two spins are (u, theta) and (-u, -theta)
4. Changing the pole direction reverses the angle sign

# Construction / Recognition

## To Construct:
1. Choose a unit vector u (pole direction)
2. Choose a nonzero angle theta
3. The rotation fixes u and rotates the perpendicular plane through theta

## To Recognize:
1. Find the eigenvalue-1 eigenvector of the rotation matrix
2. Compute the angle from the trace: trace = 1 + 2 cos theta

# Context & Application

Spins provide a convenient parametrization of non-identity rotations in R^3. They are used extensively in the classification of finite subgroups of SO_3 (Section 6.12), where counting the number of spins yields the key equation for the classification.

# Examples

**Example 1** (p. 147): A rotation about the e_1 axis through angle theta has spins (e_1, theta) and (-e_1, -theta).

**Example 2** (p. 148): Conjugation by B in SO_3 maps the rotation with spin (u, alpha) to the rotation with spin (Bu, alpha) (Corollary 5.1.28(b)).

# Relationships

## Builds Upon
- **Rotation of R^3** — A spin describes a specific rotation

## Enables
- **Finite subgroups of rotation group** — Classification via counting spins

# Common Errors

- **Error**: Treating (u, theta) and (-u, -theta) as different rotations
  **Correction**: They describe the same rotation; a rotation has exactly two spins

# Common Confusions

- **Confusion**: Thinking the identity rotation has a spin
  **Clarification**: The identity has no spin because its axis is indeterminate and its angle is 0

# Source Reference

Chapter 5: Applications of Linear Operators, Section 5.1, p. 147.

# Verification Notes

- Definition source: Direct from p. 147
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
