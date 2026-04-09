---
# === CORE IDENTIFICATION ===
concept: Unitary Group
slug: unitary-group

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
  - "$\\mathrm{U}(n)$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - general-linear-group
extends:
  - general-linear-group
related:
  - special-unitary-group
  - orthogonal-group
  - u-n-lie-algebra
contrasts_with:
  - orthogonal-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
  - "How do I compute the Lie algebra of a matrix Lie group?"
---

# Quick Definition

$\mathrm{U}(n) = \{A \in \mathrm{GL}(n, \mathbb{C}) \mid AA^* = I\}$ is the group of unitary matrices, where $A^* = \bar{A}^t$. Its Lie algebra is $\mathfrak{u}(n) = \{x \mid x + x^* = 0\}$, the skew-Hermitian matrices.

# Core Definition

**Theorem 2.29** (Kirillov): $\exp(x) \in \mathrm{U}(n) \iff x + x^* = 0$ where $x^* = \bar{x}^t$.

# Prerequisites

- **General linear group** — $\mathrm{U}(n) \subset \mathrm{GL}(n, \mathbb{C})$

# Key Properties

1. $\dim \mathrm{U}(n) = n^2$ (as a real Lie group).
2. $\mathrm{U}(n)$ is connected ($\pi_0 = \{1\}$).
3. $\pi_1(\mathrm{U}(n)) = \mathbb{Z}$ (not simply connected).
4. $\mathrm{U}(n)$ is compact.
5. Unlike $\mathrm{O}(n)$: $x + x^* = 0$ does NOT imply $\mathrm{tr}(x) = 0$ (diagonal entries are purely imaginary). So $\mathfrak{u}(n) \neq \mathfrak{su}(n)$.

# Construction / Recognition

## To Construct/Create:
1. Take all $n \times n$ complex matrices satisfying $AA^* = I$.
2. Equivalently: matrices preserving the standard Hermitian form on $\mathbb{C}^n$.

## To Identify/Recognize:
1. Complex matrices whose columns form a unitary basis.

# Context & Application

$\mathrm{U}(n)$ is fundamental in quantum mechanics and differential geometry. Its complexification gives $\mathfrak{u}(n)_\mathbb{C} = \mathfrak{gl}(n, \mathbb{C})$ (Example 3.52).

# Examples

**Example 3.52** (p. 33): $\mathfrak{u}(n)_\mathbb{C} = \mathfrak{gl}(n, \mathbb{C})$ since any complex matrix decomposes uniquely as skew-Hermitian plus Hermitian ($= i \cdot$skew-Hermitian).

**Example** (p. 11): $\mathrm{U}(n)$ acts on $S^{2n-1} \subset \mathbb{C}^n$.

# Relationships

## Builds Upon
- **General linear group** — $\mathrm{U}(n) \subset \mathrm{GL}(n, \mathbb{C})$

## Enables
- **Special unitary group** — $\mathrm{SU}(n) = \mathrm{U}(n) \cap \mathrm{SL}(n, \mathbb{C})$

## Related
- **$\mathfrak{u}(n)$ Lie algebra** — skew-Hermitian matrices

## Contrasts With
- **Orthogonal group** — preserves real symmetric form vs. Hermitian form

# Common Errors

- **Error**: Thinking $\mathfrak{u}(n) = \mathfrak{su}(n)$ as for the orthogonal case.
  **Correction**: $\mathfrak{u}(n)$ has $n^2$ dimensions while $\mathfrak{su}(n)$ has $n^2 - 1$; the difference is the trace condition.

# Common Confusions

- **Confusion**: Whether $\mathrm{U}(n)$ is a real or complex Lie group.
  **Clarification**: $\mathrm{U}(n)$ is a real Lie group of dimension $n^2$; it is not a complex Lie group.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.5, Theorem 2.29, page 17. Tables on pp. 16-17.

# Verification Notes

- Definition source: Direct from Theorem 2.29
- Confidence rationale: Explicit computation in source
- Uncertainties: None
- Cross-reference status: Verified with tables and Example 3.52
