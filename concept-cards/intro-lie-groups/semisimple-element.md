---
# === CORE IDENTIFICATION ===
concept: Semisimple Element
slug: semisimple-element

# === CLASSIFICATION ===
category: root-systems
subcategory: abstract-root-systems
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Complex Semisimple Lie Algebras"
chapter_number: 7
pdf_page: 82
section: "7.1. Semisimple elements and toroidal subalgebras"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "diagonalizable element"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - semisimple-lie-algebra
extends: []
related:
  - nilpotent-element
  - jordan-decomposition-lie-algebras
  - toroidal-subalgebra
contrasts_with:
  - nilpotent-element

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is a semisimple element of a Lie algebra?"
  - "How do semisimple elements relate to the structure of semisimple Lie algebras?"
---

# Quick Definition

An element $x \in \mathfrak{g}$ is semisimple if $\operatorname{ad} x\colon \mathfrak{g} \to \mathfrak{g}$ is a semisimple (diagonalizable) operator. Semisimple elements form the Cartan subalgebra and their eigenvalues define the root decomposition.

# Core Definition

**Definition 7.1** (Kirillov, p. 82): An element $x \in \mathfrak{g}$ is called semisimple if $\operatorname{ad} x$ is a semisimple operator $\mathfrak{g} \to \mathfrak{g}$.

For $\mathfrak{g} = \mathfrak{gl}(n, \mathbb{C})$, this coincides with the usual definition of a diagonalizable matrix (Exercise 7.1).

# Prerequisites

- **Semisimple Lie algebra** — The definition is used primarily in this context

# Key Properties

1. In any semisimple complex Lie algebra, nonzero semisimple elements exist (Corollary 7.4)
2. If $x$ is semisimple in $\mathfrak{g}$, then $\rho(x)$ is semisimple in any representation $V$ (Theorem 7.5)
3. A commutative subalgebra of semisimple elements is called toroidal

# Construction / Recognition

## To Identify:
1. Compute $\operatorname{ad} x$ as a linear operator on $\mathfrak{g}$
2. Check if $\operatorname{ad} x$ is diagonalizable (all eigenspaces span $\mathfrak{g}$)

# Context & Application

Semisimple elements are the starting point for Chapter 7. Their eigenvalues under $\operatorname{ad}$ define the root decomposition, which is the fundamental structure for classification. The key insight from $\mathfrak{sl}(2, \mathbb{C})$ — that $h$ generates weight decompositions — generalizes via semisimple elements.

# Examples

**Corollary 7.4** (p. 83): Every semisimple complex Lie algebra contains nonzero semisimple elements. If all semisimple elements were zero, every element would be nilpotent, and by Engel's theorem $\mathfrak{g}$ would be nilpotent — contradicting semisimplicity.

**Example**: In $\mathfrak{sl}(n, \mathbb{C})$, diagonal traceless matrices are semisimple elements.

# Relationships

## Enables
- **Toroidal subalgebra** — Commutative subalgebras of semisimple elements
- **Root decomposition** — Eigenvalues of semisimple elements become roots

## Contrasts With
- **Nilpotent element** — An element with $\operatorname{ad} x$ nilpotent; every element decomposes as $x_s + x_n$

# Common Confusions

- **Confusion**: Confusing "semisimple element" with "element of a semisimple algebra"
  **Clarification**: Not every element of a semisimple algebra is semisimple. The Jordan decomposition splits each element into semisimple and nilpotent parts.

# Source Reference

Chapter 7: Complex Semisimple Lie Algebras, Section 7.1, pages 82-83. Definition 7.1, Corollary 7.4.

# Verification Notes

- Definition source: Direct from Definition 7.1
- Confidence rationale: Explicitly defined
- Uncertainties: None
- Cross-reference status: Verified
