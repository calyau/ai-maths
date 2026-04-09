---
concept: Unimodular Matrix
slug: unimodular-matrix
category: matrix-groups
subcategory: matrix-properties
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Matrix Groups and Symmetry"
chapter_number: 12
pdf_page: 165
section: "The Wallpaper Groups"
extraction_confidence: high
aliases: []
prerequisites:
  - matrix-multiplication
extends: []
related:
  - lattice-in-rn
contrasts_with: []
answers_questions:
  - "What is a unimodular matrix?"
  - "How do unimodular matrices relate to lattices?"
---

# Quick Definition

A unimodular matrix is a matrix with integer entries and determinant $\pm 1$. Two bases for a lattice are related by a unimodular change-of-basis matrix.

# Core Definition

"A matrix with determinant $\pm 1$ and integer entries is called **unimodular**" (Judson, p. 165).

# Prerequisites

- **Matrix multiplication** — Basic matrix concept

# Key Properties

1. Integer entries
2. $\det(U) = \pm 1$
3. $U^{-1}$ also has integer entries (since $\det(U) = \pm 1$)
4. Two bases for the same lattice are related by a unimodular matrix

# Examples

**Example 1** (p. 165): $\begin{pmatrix} 3 & 1 \\ 5 & 2 \end{pmatrix}$ is unimodular ($\det = 6 - 5 = 1$).

# Relationships

## Related
- **Lattice** — Unimodular matrices relate different bases for the same lattice

# Source Reference

Chapter 12: Matrix Groups and Symmetry, Section 12.2, p. 165.

# Verification Notes

- Definition source: Direct from p. 165
- Confidence: HIGH
