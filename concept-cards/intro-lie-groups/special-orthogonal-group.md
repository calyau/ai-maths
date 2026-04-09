---
# === CORE IDENTIFICATION ===
concept: Special Orthogonal Group
slug: special-orthogonal-group

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
pdf_page: 16
section: "2.5"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "$\\mathrm{SO}(n, \\mathbb{K})$"
  - "rotation group"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonal-group
extends:
  - orthogonal-group
related:
  - so-3-r-lie-algebra
  - spin-group
  - special-unitary-group
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
  - "How do I compute the Lie algebra of a matrix Lie group?"
---

# Quick Definition

$\mathrm{SO}(n, \mathbb{K}) = \{A \in \mathrm{O}(n, \mathbb{K}) \mid \det A = 1\}$ is the group of rotations. It is the connected component of the identity in $\mathrm{O}(n)$ and shares the same Lie algebra $\mathfrak{so}(n) = \{x \mid x + x^t = 0\}$.

# Core Definition

**Theorem 2.29** (Kirillov): Both $\mathrm{O}(n, \mathbb{K})$ and $\mathrm{SO}(n, \mathbb{K})$ correspond to the same Lie algebra $\mathfrak{g} = \{x \mid x + x^t = 0\}$, since $x + x^t = 0$ automatically implies $\mathrm{tr}(x) = 0$ (diagonal entries are zero).

# Prerequisites

- **Orthogonal group** — $\mathrm{SO}(n)$ is the identity component

# Key Properties

1. $\dim \mathrm{SO}(n) = n(n-1)/2$.
2. $\mathrm{SO}(n, \mathbb{R})$ is connected ($\pi_0 = \{1\}$).
3. $\pi_1(\mathrm{SO}(n, \mathbb{R})) = \mathbb{Z}_2$ for $n \geq 3$; the universal cover is $\mathrm{Spin}(n)$.
4. $\mathrm{SO}(3, \mathbb{R}) \cong \mathrm{SU}(2)/\mathbb{Z}_2 \cong \mathbb{RP}^3$.

# Construction / Recognition

## To Construct/Create:
1. Take orthogonal matrices with $\det = 1$.
2. Or: the connected component of $I$ in $\mathrm{O}(n)$.

## To Identify/Recognize:
1. Orientation-preserving orthogonal transformations.

# Context & Application

$\mathrm{SO}(3, \mathbb{R})$ is the rotation group of 3-dimensional space, fundamental in physics. The relation $\mathrm{SO}(3) \cong \mathrm{SU}(2)/\mathbb{Z}_2$ connects to spinor theory.

# Examples

**Example 3.10** (p. 22): $\mathfrak{so}(3, \mathbb{R})$ has basis $J_x, J_y, J_z$ (skew-symmetric matrices); $\exp(tJ_x)$ is rotation by angle $t$ around the $x$-axis.

**Example** (p. 18-19): The morphism $\mathrm{SU}(2) \to \mathrm{SO}(3, \mathbb{R})$ via the adjoint action is a twofold cover.

# Relationships

## Builds Upon
- **Orthogonal group** — $\mathrm{SO}(n)$ is the identity component of $\mathrm{O}(n)$

## Enables
- **Spin group** — universal cover of $\mathrm{SO}(n)$
- **$\mathfrak{so}(3, \mathbb{R})$ as example** — fundamental low-dimensional example

## Related
- **$\mathrm{SU}(2)$** — double cover of $\mathrm{SO}(3)$

# Common Errors

- **Error**: Thinking $\mathrm{SO}(n)$ is simply connected.
  **Correction**: $\pi_1(\mathrm{SO}(n)) = \mathbb{Z}_2$ for $n \geq 3$; the universal cover is $\mathrm{Spin}(n)$.

# Common Confusions

- **Confusion**: Whether $\mathrm{SO}(n, \mathbb{R})$ and $\mathrm{SO}(n, \mathbb{C})$ have the same properties.
  **Clarification**: $\mathrm{SO}(n, \mathbb{R})$ is compact; $\mathrm{SO}(n, \mathbb{C})$ is not. They have different topology ($\pi_0$, $\pi_1$ differ).

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.5, Theorem 2.29, pages 16-17.

# Verification Notes

- Definition source: Direct from Theorem 2.29
- Confidence rationale: Explicit in source
- Uncertainties: None
- Cross-reference status: Verified with Section 3.10, Exercises 2.12-2.14
