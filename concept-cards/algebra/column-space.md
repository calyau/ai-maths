---
concept: Column Space
slug: column-space
category: linear-algebra
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Vector Spaces"
chapter_number: 3
pdf_page: 89
section: "3.4 Bases and Dimension"
extraction_confidence: high
aliases:
  - "image of A"
prerequisites:
  - matrix
  - subspace
  - span
extends:
  - subspace
related:
  - null-space
  - rank
  - row-space
contrasts_with:
  - null-space
answers_questions:
  - "What is a vector space?"
---

# Quick Definition

The column space of an m x n matrix A is the subspace of F^m spanned by the columns of A. It equals the image of the linear transformation X -> AX, and its dimension is the rank of A.

# Core Definition

The column space of an m x n matrix A with entries in F is the subspace of F^m spanned by the columns of A. The system AX = B has a solution iff B is in the column space (Proposition 3.4.6, Artin, p. 99).

# Prerequisites

- **Matrix** — The column space is defined for a matrix
- **Subspace** — The column space is a subspace
- **Span** — The column space is the span of the columns

# Key Properties

1. dim(column space) = rank(A)
2. AX = B has a solution iff B is in the column space
3. Column rank = row rank (Theorem 4.2.14)

# Construction / Recognition

## To Construct:
1. Take the span of the columns of A
2. Or: row-reduce A and take the columns corresponding to pivot columns

## To Recognize:
1. The set of all vectors AX as X ranges over F^n

# Context & Application

The column space is the image of the linear map X -> AX. Together with the null space, it provides a complete picture of the transformation via the rank-nullity theorem.

# Examples

**Example 1** (p. 99): The column space of A determines which systems AX = B are solvable.

# Relationships

## Builds Upon
- **Span** — Column space = span of columns

## Related
- **Null space** — dim(null space) + dim(column space) = n
- **Rank** — dim(column space) = rank
- **Row space** — Same dimension as column space

## Contrasts With
- **Null space** — Column space is the image; null space is the kernel

# Common Errors

- **Error**: Confusing column space with row space
  **Correction**: Column space is in F^m (spanned by columns); row space is in F^n (spanned by rows)

# Common Confusions

- **Confusion**: Thinking the columns of the row-reduced matrix span the same column space
  **Clarification**: Row reduction preserves the row space but changes the column space; use the ORIGINAL columns at pivot positions

# Source Reference

Chapter 3: Vector Spaces, Section 3.4, page 99.

# Verification Notes

- Definition source: From Proposition 3.4.6, p. 99
- Confidence rationale: Explicitly discussed
- Uncertainties: None
- Cross-reference status: Verified
