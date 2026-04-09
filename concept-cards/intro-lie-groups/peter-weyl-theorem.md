---
# === CORE IDENTIFICATION ===
concept: Peter-Weyl Theorem
slug: peter-weyl-theorem

# === CLASSIFICATION ===
category: representations
subcategory: characters
tier: advanced

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of Lie Groups and Lie Algebras"
chapter_number: 4
pdf_page: 50
section: "4.7 Orthogonality of characters and Peter-Weyl theorem"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Peter-Weyl"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - orthogonality-of-matrix-coefficients
  - matrix-coefficient
  - haar-measure
extends:
  - orthogonality-of-matrix-coefficients
related:
  - orthogonality-of-characters
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How do matrix coefficients of irreducible representations relate to functions on the group?"
---

# Quick Definition

The Peter-Weyl theorem states that the matrix coefficients of all irreducible representations of a compact group $G$ form an orthonormal basis (in the Hilbert space sense) of $L^2(G)$.

# Core Definition

**Theorem 4.47** (Kirillov, p. 50): The map $m: \widehat{\bigoplus}_{V_i \in \widehat{G}} V_i^* \otimes V_i \to L^2(G, dg)$ given by $m(v^* \otimes v)(g) = \langle v^*, \rho(g)v \rangle$ is an isomorphism of Hilbert spaces, where $\widehat{\bigoplus}$ is the Hilbert space direct sum.

**Corollary 4.48** (p. 50): The set of characters $\{\chi_V \mid V \in \widehat{G}\}$ is an orthonormal basis of the space of conjugation-invariant $L^2$ functions on $G$.

# Prerequisites

- **Orthogonality of matrix coefficients** — Establishes orthogonality; Peter-Weyl adds completeness
- **Matrix coefficient** — The building blocks of the decomposition
- **Haar measure** — Defines $L^2(G)$

# Key Properties

1. Every $L^2$ function on $G$ can be expanded in matrix coefficients
2. The map $m$ preserves the $G$-bimodule structure (Theorem 4.45)
3. The map $m$ is isometric (preserves inner products)
4. For class functions, characters form the orthonormal basis

# Context & Application

Peter-Weyl is the non-abelian generalization of Fourier analysis. For $G = S^1$, it reduces to the theorem that exponentials $e^{2\pi ikx}$ form an orthonormal basis of $L^2(S^1)$. The proof requires non-trivial analysis and is not given in the text.

# Examples

**Example 4.49** (p. 50): For $G = S^1 = \mathbb{R}/\mathbb{Z}$, Peter-Weyl gives: $e^{2\pi ikx}$, $k \in \mathbb{Z}$, form an orthonormal basis of $L^2(S^1, dx)$. Every $L^2$ function has a Fourier expansion $f(x) = \sum_{k \in \mathbb{Z}} c_k e^{2\pi ikx}$.

# Relationships

## Builds Upon
- **Orthogonality of matrix coefficients** — The orthogonality half; Peter-Weyl adds completeness

## Enables
- **Harmonic analysis on groups** — Peter-Weyl is the foundation

# Source Reference

Chapter 4, Section 4.7, Theorems 4.45, 4.47, Corollaries 4.46, 4.48, pp. 49-50.

# Verification Notes

- Definition source: Direct from Theorem 4.47
- Confidence rationale: Explicit theorem statement (proof not given, referenced to other sources)
- Uncertainties: None
- Cross-reference status: Verified
