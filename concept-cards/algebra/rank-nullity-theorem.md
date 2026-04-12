---
concept: Rank-Nullity Theorem
slug: rank-nullity-theorem
category: linear-algebra
subcategory: null
tier: intermediate
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Operators"
chapter_number: 4
pdf_page: 113
section: "4.1 The Dimension Formula"
extraction_confidence: high
aliases:
  - "dimension formula"
  - "rank plus nullity"
prerequisites:
  - linear-transformation
  - dimension
  - null-space
  - rank
extends: []
related:
  - linear-operator
contrasts_with: []
answers_questions:
  - "What is a linear transformation?"
---

# Quick Definition

The rank-nullity theorem states that for a linear transformation T: V -> W, dim(ker T) + dim(im T) = dim V. Equivalently, nullity + rank = dimension of the domain.

# Core Definition

Theorem 4.1.6 (Dimension Formula): Let T: V -> W be a linear transformation. Then dim(ker T) + dim(im T) = dim V (Artin, p. 114). The nullity is dim(ker T) and the rank is dim(im T), so nullity + rank = dim V (formula 4.1.7).

# Prerequisites

- **Linear transformation** — The map T
- **Dimension** — Of the kernel and image
- **Null space** — ker T
- **Rank** — dim(im T)

# Key Properties

1. nullity + rank = dim V
2. For a matrix A: nullity(A) + rank(A) = n (number of columns)
3. T is injective iff rank = dim V iff nullity = 0
4. T is surjective iff rank = dim W
5. If dim V = dim W (linear operator), injective iff surjective

# Construction / Recognition

## To Construct:
1. Not applicable (this is a theorem)

## To Recognize:
1. Any statement relating dimensions of kernel, image, and domain

# Context & Application

The dimension formula is the fundamental constraint on linear transformations. It explains why, for square matrices, injectivity and surjectivity are equivalent. It connects the null space (kernel) to the column space (image).

# Examples

**Example 1** (p. 114): A 3x5 matrix of rank 2 has nullity 5 - 2 = 3.

**Example 2** (pp. 117-118): The rank of a matrix equals the rank of its transpose (Theorem 4.2.14).

# Relationships

## Builds Upon
- **Linear transformation** — The map T
- **Dimension** — The theorem relates dimensions

## Enables
- Understanding when systems have unique solutions vs. infinite solutions

# Common Errors

- **Error**: Confusing rank with the number of nonzero rows
  **Correction**: Rank = dim(im T) = number of pivots in echelon form

# Common Confusions

- **Confusion**: Thinking the theorem only applies to square matrices
  **Clarification**: It applies to any linear transformation V -> W

# Source Reference

Chapter 4: Linear Operators, Section 4.1, pages 114-115.

# Verification Notes

- Definition source: Direct from Theorem 4.1.6, p. 114
- Confidence rationale: Named theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
