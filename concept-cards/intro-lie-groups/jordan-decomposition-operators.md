---
# === CORE IDENTIFICATION ===
concept: Jordan Decomposition for Operators
slug: jordan-decomposition-operators

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
  - "Jordan-Chevalley decomposition"
  - "semisimple-nilpotent decomposition"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - lie-algebra
extends: []
related:
  - cartan-criterion-solvability
  - semisimple-element
  - jordan-decomposition-lie-algebras
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "What is the Jordan decomposition of a linear operator?"
  - "How is the Jordan decomposition used in the Cartan criterion proof?"
---

# Quick Definition

The Jordan decomposition writes any linear operator $A$ uniquely as $A = A_s + A_n$ where $A_s$ is semisimple (diagonalizable), $A_n$ is nilpotent, and they commute. This is the technical foundation for the Cartan criteria and the theory of semisimple elements.

# Core Definition

**Theorem 6.38** (Kirillov, p. 75): Let $V$ be a finite-dimensional complex vector space.
1. Any $A \in \operatorname{End}(V)$ can be uniquely written as $A = A_s + A_n$ with $A_s$ semisimple, $A_n$ nilpotent, and $[A_s, A_n] = 0$.
2. $(\operatorname{ad} A)_s = \operatorname{ad} A_s$ and $\operatorname{ad} A_s = P(\operatorname{ad} A)$ for some polynomial $P \in t\mathbb{C}[t]$.
3. The conjugate semisimple part $\bar{A}_s$ (same eigenspaces, conjugate eigenvalues) satisfies $\operatorname{ad} \bar{A}_s = Q(\operatorname{ad} A)$ for some polynomial $Q$.

# Prerequisites

- **Lie algebra** — Used in the adjoint representation context

# Key Properties

1. $A_s$ and $A_n$ are polynomials in $A$ (without constant term)
2. The semisimple part of $\operatorname{ad} A$ is $\operatorname{ad}$ of the semisimple part of $A$
3. Part (3) is crucial for the Cartan solvability criterion proof

# Context & Application

The Jordan decomposition is the key technical tool for proving the Cartan criteria. Part (3) about the conjugate semisimple part is used to show that if $K([\mathfrak{g},\mathfrak{g}], \mathfrak{g}) = 0$, then all operators in $[\mathfrak{g},\mathfrak{g}]$ have zero eigenvalues (Lemma 6.39).

# Examples

**Example**: For $A = \begin{pmatrix} 2 & 1 \\ 0 & 2 \end{pmatrix}$: $A_s = \begin{pmatrix} 2 & 0 \\ 0 & 2 \end{pmatrix}$, $A_n = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.

# Relationships

## Enables
- **Cartan criterion (solvability)** — Uses parts (2) and (3) in the proof
- **Semisimple element** — Jordan decomposition extends to semisimple Lie algebras (Theorem 7.2)
- **Jordan decomposition in Lie algebras** — The abstract version for semisimple algebras

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.6, page 75. Theorem 6.38 (proof in Appendix B).

# Verification Notes

- Definition source: Direct from Theorem 6.38
- Confidence rationale: Explicit theorem; proof deferred to Appendix B
- Uncertainties: None
- Cross-reference status: Verified
