---
# === CORE IDENTIFICATION ===
concept: Killing Form
slug: killing-form

# === CLASSIFICATION ===
category: structure-theory
subcategory: bilinear-forms
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 74
section: "6.6. Killing form and Cartan criterion"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "K(x,y)"
  - "Cartan-Killing form"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - invariant-bilinear-form
  - trace-form
extends:
  - trace-form
related:
  - cartan-criterion-solvability
  - cartan-criterion-semisimplicity
  - semisimple-lie-algebra
contrasts_with:
  - trace-form

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Killing form?"
  - "How does the Killing form characterize semisimplicity?"
---

# Quick Definition

The Killing form $K(x,y) = \operatorname{tr}(\operatorname{ad} x \cdot \operatorname{ad} y)$ is the trace form of the adjoint representation. It is the canonical invariant bilinear form on any Lie algebra, and its non-degeneracy is equivalent to semisimplicity.

# Core Definition

**Definition 6.34** (Kirillov, p. 74): The Killing form is the bilinear form on $\mathfrak{g}$ defined by

$$K(x,y) = \operatorname{tr}(\operatorname{ad} x \cdot \operatorname{ad} y).$$

By Proposition 6.31, the Killing form is symmetric and invariant.

# Prerequisites

- **Invariant bilinear form** — The Killing form is invariant
- **Trace form** — The Killing form is the trace form of the adjoint representation

# Key Properties

1. $K$ is symmetric: $K(x,y) = K(y,x)$
2. $K$ is invariant: $K([x,y], z) = K(x, [y,z])$
3. $K$ is non-degenerate iff $\mathfrak{g}$ is semisimple (Theorem 6.37)
4. $K([\mathfrak{g},\mathfrak{g}], \mathfrak{g}) = 0$ iff $\mathfrak{g}$ is solvable (Theorem 6.36)
5. If $I$ is an ideal in $\mathfrak{g}$, the restriction of $K^{\mathfrak{g}}$ to $I$ equals $K^I$ (Exercise 6.1)
6. If $x \in \mathfrak{z}(\mathfrak{g})$, then $K(x, \cdot) = 0$
7. For a simple algebra, $K$ is the unique invariant form up to a scalar

# Construction / Recognition

## To Compute:
1. Choose a basis $x_1, \ldots, x_n$ for $\mathfrak{g}$
2. Compute the matrices of $\operatorname{ad} x_i$ in this basis
3. $K(x_i, x_j) = \operatorname{tr}(\operatorname{ad} x_i \cdot \operatorname{ad} x_j)$

# Context & Application

The Killing form is the single most important invariant of a Lie algebra. It detects both solvability and semisimplicity, provides the mechanism for decomposing semisimple algebras into simple summands, and (when restricted to a Cartan subalgebra) defines the inner product on the root space that governs the entire classification theory.

# Examples

**Example 6.35** (p. 74): For $\mathfrak{sl}(2, \mathbb{C})$ with basis $e, h, f$: $K(h,h) = 8$, $K(e,f) = K(f,e) = 4$, $K(h,e) = K(h,f) = 0$. Thus $K(x,y) = 4\operatorname{tr}(xy)$.

**Exercise 6.2**: For $\mathfrak{sl}(n, \mathbb{C})$, $K(x,y) = 2n\operatorname{tr}(xy)$.

# Relationships

## Builds Upon
- **Trace form** — The Killing form is the trace form for $V = \mathfrak{g}$
- **Invariant bilinear form** — A specific instance

## Enables
- **Cartan criterion (solvability)** — $K([\mathfrak{g},\mathfrak{g}], \mathfrak{g}) = 0$ iff solvable
- **Cartan criterion (semisimplicity)** — Non-degeneracy iff semisimple
- **Root decomposition** — Restriction to Cartan subalgebra defines the root space geometry

## Contrasts With
- **Trace form** — The Killing form uses the adjoint representation specifically; trace forms can use any representation

# Common Errors

- **Error**: Confusing $K^{\mathfrak{h}}$ (Killing form of subalgebra) with $K^{\mathfrak{g}}|_{\mathfrak{h}}$ (restriction)
  **Correction**: These differ in general; they agree when $\mathfrak{h}$ is an ideal

# Common Confusions

- **Confusion**: Thinking non-degenerate Killing form means positive definite
  **Clarification**: Non-degeneracy (no kernel) is different from positive definiteness. For compact real forms, $K$ is negative definite.

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.6, pages 74-76. Definition 6.34, Example 6.35, Theorems 6.36, 6.37.

# Verification Notes

- Definition source: Direct from Definition 6.34
- Confidence rationale: Central definition with explicit computation and characterization theorems
- Uncertainties: None
- Cross-reference status: Verified
