---
concept: Permutation Matrix
slug: permutation-matrix
category: matrices
subcategory: special-matrices
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.5 Permutations"
extraction_confidence: high
aliases: []
prerequisites:
  - permutation
  - matrix
extends: []
related:
  - sign-of-a-permutation
  - determinant
contrasts_with: []
answers_questions:
  - "What is a permutation?"
---

# Quick Definition

A permutation matrix P is a square matrix with exactly one 1 in each row and each column, all other entries being 0. Left multiplication by P permutes the entries of a vector.

# Core Definition

The permutation matrix associated to a permutation p of {1,...,n} is P = sum of e_{p(i),i} for i = 1 to n, where e_{ij} are the matrix units. Left multiplication by P permutes the entries of a column vector X according to p (Artin, pp. 31-32, formulas 1.5.7-1.5.8). The matrix associated to the product pq is the product PQ (Proposition 1.5.10).

# Prerequisites

- **Permutation** — The permutation that P represents
- **Matrix** — P is a special matrix

# Key Properties

1. Exactly one 1 in each row and column, rest are 0
2. det(P) = sign(p) = +/-1 (Proposition 1.5.10)
3. PQ corresponds to pq (composition of permutations)
4. P^(-1) = P^t (the inverse is the transpose)

# Construction / Recognition

## To Construct:
1. For each i, place a 1 in position (p(i), i) and 0 elsewhere

## To Recognize:
1. A square matrix with exactly one 1 in each row and column

# Context & Application

Permutation matrices provide a concrete matrix representation of permutations, bridging the study of permutations with matrix algebra. The map p -> P is an isomorphism from S_n to the group of permutation matrices.

# Examples

**Example 1** (p. 31): For p = (123), the permutation matrix is [[0,0,1],[1,0,0],[0,1,0]], and PX = [x_3, x_1, x_2]^t.

# Relationships

## Builds Upon
- **Permutation** — The permutation being represented

## Enables
- **Sign of a permutation** — sign(p) = det(P)

## Related
- **Determinant** — det(P) = +/-1

# Common Errors

- **Error**: Placing the 1's incorrectly when constructing P
  **Correction**: Use the formula P = sum of e_{p(i),i}; entry (p(i), i) is 1

# Common Confusions

- **Confusion**: Mixing up which index is the row and which is the column
  **Clarification**: The 1 in column i appears in row p(i)

# Source Reference

Chapter 1: Matrices, Section 1.5, pages 31-33.

# Verification Notes

- Definition source: Direct from (1.5.7), p. 32
- Confidence rationale: Explicitly defined with formula
- Uncertainties: None
- Cross-reference status: Verified
