---
concept: Similar Matrices
slug: similar-matrices
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
aliases:
  - "conjugate matrices"
  - "similarity"
prerequisites:
  - matrix
  - invertible-matrix
  - linear-operator
extends: []
related:
  - diagonalization
  - jordan-form
  - characteristic-polynomial
contrasts_with: []
answers_questions:
  - "What is a linear transformation?"
---

# Quick Definition

A matrix A is similar to A' if A' = P^(-1)AP for some invertible matrix P. Similar matrices represent the same linear operator in different bases, so they share eigenvalues, determinant, trace, and characteristic polynomial.

# Core Definition

A square matrix A is similar to another matrix A' if A' = P^(-1)AP for some invertible matrix P (Artin, p. 120). This occurs exactly when A and A' represent the same linear operator with respect to different bases (Proposition 4.3.5).

# Prerequisites

- **Matrix** — The objects being compared
- **Invertible matrix** — P must be invertible
- **Linear operator** — Similarity captures basis-independence

# Key Properties

1. Same eigenvalues (Proposition 4.4.7)
2. Same characteristic polynomial (Proposition 4.5.11)
3. Same determinant and trace
4. Same rank
5. Similarity is an equivalence relation
6. The Jordan form is the canonical representative of each similarity class

# Construction / Recognition

## To Construct:
1. Choose an invertible P and compute P^(-1)AP

## To Recognize:
1. Check that A and A' have the same characteristic polynomial (necessary but not sufficient)
2. Or check that they have the same Jordan form

# Context & Application

Similarity is the central equivalence relation in the theory of linear operators. Finding a "nice" similar matrix (diagonal or Jordan form) is the main goal of Sections 4.6-4.7.

# Examples

**Example 1** (pp. 130-131): [[3,2],[1,4]] is similar to [[5,0],[0,2]] via P = [[1,2],[1,-1]].

# Relationships

## Builds Upon
- **Linear operator** — Similar matrices represent the same operator

## Enables
- **Diagonalization** — A is similar to a diagonal matrix iff there's a basis of eigenvectors
- **Jordan form** — Every complex matrix is similar to a Jordan form

## Related
- **Characteristic polynomial** — Invariant under similarity

# Common Errors

- **Error**: Thinking similar matrices must look alike
  **Correction**: Similar matrices can appear very different but have the same invariants

# Common Confusions

- **Confusion**: Confusing P^(-1)AP with PAP^(-1)
  **Clarification**: The convention is A' = P^(-1)AP for change of basis

# Source Reference

Chapter 4: Linear Operators, Section 4.3, page 120.

# Verification Notes

- Definition source: Direct from Section 4.3, p. 120
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
