---
# === CORE IDENTIFICATION ===
concept: One-Parameter Group
slug: one-parameter-group

# === CLASSIFICATION ===
category: applications-of-linear-algebra
subcategory: differential-equations
tier: intermediate

# === PROVENANCE ===
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Applications of Linear Operators"
chapter_number: 5
pdf_page: 143
section: "5.4 The Matrix Exponential"

# === CONFIDENCE ===
extraction_confidence: medium

# === VARIANTS ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - matrix-exponential
extends: []
related:
  - special-orthogonal-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a one-parameter group of matrices?"
---

# Quick Definition

A one-parameter group is a continuous homomorphism from the additive group of real numbers R to a matrix group, typically of the form t -> e^{tA} for a fixed matrix A.

# Core Definition

The map t -> e^{tA} defines a one-parameter group of matrices: it is a continuous group homomorphism from (R, +) to GL_n, satisfying e^{(s+t)A} = e^{sA} e^{tA} and e^{0} = I. This follows from the commutative property e^{A+B} = e^A e^B when A and B commute (Artin, Theorem 5.4.4(c), p. 155), since tA and sA always commute.

# Prerequisites

- **Matrix exponential** — One-parameter groups are built from the matrix exponential

# Key Properties

1. e^{(s+t)A} = e^{sA} e^{tA} for all real s, t
2. e^{0 A} = I (the identity)
3. The derivative at t = 0 is A
4. Each e^{tA} is invertible with inverse e^{-tA}
5. If A is skew-symmetric, e^{tA} traces a path in SO_n

# Construction / Recognition

## To Construct:
1. Choose a matrix A (the "infinitesimal generator")
2. Form the family {e^{tA} | t in R}

## To Recognize:
1. A continuous family of invertible matrices M(t) with M(s+t) = M(s)M(t) and M(0) = I

# Context & Application

One-parameter groups connect linear algebra to Lie theory and differential geometry. The matrix A is the "infinitesimal generator" of the group. Artin notes that the properties of the matrix exponential are used again in Chapter 9 (on Lie groups). When A is skew-symmetric, the one-parameter group lies in SO_n, giving continuous rotations.

# Examples

**Example 1** (p. 155): For A = [[0, -1], [1, 0]], e^{tA} = [[cos t, -sin t], [sin t, cos t]], which traces out all rotations of R^2.

# Relationships

## Builds Upon
- **Matrix exponential** — The parametrization e^{tA}

## Enables
- **Lie group theory** — One-parameter groups are the building blocks (Chapter 9)

# Common Errors

- **Error**: Assuming every continuous path through the identity in GL_n is a one-parameter group
  **Correction**: A one-parameter group must satisfy the homomorphism property M(s+t) = M(s)M(t)

# Common Confusions

- **Confusion**: Thinking the one-parameter group is a subgroup of R
  **Clarification**: It is a subgroup of GL_n parametrized by R; it is the image of a homomorphism from R

# Source Reference

Chapter 5: Applications of Linear Operators, Section 5.4, Theorem 5.4.4(c), Corollary 5.4.5, pages 155-156.

# Verification Notes

- Definition source: Synthesized from the matrix exponential discussion
- Confidence rationale: Medium - the concept is implicit rather than explicitly defined as a standalone concept
- Uncertainties: Artin does not give a formal definition of "one-parameter group" in Chapter 5
- Cross-reference status: Verified
