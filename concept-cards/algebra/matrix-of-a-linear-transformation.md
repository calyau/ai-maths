---
concept: Matrix of a Linear Transformation
slug: matrix-of-a-linear-transformation
category: linear-algebra
subcategory: null
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Operators"
chapter_number: 4
pdf_page: 113
section: "4.2 The Matrix of a Linear Transformation"
extraction_confidence: high
aliases: []
prerequisites:
  - linear-transformation
  - basis
extends: []
related:
  - linear-operator
  - similar-matrices
  - change-of-basis
contrasts_with: []
answers_questions:
  - "What is a linear transformation?"
---

# Quick Definition

Given bases B of V and C of W, the matrix A of a linear transformation T: V -> W satisfies T(B) = CA and AX = Y, where X is the coordinate vector of v in basis B and Y is the coordinate vector of T(v) in basis C.

# Core Definition

Let T: V -> W be a linear transformation, B = (v_1, ..., v_n) and C = (w_1, ..., w_m) bases of V and W. The matrix A has columns that are the coordinate vectors of T(v_j) in basis C: T(v_j) = w_1 a_{1j} + ... + w_m a_{mj} (Artin, p. 116, formula 4.2.7). The matrix satisfies the dual properties T(B) = CA and AX = Y (formula 4.2.6). New bases B' = BP, C' = CQ change the matrix to A' = Q^(-1)AP (Proposition 4.2.13).

# Prerequisites

- **Linear transformation** — The map being represented
- **Basis** — Bases for both domain and codomain are needed

# Key Properties

1. T(B) = CA and AX = Y
2. The columns of A are coordinate vectors of T(v_j) in basis C
3. Under change of bases: A' = Q^(-1)AP
4. For a linear operator (V = W, B = C): A' = P^(-1)AP (conjugation)

# Construction / Recognition

## To Construct:
1. Apply T to each basis vector v_j of V
2. Express T(v_j) in terms of basis C of W
3. The coefficients form column j of A

## To Recognize:
1. A matrix that converts coordinate vectors: Y = AX

# Context & Application

Every linear transformation between finite-dimensional spaces corresponds to a matrix, once bases are chosen. Changing bases changes the matrix. The goal of canonical form theory is to choose bases that make the matrix as simple as possible.

# Examples

**Example 1** (p. 115): Counterclockwise rotation of R^2 by theta has matrix [[cos theta, -sin theta],[sin theta, cos theta]] with respect to the standard basis.

# Relationships

## Builds Upon
- **Linear transformation** — The map being represented
- **Basis** — Required for both spaces

## Enables
- **Similar matrices** — Different bases give similar matrices
- **Rank-nullity theorem** — The rank of the matrix equals the rank of T

# Common Errors

- **Error**: Confusing the matrix for T: V -> W (two bases) with T: V -> V (one basis)
  **Correction**: For V -> W, use bases B, C and formula Q^(-1)AP; for V -> V, use one basis and P^(-1)AP

# Common Confusions

- **Confusion**: Thinking the matrix IS the transformation
  **Clarification**: The matrix depends on the choice of bases; the transformation is basis-independent

# Source Reference

Chapter 4: Linear Operators, Section 4.2, pages 115-118.

# Verification Notes

- Definition source: Direct from (4.2.6)-(4.2.7), p. 116
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
