---
# === CORE IDENTIFICATION ===
concept: Matrix Exponential
slug: matrix-exponential

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
pdf_page: 15
section: "2.5"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "exponential of a matrix"
  - "$\\exp(x)$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - general-linear-group
extends: []
related:
  - exponential-map
  - one-parameter-subgroup
  - logarithmic-map
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the exponential map?"
  - "How do I use the exponential map to go between Lie group and Lie algebra?"
  - "How do I compute the Lie algebra of a matrix Lie group?"
---

# Quick Definition

The matrix exponential $\exp(x) = \sum_{k=0}^\infty \frac{x^k}{k!}$ maps $\mathfrak{gl}(n, \mathbb{K})$ to $\mathrm{GL}(n, \mathbb{K})$. It is the concrete realization of the exponential map for matrix Lie groups.

# Core Definition

**Equation (2.4)** (Kirillov): $\exp(x) = \sum_{k=0}^\infty \frac{x^k}{k!}$.

The logarithmic map is defined by **Equation (2.5)**: $\log(1 + x) = \sum_{k=1}^\infty \frac{(-1)^{k+1} x^k}{k}$, defined in a neighborhood of $1 \in \mathrm{GL}(n)$.

# Prerequisites

- **General linear group** — domain and codomain of exp

# Key Properties

1. $\log(\exp(x)) = x$ and $\exp(\log(X)) = X$ when defined (Theorem 2.28).
2. $\exp(0) = I$ and $d\exp(0) = \mathrm{id}$ (Theorem 2.28 part 2).
3. If $xy = yx$ then $\exp(x+y) = \exp(x)\exp(y)$ (Theorem 2.28 part 3).
4. $\exp(x)\exp(-x) = I$, so $\exp(x) \in \mathrm{GL}(n)$ always.
5. $\exp(AxA^{-1}) = A\exp(x)A^{-1}$ and $\exp(x^t) = (\exp(x))^t$ (Theorem 2.28 part 5).
6. $\det \exp(x) = \exp(\mathrm{tr}(x))$.

# Construction / Recognition

## To Construct/Create:
1. Compute the power series $\sum_{k=0}^\infty x^k/k!$ for a matrix $x$.
2. This always converges for any $n \times n$ matrix.

## To Identify/Recognize:
1. Any matrix of the form $\exp(x)$ for some $x \in \mathfrak{gl}(n)$.

# Context & Application

The matrix exponential is the key tool for showing that classical groups are Lie groups (Theorem 2.29). It identifies neighborhoods of the identity in $G$ with neighborhoods of $0$ in $\mathfrak{g}$, providing local coordinates.

# Examples

**Example** (p. 16): $\exp(x) \in \mathrm{SL}(n) \iff \mathrm{tr}(x) = 0$ (since $\det \exp(x) = \exp(\mathrm{tr}(x))$).

**Example** (p. 16): $\exp(x) \in \mathrm{O}(n) \iff x + x^t = 0$.

**Example 3.10** (p. 22): $\exp(tJ_x) = \begin{pmatrix} 1 & 0 & 0 \\ 0 & \cos t & -\sin t \\ 0 & \sin t & \cos t \end{pmatrix}$ is rotation around the $x$-axis.

# Relationships

## Builds Upon
- **General linear group** — $\exp: \mathfrak{gl}(n) \to \mathrm{GL}(n)$

## Enables
- **Classical group theorem** — proves classical groups are Lie groups
- **One-parameter subgroup** — $t \mapsto \exp(tx)$ is a one-parameter subgroup
- **Exponential map** — the matrix exponential is the special case for matrix groups

## Related
- **Logarithmic map** — local inverse of exp

# Common Errors

- **Error**: Assuming $\exp(x+y) = \exp(x)\exp(y)$ always.
  **Correction**: This holds only when $xy = yx$. In general, $\exp(x)\exp(y) = \exp(x + y + \frac{1}{2}[x,y] + \cdots)$ (Campbell-Hausdorff).

# Common Confusions

- **Confusion**: Whether the matrix exponential is always surjective.
  **Clarification**: It is not always surjective (Exercise 3.1: $\begin{pmatrix}-1 & 1\\0 & -1\end{pmatrix} \notin \mathrm{Im}(\exp)$ in $\mathrm{SL}(2, \mathbb{R})$). However, it is surjective for compact groups.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.5, equations (2.4)-(2.5), Theorem 2.28, pages 15-16.

# Verification Notes

- Definition source: Direct from equations (2.4)-(2.5)
- Confidence rationale: Explicit formulas and theorem
- Uncertainties: None
- Cross-reference status: Verified with Theorem 2.28, 2.29, Exercise 3.1
