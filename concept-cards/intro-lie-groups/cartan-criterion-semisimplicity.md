---
# === CORE IDENTIFICATION ===
concept: Cartan Criterion for Semisimplicity
slug: cartan-criterion-semisimplicity

# === CLASSIFICATION ===
category: structure-theory
subcategory: bilinear-forms
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Structure Theory of Lie Algebras"
chapter_number: 6
pdf_page: 75
section: "6.6. Killing form and Cartan criterion"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Cartan's criterion for semisimplicity"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - killing-form
  - semisimple-lie-algebra
  - cartan-criterion-solvability
extends: []
related:
  - cartan-criterion-solvability
  - orthogonal-complement
contrasts_with:
  - cartan-criterion-solvability

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the Killing form characterize semisimplicity?"
  - "How do I determine if a Lie algebra is semisimple?"
---

# Quick Definition

The Cartan criterion for semisimplicity states that a Lie algebra is semisimple if and only if its Killing form is non-degenerate. This is the most fundamental characterization of semisimplicity.

# Core Definition

**Theorem 6.37** (Kirillov, p. 75): A Lie algebra $\mathfrak{g}$ is semisimple iff the Killing form $K(x,y) = \operatorname{tr}(\operatorname{ad} x \cdot \operatorname{ad} y)$ is non-degenerate.

# Prerequisites

- **Killing form** — The criterion is stated in terms of $K$
- **Semisimple Lie algebra** — The property being characterized
- **Cartan criterion (solvability)** — Used in the proof

# Key Properties

1. If $K$ is non-degenerate, then $\mathfrak{g}$ is reductive (by Theorem 6.32) and $\mathfrak{z}(\mathfrak{g}) = 0$ (since $\operatorname{ad} x = 0$ implies $x \in \operatorname{Ker} K$), hence semisimple
2. Conversely, if $\mathfrak{g}$ is semisimple, then $\operatorname{Ker} K$ is a solvable ideal (by Cartan solvability criterion), hence zero
3. The proof is short given the solvability criterion

# Construction / Recognition

## To Apply:
1. Choose a basis for $\mathfrak{g}$
2. Compute the Killing form matrix $K_{ij} = \operatorname{tr}(\operatorname{ad} x_i \cdot \operatorname{ad} x_j)$
3. Compute $\det(K_{ij})$
4. $\mathfrak{g}$ is semisimple iff $\det(K_{ij}) \neq 0$

# Context & Application

This is the most important single theorem of Chapter 6. It converts the abstract condition "no solvable ideals" into a concrete, computable condition (non-degeneracy of a bilinear form). It is used throughout the subsequent theory: decomposition into simples, structure of derivations, conjugacy of Cartan subalgebras, and the root decomposition.

# Examples

**Example**: For $\mathfrak{sl}(2, \mathbb{C})$, the Killing form matrix in basis $e, h, f$ is $\begin{pmatrix} 0 & 0 & 4 \\ 0 & 8 & 0 \\ 4 & 0 & 0 \end{pmatrix}$ with determinant $-128 \neq 0$, confirming semisimplicity.

# Relationships

## Builds Upon
- **Killing form** — The criterion uses the Killing form
- **Cartan criterion (solvability)** — Used to show $\operatorname{Ker} K$ is solvable

## Enables
- **Complementary ideal** — Every ideal has a complement (Theorem 6.42)
- **Decomposition into simples** — Semisimple algebras decompose into simples
- **Root decomposition** — The Killing form restricted to $\mathfrak{h}$ is non-degenerate

## Contrasts With
- **Cartan criterion (solvability)** — Solvable: $K([\mathfrak{g},\mathfrak{g}], \mathfrak{g}) = 0$; semisimple: $\operatorname{Ker} K = 0$

# Common Errors

- **Error**: Computing the Killing form of a subalgebra using traces in the larger algebra
  **Correction**: The Killing form of a subalgebra uses traces in the subalgebra. However, for ideals, the restriction of $K^{\mathfrak{g}}$ to $I$ equals $K^I$.

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.6, pages 75-76. Theorem 6.37.

# Verification Notes

- Definition source: Direct from Theorem 6.37
- Confidence rationale: Central named theorem with proof
- Uncertainties: None
- Cross-reference status: Verified
