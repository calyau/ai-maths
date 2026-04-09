---
# === CORE IDENTIFICATION ===
concept: "Weight Symmetry for sl(2,C)"
slug: weight-symmetry-for-sl2

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
aliases:
  - "symmetry of weight multiplicities"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - classification-of-sl2-representations
  - integer-weights-for-sl2
extends:
  - classification-of-sl2-representations
related:
  - weight-decomposition-for-sl2
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why are weight multiplicities symmetric about zero?"
---

# Quick Definition

In any finite-dimensional representation of $\mathfrak{sl}(2,\mathbb{C})$, weight multiplicities are symmetric: $\dim V[n] = \dim V[-n]$, and the maps $e^n: V[-n] \to V[n]$ and $f^n: V[n] \to V[-n]$ are isomorphisms for $n \geq 0$.

# Core Definition

**Theorem 5.7(2)** (Kirillov, p. 61): Let $V$ be a finite-dimensional representation of $\mathfrak{sl}(2,\mathbb{C})$. Then $\dim V[n] = \dim V[-n]$. Moreover, for $n \geq 0$, the maps $e^n: V[-n] \to V[n]$ and $f^n: V[n] \to V[-n]$ are isomorphisms.

# Prerequisites

- **Classification of sl(2,C) representations** — Symmetry follows from the structure of irreducibles
- **Integer weights for sl(2,C)** — The weights between which symmetry holds

# Key Properties

1. Weight multiplicities are symmetric about 0
2. The operators $e^n$ and $f^n$ provide explicit isomorphisms between $V[n]$ and $V[-n]$
3. This is an early instance of Weyl group symmetry (the Weyl group of $\mathfrak{sl}(2)$ is $\mathbb{Z}/2$ acting by $n \mapsto -n$)

# Context & Application

Weight symmetry is the prototype for Weyl group symmetry of weight multiplicities in general semisimple Lie algebras. It is used in Section 5.2 to decompose polynomial spaces on the sphere.

# Examples

**Example**: For $V_4$ (highest weight 4): weights are $4, 2, 0, -2, -4$, each with multiplicity 1. The weight diagram is symmetric about 0.

**Example**: For $V_1 \oplus V_3$: weights are $3, 1, -1, -3$ (from $V_3$) and $1, -1$ (from $V_1$). Total: $\dim V[3] = 1$, $\dim V[1] = 2$, $\dim V[-1] = 2$, $\dim V[-3] = 1$. Symmetric.

# Relationships

## Builds Upon
- **Classification of sl(2,C) representations** — Source of the symmetry

## Enables
- **Decomposition of polynomial spaces** — Used in Section 5.2

# Source Reference

Chapter 5, Section 5.1, Theorem 5.7(2), p. 61.

# Verification Notes

- Definition source: Direct from Theorem 5.7(2)
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
