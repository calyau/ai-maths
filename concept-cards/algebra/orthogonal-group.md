---
# === CORE IDENTIFICATION ===
concept: Orthogonal Group
slug: orthogonal-group

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
  - "O_n"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonal-matrix
extends: []
related:
  - special-orthogonal-group
  - isometry-group
contrasts_with:
  - special-orthogonal-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the orthogonal group?"
  - "What is the relationship between O_n and SO_n?"
---

# Quick Definition

The orthogonal group O_n is the group of all n x n orthogonal matrices under matrix multiplication. It contains all rotations and reflections of R^n.

# Core Definition

The orthogonal matrices form a subgroup O_n of GL_n, called the orthogonal group (Artin, Proposition 5.1.11(a), p. 144). The product of orthogonal matrices is orthogonal, and the inverse of an orthogonal matrix (its transpose) is orthogonal.

# Prerequisites

- **Orthogonal matrix** — Elements of O_n are orthogonal matrices

# Key Properties

1. Closed under multiplication and inversion
2. A subgroup of GL_n(R)
3. Contains the special orthogonal group SO_n as a subgroup of index 2
4. Every element has determinant +1 or -1
5. In dimension 2, O_2 consists of rotations and reflections

# Construction / Recognition

## To Construct:
1. Take all n x n real matrices A satisfying A^t A = I

## To Recognize:
1. A matrix group whose elements all satisfy A^t A = I

# Context & Application

O_n describes all distance-preserving linear transformations of R^n. In the study of symmetry (Chapter 6), O_2 appears as the group of isometries that fix the origin in the plane, and it serves as the codomain of the homomorphism from the full isometry group M_n.

# Examples

**Example 1** (p. 144): O_2 consists of the rotation matrices [[c, -s], [s, c]] and the reflection matrices [[c, s], [s, -c]], where c = cos theta and s = sin theta.

**Example 2** (p. 162): The homomorphism pi: M_n -> O_n maps each isometry to its linear (orthogonal) part, with kernel the translation group T.

# Relationships

## Builds Upon
- **Orthogonal matrix** — Elements of the orthogonal group

## Enables
- **Isometry group** — M_n maps onto O_n
- **Dihedral group** — Finite subgroups of O_2

## Contrasts With
- **Special orthogonal group** — SO_n is the subgroup of O_n with determinant 1

# Common Errors

- **Error**: Assuming O_n contains only rotations
  **Correction**: O_n also contains reflections (determinant -1 elements)

# Common Confusions

- **Confusion**: Conflating O_n with SO_n
  **Clarification**: SO_n is the index-2 subgroup of determinant-1 elements; O_n also includes determinant -1 elements

# Source Reference

Chapter 5: Applications of Linear Operators, Section 5.1, Proposition 5.1.11, p. 144.

# Verification Notes

- Definition source: Direct from Proposition 5.1.11
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
