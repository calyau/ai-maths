---
concept: Homogeneous System
slug: homogeneous-system
category: matrices
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.2 Row Reduction"
extraction_confidence: high
aliases:
  - "homogeneous linear equation"
  - "AX = 0"
prerequisites:
  - system-of-linear-equations
extends:
  - system-of-linear-equations
related:
  - null-space
  - rank
contrasts_with: []
answers_questions:
  - "What is a matrix and what are its basic operations?"
---

# Quick Definition

A homogeneous system of linear equations is one of the form AX = 0. It always has the trivial solution X = 0, and has nontrivial solutions when there are more unknowns than equations.

# Core Definition

A homogeneous linear equation AX = 0 always has the trivial solution X = 0. If A is m x n with m < n, the system has a nontrivial solution (Corollary 1.2.14). For a square matrix A, the homogeneous system AX = 0 has only the trivial solution iff A is invertible (Theorem 1.2.21) (Artin, pp. 20-22).

# Prerequisites

- **System of linear equations** — A homogeneous system is the special case B = 0

# Key Properties

1. Always has the trivial solution X = 0
2. Has nontrivial solutions when m < n (more unknowns than equations)
3. For square A: AX = 0 has only X = 0 iff A is invertible
4. The solution set is a subspace (the null space of A)
5. If AX = 0 has only the trivial solution, then AX = B has a unique solution for every B

# Construction / Recognition

## To Construct:
1. Take a system AX = B and set B = 0

## To Recognize:
1. All constant terms are zero

# Context & Application

Homogeneous systems are fundamental because their solution sets are subspaces (the null space). Artin emphasizes the implication: if AX = 0 has only X = 0, then AX = B has a unique solution for all B. This is often easier to verify.

# Examples

**Example 1** (p. 22): The polynomial interpolation problem: the homogeneous system asks for a polynomial with more roots than its degree allows, forcing X = 0.

# Relationships

## Builds Upon
- **System of linear equations** — Special case with B = 0

## Enables
- **Null space** — The solution set of AX = 0
- **Rank** — Dimension of the image; related to nullity by the dimension formula

# Common Errors

- **Error**: Assuming a homogeneous system always has nontrivial solutions
  **Correction**: Only when m < n (or when A is singular for square A)

# Common Confusions

- **Confusion**: Thinking "trivial" means "unimportant"
  **Clarification**: "Trivial" here means X = 0; the trivial solution always exists

# Source Reference

Chapter 1: Matrices, Section 1.2, pages 20-22.

# Verification Notes

- Definition source: From discussion around Corollary 1.2.14 and Theorem 1.2.21
- Confidence rationale: Explicitly discussed
- Uncertainties: None
- Cross-reference status: Verified
