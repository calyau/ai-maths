---
concept: Linear Transformation
slug: linear-transformation
category: linear-algebra
subcategory: null
tier: foundational
source: "Algebra"
source_slug: algebra
authors: "Michael Artin"
chapter: "Linear Operators"
chapter_number: 4
pdf_page: 113
section: "4.1 The Dimension Formula"
extraction_confidence: high
aliases:
  - "linear map"
prerequisites:
  - vector-space
extends: []
related:
  - linear-operator
  - matrix-of-a-linear-transformation
  - kernel-linear
  - image-linear
  - rank-nullity-theorem
contrasts_with: []
answers_questions:
  - "What is a linear transformation?"
---

# Quick Definition

A linear transformation T: V -> W between vector spaces is a map preserving addition and scalar multiplication: T(v_1 + v_2) = T(v_1) + T(v_2) and T(cv) = cT(v). Every linear transformation corresponds to a matrix, once bases are chosen.

# Core Definition

A linear transformation T: V -> W from one vector space over a field F to another is a map compatible with addition and scalar multiplication: T(v_1 + v_2) = T(v_1) + T(v_2) and T(cv_1) = cT(v_1) for all v_1, v_2 in V and c in F (Artin, p. 113, formula 4.1.1). Left multiplication by a matrix A is a linear transformation F^n -> F^m.

# Prerequisites

- **Vector space** — Domain and codomain are vector spaces

# Key Properties

1. T(0) = 0
2. T(sum c_i v_i) = sum c_i T(v_i)
3. The kernel ker(T) is a subspace of V
4. The image im(T) is a subspace of W
5. dim(ker T) + dim(im T) = dim V (Dimension Formula, Theorem 4.1.6)
6. Every linear transformation V -> W corresponds to a matrix once bases are chosen

# Construction / Recognition

## To Construct:
1. Define T on a basis of V and extend linearly

## To Recognize:
1. Check T(v+w) = T(v) + T(w) and T(cv) = cT(v)

# Context & Application

Linear transformations are the structure-preserving maps of linear algebra, analogous to group homomorphisms. The dimension formula (rank-nullity theorem) is the fundamental constraint on their behavior.

# Examples

**Example 1** (p. 113): Left multiplication A: F^n -> F^m, X -> AX.

**Example 2** (p. 114): The derivative d/dx: P_n -> P_{n-1} on polynomials of degree <= n.

**Example 3** (p. 115): Counterclockwise rotation of R^2 through angle theta, with matrix [[cos theta, -sin theta],[sin theta, cos theta]].

# Relationships

## Builds Upon
- **Vector space** — Maps between vector spaces

## Enables
- **Matrix of a linear transformation** — Matrix representation
- **Rank-nullity theorem** — dim(ker) + dim(im) = dim(V)

## Related
- **Linear operator** — A linear transformation V -> V (same domain and codomain)

# Common Errors

- **Error**: Assuming a linear transformation must be injective
  **Correction**: The kernel may be nontrivial

# Common Confusions

- **Confusion**: Confusing linear transformation with linear operator
  **Clarification**: A linear operator maps V to itself; a transformation may map V to a different space W

# Source Reference

Chapter 4: Linear Operators, Section 4.1, pages 113-115.

# Verification Notes

- Definition source: Direct from (4.1.1), p. 113
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
