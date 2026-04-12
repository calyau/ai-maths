---
concept: Dimension
slug: dimension
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
  - "dim V"
prerequisites:
  - vector-space
  - basis
extends: []
related:
  - rank
  - null-space
contrasts_with: []
answers_questions:
  - "What is a basis and what is dimension?"
---

# Quick Definition

The dimension of a finite-dimensional vector space V is the number of vectors in any basis. This number is the same for all bases of V. The dimension of F^n is n.

# Core Definition

The dimension of a finite-dimensional vector space V, denoted dim V, is the number of vectors in a basis (Definition 3.4.22, Artin, p. 103). This is well-defined because any two bases have the same number of elements (Proposition 3.4.21).

# Prerequisites

- **Vector space** — Dimension is a property of a vector space
- **Basis** — Dimension counts basis vectors

# Key Properties

1. dim(F^n) = n
2. dim(W) <= dim(V) for any subspace W of V, with equality iff W = V
3. Every vector space of dimension n over F is isomorphic to F^n
4. dim(W_1 + W_2) = dim(W_1) + dim(W_2) - dim(W_1 ∩ W_2)

# Construction / Recognition

## To Construct:
1. Find any basis of V
2. Count its elements

## To Recognize:
1. The maximum number of linearly independent vectors in V

# Context & Application

Dimension is the fundamental invariant of a vector space. It completely classifies finite-dimensional vector spaces over a given field: two spaces are isomorphic iff they have the same dimension.

# Examples

**Example 1** (p. 103): dim(F^n) = n because the standard basis has n vectors.

**Example 2** (p. 100): The solution space of 2x_1 - x_2 - 2x_3 = 0 has dimension 2.

# Relationships

## Builds Upon
- **Basis** — Dimension counts basis vectors

## Enables
- **Rank** — Dimension of the image of a linear transformation
- **Null space** — Dimension of the kernel (nullity)

# Common Errors

- **Error**: Claiming a vector space has "no dimension"
  **Correction**: The zero space {0} has dimension 0 (empty basis)

# Common Confusions

- **Confusion**: Confusing the dimension of a vector space with the dimension of ambient space
  **Clarification**: A plane through the origin in R^3 has dimension 2, not 3

# Source Reference

Chapter 3: Vector Spaces, Section 3.4, page 103.

# Verification Notes

- Definition source: Direct from Definition 3.4.22, p. 103
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
