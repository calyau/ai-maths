---
# === CORE IDENTIFICATION ===
concept: Cartan Criterion for Solvability
slug: cartan-criterion-solvability

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
pdf_page: 74
section: "6.6. Killing form and Cartan criterion"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases:
  - "Cartan's criterion for solvability"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - killing-form
  - solvable-lie-algebra
  - jordan-decomposition-operators
extends: []
related:
  - cartan-criterion-semisimplicity
  - lie-theorem
  - engel-theorem
contrasts_with:
  - cartan-criterion-semisimplicity

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "How does the Killing form characterize solvability?"
  - "How do I determine if a Lie algebra is solvable using the Killing form?"
---

# Quick Definition

The Cartan criterion for solvability states that a Lie algebra $\mathfrak{g}$ is solvable if and only if $K([\mathfrak{g}, \mathfrak{g}], \mathfrak{g}) = 0$, i.e., the Killing form vanishes when one argument is a commutator.

# Core Definition

**Theorem 6.36** (Kirillov, p. 74): A Lie algebra $\mathfrak{g}$ is solvable iff $K([\mathfrak{g}, \mathfrak{g}], \mathfrak{g}) = 0$, i.e., $K(x, y) = 0$ for any $x \in [\mathfrak{g}, \mathfrak{g}]$, $y \in \mathfrak{g}$.

# Prerequisites

- **Killing form** — The criterion is stated in terms of $K$
- **Solvable Lie algebra** — The property being characterized
- **Jordan decomposition (operators)** — The proof uses the decomposition $A = A_s + A_n$

# Key Properties

1. Forward direction: if $\mathfrak{g}$ is solvable, Lie's theorem puts $\operatorname{ad} x$ in upper-triangular form, and commutators in strictly upper-triangular form, so their product has zero trace
2. Converse uses the auxiliary Lemma 6.39 and Jordan decomposition
3. The criterion works over both $\mathbb{R}$ and $\mathbb{C}$ (reduce to $\mathbb{C}$ by complexification)

# Construction / Recognition

## To Apply:
1. Compute $K(x, y) = \operatorname{tr}(\operatorname{ad} x \cdot \operatorname{ad} y)$ for $x \in [\mathfrak{g}, \mathfrak{g}]$, $y \in \mathfrak{g}$
2. If all such values are zero, $\mathfrak{g}$ is solvable
3. If any is nonzero, $\mathfrak{g}$ is not solvable

# Context & Application

This is one of the two fundamental Cartan criteria. Together with the semisimplicity criterion, it provides a complete characterization of solvable and semisimple algebras in terms of the Killing form. The proof is one of the most technically sophisticated in the chapter, using Jordan decomposition and the "conjugate semisimple part" $\bar{A}_s$.

# Examples

**Example**: For $\mathfrak{b}$ (upper-triangular matrices), the commutant $[\mathfrak{b}, \mathfrak{b}] \subset \mathfrak{n}$ (strictly upper-triangular). In the adjoint representation, commutators act as strictly upper-triangular operators, so $K([\mathfrak{b}, \mathfrak{b}], \mathfrak{b}) = 0$.

# Relationships

## Builds Upon
- **Killing form** — The criterion uses the Killing form

## Enables
- **Cartan criterion (semisimplicity)** — Uses the solvability criterion in its proof

## Contrasts With
- **Cartan criterion (semisimplicity)** — Solvability: $K([\mathfrak{g},\mathfrak{g}], \mathfrak{g}) = 0$; semisimplicity: $K$ non-degenerate

# Common Confusions

- **Confusion**: Confusing "$K = 0$ on $[\mathfrak{g},\mathfrak{g}] \times \mathfrak{g}$" with "$K = 0$"
  **Clarification**: The criterion requires $K$ to vanish only when one argument is in $[\mathfrak{g},\mathfrak{g}]$, not that $K$ is identically zero

# Source Reference

Chapter 6: Structure Theory of Lie Algebras, Section 6.6, pages 74-76. Theorem 6.36, Lemma 6.39.

# Verification Notes

- Definition source: Direct from Theorem 6.36
- Confidence rationale: Named theorem with full proof
- Uncertainties: None
- Cross-reference status: Verified
