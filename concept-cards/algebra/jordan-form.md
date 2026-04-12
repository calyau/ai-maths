---
concept: Jordan Form
slug: jordan-form
category: linear-algebra
subcategory: null
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Operators"
chapter_number: 4
pdf_page: 113
section: "4.7 Jordan Form"
extraction_confidence: high
aliases:
  - "Jordan normal form"
  - "Jordan canonical form"
  - "Jordan decomposition"
prerequisites:
  - linear-operator
  - eigenvalue
  - eigenvector
  - characteristic-polynomial
  - generalized-eigenvector
extends:
  - diagonalization
related:
  - jordan-block
  - similar-matrices
contrasts_with: []
answers_questions:
  - "What is the Jordan normal form?"
  - "How do I put a matrix in Jordan form?"
---

# Quick Definition

The Jordan form of a complex matrix A is a block diagonal matrix J = P^(-1)AP consisting of Jordan blocks along the diagonal. Every complex matrix is similar to a unique Jordan form (up to block ordering). It generalizes diagonalization.

# Core Definition

Theorem 4.7.10 (Jordan Decomposition): Let A be an n x n complex matrix. There is an invertible matrix P such that P^(-1)AP has Jordan form — a block diagonal matrix with Jordan blocks J_{lambda_i} along the diagonal (Artin, pp. 134-136). The blocks have eigenvalues lambda_i as diagonal entries and 1's on the subdiagonal. The form is unique up to the order of blocks.

# Prerequisites

- **Linear operator** — The operator being decomposed
- **Eigenvalue** — The diagonal entries of Jordan blocks
- **Eigenvector** — Ordinary eigenvectors correspond to 1x1 blocks
- **Characteristic polynomial** — Determines the eigenvalues and their multiplicities
- **Generalized eigenvector** — Needed to construct the Jordan basis

# Key Properties

1. Every complex matrix has a Jordan form
2. The Jordan form is unique up to block ordering
3. J = diag(J_1, ..., J_l) where each J_i is a Jordan block
4. Characteristic polynomial: p(t) = product of (t - lambda_i)^{d_i}
5. A is diagonalizable iff all blocks are 1x1
6. Powers: J^r can be computed using binomial expansion (D+N)^r

# Construction / Recognition

## To Construct:
1. Find eigenvalues from the characteristic polynomial
2. For each eigenvalue lambda, compute dimensions of ker(A - lambda*I)^k for k = 1, 2, ...
3. These dimensions determine the block sizes
4. Finding the actual basis (Jordan generators) is harder

## To Recognize:
1. A block diagonal matrix where each block has a single eigenvalue on the diagonal and 1's on the subdiagonal

# Context & Application

Jordan form is the complete classification of complex matrices up to similarity. It handles all cases, including those where diagonalization fails. The proof in Artin (due to Filippov) proceeds by induction, separating the nilpotent part.

# Examples

**Example 1** (p. 135): 2x2 Jordan forms: diag(lambda_1, lambda_2) or [[lambda,0],[1,lambda]].

**Example 2** (p. 137): A = [[0,1,0],[1,0,1],[0,-1,0]] has A^3 = 0, A^2 != 0, so it has a single 3x3 Jordan block with lambda = 0.

**Example 3** (p. 137): B = [[1,-1,1],[2,-2,2],[-1,1,-1]] has B^2 = 0, so it has a 2x2 block and a 1x1 block (both with lambda = 0).

# Relationships

## Builds Upon
- **Diagonalization** — Jordan form generalizes diagonalization
- **Generalized eigenvector** — Provides the Jordan basis

## Enables
- Computing matrix powers and exponentials for non-diagonalizable matrices

## Related
- **Jordan block** — The building blocks of Jordan form
- **Similar matrices** — Jordan form is unique up to similarity

# Common Errors

- **Error**: Expecting every matrix to be diagonalizable
  **Correction**: When eigenspaces are too small, Jordan blocks larger than 1x1 appear

# Common Confusions

- **Confusion**: Thinking the Jordan form depends on the basis used
  **Clarification**: The Jordan form is unique (up to block order) — it's a canonical form

# Source Reference

Chapter 4: Linear Operators, Section 4.7, pages 133-140.

# Verification Notes

- Definition source: Direct from Theorem 4.7.10
- Confidence rationale: Major theorem with complete proof
- Uncertainties: None
- Cross-reference status: Verified
