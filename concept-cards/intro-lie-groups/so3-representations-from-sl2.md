---
# === CORE IDENTIFICATION ===
concept: "SO(3) Representations from sl(2,C)"
slug: so3-representations-from-sl2

# === CLASSIFICATION ===
category: representations
subcategory: highest-weight-theory
tier: intermediate

# === PROVENANCE ===
source: "Introduction to Lie Groups and Lie Algebras"
source_slug: intro-lie-groups
authors: "Alexander Kirillov, Jr."
chapter: "Representations of sl(2,C) and Spherical Laplace Operator"
chapter_number: 5
pdf_page: 61
section: "5.1 Representations of sl(2,C)"

# === CONFIDENCE ===
extraction_confidence: high

# === VARIANTS (authority control) ===
aliases: []

# === TYPED RELATIONSHIPS ===
prerequisites:
  - classification-of-sl2-representations
  - equivalence-of-group-and-algebra-representations
  - integer-weights-for-sl2
extends:
  - classification-of-sl2-representations
related:
  - spherical-laplace-operator
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Which sl(2,C) representations correspond to SO(3) representations?"
---

# Quick Definition

Representations of $SO(3,\mathbb{R})$ correspond to those $\mathfrak{sl}(2,\mathbb{C})$-representations with all even weights. The irreducible representations of $SO(3,\mathbb{R})$ are $V_{2k}$ ($k = 0, 1, 2, \ldots$), of dimensions $1, 3, 5, \ldots$.

# Core Definition

By Exercise 5.3 (Kirillov, p. 65) and the covering map $SU(2) \to SO(3,\mathbb{R})$ with kernel $\{1, -1\}$ (Exercise 4.1):

A representation of $\mathfrak{so}(3,\mathbb{R})$ can be lifted to $SO(3,\mathbb{R})$ iff all weights are even, i.e., $V[k] = 0$ for all odd $k$. Thus the irreducible representations of $SO(3,\mathbb{R})$ are $V_0, V_2, V_4, \ldots$ (even highest weights only).

# Prerequisites

- **Classification of sl(2,C) representations** — Provides the full list of irreducibles
- **Equivalence of group and algebra representations** — For $SO(3) = SU(2)/\{\pm 1\}$
- **Integer weights** — Must be even for $SO(3)$ representations

# Key Properties

1. $SO(3,\mathbb{R})$ representations = even-highest-weight representations of $\mathfrak{sl}(2,\mathbb{C})$
2. $SU(2)$ representations = all representations of $\mathfrak{sl}(2,\mathbb{C})$
3. In physics: integer spin representations are $SO(3)$, half-integer spin are $SU(2)$-only
4. The condition comes from $e^{\pi i \rho(h)} = \mathrm{id}$ for $SO(3)$ representations

# Context & Application

This distinction between $SO(3)$ and $SU(2)$ representations has physical significance: bosons transform under $SO(3)$ representations (integer spin), while fermions require $SU(2)$ representations (half-integer spin).

# Examples

**Example**: $V_0$ (dim 1, trivial), $V_2$ (dim 3, adjoint/vector rep), $V_4$ (dim 5) are $SO(3)$ reps. $V_1$ (dim 2, spinor) is $SU(2)$-only.

# Relationships

## Builds Upon
- **Classification of sl(2,C) representations** — Restricted to even weights

## Enables
- **Spherical Laplace operator** — Uses $SO(3)$ representations $V_{2k}$

# Source Reference

Chapter 5, Exercises 5.3, p. 65; Chapter 4, Exercise 4.1, p. 55; Theorem 5.7, p. 61.

# Verification Notes

- Definition source: Synthesized from Exercise 5.3 and Theorem 5.7
- Confidence rationale: High — explicit exercises with clear statements
- Uncertainties: None
- Cross-reference status: Verified
