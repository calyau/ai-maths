---
concept: Linear Operator
slug: linear-operator
category: linear-algebra
subcategory: null
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Operators"
chapter_number: 4
pdf_page: 113
section: "4.3 Linear Operators"
extraction_confidence: high
aliases: []
prerequisites:
  - linear-transformation
  - vector-space
extends:
  - linear-transformation
related:
  - similar-matrices
  - eigenvector
  - eigenvalue
  - invariant-subspace
contrasts_with: []
answers_questions:
  - "What is a linear transformation?"
---

# Quick Definition

A linear operator is a linear transformation T: V -> V from a vector space to itself. It is represented by a square matrix with respect to any basis, and its matrix changes by conjugation (P^(-1)AP) under change of basis.

# Core Definition

A linear operator is a linear transformation T: V -> V that maps a vector space to itself (Artin, p. 119). With a single basis B, the matrix A of T satisfies T(B) = BA (formula 4.3.3). Under change of basis B' = BP, the matrix changes to A' = P^(-1)AP (Proposition 4.3.5).

# Prerequisites

- **Linear transformation** — A linear operator is a special case
- **Vector space** — Domain and codomain are the same space

# Key Properties

1. Represented by a square matrix (one basis for both domain and range)
2. Matrix changes by conjugation: A' = P^(-1)AP
3. Invertible iff det(matrix) != 0
4. Has a characteristic polynomial, eigenvalues, eigenvectors
5. Every operator on a complex space has at least one eigenvector

# Construction / Recognition

## To Construct:
1. Define T: V -> V satisfying T(v+w) = T(v) + T(w) and T(cv) = cT(v)

## To Recognize:
1. A linear map from a space to itself

# Context & Application

Linear operators are the objects studied in the eigenvalue theory of Chapter 4. The key distinction from general linear transformations is that domain = codomain, so there is only one basis to choose, and the matrix changes by conjugation rather than by Q^(-1)AP.

# Examples

**Example 1** (p. 119): Left multiplication by an n x n matrix A on F^n.

**Example 2** (p. 119): Rotation of R^2 through angle theta.

# Relationships

## Builds Upon
- **Linear transformation** — Specialized to V -> V

## Enables
- **Eigenvalue** — Defined for operators
- **Characteristic polynomial** — det(tI - A)
- **Diagonalization** — Finding a basis of eigenvectors

## Related
- **Similar matrices** — Two matrices representing the same operator

# Common Errors

- **Error**: Using two different bases (as for a general transformation)
  **Correction**: A linear operator uses ONE basis for both domain and range

# Common Confusions

- **Confusion**: Confusing the matrix of an operator with the operator itself
  **Clarification**: The matrix depends on the choice of basis; the operator is basis-independent

# Source Reference

Chapter 4: Linear Operators, Section 4.3, pages 119-120.

# Verification Notes

- Definition source: Direct from Section 4.3
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
