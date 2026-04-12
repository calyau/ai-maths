---
concept: Null Space
slug: null-space
category: linear-algebra
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Vector Spaces"
chapter_number: 3
pdf_page: 89
section: "3.1 Subspaces of R^n"
extraction_confidence: high
aliases:
  - "nullspace"
  - "kernel of a matrix"
prerequisites:
  - subspace
  - system-of-linear-equations
extends:
  - subspace
related:
  - rank
  - column-space
  - rank-nullity-theorem
contrasts_with: []
answers_questions:
  - "What is a vector space?"
---

# Quick Definition

The null space (or nullspace) of an m x n matrix A is the subspace of F^n consisting of all solutions to AX = 0. Its dimension is the nullity of A.

# Core Definition

Given an m x n matrix A, the set of vectors in F^n whose coordinate vectors solve AX = 0 is a subspace called the nullspace of A (Artin, p. 89). It is the kernel of the linear transformation X -> AX.

# Prerequisites

- **Subspace** — The null space is a subspace of F^n
- **System of linear equations** — The null space solves AX = 0

# Key Properties

1. Always a subspace of F^n (closed under addition and scalar multiplication)
2. dim(null space) = n - rank(A) (dimension formula)
3. A is invertible iff the null space is {0}
4. If m < n, the null space is nonzero (there are nontrivial solutions)

# Construction / Recognition

## To Construct:
1. Row-reduce A to echelon form
2. Solve AX = 0 by back-substitution
3. Express solutions in terms of free variables

## To Recognize:
1. The set of all X with AX = 0

# Context & Application

The null space captures all the "redundancy" in a linear transformation. Its dimension (nullity) complements the rank via the rank-nullity theorem.

# Examples

**Example 1** (p. 89): For A = [2, -1, -2], the null space is the set of (x_1, x_2, x_3) with 2x_1 - x_2 - 2x_3 = 0, a 2-dimensional subspace of R^3.

# Relationships

## Builds Upon
- **Subspace** — The null space is a subspace

## Enables
- **Rank-nullity theorem** — nullity + rank = n

## Related
- **Column space** — Image of the transformation; complement to null space
- **Rank** — dim(im T) = n - dim(null space)

# Common Errors

- **Error**: Forgetting the null space always contains 0
  **Correction**: AX = 0 always has the trivial solution X = 0

# Common Confusions

- **Confusion**: Confusing null space with "empty set"
  **Clarification**: The null space always contains at least the zero vector; it is a subspace, not empty

# Source Reference

Chapter 3: Vector Spaces, Section 3.1, page 89.

# Verification Notes

- Definition source: Direct from p. 89
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
