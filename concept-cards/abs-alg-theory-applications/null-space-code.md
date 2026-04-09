---
concept: Null Space of a Matrix
slug: null-space-code
category: applications-coding
subcategory: null
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Algebraic Coding Theory"
chapter_number: 8
pdf_page: 113
section: "8.2 Linear Codes"
extraction_confidence: high
aliases:
  - "Null(H)"
prerequisites: []
extends: []
related:
  - linear-code
  - canonical-parity-check-matrix
contrasts_with: []
answers_questions:
  - "What is the null space of a binary matrix?"
  - "How does the null space define a code?"
---

# Quick Definition

The null space of a binary matrix $H \in \mathbb{M}_{m \times n}(\mathbb{Z}_2)$ is the set of all binary $n$-tuples $\mathbf{x}$ such that $H\mathbf{x} = \mathbf{0}$. It is always a group code (subgroup of $\mathbb{Z}_2^n$).

# Core Definition

"Define the *null space* of a matrix $H \in \mathbb{M}_{m \times n}(\mathbb{Z}_2)$ to be the set of all binary $n$-tuples $\mathbf{x}$ such that $H\mathbf{x} = \mathbf{0}$. We denote the null space of a matrix $H$ by $\text{Null}(H)$" (Judson, p. 113). By Theorem 8.21, the null space is always a group code.

# Prerequisites

Basic matrix arithmetic over $\mathbb{Z}_2$.

# Key Properties

1. $\text{Null}(H) = \{\mathbf{x} \in \mathbb{Z}_2^n : H\mathbf{x} = \mathbf{0}\}$
2. Always a subgroup of $\mathbb{Z}_2^n$ (Theorem 8.21)
3. Hence always a group code
4. Checking membership is a matrix multiplication: $H\mathbf{x} = \mathbf{0}$?
5. A linear code is defined as the null space of some binary matrix

# Construction / Recognition

## To Compute:
1. Set up the system $H\mathbf{x} = \mathbf{0}$ over $\mathbb{Z}_2$
2. Solve for all $\mathbf{x}$ satisfying the system
3. The solution set is $\text{Null}(H)$

# Context & Application

The null space provides the algebraic foundation for linear codes. It connects matrix algebra over $\mathbb{Z}_2$ to coding theory.

# Examples

**Example 1** (p. 113): For $H = \begin{pmatrix} 0 & 1 & 0 & 1 & 0 \\ 1 & 1 & 1 & 1 & 0 \\ 0 & 0 & 1 & 1 & 1 \end{pmatrix}$, $\text{Null}(H) = \{(00000), (11110), (10101), (01011)\}$.

# Relationships

## Enables
- **Linear Code** — Linear codes are null spaces of binary matrices

## Related
- **Canonical Parity-Check Matrix** — Special form of $H$

# Common Errors

- **Error**: Forgetting that arithmetic is modulo 2
  **Correction**: All operations in $H\mathbf{x} = \mathbf{0}$ are in $\mathbb{Z}_2$

# Common Confusions

- **Confusion**: Confusing the null space over $\mathbb{Z}_2$ with the null space over $\mathbb{R}$
  **Clarification**: Over $\mathbb{Z}_2$, the null space is a finite set

# Source Reference

Chapter 8: Algebraic Coding Theory, Section 8.2, Theorem 8.21, page 113.

# Verification Notes

- Definition source: Direct from p. 113
- Confidence rationale: Explicit definition
- Uncertainties: None
- Cross-reference status: Verified
