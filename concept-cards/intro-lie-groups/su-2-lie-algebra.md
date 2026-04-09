---
# === CORE IDENTIFICATION ===
concept: "Lie Algebra $\\mathfrak{su}(2)$"
slug: su-2-lie-algebra

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
  - "$\\mathfrak{su}(2)$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - special-unitary-group
  - lie-algebra
extends: []
related:
  - so-3-r-lie-algebra
  - sl-2-c-lie-algebra
  - complexification
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
  - "How do I compute the Lie algebra of a matrix Lie group?"
---

# Quick Definition

$\mathfrak{su}(2)$ is the 3-dimensional real Lie algebra of traceless skew-Hermitian $2 \times 2$ matrices. A basis is $i\sigma_1, i\sigma_2, i\sigma_3$ (Pauli matrices times $i$) with $[i\sigma_1, i\sigma_2] = 2i\sigma_3$ (cyclic).

# Core Definition

**Equation (3.18)** (Kirillov): A basis of $\mathfrak{su}(2)$ is:
$$i\sigma_1 = \begin{pmatrix}0&1\\-1&0\end{pmatrix}, \quad i\sigma_2 = \begin{pmatrix}0&i\\i&0\end{pmatrix}, \quad i\sigma_3 = \begin{pmatrix}i&0\\0&-i\end{pmatrix}$$

Commutation relations: $[i\sigma_1, i\sigma_2] = 2i\sigma_3$, $[i\sigma_2, i\sigma_3] = 2i\sigma_1$, $[i\sigma_3, i\sigma_1] = 2i\sigma_2$.

# Prerequisites

- **Special unitary group** — $\mathfrak{su}(2) = \mathrm{Lie}(\mathrm{SU}(2))$
- **Lie algebra** — abstract definition

# Key Properties

1. $\dim_\mathbb{R} \mathfrak{su}(2) = 3$.
2. $\mathfrak{su}(2) \cong \mathfrak{so}(3, \mathbb{R})$ via $i\sigma_k \mapsto 2J_k$.
3. $\mathfrak{su}(2)_\mathbb{C} \cong \mathfrak{sl}(2, \mathbb{C})$ (equation 3.23).
4. Invariant form: $(x, y) = -\mathrm{tr}(xy) = \mathrm{tr}(x\bar{y}^t)$, positive definite.
5. $\mathfrak{su}(2)$ is the compact real form of $\mathfrak{sl}(2, \mathbb{C})$.

# Construction / Recognition

## To Construct/Create:
1. Take $2 \times 2$ traceless skew-Hermitian matrices: $\{x \mid x + x^* = 0, \mathrm{tr}(x) = 0\}$.

## To Identify/Recognize:
1. A 3-dimensional real Lie algebra with bracket $[e_i, e_j] = 2\epsilon_{ijk} e_k$.

# Context & Application

$\mathfrak{su}(2)$ is the simplest non-abelian compact Lie algebra and is fundamental in quantum mechanics (spin). Its complexification $\mathfrak{sl}(2, \mathbb{C})$ is the starting point for the representation theory of all semisimple Lie algebras.

# Examples

**Example** (p. 34, eq. 3.23): The complexification map $\mathfrak{su}(2) \hookrightarrow \mathfrak{sl}(2, \mathbb{C})$:
$i\sigma_1 \mapsto e - f$, $i\sigma_2 \mapsto i(e+f)$, $i\sigma_3 \mapsto ih$.

**Example** (p. 18, Exercise 2.12): The adjoint representation of $\mathrm{SU}(2)$ on $\mathfrak{su}(2) \cong \mathbb{R}^3$ gives the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3, \mathbb{R})$.

# Relationships

## Builds Upon
- **Special unitary group** — $\mathfrak{su}(2) = \mathrm{Lie}(\mathrm{SU}(2))$

## Enables
- **Representation theory of $\mathfrak{sl}(2, \mathbb{C})$** — via complexification
- **Understanding of spin** — in physics

## Related
- **$\mathfrak{so}(3, \mathbb{R})$** — isomorphic Lie algebra
- **$\mathfrak{sl}(2, \mathbb{C})$** — complexification

# Common Errors

- **Error**: Using the Pauli matrices $\sigma_k$ directly as basis of $\mathfrak{su}(2)$.
  **Correction**: The Pauli matrices are Hermitian, not skew-Hermitian. The basis of $\mathfrak{su}(2)$ is $i\sigma_k$.

# Common Confusions

- **Confusion**: Whether $\mathrm{SU}(2)$ and $\mathrm{SO}(3)$ have the same Lie algebra.
  **Clarification**: Yes, $\mathfrak{su}(2) \cong \mathfrak{so}(3, \mathbb{R})$ as abstract Lie algebras. But $\mathrm{SU}(2)$ and $\mathrm{SO}(3)$ are not isomorphic as groups ($\mathrm{SU}(2)$ is simply connected).

# Source Reference

Chapter 3: Lie Groups and Lie Algebras, Section 3.10, equations (3.18)-(3.19), (3.23), pages 34-35.

# Verification Notes

- Definition source: Direct from equations (3.18)-(3.19)
- Confidence rationale: Explicit basis and relations
- Uncertainties: None
- Cross-reference status: Verified with isomorphism maps
