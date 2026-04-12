---
concept: Identity Matrix
slug: identity-matrix
category: matrices
subcategory: special-matrices
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Matrices"
chapter_number: 1
pdf_page: 12
section: "1.1 The Basic Operations"
extraction_confidence: high
aliases:
  - "I_n"
  - "identity"
prerequisites:
  - matrix
  - diagonal-matrix
extends:
  - diagonal-matrix
related:
  - invertible-matrix
  - elementary-matrix
contrasts_with:
  - zero-matrix
answers_questions:
  - "What is a matrix and what are its basic operations?"
---

# Quick Definition

The n x n identity matrix I_n is the diagonal matrix with all diagonal entries equal to 1. It is the multiplicative identity: AI = A and IA = A.

# Core Definition

The diagonal n x n matrix all of whose diagonal entries are equal to 1 is called the n x n identity matrix, denoted I_n or simply I. It satisfies AI_n = A and I_m A = A for any m x n matrix A (Artin, p. 16).

# Prerequisites

- **Matrix** — Must understand matrix structure
- **Diagonal matrix** — The identity is a special diagonal matrix

# Key Properties

1. Square matrix with 1's on the diagonal and 0's elsewhere
2. Acts as the multiplicative identity: AI = A and IA = A
3. det(I) = 1
4. I^(-1) = I

# Construction / Recognition

## To Construct:
1. Create an n x n matrix with a_ii = 1 for all i, and a_ij = 0 for i != j

## To Recognize:
1. A square matrix with 1's on the diagonal and 0's everywhere else

# Context & Application

The identity matrix is the multiplicative identity for matrix multiplication and the identity element of the general linear group GL_n. It is the target of row reduction for invertible matrices.

# Examples

**Example 1** (p. 16): I_2 = [[1,0],[0,1]], I_3 = [[1,0,0],[0,1,0],[0,0,1]].

# Relationships

## Builds Upon
- **Diagonal matrix** — The identity is a diagonal matrix with all entries 1

## Enables
- **Invertible matrix** — Defined by AB = I = BA
- **Elementary matrix** — Obtained by modifying I

## Contrasts With
- **Zero matrix** — The additive identity, versus the multiplicative identity

# Common Errors

- **Error**: Forgetting that I_n depends on n
  **Correction**: The size of I must match the context of the multiplication

# Common Confusions

- **Confusion**: Thinking I is the only matrix commuting with all others
  **Clarification**: Scalar multiples cI also commute with all n x n matrices

# Source Reference

Chapter 1: Matrices, Section 1.1, page 16.

# Verification Notes

- Definition source: Direct from (1.1.11), p. 16
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
