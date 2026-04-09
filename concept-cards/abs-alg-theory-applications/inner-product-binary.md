---
concept: Inner Product (Binary)
slug: inner-product-binary
category: applications-coding
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Algebraic Coding Theory"
chapter_number: 8
pdf_page: 112
section: "8.2 Linear Codes"
extraction_confidence: high
aliases:
  - dot product over Z2
prerequisites: []
extends: []
related:
  - linear-code
  - canonical-parity-check-matrix
contrasts_with: []
answers_questions:
  - "What is the inner product of binary n-tuples?"
---

# Quick Definition

The inner product of two binary $n$-tuples $\mathbf{x}$ and $\mathbf{y}$ is $\mathbf{x} \cdot \mathbf{y} = x_1y_1 + \cdots + x_ny_n$, computed in $\mathbb{Z}_2$. It connects parity checking to matrix operations.

# Core Definition

"Define the *inner product* of two binary $n$-tuples to be $\mathbf{x} \cdot \mathbf{y} = x_1y_1 + \cdots + x_ny_n$, where $\mathbf{x} = (x_1, \ldots, x_n)^t$ and $\mathbf{y} = (y_1, \ldots, y_n)^t$ are column vectors" (Judson, p. 112). The inner product can also be written as $\mathbf{x} \cdot \mathbf{y} = \mathbf{x}^t\mathbf{y}$.

# Prerequisites

Binary arithmetic in $\mathbb{Z}_2$.

# Key Properties

1. Computed in $\mathbb{Z}_2$ (addition modulo 2)
2. $\mathbf{x} \cdot \mathbf{y} = \mathbf{x}^t\mathbf{y}$ (matrix product of row times column)
3. An $n$-tuple has even weight iff $\mathbf{x} \cdot \mathbf{1} = 0$ (where $\mathbf{1} = (1,1,\ldots,1)^t$)
4. Used to express parity check conditions

# Construction / Recognition

## To Compute:
1. Multiply corresponding components: $x_iy_i$
2. Sum all products modulo 2
3. Result is 0 or 1

# Context & Application

The binary inner product provides the link between parity checking and matrix algebra. The condition $H\mathbf{x} = \mathbf{0}$ is equivalent to $\mathbf{x}$ being orthogonal to each row of $H$.

# Examples

**Example 1** (p. 112): $\mathbf{x} = (011001)^t$ and $\mathbf{y} = (110101)^t$: $\mathbf{x} \cdot \mathbf{y} = 0 \cdot 1 + 1 \cdot 1 + 1 \cdot 0 + 0 \cdot 1 + 0 \cdot 0 + 1 \cdot 1 = 0$.

**Example 2** (p. 113): A 4-tuple $(x_1, x_2, x_3, x_4)$ has even parity iff $\mathbf{x} \cdot \mathbf{1} = 0$.

# Relationships

## Enables
- **Linear Code** — Null space condition uses inner products
- **Canonical Parity-Check Matrix** — Rows define parity checks via inner products

# Common Errors

- **Error**: Forgetting to reduce modulo 2
  **Correction**: All arithmetic is in $\mathbb{Z}_2$: $1 + 1 = 0$

# Common Confusions

- **Confusion**: Confusing with the real inner product
  **Clarification**: The binary inner product takes values in $\{0, 1\}$, not $\mathbb{R}$

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.2, page 112.

# Verification Notes

- Definition source: Direct from p. 112
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
