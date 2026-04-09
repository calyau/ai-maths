---
# === CORE IDENTIFICATION ===
concept: Symplectic Group
slug: symplectic-group

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
  - "$\\mathrm{Sp}(2n, \\mathbb{K})$"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - general-linear-group
extends:
  - general-linear-group
related:
  - orthogonal-group
  - compact-symplectic-group
contrasts_with:
  - orthogonal-group

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do the classical groups relate to each other?"
  - "How do I compute the Lie algebra of a matrix Lie group?"
---

# Quick Definition

$\mathrm{Sp}(2n, \mathbb{K}) = \{A \in \mathrm{GL}(2n, \mathbb{K}) \mid \omega(Ax, Ay) = \omega(x, y)\}$ is the group preserving the standard skew-symmetric bilinear form $\omega$. Its Lie algebra is $\mathfrak{sp}(2n, \mathbb{K}) = \{x \mid x + Jx^tJ^{-1} = 0\}$.

# Core Definition

**Section 2.5** (Kirillov): $\mathrm{Sp}(2n, \mathbb{K}) = \{A: \mathbb{K}^{2n} \to \mathbb{K}^{2n} \mid \omega(Ax, Ay) = \omega(x, y)\}$, where $\omega(x, y) = \sum_{i=1}^n x_i y_{i+n} - y_i x_{i+n}$, equivalently $\omega(x, y) = (Jx, y)$ with $J = \begin{pmatrix} 0 & -I_n \\ I_n & 0 \end{pmatrix}$.

**Theorem 2.29**: $\exp(x) \in \mathrm{Sp}(2n, \mathbb{K}) \iff x + Jx^tJ^{-1} = 0$.

# Prerequisites

- **General linear group** — $\mathrm{Sp}(2n) \subset \mathrm{GL}(2n)$

# Key Properties

1. $\dim \mathrm{Sp}(2n, \mathbb{K}) = n(2n + 1)$.
2. $\mathrm{Sp}(2n, \mathbb{R})$ is connected ($\pi_0 = \{1\}$) with $\pi_1 = \mathbb{Z}$.
3. $\mathrm{Sp}(2n)$ preserves the non-degenerate skew-symmetric form $\omega$.

# Construction / Recognition

## To Construct/Create:
1. Take $2n \times 2n$ matrices preserving the standard symplectic form $\omega$.
2. Equivalently: $A^t J A = J$.

## To Identify/Recognize:
1. Linear transformations preserving a non-degenerate skew-symmetric bilinear form.

# Context & Application

The symplectic group appears in Hamiltonian mechanics (symplectomorphisms of phase space) and in the theory of quadratic forms. It is one of the three infinite families of classical groups.

# Examples

**Example** (p. 14-15): $\omega(x, y) = (Jx, y)$ with $J = \begin{pmatrix} 0 & -I_n \\ I_n & 0 \end{pmatrix}$.

**Example** (Exercise 2.7): The compact group $\mathrm{Sp}(n) = \mathrm{Sp}(2n, \mathbb{C}) \cap \mathrm{SU}(2n)$ is a compact real form of $\mathrm{Sp}(2n, \mathbb{C})$ (Exercise 3.16).

# Relationships

## Builds Upon
- **General linear group** — $\mathrm{Sp}(2n) \subset \mathrm{GL}(2n)$

## Enables
- **Compact symplectic group** — $\mathrm{Sp}(n) = \mathrm{Sp}(2n, \mathbb{C}) \cap \mathrm{SU}(2n)$

## Related
- **Orthogonal group** — preserves symmetric form (contrast with skew-symmetric)
- **Example 3.29** — general framework for symmetry groups of bilinear forms

## Contrasts With
- **Orthogonal group** — preserves symmetric bilinear form, not skew-symmetric

# Common Errors

- **Error**: Confusing $\mathrm{Sp}(2n, \mathbb{K})$ with $\mathrm{Sp}(n)$ (the compact symplectic group).
  **Correction**: Notation varies between books. Kirillov uses $\mathrm{Sp}(2n, \mathbb{K})$ for the full symplectic group and $\mathrm{Sp}(n)$ for the compact form (Remark 2.27).

# Common Confusions

- **Confusion**: Whether the symplectic group requires even-dimensional space.
  **Clarification**: Yes, a non-degenerate skew-symmetric bilinear form can only exist on even-dimensional spaces.

# Source Reference

Chapter 2: Lie Groups: Basic Definitions, Section 2.5, pages 14-15, 17. Theorem 2.29, Remark 2.27.

# Verification Notes

- Definition source: Direct from Section 2.5 and Theorem 2.29
- Confidence rationale: Explicit in source
- Uncertainties: None
- Cross-reference status: Verified with Remark 2.27, Exercises 2.7, 3.16
