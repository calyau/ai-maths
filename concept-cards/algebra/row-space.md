---
concept: Row Space
slug: row-space
category: linear-algebra
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Operators"
chapter_number: 4
pdf_page: 113
section: "4.2 The Matrix of a Linear Transformation"
extraction_confidence: high
aliases:
  - "row rank"
prerequisites:
  - matrix
  - subspace
  - span
extends:
  - subspace
related:
  - column-space
  - rank
  - rank-nullity-theorem
contrasts_with:
  - column-space
answers_questions:
  - "What is a linear transformation?"
---

# Quick Definition

The row space of a matrix A is the subspace of F^n spanned by the rows of A. Its dimension (the row rank) equals the column rank (Theorem 4.2.14), so both equal the rank of A.

# Core Definition

The row space of an m x n matrix A is the subspace of F^n spanned by the rows (or equivalently, the column space of A^t). The row rank equals the column rank (Theorem 4.2.14, Artin, pp. 117-118). Row operations do not change the row space.

# Prerequisites

- **Matrix** — The row space is defined for a matrix
- **Subspace** — The row space is a subspace of F^n
- **Span** — Spanned by the rows

# Key Properties

1. dim(row space) = rank(A) = dim(column space) (Theorem 4.2.14)
2. Row operations preserve the row space
3. Row space = column space of A^t

# Construction / Recognition

## To Construct:
1. Row-reduce A; the nonzero rows of the echelon form span the row space

## To Recognize:
1. The span of the rows of A

# Context & Application

The row space is the "dual" of the column space. The fundamental theorem that row rank = column rank (Theorem 4.2.14) is a key result connecting the two perspectives.

# Examples

**Example 1** (p. 118): The row rank of A equals the column rank of A.

# Relationships

## Builds Upon
- **Span** — Row space = span of rows

## Related
- **Column space** — dim(row space) = dim(column space)
- **Rank** — Same as the rank

## Contrasts With
- **Column space** — Row space is in F^n; column space is in F^m

# Common Errors

- **Error**: Thinking row reduction changes the row space
  **Correction**: Row operations preserve the row space (they change the column space)

# Common Confusions

- **Confusion**: Thinking row rank can differ from column rank
  **Clarification**: They are always equal (Theorem 4.2.14)

# Source Reference

Chapter 4: Linear Operators, Section 4.2, pages 117-118.

# Verification Notes

- Definition source: Synthesized from Theorem 4.2.14 discussion
- Confidence rationale: Implicitly defined via row rank discussion
- Uncertainties: None
- Cross-reference status: Verified
