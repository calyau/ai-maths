---
concept: Isometry
slug: isometry
category: matrix-groups
subcategory: geometric-transformations
tier: intermediate
source: "Abstract Algebra: Theory and Applications"
source_slug: abs-alg-theory-applications
authors: "Thomas W. Judson"
chapter: "Matrix Groups and Symmetry"
chapter_number: 12
pdf_page: 161
section: "Symmetry"
extraction_confidence: high
aliases:
  - "rigid motion"
  - "distance-preserving map"
prerequisites:
  - euclidean-inner-product
extends: []
related:
  - euclidean-group
  - orthogonal-group
  - symmetry-group
contrasts_with: []
answers_questions:
  - "What is an isometry?"
  - "How are isometries related to matrix groups?"
---

# Quick Definition

An isometry (or rigid motion) in $\mathbb{R}^n$ is a distance-preserving function $f: \mathbb{R}^n \to \mathbb{R}^n$, meaning $\|f(\mathbf{x}) - f(\mathbf{y})\| = \|\mathbf{x} - \mathbf{y}\|$ for all $\mathbf{x}, \mathbf{y}$. Every isometry has the form $f(\mathbf{y}) = A\mathbf{y} + \mathbf{x}$ for some $A \in O(n)$.

# Core Definition

"An **isometry** or **rigid motion** in $\mathbb{R}^n$ is a distance-preserving function $f$ from $\mathbb{R}^n$ to $\mathbb{R}^n$. This means that $f$ must satisfy $\|f(\mathbf{x}) - f(\mathbf{y})\| = \|\mathbf{x} - \mathbf{y}\|$ for all $\mathbf{x}, \mathbf{y} \in \mathbb{R}^n$" (Judson, p. 161). By Lemma 12.13, an isometry fixing the origin is given by an element of $O(2)$. In general, every isometry of $\mathbb{R}^n$ has the form $f(\mathbf{y}) = A\mathbf{y} + \mathbf{x}$.

# Prerequisites

- **Euclidean inner product** — Distance is defined via the inner product

# Key Properties

1. Every isometry is injective
2. An isometry fixing the origin is a linear transformation in $O(n)$
3. The only isometries in $\mathbb{R}^2$ are rotations, reflections, translations, and glide reflections
4. The group of isometries on $\mathbb{R}^2$ is $E(2)$ (Theorem 12.14)
5. $f(\mathbf{y}) = A\mathbf{y} + \mathbf{x}$ for $A \in O(n)$, $\mathbf{x} \in \mathbb{R}^n$

# Examples

**Example 1** (p. 161): Translation $T_\mathbf{y}(\mathbf{x}) = \mathbf{x} + \mathbf{y}$ is an isometry that is not in $O(n)$.

**Example 2** (p. 161): A glide reflection is a translation followed by a reflection.

# Relationships

## Enables
- **Symmetry group** — Symmetry groups consist of isometries preserving a figure

## Related
- **Euclidean group** — $E(n)$ is the full group of isometries
- **Orthogonal group** — Isometries fixing the origin

# Source Reference

Chapter 12: Matrix Groups and Symmetry, Section 12.2, pages 161-162. Lemma 12.13, Theorem 12.14.

# Verification Notes

- Definition source: Direct quote from p. 161
- Confidence: HIGH
