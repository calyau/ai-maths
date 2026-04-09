---
concept: Euclidean Inner Product
slug: euclidean-inner-product
category: matrix-groups
subcategory: linear-algebra-foundations
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Matrix Groups and Symmetry"
chapter_number: 12
pdf_page: 157
section: "The Orthogonal Group O(n)"
extraction_confidence: high
aliases:
  - "dot product"
  - "standard inner product"
prerequisites:
  - vector-space
extends: []
related:
  - orthogonal-matrix
  - orthonormal-set
  - orthogonal-group
contrasts_with: []
answers_questions:
  - "What is the Euclidean inner product?"
  - "How is length defined using inner products?"
---

# Quick Definition

The Euclidean inner product (or dot product) of vectors $\mathbf{x}$ and $\mathbf{y}$ in $\mathbb{R}^n$ is $\langle \mathbf{x}, \mathbf{y} \rangle = x_1 y_1 + \cdots + x_n y_n$. The length of a vector is $\|\mathbf{x}\| = \sqrt{\langle \mathbf{x}, \mathbf{x} \rangle}$.

# Core Definition

"The **Euclidean inner product**, or **dot product**, of two vectors $\mathbf{x} = (x_1, \ldots, x_n)^t$ and $\mathbf{y} = (y_1, \ldots, y_n)^t$ is $\langle \mathbf{x}, \mathbf{y} \rangle = \mathbf{x}^t \mathbf{y} = x_1 y_1 + \cdots + x_n y_n$. We define the **length** of a vector $\mathbf{x}$ to be $\|\mathbf{x}\| = \sqrt{x_1^2 + \cdots + x_n^2}$" (Judson, p. 157-158).

# Prerequisites

- **Vector space** — Inner products are defined on vector spaces

# Key Properties (Proposition 12.6)

1. $\langle \mathbf{x}, \mathbf{y} \rangle = \langle \mathbf{y}, \mathbf{x} \rangle$ (symmetry)
2. $\langle \mathbf{x}, \mathbf{y} + \mathbf{w} \rangle = \langle \mathbf{x}, \mathbf{y} \rangle + \langle \mathbf{x}, \mathbf{w} \rangle$ (linearity)
3. $\langle \alpha\mathbf{x}, \mathbf{y} \rangle = \alpha\langle \mathbf{x}, \mathbf{y} \rangle$ (homogeneity)
4. $\langle \mathbf{x}, \mathbf{x} \rangle \geq 0$ with equality iff $\mathbf{x} = \mathbf{0}$ (positive definiteness)
5. Distance: $\|\mathbf{x} - \mathbf{y}\|$

# Examples

**Example 1** (p. 158): The vector $\mathbf{x} = (3, 4)^t$ has length $\sqrt{9 + 16} = 5$.

# Relationships

## Enables
- **Orthogonal matrix** — Defined via inner product preservation
- **Orthonormal set** — Defined using inner products

# Source Reference

Chapter 12: Matrix Groups and Symmetry, Section 12.1, pages 157-158. Proposition 12.6.

# Verification Notes

- Definition source: Direct quote from pp. 157-158
- Confidence: HIGH
