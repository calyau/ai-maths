---
concept: Orthonormal Set
slug: orthonormal-set
category: matrix-groups
subcategory: linear-algebra-foundations
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Matrix Groups and Symmetry"
chapter_number: 12
pdf_page: 158
section: "The Orthogonal Group O(n)"
extraction_confidence: high
aliases:
  - "orthonormal basis"
prerequisites:
  - euclidean-inner-product
extends: []
related:
  - orthogonal-matrix
  - orthogonal-group
contrasts_with: []
answers_questions:
  - "What is an orthonormal set of vectors?"
---

# Quick Definition

A set of vectors is orthonormal if each vector has length 1 and any two distinct vectors are orthogonal (inner product zero): $\langle \mathbf{a}_r, \mathbf{a}_s \rangle = \delta_{rs}$.

# Core Definition

"Any set of vectors satisfying these properties is called an **orthonormal set**" (Judson, p. 158), where the properties are $\langle \mathbf{a}_r, \mathbf{a}_s \rangle = \delta_{rs}$ with $\delta_{rs} = 1$ if $r = s$ and $0$ if $r \neq s$ (the Kronecker delta).

# Prerequisites

- **Euclidean inner product** — Orthonormality is defined via inner products

# Key Properties

1. Each vector has unit length: $\|\mathbf{a}_i\| = 1$
2. Distinct vectors are orthogonal: $\langle \mathbf{a}_i, \mathbf{a}_j \rangle = 0$ for $i \neq j$
3. Columns of an orthogonal matrix form an orthonormal set
4. Conversely, a matrix whose columns are orthonormal is orthogonal

# Relationships

## Enables
- **Orthogonal matrix** — Characterized by orthonormal columns

# Source Reference

Chapter 12: Matrix Groups and Symmetry, Section 12.1, p. 158.

# Verification Notes

- Definition source: Direct from p. 158
- Confidence: HIGH
