---
# === CORE IDENTIFICATION ===
concept: "Standard Basis of sl(2,C)"
slug: sl2-standard-basis

# === CLASSIFICATION ===
category: representations
subcategory: basic-definitions
tier: foundational

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of sl(2,C) and Spherical Laplace Operator"
chapter_number: 5
pdf_page: 58
section: "5.1 Representations of sl(2,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "e, f, h basis"
  - "Chevalley basis of sl(2)"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
extends: []
related:
  - weight-for-sl2
  - raising-and-lowering-operators
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the standard basis of sl(2,C)?"
  - "How does sl(2,C) serve as a building block for semisimple Lie algebras?"
---

# Quick Definition

The Lie algebra $\mathfrak{sl}(2,\mathbb{C})$ has a standard basis $\{e, f, h\}$ with commutation relations $[e,f] = h$, $[h,e] = 2e$, $[h,f] = -2f$. This is the simplest non-abelian semisimple Lie algebra.

# Core Definition

(Kirillov, p. 58, referring to Section 3.10): $\mathfrak{sl}(2,\mathbb{C})$ has a basis $e, f, h$ with commutation relations:

$$[e, f] = h, \quad [h, e] = 2e, \quad [h, f] = -2f$$

This Lie algebra is simple (Example 6.22).

# Prerequisites

- **Lie algebra** — $\mathfrak{sl}(2,\mathbb{C})$ is the fundamental example

# Key Properties

1. $h$ is the Cartan (diagonal) element; $e$ is the raising operator; $f$ is the lowering operator
2. $h$ acts diagonally in any finite-dimensional representation (Theorem 5.3)
3. $[h,e] = 2e$ means $e$ raises $h$-eigenvalues by 2
4. $[h,f] = -2f$ means $f$ lowers $h$-eigenvalues by 2
5. $\mathfrak{sl}(2,\mathbb{C})$ is simple (and therefore semisimple)

# Context & Application

$\mathfrak{sl}(2,\mathbb{C})$ is the fundamental building block of all semisimple Lie algebras. Every root of a semisimple Lie algebra determines an $\mathfrak{sl}(2)$-subalgebra. Understanding $\mathfrak{sl}(2,\mathbb{C})$ representations is the first step toward the general theory.

# Examples

**As matrices**: $e = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $f = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$, $h = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$ (Section 3.10).

# Relationships

## Enables
- **Weight theory for sl(2,C)** — $h$ defines weights
- **Raising and lowering operators** — $e$ and $f$

# Source Reference

Chapter 5, Section 5.1, p. 58; Section 3.10, p. 34.

# Verification Notes

- Definition source: Direct from p. 58 (referring to Section 3.10)
- Confidence rationale: Standard and explicit
- Uncertainties: None
- Cross-reference status: Verified
