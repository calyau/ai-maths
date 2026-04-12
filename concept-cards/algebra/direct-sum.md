---
concept: Direct Sum
slug: direct-sum
category: linear-algebra
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Vector Spaces"
chapter_number: 3
pdf_page: 89
section: "3.6 Direct Sums"
extraction_confidence: high
aliases:
  - "internal direct sum"
prerequisites:
  - vector-space
  - subspace
  - linear-independence
extends: []
related:
  - dimension
  - eigenspace
contrasts_with: []
answers_questions:
  - "What is a vector space?"
---

# Quick Definition

A vector space V is the direct sum W_1 ⊕ ... ⊕ W_k of subspaces if W_1 + ... + W_k = V and the subspaces are independent (the only way to write 0 as w_1 + ... + w_k with w_i in W_i is w_i = 0 for all i).

# Core Definition

If subspaces W_1, ..., W_k of V are independent and their sum equals V, then V is the direct sum W_1 ⊕ ... ⊕ W_k (Artin, p. 108, formula 3.6.5). Equivalently, every vector in V has a unique decomposition v = w_1 + ... + w_k with w_i in W_i. In this case, dim V = dim W_1 + ... + dim W_k.

# Prerequisites

- **Vector space** — Direct sum decomposes a vector space
- **Subspace** — The summands are subspaces
- **Linear independence** — The subspaces must be independent

# Key Properties

1. Every vector has a unique decomposition
2. dim V = sum of dim W_i
3. For two subspaces: V = W_1 ⊕ W_2 iff W_1 ∩ W_2 = {0} and W_1 + W_2 = V
4. Concatenating bases of W_i gives a basis of V

# Construction / Recognition

## To Construct:
1. Find independent subspaces whose sum is V

## To Recognize:
1. The subspaces are independent and their sum is V

# Context & Application

Direct sums arise naturally in the eigenspace decomposition of a diagonalizable operator: V = V(lambda_1) ⊕ ... ⊕ V(lambda_k). They also appear in the Jordan decomposition.

# Examples

**Example 1** (p. 108): dim(W_1 + W_2) = dim W_1 + dim W_2 - dim(W_1 ∩ W_2) (Proposition 3.6.6).

**Example 2** (Section 4.4): If T is diagonalizable, V is the direct sum of eigenspaces.

# Relationships

## Builds Upon
- **Subspace** — Summands are subspaces

## Enables
- **Diagonalization** — V = direct sum of eigenspaces

# Common Errors

- **Error**: Assuming W_1 + W_2 = V implies direct sum
  **Correction**: Also need W_1 ∩ W_2 = {0}

# Common Confusions

- **Confusion**: Confusing direct sum with Cartesian product
  **Clarification**: Internal direct sum decomposes an existing space; external product creates a new one

# Source Reference

Chapter 3: Vector Spaces, Section 3.6, pages 107-109.

# Verification Notes

- Definition source: Direct from (3.6.5), p. 108
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
