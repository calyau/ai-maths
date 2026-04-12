---
# === CORE IDENTIFICATION ===
concept: Special Orthogonal Group
slug: special-orthogonal-group

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
  - "SO_n"
  - "rotation group"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonal-group
extends:
  - orthogonal-group
related:
  - rotation-matrix
  - rotation-3d
contrasts_with:
  - orthogonal-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the special orthogonal group?"
  - "Why is SO_n called the rotation group?"
---

# Quick Definition

The special orthogonal group SO_n is the subgroup of the orthogonal group O_n consisting of orthogonal matrices with determinant 1. Its elements represent rotations.

# Core Definition

The orthogonal matrices with determinant 1 form a subgroup SO_n of O_n of index 2, the special orthogonal group (Artin, Proposition 5.1.11(b), p. 144). Because their elements represent rotations, SO_2 and SO_3 are called the two- and three-dimensional rotation groups (Artin, p. 147).

# Prerequisites

- **Orthogonal group** — SO_n is a subgroup of O_n

# Key Properties

1. Subgroup of O_n of index 2
2. All elements have determinant 1
3. SO_2 consists of all 2x2 rotation matrices
4. SO_3 consists of all 3x3 rotation matrices (Euler's Theorem)
5. Closed under multiplication and inversion

# Construction / Recognition

## To Construct:
1. Take all orthogonal matrices with determinant 1

## To Recognize:
1. Check A^t A = I and det A = 1

# Context & Application

SO_n is the group of orientation-preserving orthogonal transformations. Euler's Theorem (5.1.25) shows that SO_3 consists precisely of the rotations of R^3, making it central to the study of 3D rotational symmetry and the classification of finite subgroups of the rotation group in Chapter 6.

# Examples

**Example 1** (p. 145): SO_2 consists of all matrices [[cos theta, -sin theta], [sin theta, cos theta]], representing counterclockwise rotation through angle theta.

**Example 2** (p. 147): SO_3 elements include the matrix with 1 in the (1,1) entry and a 2x2 rotation in the lower right block, representing rotation about the e_1 axis.

# Relationships

## Builds Upon
- **Orthogonal group** — SO_n is the determinant-1 subgroup

## Enables
- **Finite subgroups of rotation group** — Classification uses SO_3
- **Rotation (3D)** — Elements of SO_3

## Contrasts With
- **Orthogonal group** — O_n also includes reflections (determinant -1)

# Common Errors

- **Error**: Assuming SO_n = O_n
  **Correction**: SO_n is exactly half of O_n; it excludes reflections

# Common Confusions

- **Confusion**: Thinking SO_4 elements are simple rotations about an axis
  **Clarification**: In dimension > 3, rotations can simultaneously rotate two orthogonal planes by different angles

# Source Reference

Chapter 5: Applications of Linear Operators, Section 5.1, Proposition 5.1.11(b), Theorem 5.1.25, pages 144-148.

# Verification Notes

- Definition source: Direct from Proposition 5.1.11(b)
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
