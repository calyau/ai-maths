---
# === CORE IDENTIFICATION ===
concept: General Linear Group
slug: general-linear-group

# === CLASSIFICATION ===
category: lie-groups
subcategory: classical-groups
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups: Basic Definitions"
chapter_number: 2
pdf_page: 14
section: "2.5"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\mathrm{GL}(n, \\mathbb{K})$"
  - "invertible matrices"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-group
extends: []
related:
  - special-linear-group
  - orthogonal-group
  - unitary-group
  - symplectic-group
  - gl-n-lie-algebra
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
  - "How do I compute the Lie algebra of a matrix Lie group?"
---

# Quick Definition

The general linear group $\mathrm{GL}(n, \mathbb{K})$ is the group of all invertible $n \times n$ matrices over $\mathbb{K}$ ($= \mathbb{R}$ or $\mathbb{C}$). It is the prototypical Lie group from which all classical groups are obtained as subgroups.

# Core Definition

(Kirillov, p. 14-15): $\mathrm{GL}(n, \mathbb{K})$ is the group of invertible $n \times n$ matrices over $\mathbb{K}$. Its Lie algebra is $\mathfrak{gl}(n, \mathbb{K})$, the space of all $n \times n$ matrices.

# Prerequisites

- **Lie group** — $\mathrm{GL}(n, \mathbb{K})$ is the fundamental example

# Key Properties

1. $\mathrm{GL}(n, \mathbb{K})$ is an open subset of $\mathbb{K}^{n^2}$, hence a manifold of dimension $n^2$ (over $\mathbb{R}$) or $2n^2$ (over $\mathbb{R}$ when $\mathbb{K} = \mathbb{C}$).
2. Lie algebra: $\mathfrak{gl}(n, \mathbb{K})$ = all $n \times n$ matrices, with bracket $[x, y] = xy - yx$.
3. $\dim \mathrm{GL}(n, \mathbb{R}) = n^2$.
4. $\pi_0(\mathrm{GL}(n, \mathbb{R})) = \mathbb{Z}_2$ (positive vs. negative determinant); $\pi_0(\mathrm{GL}(n, \mathbb{C})) = \{1\}$.
5. $\pi_1(\mathrm{GL}(n, \mathbb{R})) = \mathbb{Z}_2$ for $n \geq 3$; $\pi_1(\mathrm{GL}(n, \mathbb{C})) = \mathbb{Z}$.

# Construction / Recognition

## To Construct/Create:
1. Take all $n \times n$ matrices with nonzero determinant.

## To Identify/Recognize:
1. The group of all invertible linear transformations of $\mathbb{K}^n$.

# Context & Application

$\mathrm{GL}(n, \mathbb{K})$ is the ambient group for all classical matrix groups. The exponential map $\exp: \mathfrak{gl}(n) \to \mathrm{GL}(n)$ is defined by the matrix power series.

# Examples

**Example** (p. 15): $\exp(x) = \sum_{k=0}^\infty \frac{x^k}{k!}$ defines a map $\mathfrak{gl}(n, \mathbb{K}) \to \mathrm{GL}(n, \mathbb{K})$, and $\log(1 + x) = \sum_{k=1}^\infty \frac{(-1)^{k+1} x^k}{k}$ is its local inverse.

# Relationships

## Builds Upon
- **Lie group** — $\mathrm{GL}(n)$ is the prototypical Lie group

## Enables
- **Special linear group** — $\mathrm{SL}(n) = \ker(\det)$ inside $\mathrm{GL}(n)$
- **All classical groups** — defined as subgroups of $\mathrm{GL}(n)$
- **Matrix exponential** — defined on $\mathfrak{gl}(n)$

## Related
- **$\mathfrak{gl}(n)$ Lie algebra** — tangent space at identity

# Common Errors

- **Error**: Forgetting that $\mathrm{GL}(n, \mathbb{R})$ is not connected.
  **Correction**: It has two connected components, distinguished by the sign of the determinant.

# Common Confusions

- **Confusion**: Whether $\mathrm{GL}(n, \mathbb{C})$ is a real or complex Lie group.
  **Clarification**: It is naturally a complex Lie group of complex dimension $n^2$, but can also be viewed as a real Lie group of real dimension $2n^2$.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.5, pages 14-17. Theorem 2.29, table on p. 16-17.

# Verification Notes

- Definition source: Direct from source
- Confidence rationale: Explicit in source with full details
- Uncertainties: None
- Cross-reference status: Verified with tables on pp. 16-17
