---
concept: Lattice in Rn
slug: lattice-in-rn
category: matrix-groups
subcategory: crystallographic-groups
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Matrix Groups and Symmetry"
chapter_number: 12
pdf_page: 164
section: "The Wallpaper Groups"
extraction_confidence: high
aliases:
  - "lattice"
  - "point lattice"
prerequisites:
  - vector-space
extends: []
related:
  - wallpaper-group
  - unimodular-matrix
contrasts_with: []
answers_questions:
  - "What is a lattice in the context of symmetry groups?"
---

# Quick Definition

A lattice in $\mathbb{R}^2$ is the set of all integer linear combinations $m\mathbf{x} + n\mathbf{y}$ of two linearly independent vectors $\mathbf{x}$ and $\mathbf{y}$. Lattices provide the mathematical framework for describing repeating patterns and crystal structures.

# Core Definition

"Let us examine wallpaper patterns in the plane a little more closely. Suppose that $\mathbf{x}$ and $\mathbf{y}$ are linearly independent vectors in $\mathbb{R}^2$... A **lattice** of $\mathbf{x}$ and $\mathbf{y}$ is the set of all linear combinations $m\mathbf{x} + n\mathbf{y}$, where $m$ and $n$ are integers. The vectors $\mathbf{x}$ and $\mathbf{y}$ are said to be a **basis** for the lattice" (Judson, p. 164).

# Prerequisites

- **Vector space** — Lattices live in $\mathbb{R}^n$

# Key Properties

1. A lattice can have multiple bases
2. Two bases determine the same lattice iff they are related by a unimodular matrix
3. There is a minimum length for vectors in a lattice
4. Lattice cell shapes: parallelogram, rectangular, square, rhombic, hexagonal

# Examples

**Example 1** (p. 165): The vectors $(1,1)^t$ and $(2,0)^t$ determine the same lattice as $(-1,1)^t$ and $(-1,-1)^t$.

# Relationships

## Enables
- **Wallpaper group** — The translation subgroup of a wallpaper group forms a lattice

## Related
- **Unimodular matrix** — Relates different bases for the same lattice

# Source Reference

Chapter 12: Matrix Groups and Symmetry, Section 12.2, pp. 164-165.

# Verification Notes

- Definition source: Direct quote from p. 164
- Confidence: HIGH
