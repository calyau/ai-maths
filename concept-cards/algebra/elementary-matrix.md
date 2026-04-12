---
concept: Elementary Matrix
slug: elementary-matrix
category: matrices
subcategory: special-matrices
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.2 Row Reduction"
extraction_confidence: high
aliases: []
prerequisites:
  - matrix
  - identity-matrix
extends: []
related:
  - elementary-row-operations
  - row-reduction
  - invertible-matrix
contrasts_with: []
answers_questions:
  - "How do row operations relate to matrix invertibility?"
---

# Quick Definition

An elementary matrix is obtained from the identity matrix by a single elementary row operation. Left multiplication by an elementary matrix performs the corresponding row operation.

# Core Definition

There are three types of elementary n x n matrices, obtained by splicing elementary 2x2 matrices into an identity matrix (Artin, pp. 18-19, formula 1.2.4):
- Type (i): I with one off-diagonal entry a added (position i,j)
- Type (ii): I with two diagonal 1's replaced by 0 and two off-diagonal 0's replaced by 1 (row interchange)
- Type (iii): I with one diagonal entry replaced by a nonzero scalar c

Elementary matrices are invertible, and their inverses are also elementary (Lemma 1.2.6).

# Prerequisites

- **Matrix** — Elementary matrices are special matrices
- **Identity matrix** — Each is a modification of I

# Key Properties

1. Invertible, with elementary inverse (Lemma 1.2.6)
2. Left multiplication EX performs the corresponding row operation on X
3. Every invertible matrix is a product of elementary matrices (Theorem 1.2.16)
4. det(E) = 1 for Type (i), -1 for Type (ii), c for Type (iii)

# Construction / Recognition

## To Construct:
1. Start with the identity matrix
2. Apply one elementary row operation to it

## To Recognize:
1. An invertible matrix that differs from I by exactly one elementary modification

# Context & Application

Elementary matrices provide the theoretical foundation for row reduction. Theorem 1.2.16 shows that a matrix is invertible iff it is a product of elementary matrices, connecting the computational process of row reduction to the algebraic concept of invertibility.

# Examples

**Example 1** (p. 19): Type (i) 2x2: [[1,a],[0,1]]; Type (ii): [[0,1],[1,0]]; Type (iii): [[c,0],[0,1]].

# Relationships

## Builds Upon
- **Identity matrix** — Modified version of I

## Enables
- **Row reduction** — Each step is multiplication by an elementary matrix
- **Invertible matrix** — A is invertible iff A = E_1...E_k (Theorem 1.2.16)

## Related
- **Elementary row operations** — Each elementary matrix performs one

# Common Errors

- **Error**: Confusing the elementary matrix with the operation it performs
  **Correction**: The matrix E performs the operation when you compute EX

# Common Confusions

- **Confusion**: Thinking elementary matrices are always simple-looking
  **Clarification**: For large n, they look like I with one modification

# Source Reference

Chapter 1: Matrices, Section 1.2, pages 18-19.

# Verification Notes

- Definition source: Direct from (1.2.3)-(1.2.4), pp. 18-19
- Confidence rationale: Explicitly defined with all three types
- Uncertainties: None
- Cross-reference status: Verified
