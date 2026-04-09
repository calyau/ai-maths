---
# === CORE IDENTIFICATION ===
concept: "Integer Weights Theorem for sl(2,C)"
slug: integer-weights-for-sl2

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
  - "integrality of weights"

# === TYPED RELATIONSHIPS ===
prerequisites:
  - classification-of-sl2-representations
extends:
  - classification-of-sl2-representations
related:
  - weight-symmetry-for-sl2
contrasts_with: []

# === COMPETENCY QUESTIONS ===
answers_questions:
  - "Why are all weights of sl(2,C) representations integers?"
---

# Quick Definition

In any finite-dimensional representation of $\mathfrak{sl}(2,\mathbb{C})$, all weights are integers: the weight decomposition is $V = \bigoplus_{n \in \mathbb{Z}} V[n]$.

# Core Definition

**Theorem 5.7(1)** (Kirillov, p. 61): Let $V$ be a finite-dimensional representation of $\mathfrak{sl}(2,\mathbb{C})$. Then $V$ admits a weight decomposition with integer weights:

$$V = \bigoplus_{n \in \mathbb{Z}} V[n].$$

# Prerequisites

- **Classification of sl(2,C) representations** — Follows from the fact that all irreducibles have integer highest weights

# Key Properties

1. All weights are integers (not just rational or real)
2. This follows from complete reducibility plus the fact that each $V_n$ has integer weights
3. Analogous results hold for $\mathfrak{so}(3,\mathbb{R})$ and $SO(3,\mathbb{R})$ (Exercise 5.3)

# Context & Application

The integrality of weights is a manifestation of the "quantization" of angular momentum in physics. It generalizes to the integrality condition on weights of representations of semisimple Lie algebras (the weight must lie in the weight lattice).

# Relationships

## Builds Upon
- **Classification of sl(2,C) representations** — Integrality follows from the classification

## Related
- **Weight symmetry** — Companion result about $\dim V[n] = \dim V[-n]$

# Source Reference

Chapter 5, Section 5.1, Theorem 5.7(1), p. 61.

# Verification Notes

- Definition source: Direct from Theorem 5.7(1)
- Confidence rationale: Explicit theorem
- Uncertainties: None
- Cross-reference status: Verified
