---
# === CORE IDENTIFICATION ===
concept: "Lie Algebra $\\mathfrak{so}(3, \\mathbb{R})$"
slug: so-3-r-lie-algebra

# === CLASSIFICATION ===
category: lie-algebras
subcategory: examples
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Lie Groups and Lie Algebras"
chapter_number: 3
pdf_page: 34
section: "3.10"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\mathfrak{so}(3)$"
  - "rotation algebra"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - special-orthogonal-group
  - lie-algebra
extends: []
related:
  - su-2-lie-algebra
  - sl-2-c-lie-algebra
  - complexification
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
  - "How do I compute the Lie algebra of a matrix Lie group?"
---

# Quick Definition

$\mathfrak{so}(3, \mathbb{R})$ is the 3-dimensional real Lie algebra of skew-symmetric $3 \times 3$ matrices, with basis $J_x, J_y, J_z$ satisfying $[J_x, J_y] = J_z$, $[J_y, J_z] = J_x$, $[J_z, J_x] = J_y$.

# Core Definition

**Section 3.10** (Kirillov): A basis in $\mathfrak{so}(3, \mathbb{R})$ is given by:
$$J_x = \begin{pmatrix}0&0&0\\0&0&-1\\0&1&0\end{pmatrix}, \quad J_y = \begin{pmatrix}0&0&1\\0&0&0\\-1&0&0\end{pmatrix}, \quad J_z = \begin{pmatrix}0&-1&0\\1&0&0\\0&0&0\end{pmatrix}$$

Commutation relations: $[J_x, J_y] = J_z$, $[J_y, J_z] = J_x$, $[J_z, J_x] = J_y$.

# Prerequisites

- **Special orthogonal group** — $\mathfrak{so}(3, \mathbb{R})$ is its Lie algebra
- **Lie algebra** — abstract definition

# Key Properties

1. $\dim \mathfrak{so}(3, \mathbb{R}) = 3$.
2. The one-parameter subgroups $\exp(tJ_x)$, $\exp(tJ_y)$, $\exp(tJ_z)$ are rotations around coordinate axes.
3. $\mathfrak{so}(3, \mathbb{R}) \cong \mathfrak{su}(2)$ as Lie algebras (via $i\sigma_k \mapsto 2J_k$).
4. $\mathfrak{so}(3, \mathbb{R})_\mathbb{C} = \mathfrak{so}(3, \mathbb{C}) \cong \mathfrak{sl}(2, \mathbb{C})$.
5. Isomorphic to $(\mathbb{R}^3, \times)$ (cross product, Exercise 3.5).
6. Invariant bilinear form: $(x, y) = -\mathrm{tr}(xy) = \mathrm{tr}(xy^t)$, positive definite.

# Construction / Recognition

## To Construct/Create:
1. Take $3 \times 3$ skew-symmetric real matrices.
2. Bracket is $[x, y] = xy - yx$.

## To Identify/Recognize:
1. A 3-dimensional real Lie algebra with $[e_1, e_2] = e_3$, $[e_2, e_3] = e_1$, $[e_3, e_1] = e_2$.

# Context & Application

$\mathfrak{so}(3, \mathbb{R})$ is the infinitesimal rotation algebra, fundamental in classical mechanics and physics. It is isomorphic to $\mathfrak{su}(2)$, which connects to quantum mechanics.

# Examples

**Example 3.10** (p. 22): $\exp(tJ_x) = \begin{pmatrix}1&0&0\\0&\cos t&-\sin t\\0&\sin t&\cos t\end{pmatrix}$ is rotation by $t$ around the $x$-axis.

**Example** (Exercise 3.5): The cross product $\vec{a} \times \vec{b}$ in $\mathbb{R}^3$ gives $\mathbb{R}^3$ the same Lie algebra structure as $\mathfrak{so}(3, \mathbb{R})$.

# Relationships

## Builds Upon
- **Special orthogonal group** — $\mathfrak{so}(3) = \mathrm{Lie}(\mathrm{SO}(3))$

## Enables
- **Understanding of $\mathfrak{sl}(2, \mathbb{C})$** — via complexification

## Related
- **$\mathfrak{su}(2)$** — isomorphic as Lie algebras
- **$\mathfrak{sl}(2, \mathbb{C})$** — complexification

# Common Errors

- **Error**: Confusing $\mathfrak{so}(3, \mathbb{R})$ with its complexification $\mathfrak{so}(3, \mathbb{C})$.
  **Correction**: $\mathfrak{so}(3, \mathbb{R})$ is a 3-dimensional real algebra; $\mathfrak{so}(3, \mathbb{C})$ is 3-dimensional over $\mathbb{C}$ (= 6-dimensional over $\mathbb{R}$).

# Common Confusions

- **Confusion**: Whether $\mathfrak{so}(3)$ and $\mathfrak{su}(2)$ are "the same."
  **Clarification**: They are isomorphic as abstract Lie algebras. But they sit differently inside matrix algebras: $\mathfrak{so}(3) \subset \mathfrak{gl}(3, \mathbb{R})$ and $\mathfrak{su}(2) \subset \mathfrak{gl}(2, \mathbb{C})$.

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.10, equations (3.16)-(3.17), pages 34-35.

# Verification Notes

- Definition source: Direct from Section 3.10
- Confidence rationale: Explicit basis and relations
- Uncertainties: None
- Cross-reference status: Verified with Example 3.10, Exercise 3.5
