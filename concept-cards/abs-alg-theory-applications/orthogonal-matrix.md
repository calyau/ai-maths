---
concept: Orthogonal Matrix
slug: orthogonal-matrix
category: matrix-groups
subcategory: matrix-properties
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Matrix Groups and Symmetry"
chapter_number: 12
pdf_page: 157
section: "The Orthogonal Group O(n)"
extraction_confidence: high
aliases: []
prerequisites:
  - matrix-multiplication
extends: []
related:
  - orthogonal-group
  - euclidean-inner-product
  - orthonormal-set
contrasts_with: []
answers_questions:
  - "What is an orthogonal matrix?"
  - "What are equivalent characterizations of orthogonal matrices?"
---

# Quick Definition

A matrix $A$ is orthogonal if $A^{-1} = A^t$. Equivalently, an orthogonal matrix preserves lengths, distances, and inner products; its columns form an orthonormal set.

# Core Definition

"A matrix $A$ is **orthogonal** if $A^{-1} = A^t$" (Judson, p. 157). Theorem 12.8 establishes five equivalent characterizations: (1) columns form orthonormal set, (2) $A^{-1} = A^t$, (3) preserves inner products, (4) preserves distances, (5) preserves lengths.

# Prerequisites

- **Matrix multiplication** — Required for definition

# Key Properties

1. $A^{-1} = A^t$ (defining property)
2. $\det(A) = \pm 1$
3. Columns form an orthonormal set: $\langle \mathbf{a}_r, \mathbf{a}_s \rangle = \delta_{rs}$
4. $\langle A\mathbf{x}, A\mathbf{y} \rangle = \langle \mathbf{x}, \mathbf{y} \rangle$ (inner product preserving)
5. $\|A\mathbf{x}\| = \|\mathbf{x}\|$ (length preserving)
6. $\|A\mathbf{x} - A\mathbf{y}\| = \|\mathbf{x} - \mathbf{y}\|$ (distance preserving)

# Examples

**Example 1** (p. 157): $\begin{pmatrix} 3/5 & -4/5 \\ 4/5 & 3/5 \end{pmatrix}$ is orthogonal. It preserves the length of $\mathbf{x} = (3,4)^t$: $\|A\mathbf{x}\| = 5 = \|\mathbf{x}\|$.

# Relationships

## Enables
- **Orthogonal group** — $O(n)$ consists of all orthogonal matrices

## Related
- **Orthonormal set** — Columns of an orthogonal matrix are orthonormal

# Source Reference

Chapter 12: Matrix Groups and Symmetry, Section 12.1, pages 157-159. Theorem 12.8.

# Verification Notes

- Definition source: Direct quote from p. 157
- Characterization: Theorem 12.8 with complete proof
- Confidence: HIGH
