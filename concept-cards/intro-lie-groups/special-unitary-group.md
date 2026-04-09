---
# === CORE IDENTIFICATION ===
concept: Special Unitary Group
slug: special-unitary-group

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
pdf_page: 17
section: "2.5"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\mathrm{SU}(n)$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - unitary-group
  - special-linear-group
extends:
  - unitary-group
related:
  - su-2-lie-algebra
  - special-orthogonal-group
  - compact-real-form
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
  - "How do I compute the Lie algebra of a matrix Lie group?"
---

# Quick Definition

$\mathrm{SU}(n) = \{A \in \mathrm{U}(n) \mid \det A = 1\}$ is the group of special unitary matrices. Its Lie algebra is $\mathfrak{su}(n) = \{x \mid x + x^* = 0, \mathrm{tr}(x) = 0\}$, the traceless skew-Hermitian matrices.

# Core Definition

**Theorem 2.29** (Kirillov): $\exp(x) \in \mathrm{SU}(n) \iff x + x^* = 0$ and $\mathrm{tr}(x) = 0$.

# Prerequisites

- **Unitary group** — $\mathrm{SU}(n) \subset \mathrm{U}(n)$
- **Special linear group** — $\mathrm{SU}(n) = \mathrm{U}(n) \cap \mathrm{SL}(n, \mathbb{C})$

# Key Properties

1. $\dim \mathrm{SU}(n) = n^2 - 1$.
2. $\mathrm{SU}(n)$ is connected and simply connected for $n \geq 2$ ($\pi_0 = \pi_1 = \{1\}$).
3. $\mathrm{SU}(n)$ is compact.
4. $\mathrm{SU}(2) \cong S^3$ as a manifold (Example 2.3).
5. $\mathrm{SU}(n)$ is a compact real form of $\mathrm{SL}(n, \mathbb{C})$ (Example 3.54).

# Construction / Recognition

## To Construct/Create:
1. Take unitary matrices with determinant 1.

## To Identify/Recognize:
1. Unitary matrices with unit determinant.

# Context & Application

$\mathrm{SU}(n)$ is the prototypical compact simply-connected semisimple Lie group. $\mathrm{SU}(2)$ is especially important as the double cover of $\mathrm{SO}(3)$ and the simplest non-abelian compact Lie group. Being simply connected, representations of $\mathrm{SU}(n)$ are in bijection with representations of $\mathfrak{su}(n)$.

# Examples

**Example 2.3** (p. 8): $\mathrm{SU}(2) = \left\{\begin{pmatrix} \alpha & \beta \\ -\bar{\beta} & \bar{\alpha}\end{pmatrix} : |\alpha|^2 + |\beta|^2 = 1\right\} \cong S^3$.

**Example 3.54** (p. 34): $\mathrm{SU}(n)$ is a compact real form of $\mathrm{SL}(n, \mathbb{C})$.

**Example** (p. 18): The adjoint action of $\mathrm{SU}(2)$ on $\mathfrak{su}(2)$ gives the double cover $\mathrm{SU}(2) \to \mathrm{SO}(3, \mathbb{R})$.

# Relationships

## Builds Upon
- **Unitary group** — $\mathrm{SU}(n) \subset \mathrm{U}(n)$

## Enables
- **$\mathfrak{su}(2)$ Lie algebra** — the fundamental low-dimensional example
- **Compact real form** — $\mathrm{SU}(n)$ is a compact real form of $\mathrm{SL}(n, \mathbb{C})$

## Related
- **$\mathrm{SO}(3, \mathbb{R})$** — $\mathrm{SU}(2)/\mathbb{Z}_2 \cong \mathrm{SO}(3, \mathbb{R})$

# Common Errors

- **Error**: Thinking $\mathrm{SU}(n)$ is a complex Lie group.
  **Correction**: $\mathrm{SU}(n)$ is a real Lie group. Its complexification gives $\mathrm{SL}(n, \mathbb{C})$.

# Common Confusions

- **Confusion**: Whether $\mathrm{SU}(2)$ and $\mathrm{SO}(3)$ are isomorphic.
  **Clarification**: They are not isomorphic as Lie groups; $\mathrm{SU}(2)$ is a double cover of $\mathrm{SO}(3)$. They have isomorphic Lie algebras.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.5, Theorem 2.29, page 17. Example 2.3 p. 8.

# Verification Notes

- Definition source: Direct from Theorem 2.29 and Example 2.3
- Confidence rationale: Explicit in source
- Uncertainties: None
- Cross-reference status: Verified with Example 3.54, Exercises 2.12-2.14
